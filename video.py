from moviepy.editor import VideoFileClip
video_path = 'audio.mp4'
x=input("Play video call?:")
if x=="yes":
    clip = VideoFileClip('video/video_call.mp4')
    clip.preview()
