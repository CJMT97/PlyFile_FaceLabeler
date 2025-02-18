from plyfile import PlyData, PlyElement
import numpy as np
import sys
import os

args = sys.argv[1:]

# Read the PLY file
filename = args[0]
output_filename = filename + "_output"
prefix = " "

if len(args) > 1:
    prefix = args[1]

print('Initilising Variables...')
ply_data = PlyData.read(filename)

vertices = ply_data['vertex']
vertex_dtype = np.dtype([
    ('x', 'f4'),
    ('y', 'f4'),
    ('z', 'f4'),
    ('nx', 'f4'),
    ('ny', 'f4'),
    ('nz', 'f4'),
    ('Scalar_Classification', 'i4'),
    ('Point_ID', 'i4')
])

temp_list = []
for i in range(len(vertices)):
    temp = list(vertices[i])
    temp.append(i)
    temp_list.append(tuple(temp))

result = np.array(temp_list, dtype=vertex_dtype)
vertex_data = np.array([tuple(vertex) for vertex in result], dtype=vertex_dtype)

#np.savetxt(output_filename + ".txt", vertex_data, fmt='%f')

num_vertices = len(vertex_data)
indices = np.arange(num_vertices)
np.random.shuffle(indices)

np.savetxt(
    "test.txt",
    vertex_data,
    fmt='%f %f %f %f %f %f %d %d'
)

# chunk_size = 10000
# chunks = [indices[i:i + chunk_size] for i in range(0, num_vertices, chunk_size)]

# print(f"Total vertices: {num_vertices}")
# print(f"Chunk size: {chunk_size}")
# print(f"Number of chunks: {len(chunks)}")

# # Change this to the required filename
# directory = "Chunk_data/6_Chunks_nonormal"

# # Create directory if it does not exist
# if not os.path.exists(directory):
#     os.makedirs(directory)
#     print(f"Directory '{directory}' created successfully.")
# else:
#     print(f"Directory '{directory}' already exists.")

# for chunk_idx, chunk in enumerate(chunks):
#     sampled_vertices = vertex_data[chunk]

#      # Reset Point_IDs within the chunk
#     for i, vertex in enumerate(sampled_vertices):
#         vertex['Point_ID'] = i  # Reassign the Point_ID to start from 0 for each chunk

#     output = os.path.join(directory, f"{prefix}{chunk_idx + 1}.txt")

#     print(f"Saving chunk {chunk_idx + 1}/{len(chunks)} to {output}...")
#     np.savetxt(
#         output,
#         sampled_vertices,
#         fmt='%f %f %f %f %f %f %d %d'
#     )

# print("All chunks have been saved!")
