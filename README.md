# Simple Steganography Tool

A Python script that hides or extracts secret messages inside images using basic LSB (Least Significant Bit) encoding.

## How It Works

- **Hiding**: Replaces the least significant bit of image pixels with message bits.
- **Extracting**: Reads bits back and reconstructs the hidden message.

## Requirements

- `Pillow` library

Install it with:

```bash
pip install pillow
