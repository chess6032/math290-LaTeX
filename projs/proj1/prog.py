# Scorpions and Diamonds

from enum import Enum

USE_ANSI = True
HIGHLIGHT_COLOR = '\033[33m' if USE_ANSI else ''
DIAMOND_COLOR = '\033[36m' if USE_ANSI else ''
SCORPION_COLOR = '\033[31m' if USE_ANSI else ''
RESET_COLOR = '\033[0m' if USE_ANSI else ''

class BoxContent(Enum):
    DIAMOND = 0
    SCORPION = 1

class Box:
    def __init__(self, n):
        self.content = BoxContent.SCORPION
        self.idx = n

    def flip(self):
        self.content = BoxContent.DIAMOND if self.content == BoxContent.SCORPION else BoxContent.SCORPION

    def __str__(self):
        if self.content == BoxContent.DIAMOND:
            return DIAMOND_COLOR + 'D' + RESET_COLOR
        elif self.content == BoxContent.SCORPION:
            return SCORPION_COLOR + 's' + RESET_COLOR
        else:
            return '?'

def print_boxes(boxes):
    rowlen = 20
    # for each row...
    for i in range(int(100/rowlen)):
        # print indeces
        for j in range(rowlen):
            idx = str(i*rowlen+j+1)
            print(idx, end=' ' if len(idx) > 1 else '  ')
        print()
        # print contents
        for j in range(rowlen):
            box = boxes[i*rowlen+j]
            print(box, end='  ')
        print()
    print()

def main(n):
    # n: number of boxes
    boxes = [Box(i+1) for i in range(n)]

    print(f'{HIGHLIGHT_COLOR} START {RESET_COLOR}')
    print_boxes(boxes)
    input()

    # attendants go through...
    for i in range(n):
        k = i+1
        for box in boxes:
            if box.idx % k == 0:
                box.flip()

        print(f'{HIGHLIGHT_COLOR} k = {k} {RESET_COLOR}')
        print_boxes(boxes)
        key = input()
        if key == 'q':
            break

if __name__ == "__main__":
    main(100)