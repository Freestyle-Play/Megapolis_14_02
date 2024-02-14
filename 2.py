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

def quickSort(array):
    """
    quicksort
    :param songs:
    :return:
    """

    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)



if __name__ == '__main__':
    songs = readFile('songs.csv')
    quickSort(songs)
