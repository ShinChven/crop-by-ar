import argparse
import logging
from pathlib import Path
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(message)s')

SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.ico', '.heif']

def parse_aspect_ratio(ratio_str):
    try:
        width, height = map(int, ratio_str.split(':'))
        if width <= 0 or height <= 0:
            raise ValueError
        return width, height
    except ValueError:
        raise argparse.ArgumentTypeError("Aspect ratio must be in the format W:H with positive integers.")

def crop_image(image_path, aspect_ratio, index, total):
    digits = len(str(total))
    logging.info(f"[{index:0{digits}}/{total}] Source:\t{image_path}")
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        target_width, target_height = aspect_ratio

        # Calculate target dimensions
        target_ratio = target_width / target_height
        img_ratio = img_width / img_height

        if img_ratio > target_ratio:
            # Image is wider than target ratio, crop width
            new_width = int(target_ratio * img_height)
            left = (img_width - new_width) // 2
            right = left + new_width
            top, bottom = 0, img_height
        else:
            # Image is taller than target ratio, crop height
            new_height = int(img_width / target_ratio)
            top = (img_height - new_height) // 2
            bottom = top + new_height
            left, right = 0, img_width

        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(image_path.with_name(image_path.stem + '-cropped' + image_path.suffix))
        logging.info(f"[{index:0{digits}}/{total}] Saved:\t{image_path.with_name(image_path.stem + '-cropped' + image_path.suffix)}")

def process_images(path, aspect_ratio):
    image_paths = list(path.rglob('*')) if path.is_dir() else [path]
    image_paths = [p for p in image_paths if p.suffix.lower() in SUPPORTED_EXTENSIONS]
    total_images = len(image_paths)

    for index, image_path in enumerate(image_paths, start=1):
        crop_image(image_path, aspect_ratio, index, total_images)

def main():
    parser = argparse.ArgumentParser(description="Crop images to a specified aspect ratio.")
    parser.add_argument('path', type=Path, help="Path to an image file or directory containing images.")
    parser.add_argument('aspect_ratio', type=parse_aspect_ratio, help="Target aspect ratio in the format W:H.")
    args = parser.parse_args()

    process_images(args.path, args.aspect_ratio)

if __name__ == "__main__":
    main()
