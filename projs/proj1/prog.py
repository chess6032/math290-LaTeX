# Scorpions and Diamonds

from enum import Enum

# output formatting

class FormatOptions:
    def __init__(self, use_ansi=True, rowlen=10):
        self.HEADER_COLOR   = '\033[33m' if use_ansi else ''
        self.DIAMOND_COLOR  = '\033[36m' if use_ansi else ''
        self.SCORPION_COLOR = '\033[31m' if use_ansi else ''
        self.RESET_COLOR    = '\033[0m'  if use_ansi else ''

        self.HIGHLIGHT_FMT       = '\033[7m' if use_ansi else ''
        self.RESET_HIGHLIGHT_FMT = '\033[0m' if use_ansi else ''

        self.ROWLEN = rowlen

# classes 'n shih

class BoxContent(Enum):
    DIAMOND = 0
    SCORPION = 1

class Box:
    def __init__(self, n: int, fmt: FormatOptions):
        self.content = BoxContent.SCORPION
        self.idx = n
        self.DIAMOND_COLOR = fmt.DIAMOND_COLOR
        self.SCORPION_COLOR = fmt.SCORPION_COLOR
        self.RESET_COLOR = fmt.RESET_COLOR

    def flip(self):
        self.content = BoxContent.DIAMOND if self.content == BoxContent.SCORPION else BoxContent.SCORPION

    def __str__(self):
        if self.content == BoxContent.DIAMOND:
            return self.DIAMOND_COLOR + 'D' + self.RESET_COLOR
        elif self.content == BoxContent.SCORPION:
            return self.SCORPION_COLOR + 's' + self.RESET_COLOR
        else:
            return '?'

def print_boxes(boxes, k: int, highlights: list[int], fmt: FormatOptions):
    # for each row...
    for i in range(int(100/fmt.ROWLEN)):
        # print indeces
        for j in range(fmt.ROWLEN):
            idx = i*fmt.ROWLEN+j+1
            if idx == k:
                print(fmt.HEADER_COLOR,end='')
            if idx in highlights:
                print(fmt.HIGHLIGHT_FMT, end='')
            print(idx, end='')
            print(fmt.RESET_HIGHLIGHT_FMT + fmt.RESET_COLOR, end=' ' if len(str(idx)) > 1 else '  ')
        print()
        # print boxes
        for j in range(fmt.ROWLEN):
            box = boxes[i*fmt.ROWLEN+j]

            print(box, end='  ')
        print()
    print()

def main(n, fmt: FormatOptions):
    # n: number of boxes
    boxes = [Box(i+1, fmt) for i in range(n)]

    print(f'{fmt.HEADER_COLOR} START {fmt.RESET_COLOR}')
    print_boxes(boxes, -1, [], fmt)
    input()

    # attendants go through...
    for i in range(n):
        k = i+1
        highlights = []
        for box in boxes:
            if box.idx % k == 0:
                box.flip()
                highlights.append(box.idx)

        print(f'{fmt.HEADER_COLOR} k = {k} {fmt.RESET_COLOR}')
        print_boxes(boxes, k, highlights, fmt)
        key = input()
        if key == 'q':
            break

if __name__ == "__main__":
    fmt = FormatOptions()
    main(100, fmt)