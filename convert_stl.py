from stl import mesh
import numpy as np    

# Load the binary STL file
binary_stl = mesh.Mesh.from_file('/Users/harqian/projects/drone_modeling/dragon.stl')

# Initialize an empty set to store unique vertices
vertices = set()

# Loop through each face of the mesh and extract the points
i = 0

def get_average_point(point1, point2, point3):
    return((point1[0] + point2[0] + point3[0]) / 3, (point1[1] + point2[1] + point3[1]) / 3, (point1[2] + point2[2] + point3[2]) / 3)

print("total points:", len(binary_stl.vectors))

for facet in binary_stl.vectors:
    average_vector = np.average(facet, axis=0)
    x, y, z = tuple(average_vector)
    if i % 606 == 0:    
        vertices.add((x, y, z))
    i += 1

print(len(vertices))

# Convert the vertices into a format suitable for Desmos
desmos_format = ','.join([f"({round(x.item() - 90, 2)}, {round(y.item() - 90, 2)}, {round(z.item(), 2)})" for x, y, z in vertices])

python_format = f"[{desmos_format}]"

# Write the result to a text file
with open("/Users/harqian/projects/drone_modeling/points_desmos.txt", 'w') as f:
    f.write(f"{{{desmos_format}}}")

with open("/Users/harqian/projects/drone_modeling/points_python.py", 'w') as f:
    f.write(f"dragon_points = {python_format}")