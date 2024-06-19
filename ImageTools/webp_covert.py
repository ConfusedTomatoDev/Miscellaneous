###################################################################################
##    ConfusedTomatoDev
##    06\19\2024
##
##    Simple program that uses Pythong PIL (Photo Imaging Library)
##    to convert webp images to jpg AND optionally strip EXIF Data.
##
##    webp_convert.py
##    1. Place images to convert in Downloads/convert 
##    1a. Or update the code to use your own folder. 
##    2. Answering "Y" will remove EXIF for all, or "y" for a single file.
##    3. Answering "N" will NOT removed EXIF for all, or "n" for a single file.
## 
#################################################################################

from PIL import Image, ExifTags
import os

def get_exif_data(img):
    try:
        exif_data = img._getexif()
        if exif_data:
            return {ExifTags.TAGS.get(tag, tag): value for tag, value in exif_data.items()}
        return {}
    except AttributeError:
        return {}

def convert_image(webp_image_path, jpg_image_path, strip_exif):
    # Open the WEBP image
    img = Image.open(webp_image_path)

    if strip_exif:
        # Remove EXIF data by creating a new image object without EXIF
        data = list(img.getdata())
        img_without_exif = Image.new(img.mode, img.size)
        img_without_exif.putdata(data)
        img_without_exif.save(jpg_image_path, "JPEG")
    else:
        img.save(jpg_image_path, "JPEG")

def process_images():
    # Define the path to the folder containing WEBP images
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "convert")

    # Get a list of all WEBP images in the folder
    webp_images = [f for f in os.listdir(downloads_folder) if f.endswith('.webp')]

    apply_all = None  # To keep track of the user's choice to apply to all images

    for webp_image in webp_images:
        try:
            # Full path to the WEBP image
            webp_image_path = os.path.join(downloads_folder, webp_image)

            # Open the WEBP image
            img = Image.open(webp_image_path)

            # Get EXIF data
            exif_data = get_exif_data(img)
            if exif_data:
                print(f"EXIF data for {webp_image_path}:")
                for tag, value in exif_data.items():
                    print(f"  {tag}: {value}")
            else:
                print(f"No EXIF data for {webp_image_path}")

            if apply_all is None:
                # Ask the user if they want to strip EXIF data
                choice = input("Strip EXIF data? (y/n for single photo, Y/N for all photos): ")

                if choice == 'Y':
                    strip_exif = True
                    apply_all = True
                elif choice == 'N':
                    strip_exif = False
                    apply_all = False
                elif choice == 'y':
                    strip_exif = True
                elif choice == 'n':
                    strip_exif = False
                else:
                    print("Invalid choice, skipping this image.")
                    continue
            else:
                strip_exif = apply_all

            # Convert the image to JPG format
            jpg_image_path = os.path.join(downloads_folder, webp_image.replace(".webp", ".jpg"))
            convert_image(webp_image_path, jpg_image_path, strip_exif)

            print(f"Converted {webp_image_path} to {jpg_image_path}")
        except Exception as e:
            print(f"Failed to convert {webp_image_path}: {e}")

if __name__ == "__main__":
    process_images()
