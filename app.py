from moviepy.editor import *


def videoMaker(video_path, audio_path, videoName, video_start_time, video_end_time, audio_start_time, audio_end_time):
    video = VideoFileClip(video_path).subclip(video_start_time, video_end_time)
    audio = AudioFileClip(audio_path).subclip(audio_start_time, audio_end_time)
    
    video_with_audio = video.set_audio(audio)
    output_path = videoName
    
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    audio.close()
    video.close()


