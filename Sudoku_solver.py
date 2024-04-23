grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


# Split the grid into 3 3x3 grids - return the (x, y) coords of subgrids
def subgrid_coordinates():
    subgrids = []
    # i, j = x, y of the subgrids
    for i in range(3):     
        for j in range(3):
            # k, l = x, y of units within the subgrid.
            subgrids += [[( (k+(i*3)), (l+(j*3)) ) for k in range(3) for l in range(3)]]
    return subgrids


# Return a list of values of the given subgrid (based on its coord values from subgrid_coordinates())
def subgrid_values(subgrid, g):
    return [g[coords[0]][coords[1]] for coords in subgrid]


def print_grid(g):
    for row in range(len(g)):
        # Every thrid row print a horizontal line for readability
        if row % 3 == 0 and row != 0:
            print("---------------------")
        
        for col in range(len(g[0])):
            # Every third col print a vertical line for readability
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            
            if col == 8:
                if g[row][col] == 0:
                    print(" ")
                else:
                    print(g[row][col])
            else:
                if g[row][col] == 0:
                    print("  ", end="")
                else:
                    print(str(g[row][col]) + " ", end="")


# Returns unsolved tile coords
def unsolved(g):
    for row in range(len(g)):
        for col in range(len(g)):
            if g[row][col] == 0:
                return (row, col)


def eligible_num(g, num, row, col):
    # Check rows and cols
    for i in range(9):
        if g[row][i] == num or g[i][col] == num:
            return False

    # Check subgrid
    subgrids = subgrid_coordinates()
    # Get the subgrid num is in
    for sg in subgrids:
        if (row, col) in sg:
            # Check if num is in subgrid
            if num in subgrid_values(sg, g):
                return False

    # If we made it here, the number is eligible.
    return True


# Fill in all missing tiles from grid
def solve(g):
    # Get the first unsolved square in the grid
    unsolved_square = unsolved(g)

    # Check if the grid is solved
    if unsolved_square == None:
        print("Solved grid:")
        return True

    # For each number, try and put it into the first unsolved square
    for i in range(1,10):
        if eligible_num(g, i, unsolved_square[0], unsolved_square[1]):
            # If it is eligible, put it into the unsolved square
            g[unsolved_square[0]][unsolved_square[1]] = i

            # Recur until solved
            if solve(g) == True:
                return True

            # If recursion returns false, there is a problem and we have
            # to backtrack. Set this square to 0 and return false.
            # Then, loop on line 96 continues and we try the next number
            g[unsolved_square[0]][unsolved_square[1]] = 0

    return False

def main():
    print("Initial puzzle:")
    print_grid(grid)
    if solve(grid) == False:
        print("Grid cannot be solved")
        return
    print_grid(grid)

if __name__ == "__main__":
    main()
