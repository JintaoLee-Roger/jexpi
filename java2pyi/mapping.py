def typemap(type):
    type = type.strip()
    if type in type_mapping:
        return type_mapping[type]
    return type


type_mapping = {
    'boolean': 'bool',
    'double[]': 'Double1D',
    'double[][]': 'Double2D',
    'double[][][]': 'Double3D',
    'double[][][][]': 'Double4D',
    'float[]': 'Float1D',
    'float[][]': 'Float2D',
    'float[][][]': 'Float3D',
    'float[][][][]': 'Float4D',
    'float[][][][][]': 'Float5D',
    'int[]': 'Int1D',
    'int[][]': 'Int2D',
    'int[][][]': 'Int3D',
    'int[][][][]': 'Int4D',
    'long[]': 'Long1D',
    'long[][]': 'Long2D',
    'long[][][]': 'Long3D',
    'long[][][][]': 'Long4D',
    'short[]': 'Short1D',
    'short[][]': 'Short2D',
    'short[][][]': 'Short3D',
    'short[][][][]': 'Short4D',
    'char[]': 'Char1D',
    'char[][]': 'Char2D',
    'char[][][]': 'Char3D',
    'char[][][][]': 'Char4D',
    'byte[]': 'Byte1D',
    'byte[][]': 'Byte2D',
    'byte[][][]': 'Byte3D',
    'byte[][][][]': 'Byte4D',
    "Cdouble[]": "Cdouble1D",
    "Cdouble[][]": "Cdouble2D",
    "Cdouble[][][]": "Cdouble3D",
    "Cdouble[][][]": "Cdouble4D",
    "String[]": "String1D",
    "String[][]": "String2D",
    "String[][][]": "String3D",
    "Color[]": "Color1D"
}
