
from PIL import Image, ImageStat
import numpy as np

def calculate_brightness(image):
    grayscale = image.convert('L')
    stat = ImageStat.Stat(grayscale)
    return stat.mean[0] / 255.0

def calculate_contrast(image):
    grayscale = image.convert('L')
    stat = ImageStat.Stat(grayscale)
    return stat.stddev[0] / 128.0

def calculate_blown_highlights(image):
    np_img = np.array(image.convert("RGB"))
    mask = (np_img >= 250).all(axis=2)
    return mask.sum() / mask.size * 100

def load_template(path="qc_template.md"):
    with open(path, 'r') as file:
        return file.read()

def fill_template(template, metrics):
    return template.format(**metrics)

def generate_qc_report(image_path, template_path="qc_template.md", output_path="qc_report.md"):
    image = Image.open(image_path)
    brightness = calculate_brightness(image)
    contrast = calculate_contrast(image)
    blown_highlights = calculate_blown_highlights(image)

    metrics = {
        "brightness": brightness,
        "contrast": contrast,
        "blown_highlights": blown_highlights
    }

    template = load_template(template_path)
    filled_report = fill_template(template, metrics)

    with open(output_path, 'w') as f:
        f.write(filled_report)

    print(f"✅ QC report generated: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python qc_generator.py <image_path>")
    else:
        image_path = sys.argv[1]
        generate_qc_report(image_path)
