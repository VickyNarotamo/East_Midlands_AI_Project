import os

root_dir = "ai_powered_reader/images"

for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".txt"):
                os.remove(os.path.join(folder_path, file))
                print(f"Deleted: {file}")
