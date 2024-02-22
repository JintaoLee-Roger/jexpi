class IndexColorModel:
    """
    The IndexColorModel class is a ColorModel class that works with 
    pixel values consisting of a single sample that is an index into 
    a fixed colormap in the default sRGB color space. The colormap 
    specifies red, green, blue, and optional alpha components corresponding 
    to each index. All components are represented in the colormap as 8-bit 
    unsigned integral values. Some constructors allow the caller to specify 
    "holes" in the colormap by indicating which colormap entries are valid 
    and which represent unusable colors via the bits set in a BigInteger 
    object. This color model is similar to an X11 PseudoColor visual.
    """