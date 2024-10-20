import os
import sys
print('Welcome to RenPy')
def rename_files(directory, base_name):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        files.sort()
        for index, filename in enumerate(files, start=1):
            file_extension = os.path.splitext(filename)[1]
            new_name = f"{base_name}-{index}{file_extension}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_name}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py ren.py <directory> <base_name>")
    else:
        directory = sys.argv[1]
        base_name = sys.argv[2]
        rename_files(directory, base_name)
