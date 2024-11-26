package bsm;

import java.io.*;
import java.nio.*;
import java.nio.charset.Charset;
import java.util.*;
import java.util.regex.*;
import edu.mines.jtk.io.*;
import edu.mines.jtk.util.Parallel;

/**
 * numpy's NPY file format reader and writer.
 * <em>
 * This class is used to read and write numpy's NPY file format. It supports
 * reading and writing of the following data types: i1, i2, i4, i8, u1, u2, u4,
 * u8, f2, f4, f8.
 * 
 * Usgae example:
 * Read
 * 
 * <pre>
 * NpyFile npy = new NpyFile("data.npy");
 * int[] shape = npy.getShape();
 * String dtype = npy.getDataType();
 * // If dtype is f4 or f2, and ndim is 3
 * float[][][] array = new float[shape[0]][shape[1]][shape[2]];
 * npy.readNpy(array);
 * npy.close();
 * </pre>
 * 
 * Write
 * 
 * <pre>
 * int[] shape = new int[] { 10, 20 };
 * int[][] array = new int[shape[0]][shape[1]];
 * // Fill the array
 * NpyFile.writeNpy("data.npy", array);
 * </em>
 * 
 * @author Jintao Li
 * @version 2024.11.03
 */
public class NpyFile implements Closeable {
    public NpyFile(String filename) throws IOException {
        this._fname = filename;
        this._ais = new ArrayInputStream(filename, ByteOrder.LITTLE_ENDIAN);
        parseHeader();
    }

    public String getDataType() {
        return _dtype;
    }

    public int ndim() {
        return _shape.length;
    }

    public int[] getShape() {
        return _shape;
    }

    public ByteOrder getByteOrder() {
        return _bo;
    }

    public boolean fortranOrder() {
        return _fortranOrder;
    }

    public int getDataOffset() {
        return _dOffset;
    }

    public static void halfs2floats(byte[] array, float[] out, ByteOrder bo) throws Exception {
        if (out.length * 2 != array.length) {
            throw new Exception("The array size does not match.");
        }
        int length = out.length;
        ByteBuffer buffer = ByteBuffer.wrap(array);
        buffer.order(bo); // Set the byte order as required

        for (int i = 0; i < length; i++) {
            short halfPrecisionBits = buffer.getShort();
            out[i] = halfToFloat(halfPrecisionBits);
        }
    }

    public static void halfs2floats(byte[][] array, float[][] out, ByteOrder bo) throws Exception {
        int rows = array.length;
        int cols = array[0].length;
        if (out[0].length * 2 != cols || out.length != rows) {
            throw new Exception("The array size does not match.");
        }
        cols /= 2;

        for (int i = 0; i < rows; i++) {
            // halfs2floats(array[i], out[i]);
            ByteBuffer buffer = ByteBuffer.wrap(array[i]);
            buffer.order(bo);
            for (int j = 0; j < cols; j++) {
                short halfPrecisionBits = buffer.getShort();
                out[i][j] = halfToFloat(halfPrecisionBits);
            }
        }
    }

    public static void halfs2floats(byte[][][] array, float[][][] out, ByteOrder bo) throws Exception {
        final int n3 = out.length;
        final int n2 = out[0].length;
        final int n1 = out[0][0].length;
        if (array[0][0].length != n1 * 2 || array[0].length != n2 || array.length != n3) {
            throw new Exception("The array size does not match.");
        }

        Parallel.loop(n3, new Parallel.LoopInt() {
            public void compute(int i) {
                for (int j = 0; j < n2; j++) {
                    ByteBuffer buffer = ByteBuffer.wrap(array[i][j]);
                    buffer.order(bo);
                    // buffer.order(ByteOrder.LITTLE_ENDIAN);
                    for (int k = 0; k < n1; k++) {
                        short halfPrecisionBits = buffer.getShort();
                        out[i][j][k] = halfToFloat(halfPrecisionBits);
                    }
                }
            }
        });

    }

    public void readNpy(int[] array) throws Exception { // TODO: u2?
        checkType("i4");
        checkShape(new int[] { array.length });
        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readInts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readInts(array);
            ais.close();
        }
    }

    public void readNpy(int[][] array) throws Exception {
        checkType("i4");
        checkShape(new int[] { array.length, array[0].length });
        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readInts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readInts(array);
            ais.close();
        }
    }

    public void readNpy(int[][][] array) throws Exception {
        checkType("i4");
        checkShape(new int[] { array.length, array[0].length, array[0][0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readInts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readInts(array);
            ais.close();
        }
    }

    public void readNpy(float[] array) throws Exception {
        if (_dtype.equals("f2")) {
            checkShape(new int[] { array.length });
            byte[] buf = new byte[array.length * 2];

            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readBytes(buf);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readBytes(buf);
                ais.close();
            }
            halfs2floats(buf, array, _bo);
        } else {
            checkType("f4");
            checkShape(new int[] { array.length });
            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readFloats(array);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readFloats(array);
                ais.close();
            }
        }
    }

    public void readNpy(float[][] array) throws Exception {
        if (_dtype.equals("f2")) {
            checkShape(new int[] { array.length, array[0].length });
            byte[][] buf = new byte[array.length][array[0].length * 2];

            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readBytes(buf);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readBytes(buf);
                ais.close();
            }
            halfs2floats(buf, array, _bo);
        } else {
            checkType("f4");
            checkShape(new int[] { array.length, array[0].length });

            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readFloats(array);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readFloats(array);
                ais.close();
            }
        }
    }

    public void readNpy(float[][][] array) throws Exception {
        if (_dtype.equals("f2")) {
            checkShape(new int[] { array.length, array[0].length, array[0][0].length });
            byte[][][] buf = new byte[array.length][array[0].length][array[0][0].length * 2];

            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readBytes(buf);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readBytes(buf);
                ais.close();
                // throw new Exception("For float16 dtype, only support LITTLE_ENDIAN");
            }
            halfs2floats(buf, array, _bo);
        } else {
            checkType("f4");
            checkShape(new int[] { array.length, array[0].length, array[0][0].length });

            if (_bo == ByteOrder.LITTLE_ENDIAN) {
                _ais.readFloats(array);
            } else {
                ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
                byte[] temp = new byte[_dOffset];
                ais.readFully(temp);
                ais.readFloats(array);
                ais.close();
            }
        }
    }

    public void readNpy(double[] array) throws Exception {
        checkType("f8");
        checkShape(new int[] { array.length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readDoubles(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readDoubles(array);
            ais.close();
        }
    }

    public void readNpy(double[][] array) throws Exception {
        checkType("f8");
        checkShape(new int[] { array.length, array[0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readDoubles(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readDoubles(array);
            ais.close();
        }
    }

    public void readNpy(double[][][] array) throws Exception {
        checkType("f8");
        checkShape(new int[] { array.length, array[0].length, array[0][0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readDoubles(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readDoubles(array);
            ais.close();
        }
    }

    public void readNpy(byte[] array) throws Exception {
        checkType("i1");
        checkShape(new int[] { array.length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readBytes(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readBytes(array);
            ais.close();
        }
    }

    public void readNpy(byte[][] array) throws Exception {
        checkType("i1");
        checkShape(new int[] { array.length, array[0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readBytes(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readBytes(array);
            ais.close();
        }
    }

    public void readNpy(byte[][][] array) throws Exception {
        checkType("i1");
        checkShape(new int[] { array.length, array[0].length, array[0][0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readBytes(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readBytes(array);
            ais.close();
        }
    }

    public void readNpy(short[] array) throws Exception { // TODO: u1?
        checkType("i2");
        checkShape(new int[] { array.length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readShorts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readShorts(array);
            ais.close();
        }
    }

    public void readNpy(short[][] array) throws Exception {
        checkType("i2");
        checkShape(new int[] { array.length, array[0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readShorts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readShorts(array);
            ais.close();
        }
    }

    public void readNpy(short[][][] array) throws Exception {
        checkType("i2");
        checkShape(new int[] { array.length, array[0].length, array[0][0].length });

        if (_bo == ByteOrder.LITTLE_ENDIAN) {
            _ais.readShorts(array);
        } else {
            ArrayInputStream ais = new ArrayInputStream(_fname, ByteOrder.BIG_ENDIAN);
            byte[] temp = new byte[_dOffset];
            ais.readFully(temp);
            ais.readShorts(array);
            ais.close();
        }
    }

    public static short[] floats2halfs(float[] array) {
        int length = array.length;
        short[] halfs = new short[length];
        for (int i = 0; i < length; i++) {
            halfs[i] = floatToHalf(array[i]);
        }
        return halfs;
    }

    public static short[][] floats2halfs(float[][] array) {
        int rows = array.length;
        int cols = array[0].length;
        short[][] halfs = new short[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                halfs[i][j] = floatToHalf(array[i][j]);
            }
        }
        return halfs;
    }

    public static short[][][] floats2halfs(float[][][] array) {
        final int n3 = array.length;
        final int n2 = array[0].length;
        final int n1 = array[0][0].length;
        short[][][] halfs = new short[n3][n2][n1];

        Parallel.loop(n3, new Parallel.LoopInt() {
            public void compute(int i) {
                // for (int i = 0; i < n3; i++) {
                for (int j = 0; j < n2; j++) {
                    for (int k = 0; k < n1; k++) {
                        halfs[i][j][k] = floatToHalf(array[i][j][k]);
                    }
                }
            }
        });
        return halfs;
    }

    // TODO: u4, u8, i8?

    public static void writeNpy(String outname, int[] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i4", new int[] { array.length });
        aos.writeBytes(header);
        aos.writeInts(array);
        aos.close();
    }

    public static void writeNpy(String outname, int[][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i4", new int[] { array.length, array[0].length });
        aos.writeBytes(header);
        aos.writeInts(array);
        aos.close();
    }

    public static void writeNpy(String outname, int[][][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i4", new int[] { array.length, array[0].length, array[0][0].length });
        aos.writeBytes(header);
        aos.writeInts(array);
        aos.close();
    }

    public static void writeNpy(String outname, float[] array, boolean half) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        if (half) {
            byte[] header = constructNpyHeader("f2", new int[] { array.length });
            aos.writeBytes(header);
            short[] halfs = floats2halfs(array);
            aos.writeShorts(halfs);
        } else {
            byte[] header = constructNpyHeader("f4", new int[] { array.length });
            aos.writeBytes(header);
            aos.writeFloats(array);
        }
        aos.close();
    }

    public static void writeNpy(String outname, float[] array) throws IOException {
        writeNpy(outname, array, false);
    }

    public static void writeNpy(String outname, float[][] array, boolean half) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        if (half) {
            byte[] header = constructNpyHeader("f2", new int[] { array.length, array[0].length });
            aos.writeBytes(header);
            short[][] halfs = floats2halfs(array);
            aos.writeShorts(halfs);
        } else {
            byte[] header = constructNpyHeader("f4", new int[] { array.length, array[0].length });
            aos.writeBytes(header);
            aos.writeFloats(array);
        }
        aos.close();
    }

    public static void writeNpy(String outname, float[][] array) throws IOException {
        writeNpy(outname, array, false);
    }

    public static void writeNpy(String outname, float[][][] array, boolean half) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        if (half) {
            byte[] header = constructNpyHeader("f2", new int[] { array.length, array[0].length, array[0][0].length });
            aos.writeBytes(header);
            short[][][] halfs = floats2halfs(array);
            aos.writeShorts(halfs);
        } else {
            byte[] header = constructNpyHeader("f4", new int[] { array.length, array[0].length, array[0][0].length });
            aos.writeBytes(header);
            aos.writeFloats(array);
        }
        aos.close();
    }

    public static void writeNpy(String outname, float[][][] array) throws IOException {
        writeNpy(outname, array, false);
    }

    public static void writeNpy(String outname, double[] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("f8", new int[] { array.length });
        aos.writeBytes(header);
        aos.writeDoubles(array);
        aos.close();
    }

    public static void writeNpy(String outname, double[][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("f8", new int[] { array.length, array[0].length });
        aos.writeBytes(header);
        aos.writeDoubles(array);
        aos.close();
    }

    public static void writeNpy(String outname, double[][][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("f8", new int[] { array.length, array[0].length, array[0][0].length });
        aos.writeBytes(header);
        aos.writeDoubles(array);
        aos.close();
    }

    public static void writeNpy(String outname, byte[] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i1", new int[] { array.length });
        aos.writeBytes(header);
        aos.writeBytes(array);
        aos.close();
    }

    public static void writeNpy(String outname, byte[][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i1", new int[] { array.length, array[0].length });
        aos.writeBytes(header);
        aos.writeBytes(array);
        aos.close();
    }

    public static void writeNpy(String outname, byte[][][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i1", new int[] { array.length, array[0].length, array[0][0].length });
        aos.writeBytes(header);
        aos.writeBytes(array);
        aos.close();
    }

    public static void writeNpy(String outname, short[] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i2", new int[] { array.length });
        aos.writeBytes(header);
        aos.writeShorts(array);
        aos.close();
    }

    public static void writeNpy(String outname, short[][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i2", new int[] { array.length, array[0].length });
        aos.writeBytes(header);
        aos.writeShorts(array);
        aos.close();
    }

    public static void writeNpy(String outname, short[][][] array) throws IOException {
        if (!outname.endsWith(".npy")) {
            outname += ".npy";
        }
        ArrayOutputStream aos = new ArrayOutputStream(outname, ByteOrder.LITTLE_ENDIAN);
        byte[] header = constructNpyHeader("i2", new int[] { array.length, array[0].length, array[0][0].length });
        aos.writeBytes(header);
        aos.writeShorts(array);
        aos.close();
    }

    @Override
    public void close() throws IOException {
        if (_ais != null) {
            _ais.close();
        }
    }

    private String _fname; // file name
    private String _dtype; // Data type string, e.g. "i4", "u1", "f4"
    private int[] _shape; // Shape of the data
    private ByteOrder _bo; // byte-order
    private boolean _fortranOrder; // Whether or not it is a Fortran order, only support C order
    private int _dOffset; // Offset of the data in the file
    private ArrayInputStream _ais; 
    private final byte[] _magic = new byte[] { (byte) 0x93, 'N', 'U', 'M', 'P', 'Y' };

    // Supported data types mapped to byte size
    private static final Map<String, Integer> DATA_TYPE_SIZE_MAP = new HashMap<String, Integer>();

    static {
        DATA_TYPE_SIZE_MAP.put("u1", 1);
        DATA_TYPE_SIZE_MAP.put("i1", 1);
        DATA_TYPE_SIZE_MAP.put("i2", 2);
        // DATA_TYPE_SIZE_MAP.put("u2", 2);
        DATA_TYPE_SIZE_MAP.put("i4", 4);
        // DATA_TYPE_SIZE_MAP.put("u4", 4);
        DATA_TYPE_SIZE_MAP.put("i8", 8);
        // DATA_TYPE_SIZE_MAP.put("u8", 8);
        DATA_TYPE_SIZE_MAP.put("f2", 2);
        DATA_TYPE_SIZE_MAP.put("f4", 4);
        DATA_TYPE_SIZE_MAP.put("f8", 8);
    }

    private void parseHeader() throws IOException {
        // Read the magic number.
        byte[] magic = new byte[6];
        _ais.readFully(magic);
        boolean matches = true;
        for (int i = 0; i < _magic.length; i++) {
            if (magic[i] != _magic[i]) {
                matches = false;
                break;
            }
        }
        if (!matches) {
            _ais.close();
            StringBuilder hexMagicString = new StringBuilder();
            for (byte c : magic) {
                hexMagicString.append(String.format("\\u%04x", c));
            }
            throw new IOException("Not a valid NumPy file, magic string is: " + hexMagicString
                    + ", but expected: \\u0093\\u004e\\u0055\\u004d\\u0050\\u0059");
        }

        // Read version number
        byte major = _ais.readByte();
        byte minor = _ais.readByte();

        // Read header length
        int headerLen;
        if (major == 1) {
            headerLen = _ais.readUnsignedShort();
            _dOffset = 10 + headerLen;
        } else if (major == 2) {
            headerLen = _ais.readInt();
            _dOffset = 12 + headerLen;
        } else {
            _ais.close();
            throw new IOException("Unsupported version: " + major + "." + minor);
        }

        // Read header content
        byte[] headerBytes = new byte[headerLen];
        _ais.readFully(headerBytes);
        String header = new String(headerBytes, Charset.forName("ISO-8859-1")).trim();

        // Parsing header dictionaries
        Map<String, String> headerMap = parseHeaderDict(header);

        // get dtype
        String descr = headerMap.get("descr");
        char endianChar = descr.charAt(0);
        if (endianChar == '<' || endianChar == '|') {
            _bo = ByteOrder.LITTLE_ENDIAN;
        } else if (endianChar == '>') {
            _bo = ByteOrder.BIG_ENDIAN;
        } else {
            _ais.close();
            throw new IOException("Unknown byte order symbol: " + endianChar);
        }
        _dtype = descr.substring(1);

        // Checking for supported data types
        if (!DATA_TYPE_SIZE_MAP.containsKey(_dtype)) {
            _ais.close();
            throw new IOException("Unsupported data type: " + _dtype);
        }

        // get fortran_order
        _fortranOrder = Boolean.parseBoolean(headerMap.get("fortran_order"));

        // get shape
        _shape = parseShape(headerMap.get("shape"));
    }

    private int[] parseShape(String shapeStr) {
        shapeStr = shapeStr.trim();
        if (shapeStr.startsWith("(") && shapeStr.endsWith(")")) {
            shapeStr = shapeStr.substring(1, shapeStr.length() - 1).trim();
        }
        String[] dims = shapeStr.split(",");
        List<Integer> shapeList = new ArrayList<Integer>();
        for (String dim : dims) {
            dim = dim.trim();
            if (!dim.isEmpty()) {
                shapeList.add(Integer.parseInt(dim));
            }
        }
        int[] shape = new int[shapeList.size()];
        for (int i = 0; i < shapeList.size(); i++) {
            shape[i] = shapeList.get(i);
        }
        return shape;
    }

    private Map<String, String> parseHeaderDict(String header) throws IOException {
        Map<String, String> map = new HashMap<>();

        header = header.trim();
        if (header.startsWith("{") && header.endsWith("}")) {
            header = header.substring(1, header.length() - 1).trim();
        } else {
            throw new IOException("Header formatting error.");
        }

        Pattern pattern = Pattern.compile("'([^']+)'\\s*:\\s*(?:'([^']*)'|\"([^\"]*)\"|(\\([^)]*\\))|([^,]+))(?=,|$)");
        Matcher matcher = pattern.matcher(header);

        while (matcher.find()) {
            String key = matcher.group(1);
            String value = null;

            if (matcher.group(2) != null) {
                // Values wrapped in single quotes '()'
                value = matcher.group(2);
            } else if (matcher.group(3) != null) {
                // Double quotes wrap the value
                value = matcher.group(3);
            } else if (matcher.group(4) != null) {
                // A tuple wrapped in parentheses
                value = matcher.group(4);
            } else if (matcher.group(5) != null) {
                // Other non-comma values
                value = matcher.group(5).trim();
            }

            if (value != null) {
                map.put(key, value);
            }
        }

        return map;
    }

    private void checkType(String expectedType) throws Exception {
        if (_dtype.equals("i1") && expectedType.equals("u1")) {
            expectedType = "i1";
        }
        if (_dtype.equals("u1") && expectedType.equals("i1")) {
            expectedType = "u1";
        }
        if (!_dtype.equals(expectedType)) {
            throw new Exception("The data types don't match, and the expected type is " + expectedType
                    + ", but the type in the file is " + _dtype);
        }
    }

    private void checkShape(int[] arrayShape) throws Exception {
        if (_shape.length != arrayShape.length) {
            throw new Exception("Data dimensions do not match. The expected dimension is " + _shape.length
                    + ", but introduced " + arrayShape.length + "d array.");
        }
        for (int i = 0; i < _shape.length; i++) {
            if (_shape[i] != arrayShape[i]) {
                throw new Exception("Array shapes do not match, the expected shape is " + Arrays.toString(_shape)
                        + ", but the array shape passed in is " + Arrays.toString(arrayShape));
            }
        }
    }

    private static float halfToFloat(short halfPrecisionBits) {
        int h = halfPrecisionBits & 0xFFFF; // Make sure it's an unsigned 16-bit number

        int sign = (h >> 15) & 0x00000001;
        int exponent = (h >> 10) & 0x0000001F;
        int fraction = h & 0x000003FF;

        int floatSign = sign << 31;
        int floatExponent;
        int floatFraction;

        if (exponent == 0) {
            if (fraction == 0) {
                // Positive or negative zero
                return Float.intBitsToFloat(floatSign);
            } else {
                // Non-normalized number -> Normalized
                // Find the first non-zero position
                int shift = 0;
                while ((fraction & 0x00000400) == 0) {
                    fraction <<= 1;
                    shift++;
                }
                fraction &= 0x000003FF; // Clear hidden bits
                exponent = 1 - shift;
                floatExponent = (exponent + (127 - 15)) << 23;
                floatFraction = fraction << 13;
            }
        } else if (exponent == 31) {
            if (fraction == 0) {
                // Positive infinity or negative infinity
                floatExponent = 0xFF << 23;
                floatFraction = 0;
            } else {
                // NaN
                floatExponent = 0xFF << 23;
                floatFraction = fraction << 13;
            }
        } else {
            // normalized number
            floatExponent = (exponent + (127 - 15)) << 23;
            floatFraction = fraction << 13;
        }

        int floatBits = floatSign | floatExponent | floatFraction;
        return Float.intBitsToFloat(floatBits);
    }

    private static short floatToHalf(float value) {
        int floatBits = Float.floatToIntBits(value);

        int sign = (floatBits >>> 16) & 0x8000; // sign bit
        int exponent = ((floatBits >>> 23) & 0xFF) - 127 + 15; // Adjustment index offset
        int fraction = floatBits & 0x7FFFFF; // mantissa

        if (exponent <= 0) {
            if (exponent < -10) {
                // Too small, denoted as zero
                return (short) sign;
            }
            // unnormalized number
            fraction = (fraction | 0x800000) >>> (1 - exponent);
            // round
            if ((fraction & 0x1000) != 0) {
                fraction += 0x2000;
            }
            return (short) (sign | (fraction >>> 13));
        } else if (exponent == 0xFF - (127 - 15)) {
            if (fraction == 0) {
                // infinity
                return (short) (sign | 0x7C00);
            } else {
                // NaN
                return (short) (sign | 0x7C00 | (fraction >>> 13));
            }
        }

        if (exponent > 30) {
            // Overflow, expressed as infinity
            return (short) (sign | 0x7C00);
        }

        // Normalized number
        // round
        if ((fraction & 0x1000) != 0) {
            fraction += 0x2000;
            if ((fraction & 0x800000) != 0) {
                fraction = 0;
                exponent += 1;
                if (exponent > 30) {
                    return (short) (sign | 0x7C00);
                }
            }
        }

        return (short) (sign | (exponent << 10) | (fraction >>> 13));
    }

    private static byte[] constructNpyHeader(String dtype, int[] shape) {
        String bo = "<";
        if (dtype.equals("i1") || dtype.equals("u1")) {
            bo = "|";
        }
        String descr = bo + dtype; // e.g., '<i4', '<f4'
        // boolean fortranOrder = false; 

        // shape, e.g.,  (3, 4) , (10, )
        StringBuilder shapeBuilder = new StringBuilder();
        shapeBuilder.append('(');
        for (int i = 0; i < shape.length; i++) {
            shapeBuilder.append(shape[i]);
            if (i < shape.length - 1) {
                shapeBuilder.append(", ");
            }
        }
        if (shape.length == 1) {
            shapeBuilder.append(','); // shape in 1d (10, )
        }
        shapeBuilder.append(')');

        // Constructing the header dictionary string
        String headerDict = String.format("{'descr': '%s', 'fortran_order': False, 'shape': %s, }",
                descr,
                shapeBuilder.toString());

        // Ensure that the header length is a multiple of 64, padding with spaces to fulfill the requirement
        int headerLen = headerDict.length() + 10; // Magic number and header length bytes
        int padding = 64 - (headerLen % 64);

        // Append spaces to pad the header
        StringBuilder paddedHeader = new StringBuilder(headerDict);
        for (int i = 0; i < padding; i++) {
            paddedHeader.append(' ');
        }
        headerDict = paddedHeader.toString();

        byte[] magic = new byte[] { (byte) 0x93, 'N', 'U', 'M', 'P', 'Y' };
        byte majorVersion = 1;
        byte minorVersion = 0;
        int headerLength = headerDict.length();

        ByteArrayOutputStream header = new ByteArrayOutputStream();
        try {
            header.write(magic);
            header.write(majorVersion);
            header.write(minorVersion);
            header.write(headerLength & 0xFF);
            header.write((headerLength >> 8) & 0xFF);
            header.write(headerDict.getBytes("ISO-8859-1"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        return header.toByteArray();
    }
}