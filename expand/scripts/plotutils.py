from common import *
from utils import *

_PNG = get_pngDir()

jet = ColorMap.JET
gray = ColorMap.GRAY
bwr = ColorMap.BLUE_WHITE_RED
rwb = ColorMap.RED_WHITE_BLUE
gmt_jet = ColorMap.GMT_JET
gyr = ColorMap.GRAY_YELLOW_RED
hue = ColorMap.HUE
hbr = ColorMap.HUE_BLUE_TO_RED
hrb = ColorMap.HUE_RED_TO_BLUE
prism = ColorMap.PRISM


###############  plot 1/2/3D  ################
def plot1D(c1=None,
           yc=None,
           s1=None,
           ys=None,
           d1=None,
           yd=None,
           hlabel="Samples",
           vlabel="Amplitude",
           png=None):
    r"""
    plot 1D lines.
    c1,s1,d1: Samplings, default=None
    yc,ys,yd: 1D array, default=None
    """
    sp = SimplePlot(SimplePlot.Origin.LOWER_LEFT)
    if c1 and yc:
        pvc = sp.addPoints(c1, yc)
        pvc.setLineColor(Color.BLUE)
    if s1 and ys:
        pvs = sp.addPoints(s1, ys)
        pvs.setLineColor(Color.RED)
    if d1 and yd:
        pvd = sp.addPoints(d1, yd)
        pvd.setLineColor(Color(0, 128, 0))
    # sp.setVLimits(-0.5,2)
    sp.setSize(900, 400)
    sp.setHLabel(hlabel)
    sp.setVLabel(vlabel)
    if png and _PNG:
        sp.paintToPng(300, 7.0, _PNG + png + ".png")


def plot2D(f,
           g=None,
           s1=None,
           s2=None,
           wx=500,
           wz=800,
           cmin=None,
           cmax=None,
           cmap=gray,
           nearest=None,
           gmin=None,
           gmax=None,
           gmap=jet,
           clab=None,
           axis=True,
           title=None,
           png=None):
    r"""
    plot 2D image
    f: image
    s1,s2: Samplings of two dimensions, default=Sampling(n)
    wx,wz: the image size
    cmin,cmax: the vaule limitation
    cmap: color map, default=gray, choice={jet,gray,bwr,gmt_jet,gyr,hue,hbr,hrb,prism,rwb}
    clab:
    axis: default=True
    title,png: default=None
    """
    n2 = len(f)
    n1 = len(f[0])
    if s1 is None:
        s1 = Sampling(n1)
    if s2 is None:
        s2 = Sampling(n2)

    orientation = PlotPanel.Orientation.X1DOWN_X2RIGHT
    if axis:
        panel = PlotPanel(1, 1, orientation)
    else:
        panel = PlotPanel(1, 1, orientation, PlotPanel.AxesPlacement.NONE)
    pxv = panel.addPixels(0, 0, s1, s2, f)
    pxv.setColorModel(cmap)
    if cmin and cmax:
        pxv.setClips(cmin, cmax)
    if title:
        panel.addTitle(title)
    if clab:
        cbar = panel.addColorBar(clab)
        pxv.addColorMapListener(cbar)
        cbar.setWidthMinimum(120)
        # cbar.paintToPng(137,1,pngDir+png+"cbar.png")
    if g:
        pv = panel.addPixels(s1, s2, g)
        if nearest:
            pv.setInterpolation(PixelsView.Interpolation.NEAREST)
        else:
            pv.setInterpolation(PixelsView.Interpolation.LINEAR)
        pv.setColorModel(gmap)
        if gmin and gmax:
            pv.setClips(gmin, gmax)
    moc = panel.getMosaic()
    frame = PlotFrame(panel)
    frame.setDefaultCloseOperation(PlotFrame.EXIT_ON_CLOSE)
    frame.setVisible(True)
    frame.setSize(wx, wz)
    if _PNG and png:
        frame.paintToPng(720, 3.333, _PNG + png + ".png")
        if clab:
            cbar.paintToPng(137, 1, _PNG + png + "cbar.png")


def plot3D(f,
           g=None,
           rgt=None,
           horizons=None,
           ks=None,
           cmin=None,
           cmax=None,
           cmap=None,
           clab=None,
           cint=None,
           samples=None,
           smin=None,
           smax=None,
           png=None):
    r"""
    3-D graphics
    f: 3D seismic volume
    g: a 3D volume covered on f
    rgt: plot rgt
    horizons: one or muti horizons to display
    ks: display control points for seismic horizon picking
    """
    n3 = len(f)
    n2 = len(f[0])
    n1 = len(f[0][0])
    # s1,s2,s3 = Sampling(n1),Sampling(n2, 12.5, 0),Sampling(n3, 25, 0)
    s1, s2, s3 = Sampling(n1), Sampling(n2, 1, 0), Sampling(n3, 1, 0)
    f1, f2, f3 = s1.getFirst(), s2.getFirst(), s3.getFirst()
    d1, d2, d3 = s1.getDelta(), s2.getDelta(), s3.getDelta()
    l1, l2, l3 = s1.getLast(), s2.getLast(), s3.getLast()

    sf = SimpleFrame(AxesOrientation.XRIGHT_YOUT_ZDOWN)
    cbar = None
    if g == None:
        ipg = sf.addImagePanels(s1, s2, s3, f)
        if cmap != None:
            ipg.setColorModel(cmap)
        if cmin != None and cmax != None:
            ipg.setClips(cmin, cmax)
        else:
            ipg.setClips(min(f) / 2, max(f) / 2)
        if clab:
            cbar = addColorBar(sf, clab, cint)
            ipg.addColorMapListener(cbar)
    else:
        ipg = ImagePanelGroup2(s1, s2, s3, f, g)
        ipg.setClips1(min(f) / 2, max(f) / 2)
        if cmin != None and cmax != None:
            ipg.setClips2(cmin, cmax)
        if cmap == None:
            cmap = jetFill(0.8)
        ipg.setColorModel2(cmap)
        if clab:
            cbar = addColorBar(sf, clab, cint)
            ipg.addColorMap2Listener(cbar)
        sf.world.addChild(ipg)
    if cbar:
        cbar.setWidthMinimum(100)

    if horizons:
        for ih in range(len(horizons)):
            tg = TriangleGroup(True, s3, s2, horizons[ih][0], horizons[ih][1],
                               horizons[ih][2], horizons[ih][3])
            states = StateSet()
            cs = ColorState()
            cs.setColor(Color.ORANGE)
            states.add(cs)
            lms = LightModelState()
            lms.setTwoSide(True)
            states.add(lms)
            ms = MaterialState()
            ms.setColorMaterial(GL_AMBIENT_AND_DIFFUSE)
            ms.setSpecular(Color.WHITE)
            ms.setShininess(100.0)
            states.add(ms)
            tg.setStates(states)
            sf.world.addChild(tg)

    if ks:
        pg = setPointGroup(ks[0], ks[1], ks[2], 10)
        sf.world.addChild(pg)
    if rgt:
        mc = MarchingCubes(s1, s2, s3, rgt)
        ct = mc.getContour(100)
        tg = TriangleGroup(ct.i, ct.x, ct.u)
        states = StateSet()
        cs = ColorState()
        cs.setColor(Color.ORANGE)
        states.add(cs)
        lms = LightModelState()
        lms.setTwoSide(True)
        states.add(lms)
        ms = MaterialState()
        ms.setColorMaterial(GL_AMBIENT_AND_DIFFUSE)
        ms.setSpecular(Color.WHITE)
        ms.setShininess(100.0)
        states.add(ms)
        tg.setStates(states)
        sf.world.addChild(tg)
    if samples:
        fx, x1, x2, x3 = samples
        if smin and smax:
            vmin, vmax, vmap = smin, smax, ColorMap.JET
        else:
            vmin, vmax = -2, 2
        ns = len(fx)
        for k, fxi in enumerate(fx):
            x1i = x1[k]
            x2i = x2[k]
            x3i = x3[k]
            pg = makePointGroup(fxi, x1i, x2i, x3i, vmin, vmax, None)
            sf.world.addChild(pg)

    ipg.setSlices(n1 - 1, 0, 0)  # h, left, right: which slice
    if cbar:
        sf.setSize(1300, 1200)
    else:
        sf.setSize(1200, 1200)  # frame size
    vc = sf.getViewCanvas()
    vc.setBackground(Color.WHITE)
    radius = 0.5 * sqrt(n1 * n1 + n2 * n2 + n3 * n3)
    ov = sf.getOrbitView()
    zscale = 1 * max(n2 * d2, n3 * d3) / (n1 * d1)  # z scale,
    zscale = 1
    ov.setAxesScale(1, 1, zscale)
    ov.setScale(1.0)  # image size
    ov.setWorldSphere(BoundingSphere(BoundingBox(f3, f2, f1, l3, l2, l1)))
    ov.setTranslate(Vector3(0, 0, 0))
    ov.setAzimuthAndElevation(50.0,
                              50.0)  # Azimuth, Elevation or vertical flip
    sf.setVisible(True)
    if png and _PNG:
        sf.paintToFile(_PNG + png + ".png")
        if cbar:
            cbar.paintToPng(137, 1, _PNG + png + "cbar.png")


###########  graphics setting  ################
def jetFill(alpha):
    return ColorMap.setAlpha(ColorMap.JET, alpha)


def jetFillExceptMin(alpha):
    a = fillfloat(alpha, 256)
    a[0] = 0.0
    return ColorMap.setAlpha(ColorMap.JET, a)


def gmtFillExceptMin(alpha):
    a = fillfloat(alpha, 256)
    a[0] = 0.0
    return ColorMap.setAlpha(ColorMap.GMT_JET, a)


def jetRamp(alpha):
    return ColorMap.setAlpha(ColorMap.JET, rampfloat(0.0, alpha / 256, 256))


def bwrFill(alpha):
    return ColorMap.setAlpha(ColorMap.BLUE_WHITE_RED, alpha)


def bwrNotch(alpha):
    a = zerofloat(256)
    for i in range(len(a)):
        if i < 128:
            a[i] = alpha * (128.0 - i) / 128.0
        else:
            a[i] = alpha * (i - 127.0) / 128.0
    return ColorMap.setAlpha(ColorMap.BLUE_WHITE_RED, a)


def hueFill(alpha):
    return ColorMap.getHue(0.0, 1.0, alpha)


def hueFillExceptMin(alpha):
    a = fillfloat(alpha, 256)
    a[0] = 0.0
    return ColorMap.setAlpha(ColorMap.getHue(0.0, 1.0), a)


def addColorBar(frame, clab=None, cint=None):
    cbar = ColorBar(clab)
    if cint:
        cbar.setInterval(cint)
    cbar.setFont(Font("Arial", Font.PLAIN, 32))  # size by experimenting
    cbar.setWidthMinimum
    cbar.setBackground(Color.WHITE)
    frame.add(cbar, BorderLayout.EAST)
    return cbar


def convertDips(ft):
    return FaultScanner.convertDips(0.2, ft)  # 5:1 vertical exaggeration


def makePointGroup(f, x1, x2, x3, cmin, cmax, cbar):
    n = len(x1)
    xyz = zerofloat(3 * n)
    copy(n, 0, 1, x3, 0, 3, xyz)
    copy(n, 0, 1, x2, 1, 3, xyz)
    copy(n, 0, 1, x1, 2, 3, xyz)
    rgb = None
    if cmin < cmax:
        cmap = ColorMap(cmin, cmax, ColorMap.getJet(1.0))
        if cbar:
            cmap.addListener(cbar)
        rgb = cmap.getRgbFloats(f)
    pg = PointGroup(xyz, rgb)
    ps = PointState()
    ps.setSize(8)
    ps.setSmooth(True)
    ss = StateSet()
    ss.add(ps)
    pg.setStates(ss)
    return pg


def setPointGroup(k1, k2, k3, size):
    np = len(k1)
    xyz = zerofloat(np * 3)
    rgb = zerofloat(np * 3)
    ki = 0
    for i in range(np):
        xyz[ki] = k3[i]
        xyz[ki + 1] = k2[i]
        xyz[ki + 2] = k1[i]
        rgb[ki] = 0  #1/225
        rgb[ki + 1] = 1  #225/225
        rgb[ki + 2] = 0  #1/225
        ki = ki + 3
    pg = PointGroup(size, xyz, rgb)
    states = StateSet()
    cs = ColorState()
    cs.setColor(Color.GREEN)
    states.add(cs)
    lms = LightModelState()
    lms.setTwoSide(True)
    states.add(lms)
    ms = MaterialState()
    ms.setColorMaterial(GL_AMBIENT_AND_DIFFUSE)
    ms.setShininess(100.0)
    states.add(ms)
    pg.setStates(states)
    return pg
