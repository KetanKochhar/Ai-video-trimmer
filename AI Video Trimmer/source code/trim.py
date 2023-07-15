import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import AudioClip
import numpy as np
def trim():
    # Load the video clip from the location saved in txt file 
    f = open("temp.txt" , "r")
    path = f.readlines()
    video = VideoFileClip(path[0])
    f.close()

    # Get the audio of the clip
    audio = video.audio

    # Spliting the audio into chunks of 1 second
    chunks = [audio.subclip(start, start+1) for start in np.arange(0, audio.duration, 1)]

    # Calculating the volume of each chunk and store it in the form of list
    volumes = [chunk.max_volume() for chunk in chunks]

    # Calculating the average volume of the audio
    average_volume = sum(volumes) / len(volumes)

    # Find the start and end times of each silence in the audio
    silences = []

    for i in range(len(volumes)):
        if volumes[i] < average_volume - 0.1:
            start = i
            while i < len(volumes) and volumes[i] < average_volume - 0.1:
                i += 1
            end = i
            silences.append([start, end])

    print(silences)
    # print("silences found in the audio file are \n" ,silences)


    final_silences = []
    for x in range(len(silences)-1):
        if silences[x][1] == silences[x+1][1]:
            final_silences.append(silences[x])
    print(final_silences)
    for rem in range(len(final_silences)):
        if final_silences[-1][1] > int(video.duration):
            final_silences.pop()
    print(final_silences)

    # Adding the time stapms of clips that containts audio into the list audio
    audio = []
    start = 0 
    end = 0 
    for x in range(int(video.duration) + 1):
        for tup in range(len(final_silences)):
            if x == final_silences[tup][0]:
                end = x 
                dur = [start , end]
                start = final_silences[tup][1]
                # print(dur)
                audio.append(dur)
    audio[-1][1] = int(video.duration)
    print("with  audio",audio)

    # creting the new video from the list 
    for x in range(0,len(audio),1):
        START = audio[x][0]
        END = audio[x][1]
        new = video.subclip(START , END)
        new.write_videofile(f"output/output_part_{x}.mp4")
        #os.system("cls")
