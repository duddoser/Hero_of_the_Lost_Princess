from pydub import AudioSegment

a = AudioSegment.from_mp3("data/background_music_1.mp3")
b = AudioSegment.from_mp3("data/background_music_2.mp3")
c = AudioSegment.from_mp3("data/background_music_3.mp3")
a.export("data/background_music_1.ogg", format="ogg")
b.export("data/background_music_2.ogg", format="ogg")
c.export("data/background_music_3.ogg", format="ogg")
