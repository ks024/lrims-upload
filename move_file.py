import os
import shutil
import argparse

def move_file(params):
    source_dir = params.source_dir
    dest_dir = params.dest_dir

    # Creating destination dir if not exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get a list of files from the source directory
    files_list = [file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file))]

    # Initialize a counter for moved files
    files_moved_count = 0

    if not files_list:
        print("No files found in the source directory.")
    else:
        # Loop through all files in the source directory
        for file in files_list:
            # Construct the source and destination file paths.
            source_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)

            try:
                # Move the file to the destination directory
                shutil.move(source_path, dest_path)
                print(f'Moved {file} to {dest_dir}.')
                files_moved_count += 1

            except shutil.Error as e:
                print(f"Error occurred while moving {file}: {e}")
            except OSError as e:
                print(f"Error occurred while moving {file}: {e}")

        print(f'\n{files_moved_count}/{len(files_list)} files moved successfully')

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Move files from a source directory to a destination directory.')
    parser.add_argument('--source_dir', type=str, help='Path to the source directory')
    parser.add_argument('--dest_dir', type=str, help='Path to the destination directory')
    args = parser.parse_args()

    # Call the move_file function with the parsed arguments
    move_file(args)
