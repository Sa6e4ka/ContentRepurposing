from moviepy.editor import VideoFileClip, concatenate_videoclips
# pip install moviepy

def merge_videos(video_paths, output_dir='output.mp4'):
    clips = [VideoFileClip(video) for video in video_paths]

    final_clip = concatenate_videoclips(clips, method="compose")

    final_clip.write_videofile(output_dir, codec='libx264', audio_codec='aac', preset='medium', threads=4, bitrate='2000k')


