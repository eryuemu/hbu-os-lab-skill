#!/usr/bin/env python3
"""
crop_photos.py
河北大学选修课操作系统实验照片预处理脚本

功能：
1. 自动检测并裁剪手机翻拍照片四周的冗余边缘及底部相机水印（如 realme / iPhone 边框与文字）。
2. 将超大分辨率图片等比压缩至适合文档排版的适度尺寸（最大宽 1920px，LANCZOS 高质量抗锯齿）。
3. 保证插入 DOCX 后的体积适中，排版紧凑。
"""

import os
import sys
import argparse
from PIL import Image

def process_image(input_path, output_path, crop_bottom_pct=0.06, crop_top_pct=0.02, crop_side_pct=0.03, max_width=1920):
    try:
        with Image.open(input_path) as img:
            img = img.convert('RGB')
            w, h = img.size
            
            # 计算裁剪边界
            left = int(w * crop_side_pct)
            right = int(w * (1.0 - crop_side_pct))
            top = int(h * crop_top_pct)
            bottom = int(h * (1.0 - crop_bottom_pct))
            
            cropped = img.crop((left, top, right, bottom))
            cw, ch = cropped.size
            
            # 缩放至适宜宽度
            if cw > max_width:
                scale = max_width / float(cw)
                new_size = (max_width, int(ch * scale))
                cropped = cropped.resize(new_size, Image.Resampling.LANCZOS)
            
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            cropped.save(output_path, 'PNG', quality=90)
            print(f"[OK] {os.path.basename(input_path)} -> {output_path} ({cropped.size[0]}x{cropped.size[1]})")
            return True
    except Exception as e:
        print(f"[ERROR] Failed to process {input_path}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Preprocess and crop photos for HBU OS Lab Reports.")
    parser.add_argument("--input", "-i", nargs="+", help="Input image file(s) or directories.")
    parser.add_argument("--output_dir", "-o", required=True, help="Target output directory for cleaned images.")
    parser.add_argument("--crop_bottom", type=float, default=0.06, help="Bottom crop percentage to eliminate watermark (default 0.06).")
    parser.add_argument("--max_width", type=int, default=1920, help="Max width in pixels (default 1920).")
    
    args = parser.parse_args()
    
    inputs = []
    if args.input:
        for inp in args.input:
            if os.path.isdir(inp):
                for f in sorted(os.listdir(inp)):
                    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                        inputs.append(os.path.join(inp, f))
            elif os.path.isfile(inp):
                inputs.append(inp)
                
    if not inputs:
        print("No valid input images found.")
        sys.exit(1)
        
    for idx, img_path in enumerate(inputs, 1):
        ext = ".png"
        out_name = f"fig_{idx:02d}_{os.path.splitext(os.path.basename(img_path))[0]}{ext}"
        out_path = os.path.join(args.output_dir, out_name)
        process_image(img_path, out_path, crop_bottom_pct=args.crop_bottom, max_width=args.max_width)

if __name__ == "__main__":
    main()
