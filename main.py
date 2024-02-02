import os
from pygifsicle import optimize
from PIL import Image
from moviepy.editor import VideoFileClip
from tkinter import Tk, filedialog
from multiprocessing import Pool

# Set important variables
IMAGE_QUALITY = 20
VIDEO_BITRATE = "2000k"
TMP_DIR = "tmp"


def ask_for_folder(message):
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=message)
    return folder_path


def compress_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'JPEG', quality=IMAGE_QUALITY)
    except OSError:
        print(f"Skipping corrupted image: {input_path}")


def compress_gif(input_path, output_path):
    # Optimize a GIF using gifsicle
    optimize(source=input_path, destination=output_path,
             options=['--colors=256', '--lossy'])


def compress_video(input_path, output_path):
    # Compress a video by reducing its bitrate
    clip = VideoFileClip(input_path)
    clip.write_videofile(os.path.join(
        TMP_DIR, output_path), bitrate=VIDEO_BITRATE)
    os.replace(os.path.join(TMP_DIR, output_path), output_path)


def process_file(file_info):
    # Process a file based on its extension
    file, input_folder, output_folder = file_info
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)

    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(f"Compressing image: {input_path} => {output_path}")
        compress_image(input_path, output_path)
    elif file.lower().endswith('.gif'):
        print(f"Compressing GIF: {input_path} => {output_path}")
        compress_gif(input_path, output_path)
    elif file.lower().endswith('.mp4'):
        print(f"Compressing video: {input_path} => {output_path}")
        compress_video(input_path, output_path)


def main():
    # Create the temporary directory if it doesn't exist
    os.makedirs(TMP_DIR, exist_ok=True)

    input_folder = ask_for_folder("Select input folder")
    output_folder = ask_for_folder("Select output folder")

    if input_folder and output_folder:
        print("Input folder:", input_folder)
        print("Output folder:", output_folder)

        file_list = os.listdir(input_folder)
        file_info_list = [(file, input_folder, output_folder) for file in file_list if file.lower(
        ).endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4'))]

        with Pool() as p:
            p.map(process_file, file_info_list)

        print("Compression completed successfully.")


if __name__ == "__main__":
    main()
