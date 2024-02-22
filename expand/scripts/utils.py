from common import *
from customcmap import *

################  project setting  ##########

_ROOT = ''
_N1, _N2, _N3 = 0, 0, 0
_D1, _D2, _D2 = 0, 0, 0
_F1, _F2, _F3 = 0, 0, 0
_S1, _S2, _S3 = 0, 0, 0
_PNG = ''


def set_dims(n1, n2, n3, d1, d2, d3, f1=0, f2=0, f3=0):
    global _N1, _N2, _N3
    global _D1, _D2, _D2
    global _F1, _F2, _F3
    global _S1, _S2, _S3
    _N1, _N2, _N3 = n1, n2, n3
    _D1, _D2, _D2 = d1, d2, d3
    _F1, _F2, _F3 = f1, f2, f3
    _S1 = Sampling(n1, d1, f1)
    _S2 = Sampling(n2, d2, f2)
    _S3 = Sampling(n3, d3, f3)


def set_dirs(root, png):
    global _ROOT, _PNG
    _ROOT = root
    _PNG = png


def get_samplings():
    if isinstance(_S1, int):
        raise RuntimeError("call `set_dims` to initial first")
    return _S1, _S2, _S3


def get_root():
    return _ROOT


def get_pngDir():
    return _PNG


################  IO  #######################


def process_name(name):
    if not name.endswith('.dat'):
        name = name + '.dat'
    if '/' in name:
        fileName = name
    else:
        fileName = _ROOT + name

    return fileName


def readImage1D(name, n, bo='<'):
    """ 
    Reads an image from a file with specified dimemsions.
    """
    bo = get_endian(bo)
    fileName = process_name(name)
    image = zerofloat(n)
    ais = ArrayInputStream(fileName, bo)
    ais.readFloats(image)
    ais.close()
    return image


def readImage2D(name, n1, n2, bo='<'):
    """ 
    Reads an image from a file with specified dimemsions.
    """
    bo = get_endian(bo)
    fileName = process_name(name)
    image = zerofloat(n1, n2)
    ais = ArrayInputStream(fileName, bo)
    ais.readFloats(image)
    ais.close()
    return image


def readImage3D(name, n1, n2, n3, bo='<'):
    """ 
    Reads an image from a file with specified dimemsions.
    """
    bo = get_endian(bo)
    fileName = process_name(name)
    image = zerofloat(n1, n2, n3)
    ais = ArrayInputStream(fileName, bo)
    ais.readFloats(image)
    ais.close()
    return image


def readImage3Ds(name, bo='<'):
    """ 
    Reads an image from a file with default dimensions.
    """
    bo = get_endian(bo)
    fileName = process_name(name)
    image = zerofloat(_N1, _N2, _N3)
    ais = ArrayInputStream(fileName, bo)
    ais.readFloats(image)
    ais.close()
    return image


def writeImage(name, image, bo='<'):
    """ 
    Writes an image to a file with specified name.
    """
    bo = get_endian(bo)
    fileName = process_name(name)
    aos = ArrayOutputStream(fileName, bo)
    aos.writeFloats(image)
    aos.close()


def get_endian(bo):
    if bo in ['<', 'little', 'l', ByteOrder.LITTLE_ENDIAN]:
        return ByteOrder.LITTLE_ENDIAN
    elif bo in ['>', 'big', 'b', ByteOrder.BIG_ENDIAN]:
        return ByteOrder.BIG_ENDIAN
    else:
        # fmt: off
        raise ValueError("If is little endian, set bo='<', or 'l', or 'little'; if is big endian, set bo='>', or 'b', or 'big'")  # noqa: E501


################  colormap  #######################
def list_custom_cmap():
    return custom_cmap.keys()


def get_custom_cmap(cmap):
    if cmap not in custom_cmap.keys():
        raise RuntimeError("cmap must be one of:", custom_cmap.keys())
    cdict = custom_cmap[cmap]
    seg = cdict['seg']
    rseg = cdict['r']
    gseg = cdict['g']
    bseg = cdict['b']
    nseg = len(seg) - 1

    r = zerofloat(256)
    g = zerofloat(256)
    b = zerofloat(256)

    for i in range(256):
        x = i / 255.0
        for j in range(nseg):
            beg = seg[j]
            end = 1.1 if seg[j + 1] == 1.0 else seg[j + 1]
            if x < end and x >= beg:
                y = (x - seg[j]) / (seg[j + 1] - seg[j])
                r[i] = rseg[j] + (rseg[j + 1] - rseg[j]) * y
                g[i] = gseg[j] + (gseg[j + 1] - gseg[j]) * y
                b[i] = bseg[j] + (bseg[j + 1] - bseg[j]) * y

    return ColorMap(0.0, 1.0, r, g, b).getColorModel()



################ Filter Noise #############

def filter_noise(gx, level):
    gs = zerofloat(gx)
    lof = LocalOrientFilter(4, 1)
    ets = lof.applyForTensors(gx)
    lsf = LocalSmoothingFilter()
    lsf.apply(ets, level, gx, gs)

    return sub(gx, gs)
