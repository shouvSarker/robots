# functions to return directions
west = lambda : 'W'
east = lambda : 'E'
north = lambda : 'N'
south = lambda : 'S'

# functions to return if they are of a certain value
is_left = lambda direction: 1 if direction == 'L' else 0
is_move = lambda direction: 1 if direction == 'M' else 0
is_north = lambda state: 1 if state == 'N' else 0
is_south = lambda state: 1 if state == 'S' else 0
is_east = lambda state: 1 if state == 'E' else 0
is_west = lambda state: 1 if state == 'W' else 0

# functions to flip (swap between two possible logical values, i.e. return east if west) the input
swap_north = lambda state: east() if state == 'W' else west()
swap_east = lambda state: south() if state == 'N' else north()

# functions to change directions
change_north = lambda direction: west() if is_left(direction) else east()
change_south = lambda direction: swap_north(change_north(direction)) # flipping north's return gives us south
change_east = lambda direction: north() if is_left(direction) else south()
change_west = lambda direction: swap_east(change_east(direction)) # flipping east's return gives us west

# moving grids based on the side facing
move = lambda current, direction, func1, func2:  func1(current) and func2(direction)

# functions to move from a specific position
from_north = lambda current, direction:  move(current, direction, is_north, change_north)
from_south = lambda current, direction:  move(current, direction, is_south, change_south)
from_east = lambda current, direction:  move(current, direction, is_east, change_east)
from_west = lambda current, direction:  move(current, direction, is_west, change_west)

# changing grid position while ensuring not going out of bound
increase = lambda position, index, limit: position[index] + 1 if position[index] < limit else position[index]
decrease = lambda position, index: position[index] - 1 if position[index] > 0 else position[index]

# to decide which side the robot is facing
which_side = lambda state, side1, side2: side1(state) or side2(state)

# pass decision as to keep position or not, if yes, keep the current position on the axis
keep = lambda position, side1, side2, index: which_side(position[2], side1, side2) and str(position[index])

# change the position forward or backwards
change = lambda position, side, index, limit: str(increase(position, index, limit)) if side(position[2]) else str(decrease(position, index))

move_x = lambda position, x_limit:
initiate_move = lambda position, x_limit, y_limit:

def find_position(position, movement, x_limit, y_limit):
    new_position = []
    # func_list = [is_east, is_west, is_north, is_south]
    # print(position)
    if is_move(movement[0]):
        print("Moving")
        new_position.append(int(keep(position, is_north, is_south, 0) or change(position, is_east, 0, x_limit)))
        new_position.append(int(keep(position, is_east, is_west, 1) or change(position, is_north, 1, y_limit)))

        new_position.append(position[2])
    else:
        args = dict(current=position[2], direction=movement[0])
        print("going left")
        new_position.extend(position[:2])
        new_position.append(from_north(**args) or from_south(**args) or from_east(**args) or from_west(**args))

    if len(movement) == 1:
        print("Finished")
        return new_position

    return find_position(new_position, movement[1:], x_limit, y_limit)


size = [5, 5]
position = [3, 3, 'E']
movement = ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M']

print(find_position(position, movement, size[0], size[1]))