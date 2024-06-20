###################################################################################
##    ConfusedTomatoDev
##    06\19\2024
##
##    Simple program that uses Pythong PIL (Photo Imaging Library)
##    to convert webp images to jpg AND optionally strip EXIF Data.
##    Required:
##    pip install pillow
##    pip install piexif
##
##    Usage:
##    webp_convert.py
##    1. Place images to convert in Downloads/convert/
##    1a. Or update the code to use your own working folders if needed. ln 55-59)
##    2. Answering "Y" will remove EXIF for all, or "y" for a single file.
##    3. Answering "N" will NOT removed EXIF for all, or "n" for a single file.
##    4. Converted images will be placed in Downloads/convert/converted/
## 
###################################################################################

from PIL import Image, ExifTags
import piexif
import os

def get_exif_data(img):
    try:
        exif_data = img.info.get("exif", {})
        if exif_data:
            exif_dict = piexif.load(exif_data)
            return exif_dict
        return {}
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
        return {}

def strip_metadata(image_path):
    img = Image.open(image_path)
    data = list(img.getdata())
    img_without_metadata = Image.new(img.mode, img.size)
    img_without_metadata.putdata(data)
    return img_without_metadata

def convert_image(webp_image_path, jpg_image_path, strip_exif):
    # Open the WEBP image
    img = Image.open(webp_image_path)

    if strip_exif:
        # Remove EXIF, IPTC, and XMP data
        img_without_metadata = strip_metadata(webp_image_path)
        img_without_metadata.save(jpg_image_path, "JPEG")
    else:
        img.save(jpg_image_path, "JPEG")

def process_images():
    # Define the path to the folder containing WEBP images
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "convert")

    # Define the path to the output folder for converted images
    converted_folder = os.path.join(os.path.expanduser("~"), "Downloads", "convert", "converted")

    # Create the converted folder if it doesn't exist
    if not os.path.exists(converted_folder):
        os.makedirs(converted_folder)

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
            strip_exif = False

            if exif_data:
                print(f"EXIF data for:\n{webp_image_path}\n")
                for ifd in exif_data:
                    print(f"{ifd}: {exif_data[ifd]}")

                if apply_all is None:
                    # Ask the user if they want to strip EXIF data
                    choice = input("\nStrip EXIF/IPTC/XMP data? (y/n for single photo, Y/N for all photos): ")

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
                        print("Invalid choice, skipping this image.\n\n")
                        continue
                else:
                    strip_exif = apply_all

            # Convert the image to JPG format
            jpg_image_path = os.path.join(converted_folder, webp_image.replace(".webp", ".jpg"))
            convert_image(webp_image_path, jpg_image_path, strip_exif)

            print(f"\nConverted\n{webp_image_path}\nto\n{jpg_image_path}\n\n")
        except Exception as e:
            print(f"Failed to convert {webp_image_path}: {e}\n\n")

if __name__ == "__main__":
    process_images()
