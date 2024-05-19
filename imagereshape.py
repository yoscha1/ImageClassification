from PIL import Image
import os

# List of image extensions to check
extensions = ['jpg', 'jpeg', 'png', 'gif']

# Directory containing images
image_dir = "images"

# List all files in the directory
images = os.listdir(image_dir)

# Process each image
for image in images:
    ext = image.split(".")[-1].lower()  # Ensure extension is lowercase for comparison
    if ext in extensions:
        im = Image.open(os.path.join(image_dir, image))
        im_resized = im.resize((32, 32))
        # Convert image to RGB if it has an alpha channel
        if im_resized.mode == 'RGBA':
            im_resized = im_resized.convert('RGB')
        # Save the resized image
        filepath = os.path.join(image_dir, f"{os.path.splitext(image)[0]}.jpg")
        im_resized.save(filepath)

