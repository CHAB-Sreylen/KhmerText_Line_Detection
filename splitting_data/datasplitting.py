
import os
import random
import shutil

# Original directories for images and labels
orig_images_path = "C:/16000Doc/sample5/images"
orig_labels_path = "C:/16000Doc/sample5/labels"

DATASET_PATH = "E:/TextLine/KhmerText_Line_Detection/16000data"

# Create YOLO folder structure
subdirs = [
    "images/train", "images/val", "images/test",
    "labels/train", "labels/val", "labels/test"
]
for subdir in subdirs:
    os.makedirs(os.path.join(DATASET_PATH, subdir), exist_ok=True)

# Get list of image files
image_files = [
    f for f in os.listdir(orig_images_path)
    if f.lower().endswith(('.png', '.jpg', '.jpeg')) and os.path.isfile(os.path.join(orig_images_path, f))
]

print(f"Found {len(image_files)} images")

# Shuffle images
random.seed(42)
random.shuffle(image_files)

# Split into 80% train, 10% validation, 10% testing
train_split = int(len(image_files) * 0.8)
val_split = int(len(image_files) * 0.9)  # 90% includes both train and val

train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]

def get_label_filename(image_filename):
    base, _ = os.path.splitext(image_filename)
    return base + ".txt"

def move_files(file_list, subset):
    for img in file_list:
        src_img = os.path.join(orig_images_path, img)
        dest_img = os.path.join(DATASET_PATH, f"images/{subset}", img)

        label_file = get_label_filename(img)
        src_label = os.path.join(orig_labels_path, label_file)
        dest_label = os.path.join(DATASET_PATH, f"labels/{subset}", label_file)

        if not os.path.isfile(src_label):
            print(f"Warning: Label not found - {src_label}")
            continue

        shutil.copy2(src_img, dest_img)
        shutil.copy2(src_label, dest_label)

    print(f"Moved {len(file_list)} images and labels to {subset} set")

# Move files to respective directories
move_files(train_files, 'train')
move_files(val_files, 'val')
move_files(test_files, 'test')

print("Dataset preparation complete.")
