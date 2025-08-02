#!/usr/bin/env python3
"""
Script to create a test image with watermark for demonstration
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_test_image():
    """Create a test image with watermark for demonstration"""
    # Create a test image that simulates the user's image
    img = Image.new('RGB', (1080, 1080), color='lightgray')
    draw = ImageDraw.Draw(img)
    
    # Add some server room-like content
    # Background
    draw.rectangle([0, 0, 1080, 1080], fill=(240, 240, 240))
    
    # Add some server rack representations
    for i in range(3):
        x = 150 + i * 300
        draw.rectangle([x, 200, x + 200, 800], fill='darkblue', outline='black', width=3)
        
        # Add some lights/indicators
        for j in range(8):
            y = 250 + j * 60
            draw.ellipse([x + 20, y, x + 40, y + 20], fill='green')
            draw.ellipse([x + 60, y, x + 80, y + 20], fill='red')
    
    # Add some people silhouettes (simplified)
    draw.ellipse([300, 600, 350, 650], fill='navy')  # head
    draw.rectangle([310, 650, 340, 750], fill='navy')  # body
    
    draw.ellipse([500, 600, 550, 650], fill='navy')  # head
    draw.rectangle([510, 650, 540, 750], fill='navy')  # body
    
    # Add the watermark in bottom right corner (this is what we want to remove)
    try:
        # Try to create a larger font for the watermark
        font_size = 40
        try:
            # This might not work on all systems, but worth trying
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
        except:
            font = ImageFont.load_default()
    except:
        font = None
    
    # Add watermark
    watermark_text = "通义AI"
    watermark_position = (900, 1000)  # Bottom right area
    draw.text(watermark_position, watermark_text, fill='gray', font=font)
    
    # Save the test image
    img.save('input_image.jpg', 'JPEG', quality=95)
    print("Test image with watermark created: input_image.jpg")
    print(f"Image size: {img.size}")
    
    return 'input_image.jpg'

if __name__ == "__main__":
    create_test_image()