#!/usr/bin/env python3
"""
Image watermark removal script
Removes the "通义AI" watermark from the bottom right corner of an image
"""

import cv2
import numpy as np
import argparse
import os
from pathlib import Path

def create_watermark_mask(image, watermark_region=None):
    """
    Create a mask for the watermark region
    """
    height, width = image.shape[:2]
    
    # Default watermark region (bottom right corner)
    if watermark_region is None:
        # Typical watermark location - adjust these values based on the actual watermark position
        x1 = int(width * 0.85)  # Start from 85% of width
        y1 = int(height * 0.9)  # Start from 90% of height
        x2 = width
        y2 = height
    else:
        x1, y1, x2, y2 = watermark_region
    
    # Create mask
    mask = np.zeros((height, width), dtype=np.uint8)
    mask[y1:y2, x1:x2] = 255
    
    return mask

def remove_watermark_inpaint(image_path, output_path, watermark_region=None):
    """
    Remove watermark using OpenCV inpainting
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")
    
    # Create watermark mask
    mask = create_watermark_mask(image, watermark_region)
    
    # Apply inpainting to remove the watermark
    result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    
    # Save the result
    cv2.imwrite(output_path, result)
    print(f"Watermark removed. Output saved to: {output_path}")
    
    return result

def remove_watermark_advanced(image_path, output_path):
    """
    Advanced watermark removal using multiple techniques
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")
    
    height, width = image.shape[:2]
    
    # Create a more precise mask for the watermark
    # Convert to grayscale for analysis
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Focus on the bottom right area where watermark typically appears
    roi_x1, roi_y1 = int(width * 0.7), int(height * 0.8)
    roi_x2, roi_y2 = width, height
    roi = gray[roi_y1:roi_y2, roi_x1:roi_x2]
    
    # Apply threshold to detect text-like regions
    _, thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Find contours in the ROI
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create mask
    mask = np.zeros((height, width), dtype=np.uint8)
    
    # Add detected contours to mask (shifted back to full image coordinates)
    for contour in contours:
        # Shift contour coordinates back to full image
        contour[:, :, 0] += roi_x1
        contour[:, :, 1] += roi_y1
        cv2.drawContours(mask, [contour], -1, 255, -1)
    
    # Also add a rectangular region for the typical watermark area
    mask[int(height * 0.9):height, int(width * 0.8):width] = 255
    
    # Apply morphological operations to clean up the mask
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # Apply inpainting
    result = cv2.inpaint(image, mask, 5, cv2.INPAINT_TELEA)
    
    # Save the result
    cv2.imwrite(output_path, result)
    print(f"Advanced watermark removal completed. Output saved to: {output_path}")
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Remove watermark from image')
    parser.add_argument('input_image', help='Path to input image')
    parser.add_argument('--output', '-o', help='Output image path (default: input_cleaned.jpg)')
    parser.add_argument('--method', '-m', choices=['simple', 'advanced'], default='advanced',
                       help='Watermark removal method (default: advanced)')
    parser.add_argument('--region', '-r', nargs=4, type=int, metavar=('x1', 'y1', 'x2', 'y2'),
                       help='Custom watermark region coordinates')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input_image):
        print(f"Error: Input file '{args.input_image}' not found")
        return 1
    
    # Set output path
    if args.output:
        output_path = args.output
    else:
        input_path = Path(args.input_image)
        output_path = input_path.parent / f"{input_path.stem}_cleaned{input_path.suffix}"
    
    try:
        if args.method == 'simple':
            remove_watermark_inpaint(args.input_image, output_path, args.region)
        else:
            remove_watermark_advanced(args.input_image, output_path)
        
        print("Watermark removal completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())