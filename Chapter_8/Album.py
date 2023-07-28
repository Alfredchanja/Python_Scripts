"""
Alfred Gachanja
19-07-2023
In this program I practice what I learned about functions and dictionaries.
"""

def make_album(artist_name, album_title, number_of_tracks=''):
    music_album = {'artist':  artist_name, 'album': album_title}
    if number_of_tracks:
        music_album['tracks'] = number_of_tracks
    return music_album

music = make_album('Ruth B', 'Safe Haven')
print(music)

music = make_album('JJ Heller', 'I dream of you', 15)
print(music)

while True:
    print("\nWho is you favourite artist and your favourite album from them")
    print("Enter 'q' to quit the program.\n")
    artist_nm = input("Name of the artist: ")
    if artist_nm == 'q':
        break
    album_nm = input("Name of the album: ")
    if album_nm == 'q':
        break
    tracks = input("Number of tracks in the album: ")
    if tracks == 'q':
        break

    music = make_album(artist_nm, album_nm, tracks)
    print(music)