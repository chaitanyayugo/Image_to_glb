import numpy as np
import trimesh
import cv2

def generate_glb(image_path: str, depth_map: np.ndarray, output_path: str):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (256, 256))
    depth = cv2.resize(depth_map, (256, 256))

    h, w = depth.shape
    y_coords, x_coords = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')

    # Create 3D vertices
    z = depth.astype(np.float32) / 255.0 * 2.0  # depth scale
    vertices = np.stack([
        x_coords.flatten() / w,
        y_coords.flatten() / h,
        z.flatten()
    ], axis=-1)

    # Create faces (triangles)
    faces = []
    for y in range(h - 1):
        for x in range(w - 1):
            i = y * w + x
            faces.append([i, i + 1, i + w])
            faces.append([i + 1, i + w + 1, i + w])

    faces = np.array(faces)

    # Apply texture
    colors = img.reshape(-1, 3)
    mesh = trimesh.Trimesh(
        vertices=vertices,
        faces=faces,
        vertex_colors=colors
    )

    mesh.export(output_path)
    print(f"GLB saved to {output_path}")
