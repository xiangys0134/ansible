#!/usr/bin/env python3
"""
Script to help process user's actual image
"""

import os
import sys

def show_usage_instructions():
    """Show instructions for using the watermark removal tools"""
    print("=== 通义AI 水印去除工具使用说明 ===")
    print()
    print("您有以下几种方式来处理您的图片：")
    print()
    print("方法1：如果您的图片已经保存在此目录中")
    print("   python3 remove_tongyi_watermark.py 您的图片名.jpg")
    print()
    print("方法2：使用通用水印去除工具")
    print("   python3 remove_watermark.py 您的图片名.jpg --method advanced")
    print()
    print("方法3：自定义水印区域")
    print("   python3 remove_watermark.py 您的图片名.jpg --region x1 y1 x2 y2")
    print("   (其中 x1,y1,x2,y2 是水印区域的坐标)")
    print()
    print("可用的工具文件：")
    print("   - remove_tongyi_watermark.py: 专门针对'通义AI'水印的优化工具")
    print("   - remove_watermark.py: 通用水印去除工具")
    print("   - save_image.py: 用于创建测试图片")
    print()
    print("输出文件：")
    print("   - 处理后的图片将保存为 *_no_watermark.jpg 或您指定的文件名")
    print("   - 生成的遮罩文件保存为 *_mask.jpg (用于调试)")
    print()
    print("示例命令：")
    print("   python3 remove_tongyi_watermark.py your_image.jpg")
    print("   python3 remove_tongyi_watermark.py your_image.jpg --output clean_image.jpg")
    print()

def list_available_files():
    """List files in current directory"""
    print("当前目录中的文件：")
    files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    if files:
        for f in files:
            print(f"   - {f}")
    else:
        print("   未找到图片文件")
    print()

def main():
    print("通义AI水印去除工具")
    print("=" * 50)
    
    list_available_files()
    show_usage_instructions()
    
    # Check if user provided an image file argument
    if len(sys.argv) > 1:
        image_file = sys.argv[1]
        if os.path.exists(image_file):
            print(f"检测到图片文件: {image_file}")
            print("正在处理...")
            
            # Process with the specialized tool
            os.system(f"python3 remove_tongyi_watermark.py {image_file}")
        else:
            print(f"错误：文件 '{image_file}' 不存在")
    else:
        print("要处理图片，请运行：")
        print("   python3 process_user_image.py 您的图片文件名.jpg")

if __name__ == "__main__":
    main()