
# QC Assistant CLI Tool

This tool generates a Quality Control (QC) report for real estate HDR images using Python.

## Features

- Computes brightness, contrast, and blown highlight percentage
- Fills a markdown template with results
- Outputs a professional-quality QC report

## How to Use

1. Install dependencies:
```
pip install pillow numpy
```

2. Run the CLI tool:
```
python qc_generator.py <path_to_image>
```

Example:
```
python qc_generator.py brownie-13.jpg
```

The output report will be saved as `qc_report.md`.

---

This tool uses the template `qc_template.md` to match BoxBrownie-style HDR QC reviews.
