import os
import json
import random

# Directory containing files
directory = "Chunk_data/11_Chunks"

# Get files with exactly 10000 lines
def get_files_with_10000_lines(directory):
    valid_files = []
    for f in os.listdir(directory):
        file_path = os.path.join(directory, f)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                line_count = sum(1 for line in file)
                if line_count == 10000:
                    valid_files.append(os.path.splitext(f)[0])  # Append filename without extension
    return valid_files

# Retrieve valid files
files = get_files_with_10000_lines(directory)

# Ensure we only take the first 100 files if more than 100 valid files exist
#files = files[:100]

# Shuffle the files to ensure randomness
random.shuffle(files)

# Split into train (70%), validation (10%), and test (20%)
train_size = int(0.7 * len(files))  # 70 files
val_size = int(0.1 * len(files))    # 10 files
test_size = len(files) - train_size - val_size  # 20 files

train_files = files[:train_size]
val_files = files[train_size:train_size + val_size]
test_files = files[train_size + val_size:]

# Convert to JSON format
def save_json(filename, data):
    json_data = json.dumps([os.path.join(directory, f).replace("\\", "/") for f in data], indent=4)
    with open(filename, "w") as f:
        f.write(json_data)

# Save to separate JSON files
save_json("train.json", train_files)
save_json("validation.json", val_files)
save_json("test.json", test_files)
save_json("all.json", files)

print("Splitting complete! Files saved as train.json, validation.json, and test.json.")