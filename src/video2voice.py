import moviepy.editor as mp


def video2voice(VIDEO_FILE):
    #clip = mp.VideoFileClip("C:\\Users\\01097\\PycharmProjects\\untitled\\video\\"+VIDEO_FILE)
    #clip.audio.write_audiofile("C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\test10.wav")

    clip = mp.VideoFileClip("/home/ubuntu/capstone-2020-4/src/video" + VIDEO_FILE)
    clip.audio.write_audiofile("/home/ubuntu/capstone-2020-4/src/voice/test10.wav")

    print("finished extract voice")


video2voice("test3.mp4")