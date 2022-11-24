# Let me get rid of the non-AI stuff first

MAZE_0 = [
    "AB",
    "  "
]

MAZE_1 = [
    "A ",
    "B "
]

MAZE_2 = [
    "A ",
    " B"
]

MAZE_3 = [
    " B",
    "A "
]

MAZE_4 = [
    "A ",
    "  "
]

MAZE_5 = [
    "AX",
    " B"
]

MAZE_6 = [
    "A ",
    "XB"
]

MAZE_7 = [
    "A X",
    "X  ",
    "  B"
]


MAZE_7 = [
    "A   X",
    "   X ",
    " X  X",
    "    B"
]

MAZE_8 = [
    "A   X",
    "   X ",
    " XX X",
    "    B"
]

MAZE_9 = [
    "A   X",
    "  XX ",
    " X  X",
    "  X B"
]

INITIAL_STATE_MARKER = 'A'
END_STATE_MARKER = 'B'
WALL_MARKER = 'X'
EMPTY_MARKER = ' '


def get_maze_as_2d_matrix(maze_as_str):
    matrix = []
    for str in maze_as_str:
        row = []
        for c in str:
            row.append(c)
        matrix.append(row)
    return matrix


def pretty_print_maze(maze_matrix):
    def print_first_line():
        print("╔", end="")
        for i in range(len(maze_matrix[0]) - 1):
            print("═══╦", end="")
        print("═══╗")

    def print_separator_line():
        print("╠", end="")
        for i in range(len(maze_matrix[0]) - 1):
            print("═══╬", end="")
        print("═══╣")

    def print_last_line():
        print("╚", end="")
        for i in range(0, len(maze_matrix[0]) - 1):
            print("═══╩", end="")
        print("═══╝")

    print_first_line()
    for row in range(len(maze_matrix)):
        print("║", end="")
        for col in range(len(maze_matrix[row])):
            print(f" {maze_matrix[row][col]} ", end="")
            print("║", end="" if col < len(maze_matrix[row]) - 1 else "\n")
        if row < len(maze_matrix) - 1:
            print_separator_line()
        else:
            print_last_line()


def find_initial_state_in_maze(maze_matrix):
    for row_index in range(len(maze_matrix)):
        for col_index in range(len(maze_matrix)):
            if maze_matrix[row_index][col_index] == INITIAL_STATE_MARKER:
                return (row_index, col_index)


class Node:
    def __init__(self, state, parent_node, action, cost):
        self.state = state
        self.parent_node = parent_node
        self.action = action
        self.cost = cost

    def __repr__(self):
        return f"({self.state}; parent={self.parent_node.state}, action={self.action}; cost={self.cost}"


class ExploredNodes:
    def __init__(self):
        self.explored_set = set()

    def add(self, node):
        self.explored_set.add(node.state)

    def contains(self, node):
        if node.state in self.explored_set:
            return True
        else:
            return False


class Frontier:
    """This is a LIFO Frontier"""
    def __init__(self, initial_node):
        self.nodes_in_frontier = [initial_node]

    def remove(self):
        node = self.nodes_in_frontier[-1]
        self.nodes_in_frontier = self.nodes_in_frontier[:-1]
        return node

    def add(self, node):
        self.nodes_in_frontier.append(node)

    def is_empty(self):
        return len(self.nodes_in_frontier) == 0

    def __repr__(self):
        solution_str = ""
        for node in self.nodes_in_frontier:
            solution_str += f"from {node.state} move {node.action} (cost={node.cost})\n"
        return solution_str


class QueueFrontier(Frontier):
    """This is a FIFO Frontier"""

    def remove(self):
        node = self.nodes_in_frontier[0]
        self.nodes_in_frontier = self.nodes_in_frontier[1:]
        return node


def test_goal(maze, state):
    row, col = state
    return True if maze[row][col] == END_STATE_MARKER else False


def expand_node(node, maze, frontier, explored):
    def find_transition_nodes(maze, state):
        transition_nodes = []
        candidate_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for candidate_move in candidate_moves:
            cur_row, cur_col = state
            step_row, step_col = candidate_move
            next_row = cur_row + step_row
            next_col = cur_col + step_col
            if next_row >= 0 and next_row < len(maze) and next_col >= 0 and next_col < len(maze[0]) and maze[next_row][next_col] != WALL_MARKER:
                transition_nodes.append(Node((next_row, next_col), node, candidate_move, node.cost + 1))
        return transition_nodes

    transition_nodes = find_transition_nodes(maze, node.state)
    for transition_node in transition_nodes:
        if not explored.contains(transition_node):
            frontier.add(transition_node)


def print_solution(node: Node) -> None:
    solution_moves = []
    while node.parent_node is not None:
        solution_moves.append(f"from {node.parent_node.state} move {node.action} to {node.state} (cost={node.cost})")
        node = node.parent_node
    solution_moves.append("Solution Found!")
    solution_moves.reverse()
    print("\n".join(solution_moves))


if __name__ == "__main__":
    maze = get_maze_as_2d_matrix(MAZE_8)
    pretty_print_maze(maze)
    initial_state = find_initial_state_in_maze(maze)

    start_node = Node(initial_state, None, None, 0)
    # frontier = Frontier(start_node) # this is LIFO frontier
    frontier = QueueFrontier(start_node)  # this is FIFO frontier
    explored_nodes = ExploredNodes()

    node = start_node
    while not test_goal(maze, node.state) and not frontier.is_empty():
        node = frontier.remove()
        if not test_goal(maze, node.state):
            explored_nodes.add(node)
            expand_node(node, maze, frontier, explored_nodes)

    if test_goal(maze, node.state):
        print_solution(node)
    else:
        print(f"No solution found!")
