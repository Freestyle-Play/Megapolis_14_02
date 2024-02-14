import csv

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


def genHash(songs):
    """
    generate hash table of songs
    :param songs: list
    :return:
    """
    for song in songs:
        print(hash(song['artist_name']))



if __name__ == '__main__':
    songs = readFile('songs.csv')
    genHash(songs)
