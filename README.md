# PyMediaShrinker

This script compresses images, GIFs, and videos in a given input directory and writes the compressed files to an output directory. It uses the Python Imaging Library (PIL) for image compression, the `gifsicle` command-line tool for GIF optimization, and the `moviepy` library for video compression.

## Supported Formats

- Images: PNG (.png), JPEG (.jpg, .jpeg)
- GIFs: GIF (.gif)
- Videos: MP4 (.mp4)

## Requirements

- PIL
- moviepy
- gifsicle

## Usage
1. Upon opening the script, you will be prompted to choose an input folder. **THE SCRIPT WILL CONVERT EVERYTHING SUPPORTED THAT IS INSIDE THAT FOLDER**.
2. Then you can choose an output folder.
3. Voilà! The script will do its magic.
