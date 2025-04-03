import os

def rename_images_in_folder(folder_path, prefix="kh_doc"):
    """Renames all image files in a folder to 'prefix1.jpg', 'prefix2.png', etc.

    Args:
        folder_path: The path to the folder containing the images.
        prefix: The prefix to use for the renamed files (default: "kh_doc").
    """

    try:
        image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'))])
        for index, filename in enumerate(image_files):
            old_filepath = os.path.join(folder_path, filename)
            _, ext = os.path.splitext(filename)  # Get the file extension
            new_filename = f"{prefix}{index + 1}{ext}"
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")

        print(f"Successfully renamed {len(image_files)} images.")

    except FileNotFoundError:
        print(f"Error: Folder not found: {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
image_folder_path = "C:/Users/Sreylen/Desktop/Intern_I5/Data_Preprocessing/MPTC Layout"  # Replace with your folder path
rename_images_in_folder(image_folder_path)
