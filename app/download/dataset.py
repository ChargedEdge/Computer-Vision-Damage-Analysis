import os
import shutil
from sklearn.model_selection import train_test_split



def move_dataset(download_dir, model_dir, class_name):
    # Collect all the images
    images = [f for f in os.listdir(download_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]


    # Split data for testing and validation
    training_imgs, validation_imgs = train_test_split(images, train_size=0.8, test_size=0.2, random_state=42)

    # Create the output folders
    train_dir = os.path.join(model_dir, class_name, "train")
    validation_dir = os.path.join(model_dir, class_name, "validation")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)

    # Copy images
    for img in training_imgs:
        shutil.copy(os.path.join(download_dir, img), os.path.join(train_dir, img))

    for img in validation_imgs:
        shutil.copy(os.path.join(download_dir, img), os.path.join(validation_dir, img))
