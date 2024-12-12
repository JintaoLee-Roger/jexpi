package bsm;

import java.util.Map;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.List;
import java.io.*;
import java.util.zip.ZipEntry;
import java.util.zip.ZipException;
import java.util.zip.ZipFile;
import java.util.zip.ZipOutputStream;

/**
 * The NpzFile class provides functionality for reading and writing NumPy .npz
 * files.
 * It allows users to work with compressed or uncompressed multi-array archives
 * in the .npz format.
 *
 * <p>
 * Features include:
 * </p>
 * <ul>
 * <li>Reading all or specific arrays from an existing .npz file.</li>
 * <li>Retrieving keys of arrays stored in the file.</li>
 * <li>Checking for the existence of a specific key in the archive.</li>
 * <li>Writing single or multiple arrays to a new .npz file, with optional
 * compression and floating-point precision (FP16 support).</li>
 * </ul>
 *
 * <p>
 * Note:
 * </p>
 * <ul>
 * <li>The class implements {@link Closeable}, ensuring proper resource
 * management when reading .npz files.</li>
 * <li>Writing to .npz files is handled by static methods, eliminating the need
 * for an instance when creating files.</li>
 * </ul>
 * 
 * <p>
 * Example Usage:
 * </p>
 * 
 * <pre>{@code

    // Reading from an existing .npz file
    NpzFile npz = new NpzFile("example.npz");

    // Get all keys in the .npz file
    List<String> keys = npz.getKeys();
    System.out.println("Keys: " + keys);

    // Read a specific array
    NpyFile array1 = npz.readNpz("array1");

    // Check if a key exists
    boolean hasKey = npz.containsKey("array2");
    System.out.println("Contains 'array2': " + hasKey);

    // Write a single array to a new .npz file
    int[] data = { 1, 2, 3, 4, 5 };
    NpzFile.writeNpz("new_data.npz", "my_array", data, true);

 * @author Jintao Li
 * @version 2024.12.12
 */

public class NpzFile implements Closeable {

    private ZipFile zipFile; // Used to read the ZipFile

    /**
     * Constructor to initialize NpzFile.
     *
     * @param filePath Path to the .npz file
     * @throws IOException If the file cannot be accessed
     */
    public NpzFile(String filePath) throws IOException {
        // Check if the file exists
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IOException("File does not exist: " + filePath);
        }

        // Check if the file is a valid ZIP file
        try {
            this.zipFile = new ZipFile(filePath);
        } catch (ZipException e) {
            throw new IOException("Invalid file format: not a valid ZIP file: " + filePath, e);
        }
    }

    /**
     * Get the ZipFile object (for internal use).
     *
     * @return The ZipFile object
     */
    protected ZipFile getZipFile() {
        return this.zipFile;
    }

    /**
     * Read all data from the .npz file.
     *
     * @return A map of keys to corresponding NpyFile objects
     * @throws IOException If an error occurs while reading
     */
    public Map<String, NpyFile> readNpz() throws IOException {
        Map<String, NpyFile> result = new HashMap<>();

        // Iterate over all entries
        Enumeration<? extends ZipEntry> entries = zipFile.entries();
        while (entries.hasMoreElements()) {
            ZipEntry entry = entries.nextElement();
            String name = entry.getName();

            // Only process .npy files
            if (name.endsWith(".npy")) {
                String key = name.substring(0, name.length() - 4); // Remove the suffix
                try (InputStream is = zipFile.getInputStream(entry)) {
                    result.put(key, new NpyFile(is));
                }
            }
        }

        return result;
    }

    /**
     * Read a specific array by key.
     *
     * @param key The key of the array to read
     * @return The corresponding NpyFile object
     * @throws IOException              If an error occurs while reading
     * @throws IllegalArgumentException If the key does not exist
     */
    public NpyFile readNpz(String key) throws IOException, IllegalArgumentException {
        ZipEntry entry = zipFile.getEntry(key + ".npy");

        if (entry == null) {
            throw new IllegalArgumentException("Key does not exist: " + key);
        }

        try (InputStream is = zipFile.getInputStream(entry)) {
            return new NpyFile(is); // Assumes NpyFile supports initialization from InputStream
        }
    }

    /**
     * Get a list of all keys in the .npz file.
     *
     * @return A list of keys
     * @throws IOException If an error occurs while accessing the file
     */
    public List<String> getKeys() throws IOException {
        List<String> keys = new ArrayList<>();
        Enumeration<? extends ZipEntry> entries = zipFile.entries();
        while (entries.hasMoreElements()) {
            ZipEntry entry = entries.nextElement();
            String name = entry.getName();
            if (name.endsWith(".npy")) { // Only process .npy files
                keys.add(name.substring(0, name.length() - 4)); // Remove the suffix
            }
        }
        return keys;
    }

    // 静态方法：写入单个数组
    public static void writeNpz(String filePath, String key, Object array, boolean compressed, boolean fp16)
            throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filePath);
                ZipOutputStream zos = new ZipOutputStream(fos)) {

            // If not compressed, set the compression method to STORED
            if (!compressed) {
                zos.setLevel(ZipOutputStream.STORED);
            }

            addArrayToZip(zos, key, array, fp16);
        }
    }

    public static void writeNpz(String filePath, String key, Object array, boolean compressed) throws IOException {
        writeNpz(filePath, key, array, compressed, false);
    }

    public static void writeNpz(String filePath, String key, Object array) throws IOException {
        writeNpz(filePath, key, array, true, false);
    }

    // 静态方法：批量写入多个数组
    public static void writeNpz(String filePath, Map<String, Object> data, boolean compressed, boolean fp16)
            throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filePath);
                ZipOutputStream zos = new ZipOutputStream(fos)) {

            // If not compressed, set the compression method to STORED
            if (!compressed) {
                zos.setLevel(ZipOutputStream.STORED);
            }

            for (Map.Entry<String, Object> entry : data.entrySet()) {
                String key = entry.getKey();
                Object array = entry.getValue();
                addArrayToZip(zos, key, array, fp16);
            }
        }
    }

    public static void writeNpz(String filePath, Map<String, Object> data, boolean compressed) throws IOException {
        writeNpz(filePath, data, compressed, false);
    }

    public static void writeNpz(String filePath, Map<String, Object> data) throws IOException {
        writeNpz(filePath, data, true, false);
    }

    private static void addArrayToZip(ZipOutputStream zos, String key, Object array, boolean fp16) throws IOException {
        // Create a new entry in the ZIP stream
        ZipEntry entry = new ZipEntry(key + ".npy");
        zos.putNextEntry(entry);

        // Write the array directly to the ZIP stream using NpyFile
        if (array instanceof int[]) {
            NpyFile.writeNpy(zos, (int[]) array);
        } else if (array instanceof int[][]) {
            NpyFile.writeNpy(zos, (int[][]) array);
        } else if (array instanceof int[][][]) {
            NpyFile.writeNpy(zos, (int[][][]) array);
        } else if (array instanceof float[]) {
            NpyFile.writeNpy(zos, (float[]) array, fp16);
        } else if (array instanceof float[][]) {
            NpyFile.writeNpy(zos, (float[][]) array, fp16);
        } else if (array instanceof float[][][]) {
            NpyFile.writeNpy(zos, (float[][][]) array, fp16);
        } else if (array instanceof byte[]) {
            NpyFile.writeNpy(zos, (byte[]) array);
        } else if (array instanceof byte[][]) {
            NpyFile.writeNpy(zos, (byte[][]) array);
        } else if (array instanceof byte[][][]) {
            NpyFile.writeNpy(zos, (byte[][][]) array);
        } else if (array instanceof double[]) {
            NpyFile.writeNpy(zos, (double[]) array);
        } else if (array instanceof double[][]) {
            NpyFile.writeNpy(zos, (double[][]) array);
        } else if (array instanceof double[][][]) {
            NpyFile.writeNpy(zos, (double[][][]) array);
        } else if (array instanceof short[]) {
            NpyFile.writeNpy(zos, (short[]) array);
        } else if (array instanceof short[][]) {
            NpyFile.writeNpy(zos, (short[][]) array);
        } else if (array instanceof short[][][]) {
            NpyFile.writeNpy(zos, (short[][][]) array);
        } else {
            throw new IllegalArgumentException("Unsupported array type for key: " + key);
        }

        zos.closeEntry(); // Close the current ZIP entry
    }

    /**
     * Check if a specific key exists in the .npz file.
     *
     * @param key The key to check
     * @return True if the key exists, otherwise false
     * @throws IOException If an error occurs while accessing the file
     */
    public boolean containsKey(String key) throws IOException {
        Enumeration<? extends ZipEntry> entries = zipFile.entries();
        while (entries.hasMoreElements()) {
            ZipEntry entry = entries.nextElement();
            if (entry.getName().equals(key + ".npy")) { // Key matches a .npy file
                return true;
            }
        }
        return false;
    }

    /**
     * Close the file and release resources.
     * Implements the Closeable interface to support try-with-resources.
     *
     * @throws IOException If an error occurs while closing the file
     */
    @Override
    public void close() throws IOException {
        if (this.zipFile != null) {
            this.zipFile.close();
        }
    }
}