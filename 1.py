import csv
import datetime


# {'\ufeffstreams': '0', 'artist_name': 'Universe Infinity', 'track_name': 'Catch of My Life', 'date': '08.06.2023'}
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

def getSongs(songs):
    """
    выдает все песни по дате выхода не позже 01.01.2002
    :param songs:
    :return:
    """
    for song in songs:
        date = "01.01.2002".split('.')
        curent_date = song["date"].split(".")
        if curent_date[-1] == date[-1] and curent_date[-2] == date[-2] and curent_date[-3] == date[-3]:
            print(f"{song['track_name']} - {song['artist_name']} - {song['streams']}")

def fixReport(songs):
    """
    fix DB report
    :param songs:
    :return:
    """
    dn = "12.05.2023".split('.')
    dn = datetime.date(year=int(dn[-1]), month=int(dn[-2]), day=int(dn[-3]))
    for i in range(0, len(songs)):
        song = songs[i]
        if song["streams"] == "0":
            di = song["date"].split(".")
            di = datetime.date(year=int(di[-1]), month=int(di[-2]), day=int(di[-3]))
            Ln = len(song["artist_name"])
            Ls = len(song["track_name"])
            tn = (dn - di)/(Ln + Ls) * 10000
            if tn.days < 0: tn = tn.days * (-1)
            songs[i]["streams"] = str(tn)

def writeFile(filename):
    """
    Write new DB report
    :param filename:
    :return:
    """
    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, delimiter=",", fieldnames=["streams","artist_name","track_name","date"])
        writer.writeheader()
        for song in songs:
            writer.writerow(song)

if __name__ == '__main__':
    songs = readFile('songs.csv')
    getSongs(songs)
    fixReport(songs)
    writeFile('songs_new.csv')
