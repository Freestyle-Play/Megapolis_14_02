import csv

def readFile(filename):
    """
    Read file and create list of songs
    :param filename:
    :return: list
    """
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=",")
        songs = []
        for row in reader:
            songs.append(row)
        return songs

def search(text, songs):
    """
    search
    :param text:
    :param songs:
    :return:
    """
    for song in songs:
        if text in song["artist_name"]:
            print(f"У {song['artist_name']} найдена песня: {song['track_name']}")
            return
    print("К сожалению, ничего не удалось найти")


if __name__ == '__main__':
    songs = readFile('songs.csv')

    text = input("Введите текст: ")
    while text != "0":
        search(text, songs)
        text = input("Введите текст: ")

