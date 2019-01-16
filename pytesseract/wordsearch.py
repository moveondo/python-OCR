from tkinter import *
from PIL import Image
import pytesseract

root = Tk()


# resizes the wordsearch and turns into text
def translate(image):
    im = Image.open(image)
    basewidth = 2200
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), Image.ANTIALIAS)
    text = pytesseract.image_to_string(im, lang="chi_sim")

    return text


def toGrid(array):
    rowLength = array.index('\n')
    grid = []

    grid.append(array[:rowLength])
    array = array[rowLength:]

    while array:
        array = array[1:]
        grid.append(array[:rowLength])
        array = array[rowLength:]

    return grid


def toBank(array):
    grid = []

    length = array.index('\n')
    grid.append(array[:length])
    array = array[length:]

    while array:
        array = array[1:]
        try:
            length = array.index('\n')
            grid.append(array[:length])
            array = array[length:]
        except:
            grid.append(array[0:])
            array = []

    bank = []

    for word in grid:
        bank.append(''.join(word))

    return bank


highlight = []


def highlightpos(wordlen, pos, direction):
    for i in range(0, wordlen):
        if direction == 'N':
            highlight.append([pos[0] - i, pos[1]])
        elif direction == 'NE':
            highlight.append([pos[0] - i, pos[1] + i])
        elif direction == 'E':
            highlight.append([pos[0], pos[1] + i])
        elif direction == 'SE':
            highlight.append([pos[0] + i, pos[1] + i])
        elif direction == 'S':
            highlight.append([pos[0] + i, pos[1]])
        elif direction == 'SW':
            highlight.append([pos[0] + i, pos[1] - i])
        elif direction == 'W':
            highlight.append([pos[0], pos[1] - i])
        elif direction == 'NW':
            highlight.append([pos[0] - i, pos[1] - i])


def checkFirst(grid, word):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            try:
                if grid[i][j] == word[0]:
                    pos = [i, j]
                    checkSecond(grid, word, pos)
                else:
                    pass
            except:
                pass


def checkSecond(grid, word, pos):
    xy = pos.copy()
    for i in range(0, 1):
        try:
            if grid[pos[0] - 1][pos[1]] == word[1] and directionSearch(grid, pos, "N", word):
                highlightpos(len(word), xy, "N")
                print(word, xy, "N")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] - 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "NE", word):
                highlightpos(len(word), xy, "NE")
                print(word, xy, "NE")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0]][pos[1] + 1] == word[1] and directionSearch(grid, pos, "E", word):
                highlightpos(len(word), xy, "E")
                print(word, xy, "E")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1] + 1] == word[1] and directionSearch(grid, pos, "SE", word):
                highlightpos(len(word), xy, "SE")
                print(word, xy, "SE")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1]] == word[1] and directionSearch(grid, pos, "S", word):
                highlightpos(len(word), xy, "S")
                print(word, xy, "S")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] + 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "SW", word):
                highlightpos(len(word), xy, "SW")
                print(word,len(word), xy, "SW")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0]][pos[1] - 1] == word[1] and directionSearch(grid, pos, "W", word):
                highlightpos(len(word), xy, "W")
                print(word, xy, "W")
                break
            else:
                pass
        except:
            pass
        try:
            if grid[pos[0] - 1][pos[1] - 1] == word[1] and directionSearch(grid, pos, "NW", word):
                highlightpos(len(word), xy, "NW")
                print(word, xy, "NW")
                break
            else:
                pass
        except:
            pass


def nDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -= 1
            else:
                return False
        elif position[0] == 0:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def neDirection(array, position, word):
    width = len(array[0]) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0 and position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -= 1
                position[1] += 1
            else:
                return False
        elif position[0] == 0 or position[1] == width:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def eDirection(array, position, word):
    width = len(array[0]) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[1] += 1
            else:
                return False
        elif position[1] == width:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def seDirection(array, position, word):
    height = len(array) - 1
    width = len(array[0]) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height and position[1] != width:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] += 1
                position[1] += 1
            else:
                return False
        elif position[0] == height or position[1] == width:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def sDirection(array, position, word):
    height = len(array) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] += 1
            else:
                return False
        elif position[0] == height:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def swDirection(array, position, word):
    height = len(array) - 1
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != height and position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] += 1
                position[1] -= 1
            else:
                return False
        elif position[0] == height or position[1] == 0:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def wDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[1] -= 1
            else:
                return False
        elif position[1] == 0:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def nwDirection(array, position, word):
    possible = True
    while possible:
        if word == "":
            return True
        elif position[0] != 0 and position[1] != 0:
            if word[0] == array[position[0]][position[1]]:
                word = word[1:]
                position[0] -= 1
                position[1] -= 1
            else:
                return False
        elif position[0] == 0 or position[1] == 0:
            if len(word) > 1:
                return False
            elif word != array[position[0]][position[1]]:
                return False
            else:
                return True


def directionSearch(array, position, direction, word):
    temppos = position.copy()
    if direction == "N":
        return nDirection(array, temppos, word)
    elif direction == "NE":
        return neDirection(array, temppos, word)
    elif direction == "E":
        return eDirection(array, temppos, word)
    elif direction == "SE":
        return seDirection(array, temppos, word)
    elif direction == "S":
        return sDirection(array, temppos, word)
    elif direction == "SW":
        return swDirection(array, temppos, word)
    elif direction == "W":
        return wDirection(array, temppos, word)
    elif direction == "NW":
        return nwDirection(array, temppos, word)


wordSearchArray = translate("./db/table.jpg")
# im = Image.open("test-image3.png")
# wordSearchArray = pytesseract.image_to_string(im, lang = "eng")
wordBankArray = translate("./db/table.jpg")

wordSearch = toGrid(list(wordSearchArray))
wordBank = toBank(list(wordBankArray))

for word in wordBank:
    checkFirst(wordSearch, word)
#
# print(highlight)
# print(wordSearch)
print(wordBank)

for i in range(0, len(wordSearch)):
    for j in range(0, len(wordSearch[i])):
        letter = Label(text=wordSearch[i][j], font=("Ariel", 15)).grid(column=j, row=i)

for q in range(0, len(highlight)):
    highlightletter = Label(text=wordSearch[highlight[q][0]][highlight[q][1]], font=("Ariel", 15), fg='red').grid(
        column=highlight[q][1], row=highlight[q][0])

root.mainloop()
