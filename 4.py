import csv
import string


def readFile(filename):
    """
    Read file and create list of songs
    :param filename: str
    :return: list
    """
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=",")
        songs = []
        for row in reader:
            songs.append(row)
        return songs

def findRussianArtist(songs):
    """
    find Russian artist and foreign artists
    :param songs: list
    :return:
    """
    russian_artists = []
    foreign_artists = []
    alphabet = "".join([chr(letters) for letters in range(1040, 1103+1)]) + "ёЁ"
    for song in songs:
        if song["artist_name"][0] in alphabet:
            if song["artist_name"] not in russian_artists:
                russian_artists.append(song["artist_name"])
        else:
            if song["artist_name"] not in foreign_artists:
                foreign_artists.append(song["artist_name"])
    print(f"Количество российских исполнителей: {len(russian_artists)}")
    print(f"Количество иностранных исполнителей: {len(foreign_artists)}")
    return russian_artists






if __name__ == '__main__':
    songs = readFile('songs.csv')
    russian_artists = findRussianArtist(songs)
