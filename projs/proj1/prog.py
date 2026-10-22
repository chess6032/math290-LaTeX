# Scorpions and Diamonds

from enum import Enum

# output formatting

USE_ANSI = True

HEADER_COLOR = '\033[33m'   if USE_ANSI else ''
DIAMOND_COLOR = '\033[36m'  if USE_ANSI else ''
SCORPION_COLOR = '\033[31m' if USE_ANSI else ''
RESET_COLOR = '\033[0m'     if USE_ANSI else ''

HIGHLIGHT_FMT = '\033[7m' if USE_ANSI else ''
RESET_HIGHLIGHT_FMT = '\033[0m' if USE_ANSI else ''

ROWLEN = 10

# classes 'n shih

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

def print_boxes(boxes, k, highlights):
    # for each row...
    for i in range(int(100/ROWLEN)):
        # print indeces
        for j in range(ROWLEN):
            idx = i*ROWLEN+j+1
            if idx == k:
                print(HEADER_COLOR,end='')
            if idx in highlights:
                print(HIGHLIGHT_FMT, end='')
            print(idx, end='')
            print(RESET_HIGHLIGHT_FMT + RESET_COLOR, end=' ' if len(str(idx)) > 1 else '  ')
        print()
        # print boxes
        for j in range(ROWLEN):
            box = boxes[i*ROWLEN+j]

            print(box, end='  ')
        print()
    print()

def main(n):
    # n: number of boxes
    boxes = [Box(i+1) for i in range(n)]

    print(f'{HEADER_COLOR} START {RESET_COLOR}')
    print_boxes(boxes, -1, [])
    input()

    # attendants go through...
    for i in range(n):
        k = i+1
        highlights = []
        for box in boxes:
            if box.idx % k == 0:
                box.flip()
                highlights.append(box.idx)

        print(f'{HEADER_COLOR} k = {k} {RESET_COLOR}')
        print_boxes(boxes, k, highlights)
        key = input()
        if key == 'q':
            break

if __name__ == "__main__":
    main(100)