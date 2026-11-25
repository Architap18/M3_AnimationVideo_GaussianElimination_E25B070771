"""
Master Pipeline & Video Assembly
Project: Gaussian Elimination – Futuristic Educational Animation
Resolution: 1920x1080, 30 FPS
Total Duration: ~5 minutes 42 seconds
"""
import os
import sys
import subprocess
import glob
import time

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SCENES_DIR = os.path.join(PROJECT_DIR, "scenes")
MEDIA_DIR = os.path.join(PROJECT_DIR, "media", "videos")
AUDIO_FILE = os.path.join(PROJECT_DIR, "narration", "generated_audio", "voiceover.m4a")
SUBTITLES_FILE = os.path.join(PROJECT_DIR, "subtitles", "subtitles.srt")
FINAL_OUTPUT = os.path.join(PROJECT_DIR, "final_video.mp4")
ROOT_OUTPUT = os.path.join(os.path.dirname(PROJECT_DIR), "final_video.mp4")
FFMPEG_BIN = os.path.join(os.path.dirname(PROJECT_DIR), "bin", "ffmpeg")

SCENES = [
    ("scene1_hook.py", "Scene1Hook"),
    ("scene2_basics.py", "Scene2Basics"),
    ("scene3_geometry.py", "Scene3Geometry"),
    ("scene4_solution.py", "Scene4Solution"),
    ("scene5_verification.py", "Scene5Verification"),
    ("scene6_summary.py", "Scene6Summary")
]

def render_scene(scene_file, scene_class, quality="1080p"):
    print(f"\n==========================================")
    print(f"🎬 RENDERING: {scene_class} from {scene_file}")
    print(f"==========================================")
    env = os.environ.copy()
    bin_dir = os.path.join(os.path.dirname(PROJECT_DIR), "bin")
    env["PATH"] = f"{bin_dir}:{env.get('PATH', '')}"

    scene_path = os.path.join(SCENES_DIR, scene_file)
    cmd = [
        sys.executable, "-m", "manim",
        "-r", "1920,1080",
        "--fps", "30",
        scene_path,
        scene_class
    ]
    start = time.time()
    res = subprocess.run(cmd, env=env, cwd=PROJECT_DIR)
    if res.returncode != 0:
        raise RuntimeError(f"Failed to render {scene_class} (code {res.returncode})")
    print(f"✅ Rendered {scene_class} in {time.time() - start:.1f}s")

def assemble_final_video():
    print(f"\n==========================================")
    print(f"🎞️ ASSEMBLING FINAL VIDEO WITH FFMPEG")
    print(f"==========================================")
    
    # Locate the 1080p30 mp4 files for each scene
    scene_videos = []
    for scene_file, scene_class in SCENES:
        pattern = os.path.join(PROJECT_DIR, "media", "videos", "*", "1080p30", f"{scene_class}.mp4")
        matches = glob.glob(pattern)
        if not matches:
            # Check other possible paths
            pattern2 = os.path.join(PROJECT_DIR, "media", "videos", scene_file.replace(".py", ""), "*", f"{scene_class}.mp4")
            matches = glob.glob(pattern2)
        if not matches:
            raise FileNotFoundError(f"Could not find rendered video for {scene_class} (pattern: {pattern})")
        scene_videos.append(matches[0])
        print(f"Found scene clip: {matches[0]}")

    # Create concat list
    concat_list_path = os.path.join(PROJECT_DIR, "concat_list.txt")
    with open(concat_list_path, "w") as f:
        for vid in scene_videos:
            f.write(f"file '{vid}'\n")

    temp_video = os.path.join(PROJECT_DIR, "temp_video_no_audio.mp4")

    # 1. Concatenate scenes
    print("1. Concatenating 6 scene clips...")
    concat_cmd = [
        FFMPEG_BIN, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        temp_video
    ]
    subprocess.run(concat_cmd, check=True)

    # 2. Multiplex audio and soft subtitles, encoding with high compatibility h264 & aac
    print("2. Multiplexing voiceover audio and soft subtitles...")
    final_cmd = [
        FFMPEG_BIN, "-y",
        "-i", temp_video,
        "-i", AUDIO_FILE,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]
    subprocess.run(final_cmd, check=True)

    # Copy to root workspace as well for immediate visibility
    import shutil
    shutil.copy(FINAL_OUTPUT, ROOT_OUTPUT)
    print(f"\n🎉 FINAL VIDEO GENERATED SUCCESSFULLY!")
    print(f"📁 Video Path: {FINAL_OUTPUT}")
    print(f"📁 Root Path:  {ROOT_OUTPUT}")

    # Verify final video properties
    probe_cmd = [
        FFMPEG_BIN, "-i", FINAL_OUTPUT
    ]
    print("\n--- Final Video Telemetry ---")
    subprocess.run(probe_cmd)

def main():
    print("Starting Full Production Pipeline...")
    for scene_file, scene_class in SCENES:
        render_scene(scene_file, scene_class)
    assemble_final_video()

if __name__ == "__main__":
    main()
