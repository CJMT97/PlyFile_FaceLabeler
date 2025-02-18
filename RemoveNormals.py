import sys

def process_ply(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    header = []
    vertex_lines = []
    face_lines = []
    header_ended = False
    
    for line in lines:
        if not header_ended:
            header.append(line)
            if line.strip() == "end_header":
                header_ended = True
        else:
            parts = line.strip().split()
            if len(parts) == 7:  # Assuming format: x, y, z, nx, ny, nz, s
                vertex_lines.append(f"{parts[0]} {parts[1]} {parts[2]} {parts[6]}\n")
            if len(parts) == 5: 
                face_lines.append(f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} {parts[4]}\n")
    
    # Update header by removing normal properties
    new_header = []
    for line in header:
        if "property float nx" in line or "property float ny" in line or "property float nz" in line:
            continue
        new_header.append(line)
    
    with open(output_file, 'w') as f:
        f.writelines(new_header)
        f.writelines(vertex_lines)
        f.writelines(face_lines)
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_normals.py input.ply output.ply")
    else:
        process_ply(sys.argv[1], sys.argv[2])
