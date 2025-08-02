#!/usr/bin/env python3
"""
Specialized script for removing "通义AI" watermark from images
"""

import cv2
import numpy as np
import argparse
import os
from pathlib import Path

def detect_watermark_region(image):
    """
    Detect the watermark region more precisely
    """
    height, width = image.shape[:2]
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Focus on bottom right quadrant where watermarks typically appear
    roi_height = height // 3
    roi_width = width // 3
    roi_x = width - roi_width
    roi_y = height - roi_height
    
    roi = gray[roi_y:height, roi_x:width]
    
    # Apply threshold to detect text-like regions
    # Use adaptive threshold for better text detection
    adaptive_thresh = cv2.adaptiveThreshold(
        roi, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )
    
    # Also try regular threshold
    _, regular_thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Combine both thresholds
    combined_thresh = cv2.bitwise_or(adaptive_thresh, regular_thresh)
    
    # Apply morphological operations to clean up and connect text components
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    combined_thresh = cv2.morphologyEx(combined_thresh, cv2.MORPH_CLOSE, kernel)
    
    # Find contours
    contours, _ = cv2.findContours(combined_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create full image mask
    mask = np.zeros((height, width), dtype=np.uint8)
    
    # Filter contours by size and add to mask
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  # Filter out very small noise
            # Shift contour coordinates back to full image
            shifted_contour = contour.copy()
            shifted_contour[:, :, 0] += roi_x
            shifted_contour[:, :, 1] += roi_y
            cv2.drawContours(mask, [shifted_contour], -1, 255, -1)
    
    # Add a broader region in the bottom right as backup
    backup_x1, backup_y1 = int(width * 0.75), int(height * 0.85)
    backup_x2, backup_y2 = width, height
    cv2.rectangle(mask, (backup_x1, backup_y1), (backup_x2, backup_y2), 255, -1)
    
    # Apply morphological operations to final mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    return mask

def remove_watermark_advanced(image_path, output_path):
    """
    Advanced watermark removal with multiple inpainting methods
    """
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")
    
    print(f"Processing image: {image.shape}")
    
    # Detect watermark region
    mask = detect_watermark_region(image)
    
    # Save mask for debugging
    mask_path = output_path.replace('.jpg', '_mask.jpg').replace('.png', '_mask.png')
    cv2.imwrite(mask_path, mask)
    print(f"Mask saved to: {mask_path}")
    
    # Try different inpainting methods
    methods = [
        (cv2.INPAINT_TELEA, "TELEA"),
        (cv2.INPAINT_NS, "Navier-Stokes")
    ]
    
    best_result = None
    best_method = None
    
    for method, method_name in methods:
        print(f"Trying {method_name} inpainting...")
        result = cv2.inpaint(image, mask, 7, method)
        
        if best_result is None:
            best_result = result
            best_method = method_name
        else:
            # You could add quality comparison here if needed
            best_result = result
            best_method = method_name
    
    # Apply additional smoothing to the inpainted region
    # Create a slightly dilated mask for blending
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    dilated_mask = cv2.dilate(mask, kernel, iterations=1)
    
    # Apply Gaussian blur to smooth the inpainted region
    blurred = cv2.GaussianBlur(best_result, (5, 5), 0)
    
    # Blend the blurred inpainted region with the original
    mask_norm = dilated_mask.astype(np.float32) / 255.0
    mask_norm = np.expand_dims(mask_norm, axis=2)
    
    final_result = (best_result.astype(np.float32) * (1 - mask_norm) + 
                   blurred.astype(np.float32) * mask_norm).astype(np.uint8)
    
    # Save the result
    cv2.imwrite(output_path, final_result)
    print(f"Watermark removed using {best_method}. Output saved to: {output_path}")
    
    return final_result

def main():
    parser = argparse.ArgumentParser(description='Remove "通义AI" watermark from image')
    parser.add_argument('input_image', help='Path to input image')
    parser.add_argument('--output', '-o', help='Output image path (default: input_no_watermark.jpg)')
    
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
        output_path = input_path.parent / f"{input_path.stem}_no_watermark{input_path.suffix}"
    
    try:
        remove_watermark_advanced(args.input_image, str(output_path))
        print("Watermark removal completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())