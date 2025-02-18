import os
import shutil
import re

def extract_high_percentage_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    for filename in os.listdir(source_dir):
        match = re.search(r'(\d+)%', filename)
        if match:
            percentage = int(match.group(1))
            if percentage >= 60:
                source_path = os.path.join(source_dir, filename)
                dest_path = os.path.join(destination_dir, filename)
                shutil.copy(source_path, dest_path)
                print(f"Copied: {filename}")

source_directory = "Chunk_data/11_Chunks"  # Replace with actual source directory
destination_directory = "Chunk_data/11_Chunks_60%^"  # Replace with actual destination directory
extract_high_percentage_files(source_directory, destination_directory)