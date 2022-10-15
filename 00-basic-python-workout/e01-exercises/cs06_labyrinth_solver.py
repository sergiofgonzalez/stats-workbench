###
# Labyrinth solver using stacks
#
#   The labyrinth is modeled as a 2D character array using the following characters:
#   'E': entry point of the labyrinth (where the quest begins!)
#   'X': exit point of the labyrinth
#   '▄': wall
#   'P': visited cell
#   ' ': empty cell (corridor)

from operator import truediv
from cs03_stack import Stack


LABYRINTH_1 = [
    "I   X",
    "   X ",
    " X  X",
    "    E"
]

LABYRINTH_2 = [
    "I   X",
    "   X ",
    " XX X",
    "    E"
]

LABYRINTH_3_NO_EXIT = [
    "I   X",
    "  XX ",
    " X  X",
    "  X E"
]

LABYRINTH = LABYRINTH_2


class LabyrinthSolver:
    class Constants:
        ENTRY_MARKER = 'I'
        EXIT_MARKER = 'E'
        WALL_MARKER = 'X'
        EMPTY_MARKER = ' '
        VISITED_MARKER = 'V'
        DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, labyrinth):
        self.labyrinth = self.__get_labyrinth_as_2d_array(labyrinth)
        self.constants = LabyrinthSolver.Constants()
        self.__validate_labyrinth()
        self.num_rows = len(self.labyrinth)
        self.num_cols = len(self.labyrinth[0])
        self.entry_loc = self.entry_loc()
        self.exit_loc = self.exit_loc()
        self.movements_stack = Stack()
        self.current_loc = self.entry_loc
        self.current_dir_index = 0
        self.labyrinth[self.current_loc[0]][self.current_loc[1]] = self.constants.EMPTY_MARKER

    def solve(self):
        done = False

        self.movements_stack.push({"location": self.current_loc, "direction": self.current_dir_index})
        while not done:
            if self.movements_stack.is_empty():
                done = True
            else:
                movement = self.movements_stack.peek()
                current_row, current_col = movement["location"]
                current_dir = movement["direction"]
                if self.__in_exit_loc():
                    done = True
                else:
                    next_row, next_col = self.__next_loc(current_row, current_col, current_dir)
                    if self.__is_viable_loc(next_row, next_col):
                        self.labyrinth[next_row][next_col] = self.constants.VISITED_MARKER
                        self.movements_stack.push({"location": (next_row, next_col), "direction": 0})
                    else:
                        backtracked_movement = self.movements_stack.pop()
                        backtracked_loc = backtracked_movement["location"]
                        backtracked_dir = backtracked_movement["direction"]
                        if backtracked_dir < len(self.constants.DIRECTIONS) - 1:
                            self.movements_stack.push({"location": backtracked_loc, "direction": backtracked_dir + 1})

        self.labyrinth[self.entry_loc[0]][self.entry_loc[1]] = self.constants.ENTRY_MARKER
        self.labyrinth[self.exit_loc[0]][self.exit_loc[1]] = self.constants.EXIT_MARKER

        if self.movements_stack.is_empty():
            return False
        else:
            return True

    def __in_exit_loc(self):
        current_movement = self.movements_stack.peek()
        current_row, current_col = current_movement["location"]
        current_dir = current_movement["direction"]
        return current_row == self.exit_loc[0] and current_col == self.exit_loc[1]

    def __next_loc(self, row, col, dir):
        current_direction = self.constants.DIRECTIONS[dir]
        if current_direction == 'N':
            next_pos = (row - 1, col)
        elif current_direction == 'E':
            next_pos = (row, col + 1)
        elif current_direction == 'S':
            next_pos = (row + 1, col)
        elif current_direction == 'W':
            next_pos = (row, col - 1)
        else:
            raise ValueError(f"Unexpected direction index: {dir}")

        return next_pos

    def __is_viable_loc(self, row, col):
        if (
            row < 0 or row >= self.num_rows or
            col < 0 or col >= self.num_cols or
            self.labyrinth[row][col] == self.constants.WALL_MARKER or
            self.labyrinth[row][col] == self.constants.VISITED_MARKER
        ):
            return False
        else:
            return True

    def __get_labyrinth_as_2d_array(self, labyrinth):
        matrix = []
        for i in range(0, len(labyrinth)):
            row = []
            for j in range(0, len(labyrinth[i])):
                row.append(labyrinth[i][j])
            matrix.append(row)
        return matrix

    def __validate_labyrinth(self):
        if len(LABYRINTH) == 0:
            print("ERROR: labyrinth is empty")
            raise SystemExit

        num_cols = len(LABYRINTH[0])
        for row in range(0, len(LABYRINTH)):
            if len(LABYRINTH[row]) != num_cols:
                print("ERROR: invalid labyrinth shape: all rows must have the same length")
                raise SystemExit

        num_entries = 0
        num_exits = 0
        for row in range(0, len(LABYRINTH)):
            for col in range(0, len(LABYRINTH[0])):
                if LABYRINTH[row][col] == self.constants.ENTRY_MARKER:
                    num_entries += 1
                elif LABYRINTH[row][col] == self.constants.EXIT_MARKER:
                    num_exits += 1
                elif LABYRINTH[row][col] != self.constants.WALL_MARKER and LABYRINTH[row][col] != ' ':
                    print(f"ERROR: invalid characters in the labyrinth '{LABYRINTH[row][col]}'")
                    raise SystemExit

    def __find_in_labyrinth(self, elem):
        for row in range(0, len(LABYRINTH)):
            for col in range(0, len(LABYRINTH[0])):
                if LABYRINTH[row][col] == elem:
                    return (row, col)

    def entry_loc(self):
        return self.__find_in_labyrinth(self.constants.ENTRY_MARKER)

    def exit_loc(self):
        return self.__find_in_labyrinth(self.constants.EXIT_MARKER)

    def print_labyrinth(self):
        # ╔═══╦═══╦═══╗
        # ║ X ║ █ ║   ║
        # ╠═══╬═══╬═══╣
        # ║ X ║ █ ║   ║
        # ╠═══╬═══╬═══╣
        # ║ X ║ █ ║   ║
        # ╚═══╩═══╩═══╝

        def print_first_line():
            print("╔", end="")
            for i in range(0, len(self.labyrinth[0]) - 1):
                print("═══╦", end="")
            print("═══╗")

        def print_separator_line():
            print("╠", end="")
            for i in range(0, len(self.labyrinth[0]) - 1):
                print("═══╬", end="")
            print("═══╣")

        def print_last_line():
            print("╚", end="")
            for i in range(0, len(self.labyrinth[0]) - 1):
                print("═══╩", end="")
            print("═══╝")

        print_first_line()
        for row in range(0, len(self.labyrinth)):
            print("║", end="")
            for col in range(0, len(self.labyrinth[row])):
                print(f" {self.labyrinth[row][col]} ", end="")
                print("║", end="" if col < len(self.labyrinth[row]) - 1 else "\n")
            if row < len(self.labyrinth) - 1:
                print_separator_line()
            else:
                print_last_line()


labyrinth_solver = LabyrinthSolver(LABYRINTH)
if (labyrinth_solver.solve()):
    print("Found the exit! We're saved!")
    print(labyrinth_solver.movements_stack)
    labyrinth_solver.print_labyrinth()
else:
    print("Couldn't find the exit! We're doomed!")
    print(labyrinth_solver.movements_stack)
    labyrinth_solver.print_labyrinth()
