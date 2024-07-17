import numpy as np
import open3d as o3d
from scipy.interpolate import griddata, NearestNDInterpolator

def interpolate(points, x_step=0.1, y_step=0.1, method='linear'):
    # Extract x, y, z data from points
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]

    # Determine the boundaries of x and y
    x_min, x_max = np.min(x), np.max(x)
    y_min, y_max = np.min(y), np.max(y)

    # Create grid points
    grid_x, grid_y = np.meshgrid(np.arange(x_min, x_max + x_step, x_step),
                                 np.arange(y_min, y_max + y_step, y_step))

    # Perform interpolation using griddata
    grid_z = griddata((x, y), z, (grid_x, grid_y), method=method)

    # Find the indices of NaN values in grid_z
    nan_indices = np.isnan(grid_z)

    if len(nan_indices) > 0:
        # Fill NaN values using nearest neighbor interpolation
        nearest_interpolator = NearestNDInterpolator((x, y), z)
        grid_z[nan_indices] = nearest_interpolator(grid_x[nan_indices], grid_y[nan_indices])

    return np.stack((grid_x, grid_y, grid_z), axis=-1)

def reconstruct(points, path):
    # Create a vertex grid corresponding to the points
    vertices = np.reshape(points, [points.shape[0]*points.shape[1], points.shape[2]])

    # Create triangle indices
    triangles = []
    for i in range(points.shape[0] - 1):
        for j in range(points.shape[1] - 1):
            # Vertex indices
            idx = i * points.shape[1] + j
            # Two triangles
            triangles.append([idx, idx + 1, idx + points.shape[1]])
            triangles.append([idx + 1, idx + 1 + points.shape[1], idx + points.shape[1]])

    triangles = np.array(triangles)

    # Create 3D mesh
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(vertices)
    mesh.triangles = o3d.utility.Vector3iVector(triangles)
    mesh.compute_vertex_normals()  # Compute normals for better visualization

    # Save as a PLY file
    o3d.io.write_triangle_mesh(path, mesh, write_ascii=True)

    print("3D mesh model has been saved!")

def main():
    # Read ground point cloud file
    pcd = o3d.io.read_point_cloud('./ground.ply') # Replace with your ground point cloud file path

    # Remove outliers
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

    # Downsample
    downsampled = cl.voxel_down_sample(voxel_size=0.5)

    points = np.array(downsampled.points)

    # Fill missing values
    interpolated_points = interpolate(points, x_step=10, y_step=10)

    # Reconstruct mesh
    reconstruct(interpolated_points, '/') # Replace with your desired save path

    print()

if __name__ == '__main__':
    main()
