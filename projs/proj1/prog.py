# Scorpions and Diamonds

from enum import Enum

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
            return 'D'
        elif self.content == BoxContent.SCORPION:
            return 's'
        else:
            return '?'


N = 100
boxes = [Box(i+1) for i in range(N)]

def print_boxes(boxes):
    rowlen = 20
    for i in range(int(100/rowlen)):
        for j in range(rowlen):
            idx = str(i*rowlen+j+1)
            print(idx, end=' ' if len(idx) > 1 else '  ')
        print()
        for j in range(rowlen):
            box = boxes[i*rowlen+j]
            print(box, end='  ')
        print()
    print()

def main():
    # attendants go through...
    for i in range(N):
        k = i+1
        for box in boxes:
            if box.idx % k == 0:
                box.flip()

        print(f'******* k = {k} ******* ')
        print_boxes(boxes)
        key = input()
        if key == 'q':
            break

if __name__ == "__main__":
    main()