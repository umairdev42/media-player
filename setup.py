import sys
from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the actual name of your Python script
script_name = "main.py"

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable(script_name, base=base)]

build_options = {
    "packages": ["tkinter", "os", "threading", "shutil", "subprocess"],
    "include_files": ["images/", "dependencies/SpleeterGui.exe", "audio-player.py", "audio-clipper.py", "enhance-video.py", "dependencies/GridPlayer.exe", "video-converter.py", "dependencies/opencv_videoio_ffmpeg470.dll", "dependencies/SDL2.dll", "dependencies/SDL2_image.dll", "dependencies/SDL2_ttf.dll", "dependencies/SDL2_mixer.dll", "dependencies/libjpeg-9.dll", "dependencies/libFLAC-8.dll"],
}

setup(
    name="PlayerExApp",
    version="1.0",
    description="Player Ex | Media Player",
    options={"build_exe": build_options},
    executables=executables,
)
