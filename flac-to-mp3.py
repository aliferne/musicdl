#!/usr/bin/env python3
"""
批量将 FLAC 文件转换为 MP3，保留文件名和元数据。
依赖：ffmpeg（需系统安装）
用法：python flac2mp3.py [目录] [比特率]
"""

import os
import sys
import subprocess
from pathlib import Path

# 默认参数
DEFAULT_BITRATE = "320k"
DEFAULT_INPUT_DIR = "."


def convert_flac_to_mp3(input_dir=".", bitrate=DEFAULT_BITRATE):
    """
    遍历 input_dir 下的所有 .flac 文件，转换为同名的 .mp3
    """
    input_path = Path(input_dir).resolve()
    if not input_path.is_dir():
        print(f"错误：'{input_path}' 不是一个有效目录")
        sys.exit(1)

    flac_files = list(input_path.glob("*.flac"))
    if not flac_files:
        print(f"在 '{input_path}' 中没有找到 .flac 文件")
        return

    print(f"找到 {len(flac_files)} 个 FLAC 文件，开始转换...")
    for flac_file in flac_files:
        mp3_file = flac_file.with_suffix(".mp3")
        if mp3_file.exists():
            # 询问是否覆盖（可添加 -y 自动覆盖）
            print(f"⚠️  '{mp3_file}' 已存在，跳过（如需覆盖请删除 -y 注释）")
            continue

        print(f"转换: {flac_file.name} -> {mp3_file.name}")
        cmd = [
            "ffmpeg",
            "-i",
            str(flac_file),
            "-ab",
            bitrate,
            "-acodec",
            "libmp3lame",
            "-map_metadata",
            "0",  # 保留元数据
            "-y",  # 自动覆盖（若想不覆盖，删除此行）
            str(mp3_file),
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ 转换失败: {flac_file.name}")
            print(e.stderr)
        except FileNotFoundError:
            print(
                "❌ 未找到 ffmpeg，请先安装：sudo apt install ffmpeg 或 brew install ffmpeg"
            )
            sys.exit(1)

    print("✅ 全部转换完成！")


if __name__ == "__main__":
    # 简单参数解析
    args = sys.argv[1:]
    input_dir = DEFAULT_INPUT_DIR
    bitrate = DEFAULT_BITRATE

    if len(args) >= 1:
        input_dir = args[0]
    if len(args) >= 2:
        bitrate = args[1]

    convert_flac_to_mp3(input_dir, bitrate)
