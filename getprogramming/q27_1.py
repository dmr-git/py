#!/usr/bin/python3

song_rating = {"song1": 3, "song2": 5, "song3": 4, "song4": 5, "song5": 2}

for song in song_rating.keys():
    if song_rating[song] == 5:
        print(song)
