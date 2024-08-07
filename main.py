import os

def rename_files_in_directory(directory, lookup_name, replacement_name):
    for filename in os.listdir(directory):
        # Check if the file contains the lookup_name
        if lookup_name in filename:
            # Create the new filename by replacing lookup_name with replacement_name
            base_name, ext = os.path.splitext(filename)
            new_base_name = base_name.replace(lookup_name, replacement_name)
            new_filename = new_base_name + ext

            # Get the full path for the old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Check if the new filename already exists
            if os.path.exists(new_file):
                print(f'Skipped renaming {filename} -> {new_filename} because the new file already exists.')
            else:
                # Rename the file
                os.rename(old_file, new_file)
                print(f'Renamed: {filename} -> {new_filename}')

def get_filepath():
    while True:
        filepath = input("Enter your folder path: ")

        # Remove surrounding quotes if present
        if filepath.startswith('"') and filepath.endswith('"'):
            filepath = filepath[1:-1]

        # Replace backslashes with forward slashes
        filepath = filepath.replace('\\', '/')

        # Check if the path is a directory
        if os.path.isdir(filepath):
            return filepath
        else:
            print("This is not a folder. Please enter a folder path!")

def main():
    filepath = get_filepath()
    lookup_string = input("Enter the string that you want to update: ")
    new_string = input("Enter the new string that you want to enter: ")
    rename_files_in_directory(filepath, lookup_string, new_string)

if __name__ == '__main__':
    main()
