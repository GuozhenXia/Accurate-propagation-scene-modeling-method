# Accurate-propagation-scene-modeling-method
This is a detailed description of all the open source codes used in the paper “Path Loss Prediction in Urban Environments with Sionna-RT Based on Accurate Propagation Scene Models At 2.8 GHz”.

## Point clouds segmentation
We use the RandLA-Net network, trained on the SensatUrban dataset, to perform point cloud segmentation. The dataset can be downloaded from https://github.com/QingyongHu/SensatUrban. This repository also provides training scripts for the RandLA-Net network.

## Surface reconstruction
### Building point Clouds 
We use the Polyfit method for surface reconstruction of building point clouds. The code for the Polyfit algorithm can be found at the following URL: https://github.com/LiangliangNan/PolyFit.

### Ground point clouds
The reconstruction of ground point clouds consists of four steps: outlier removal, downsampling, interpolation to fill gaps, and the final reconstruction. The code for this process can be found in this repository.

### Remaining point clouds
We use the Ball Pivoting Algorithm (BPA) for robust reconstruction of the remaining point clouds, including vegetation, fence, and street facility point clouds. Although the Open3d library in Python provides an implementation of this algorithm, it requires manually setting the radius of the pivoting ball, which can significantly impact the reconstruction quality. We found that the Meshlab software (https://www.meshlab.net/) supports automatic estimation of the pivoting ball radius, resulting in higher reconstruction quality. The Pymeshlab library (https://pymeshlab.readthedocs.io/en/latest/) can be used to call Meshlab for batch reconstructions.

## Ray Tracing
We use Nvidia's open-source Sionna-RT (https://nvlabs.github.io/sionna/) for ray tracing simulation. Sionna-RT is built on Mitsuba 3 and TensorFlow, enabling highly efficient simulations of direct transmission, reflection, diffraction, and scattering.

