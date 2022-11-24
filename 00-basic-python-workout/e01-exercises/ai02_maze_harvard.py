import os
import sys


class Node:
    def __init__(self, state, parent_node, action, cost):
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.cost = cost

    def __repr__(self):
        return f"({self.state}; parent={self.parent_node.state}, action={self.action}; cost={self.cost}"


class StackFrontier:
    """This is a LIFO Frontier"""

    def __init__(self):
        self.frontier = []

    def empty(self):
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if self.empty():
            raise Exception("Cannot remove from empty StackFrontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def __repr__(self):
        solution_str = ""
        for node in self.frontier:
            solution_str += f"from {node.state} move {node.action} (cost={node.cost})\n"
        return solution_str


class QueueFrontier(StackFrontier):
    """This is a FIFO Frontier"""

    def remove(self):
        if self.empty():
            raise Exception("Cannot remove from empty QueueFrontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze:
    INITIAL_STATE_MARKER = 'A'
    END_STATE_MARKER = 'B'
    WALL_MARKER = '#'
    EMPTY_MARKER = ' '
    DEPTH_FIRST_SEARCH = "DFS"
    BREADTH_FIRST_SEARCH = "BFS"

    def __init__(self, filename, search_mode):

        # Read file contents
        with open(filename) as f:
            contents = f.read()

        # Validate that contents have exactly one start point and one goal
        if contents.count(Maze.INITIAL_STATE_MARKER) != 1:
            raise Exception("Maze must have exactly one start point")

        if contents.count(Maze.END_STATE_MARKER) != 1:
            raise Exception("Maze must have exactly one goal")

        # Split file contents in lines and get maze height and width
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # model the maze as a 2D array of boolean values with walls set to True
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == Maze.INITIAL_STATE_MARKER:
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == Maze.END_STATE_MARKER:
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == Maze.EMPTY_MARKER:
                        row.append(False)
                    elif contents[i][j] == Maze.WALL_MARKER:
                        row.append(True)
                    else:
                        raise Exception(f"Invalid character in Maze: '{contents[i][j]}'")
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None

        # keep track of search_mode to configure the frontier
        self.search_mode = search_mode

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Finds the solution, if one exists"""

        # keep track of number of states explored
        self.num_explored = 0

        # Initialize frontier with the starting node
        start = Node(state=self.start, parent_node=None, action=None, cost=0)
        if self.search_mode == Maze.DEPTH_FIRST_SEARCH:
            frontier = StackFrontier()
        else:
            frontier = QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set within the method
        self.explored = set()

        # Repeat until solution found or no solution found
        while True:

            # If frontier is empty, no solution is available
            if frontier.empty():
                raise Exception("No solution found to the maze")

            # Get a node from the frontier
            node = frontier.remove()
            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent_node is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent_node
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # If it's not a solution, mark node as explored
            self.explored.add(node.state)

            # Then, add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent_node=node, action=action, cost=node.cost + 1)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("DejaVuSans.ttf", 14)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    ([
                        (j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)
                    ]),
                    fill=fill
                )
                if (i, j) == self.start:
                    draw.text((j * cell_size + cell_border, i * cell_size + cell_border), "Start", (0, 0, 0), font=font)
                elif (i, j) == self.goal:
                    draw.text((j * cell_size + cell_border, i * cell_size + cell_border), "Goal", (0, 0, 0), font=font)

        img.save(filename)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3 or (len(sys.argv) == 3 and sys.argv[2].upper() != Maze.DEPTH_FIRST_SEARCH and sys.argv[2].upper() != Maze.BREADTH_FIRST_SEARCH):
        sys.exit("Usage: python ai02_maze_harvard.py path/to/maze.txt [dfs|bfs]\nNote: dfs is the default search mode")

    m = Maze(sys.argv[1], search_mode=Maze.DEPTH_FIRST_SEARCH if len(sys.argv) == 2 else sys.argv[2].upper())
    print("Maze:")
    m.print()

    print(f"Solving maze using {m.search_mode}...")
    m.solve()

    print(f"States explored: {m.num_explored}")
    print("Solution:")
    m.print()

    image_filename = f"{os.path.splitext(sys.argv[1])[0]}{os.extsep}png"
    m.output_image(image_filename, show_explored=True)

    print(f"See '{image_filename}' for the graphical representation of the solution")
