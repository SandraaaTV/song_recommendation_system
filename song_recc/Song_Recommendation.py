

from song_recc import Camera
import pandas as pd
import random
from flask import Flask,redirect

def song_recommendations():
    emotion = Camera.snapshot()
    print(emotion)
    return emotion
    
    
    
    
    # if emotion=="Sad":
    #     return redirect('/sad_emoji')
    # if emotion=="Angry":
    #     return redirect('/angry_emoji')
    # if emotion=="Disgust":
    #     return redirect('/disgust_emoji')
    # if emotion=="Fear":
    #     return redirect('/fear_emoji')
    # if emotion=="Happy":
    #     return redirect('/happy_emoji')
    # if emotion=="Surprise":
    #     return redirect('/surprised_emoji')
    # if emotion=="Neutral":
    #     return redirect('/neutral_emoji')
    
    
    
    
    
    # csv_name = "Song_Names/" + emotion + ".csv"
    # df = pd.read_csv(csv_name)
    # data = df.values.tolist()
    # length = len(data)
    
    # r = random.sample(range(0,length), 10)
    # song_name = []
    # songs = []
    # for i in range(10):
    #     songs.append(str(data[r[i]]))
    #     song_name.append(songs[i].split('-')[0])
    #     song_name[i] = song_name[i].strip("['")
        
    # return song_name
    
    
