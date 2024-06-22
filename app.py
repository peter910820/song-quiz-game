import eel, time, asyncio, os
from pytube import YouTube, Playlist
from pydub import AudioSegment
import pygame

forbidden_char = ['/','\\',':','*','?','"','<','>',"|"]
song_path = "E:\Code\song-quiz-game\static"
music_list = []
title = ""

@eel.expose
def game_start(url):
    global title
    print(f"URL: {url}")
    url_parse = Playlist(url)
    print(url_parse.video_urls)
    for p in url_parse.video_urls:
        music_list.append(p)
    print(music_list)
    music = YouTube(music_list[0])
    title = music.title
    try:
        music.streams.filter().get_lowest_resolution().download(filename=f"{song_path}/{title}.mp4")
    except:
        for f in forbidden_char:
            title = title.replace(f," ")
        music.streams.filter().get_lowest_resolution().download(filename=f"{song_path}/{title}.mp4")
    convert_to_mp4(title)

def convert_to_mp4(title):
    audio = AudioSegment.from_file(f"{song_path}/{title}.mp4")
    audio.export(f"{song_path}/{title}.mp3", format='mp3')
    os.remove(f"{song_path}/{title}.mp4")

@eel.expose
def play():
    for _ in range(2):
        pygame.mixer.init()
        pygame.mixer.music.load(f"{song_path}/{title}.mp3")
        pygame.mixer.music.play()
        time.sleep(5)
        pygame.mixer.quit()

@eel.expose
def get_title():
    return title

@eel.expose
def next_song():
    global title
    music_list.pop(0)
    os.remove(f"{song_path}/{title}.mp3")
    music = YouTube(music_list[0])
    title = music.title
    try:
        music.streams.filter().get_lowest_resolution().download(filename=f"{song_path}/{title}.mp4")
    except:
        for f in forbidden_char:
            title = title.replace(f," ")
        music.streams.filter().get_lowest_resolution().download(filename=f"{song_path}/{title}.mp4")
    convert_to_mp4(title)
    return True

def convert_to_mp4(title):
    print(music_list)
    audio = AudioSegment.from_file(f"{song_path}/{title}.mp4")
    audio.export(f"{song_path}/{title}.mp3", format='mp3')
    os.remove(f"{song_path}/{title}.mp4")

if __name__ == "__main__":
    eel.init('interface')
    eel.start('./index.html',size = (600,600), position = (400, 100))