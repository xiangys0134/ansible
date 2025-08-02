# 通义AI水印去除工具 / TongYi AI Watermark Removal Tool

这个工具集专门用于去除图片中的"通义AI"水印，使用OpenCV的图像修复技术。

This toolkit is designed to remove "通义AI" watermarks from images using OpenCV inpainting techniques.

## 功能特点 / Features

- 🎯 专门针对"通义AI"水印优化
- 🔍 智能水印区域检测
- 🛠️ 多种图像修复算法
- 📊 支持多种图片格式 (JPG, PNG, BMP)
- 🎨 高质量的修复效果

## 安装依赖 / Installation

```bash
# 安装系统依赖
sudo apt update
sudo apt install -y python3-opencv python3-numpy python3-pil python3-venv

# 或者使用 pip (需要虚拟环境)
pip install opencv-python numpy Pillow
```

## 使用方法 / Usage

### 1. 专门的通义AI水印去除工具

```bash
# 基本用法
python3 remove_tongyi_watermark.py your_image.jpg

# 指定输出文件名
python3 remove_tongyi_watermark.py your_image.jpg --output clean_image.jpg
```

### 2. 通用水印去除工具

```bash
# 高级模式 (推荐)
python3 remove_watermark.py your_image.jpg --method advanced

# 简单模式
python3 remove_watermark.py your_image.jpg --method simple

# 自定义水印区域
python3 remove_watermark.py your_image.jpg --region x1 y1 x2 y2
```

### 3. 交互式帮助工具

```bash
python3 process_user_image.py
```

## 工具说明 / Tool Description

### remove_tongyi_watermark.py
专门针对"通义AI"水印设计的高级去除工具：
- 智能检测水印位置
- 使用多种阈值技术
- 应用形态学操作优化
- 支持TELEA和Navier-Stokes修复算法

### remove_watermark.py
通用水印去除工具：
- 支持自定义水印区域
- 多种修复方法
- 适用于各种类型的水印

### save_image.py
测试图片生成器：
- 创建带有"通义AI"水印的测试图片
- 用于验证工具效果

## 输出文件 / Output Files

- `*_no_watermark.jpg` - 去除水印后的图片
- `*_mask.jpg` - 检测到的水印区域遮罩 (调试用)

## 技术原理 / Technical Details

1. **水印检测**: 使用自适应阈值和OTSU阈值的组合检测文本区域
2. **区域优化**: 通过形态学操作清理和连接文本组件
3. **图像修复**: 使用OpenCV的TELEA和Navier-Stokes算法进行图像修复
4. **后处理**: 应用高斯模糊和混合技术优化修复效果

## 使用示例 / Examples

```bash
# 示例1：处理单个图片
python3 remove_tongyi_watermark.py photo.jpg

# 示例2：批量处理 (bash)
for img in *.jpg; do
    python3 remove_tongyi_watermark.py "$img"
done

# 示例3：指定输出目录
python3 remove_tongyi_watermark.py input.jpg --output ./cleaned/output.jpg
```

## 注意事项 / Notes

1. 输入图片应为常见格式 (JPG, PNG, BMP)
2. 水印通常位于图片右下角，工具会自动检测
3. 对于复杂背景，可能需要手动调整参数
4. 建议先用测试图片验证效果

## 故障排除 / Troubleshooting

### 常见问题

1. **导入错误**: 确保已安装OpenCV
   ```bash
   python3 -c "import cv2; print(cv2.__version__)"
   ```

2. **权限错误**: 确保有读写文件的权限

3. **效果不佳**: 尝试使用通用工具并手动指定水印区域

## 许可证 / License

MIT License

## 贡献 / Contributing

欢迎提交Issue和Pull Request来改进这个工具。

## 更新日志 / Changelog

- v1.0: 初始版本，支持基本的水印去除功能
- v1.1: 添加了专门的通义AI水印检测算法
- v1.2: 改进了图像修复质量和处理速度