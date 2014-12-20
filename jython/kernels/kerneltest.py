# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @UIService ui

from net.imglib2.img.planar import PlanarImgFactory;
from net.imglib2.type.numeric.integer import ShortType;
from net.imglib2.type.numeric.real import FloatType;
from net.imglib2.type.numeric.real import DoubleType;

from jarray import array

from net.imglib2.meta import ImgPlus

# define a local directory to get the images from
directory="/home/bnorthan/Brian2014/Images/TempForEasyAccess/"

helaCellsName="HelaCellsRedChannelCropped.tif"
barsName="Bars_32.tif"

helaCells=data.open(directory+helaCellsName);
bars=data.open(directory+barsName);

display.createDisplay("HelaCells", helaCells);

gaussianKernel =ops.gaussKernel( 2, 5.0);
gaussianKernel3D =ops.gaussKernel(array([4.0, 4.0, 2.0], 'd'));
logKernel=ops.logKernel(2, 5.0, None, FloatType(),PlanarImgFactory()) 

display.createDisplay("gausskernel", ImgPlus(gaussianKernel));

dimensions2D=array([helaCells.dimension(0), helaCells.dimension(1)], 'l');
dimensions3D=array([bars.dimension(0), bars.dimension(1), bars.dimension(2)], 'l');

gaussianFiltered=ops.createImg( PlanarImgFactory(), FloatType(), dimensions2D)
logFiltered=ops.createImg(PlanarImgFactory(), FloatType(), dimensions2D)
barsGaussianFiltered=ops.createImg(PlanarImgFactory(), FloatType(), dimensions3D)

ops.convolve(gaussianFiltered, helaCells, gaussianKernel)
ops.convolve(logFiltered, helaCells, logKernel)
ops.convolve(barsGaussianFiltered, bars, gaussianKernel3D);

display.createDisplay("gaussian", ImgPlus(gaussianFiltered));
display.createDisplay("log", ImgPlus(logFiltered));
display.createDisplay("bars convolved", ImgPlus(barsGaussianFiltered));