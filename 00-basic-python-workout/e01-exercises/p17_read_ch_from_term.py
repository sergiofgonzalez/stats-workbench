from cs19_circular_doubly_linked_list import CircularDoublyLinkedList
import platform


class CharReader:
    def __init__(self):
        if platform.system() == "Linux":
            self.impl = _get_ch_linux()
        else:
            self.impl = _get_ch_win()

    def __call__(self):
        return self.impl()


class _get_ch_linux:
    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _get_ch_win:
    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = CharReader()

print("Option A")
print("Option B")
print("Option C")

done = False
while not done:
    print("Choose your poison (q to quit): ", end="")
    ch = getch()
    if ch.lower() == 'q':
        done = True
    else:
        print(f'{ch}')
