# Accurate-propagation-scene-modeling-method
This is a detailed description of all the open source codes used in the paper “Path Loss Prediction in Urban Environments with Sionna-RT Based on Accurate Propagation Scene Models At 2.8 GHz”.

## Point clouds segmentation
我们使用Senast数据集训练得到的RandLA-Net网络执行点云分割。数据集的下载地址为https://github.com/QingyongHu/SensatUrban. 该仓库同时还提供了RandLA-Net网络的训练脚本。

## Surface reconstruction
### Building point Clouds 
我们使用Polyfit方法对建筑点云进行表面重建，Polyfit算法的代码可以在以下网址获取：https://github.com/LiangliangNan/PolyFit.

### Ground point clouds
地面点云的重建分为四步，离群值去除、下采样、插值填补空缺以及最后的重建，这部分代码可在本仓库中获取。

### Remaining point clouds
其余的点云，包括植被点云、围栏点云以及街道设施点云，我们采用Ball Pivoting Algorithm（BPA）进行高鲁棒性重建。虽然Python的Open3d库提供了该算法的调用，但需要人为设定旋转球的半径，该参数会显重影响重建的质量。我们发现Meshlab软件（https://www.meshlab.net/ ）提供的BPA支持自动猜测旋转球的半径，其重建质量较高。Pymeshlab库(https://pymeshlab.readthedocs.io/en/latest/ )可批量调用Meshlab软件进行重建。

