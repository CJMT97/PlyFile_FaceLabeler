from plyfile import PlyData, PlyElement
import numpy as np
import sys

args = sys.argv[1:]

# Read the PLY file
filename = args[0]

if len(args) > 1:
    output_filename = args[0]

print('Initilising Variables...')
ply_data = PlyData.read(filename)

# Access vertices and faces
vertices = ply_data['vertex']
vertex_dtype = np.dtype([
    ('x', 'f4'),
    ('y', 'f4'),
    ('z', 'f4'),
    ('Scalar_Classification', 'f4')
])

print('Reading Vertices...')
# Convert vertices to a structured NumPy array
vertex_data = np.array([tuple(vertex) for vertex in vertices], dtype=vertex_dtype)

print('Reading Faces...')
faces = ply_data['face']
face_data = [face['vertex_indices'] for face in faces]

lbl_face_data = []
count = 0
total_faces = len(face_data)
for face_index in range(total_faces):
    if face_index % (total_faces // 10) == 0 and face_index != 0:
        progress = (face_index / total_faces) * 100
        print(f"Labeling: {progress:.0f}%")

    weights = [0, 0, 0] 

    for vertice_index in face_data[face_index]:
        if len(vertices[vertice_index]) > 3:
            weights[int(vertices[vertice_index][3])] += 1

    lbl = np.argmax(weights)
    lbl_face_data.append((face_data[face_index], lbl))

print('Formatting...')
face_dtype = np.dtype([
    ('vertex_indices', 'i4', (3,)),
    ('Scalar_Classification', 'i4')  # Using 'O' to allow a variable-length list of integers for each face
])

new_data = np.array([face for face in lbl_face_data], dtype=face_dtype)

vertex_element = PlyElement.describe(vertex_data, 'vertex')
face_element = PlyElement.describe(new_data, 'face')
print('Formatting Complete')
if len(args) > 1:
    print('Writing data to ' + output_filename)
    PlyData([vertex_element, face_element], text=True).write(output_filename)
else:
    print('Writing data to ' + filename + "_labeled.ply")
    PlyData([vertex_element, face_element], text=True).write(filename + "_labeled.ply")
print('Process Complete')