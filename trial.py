def west():
    return 'W'


def east():
    return 'E'


def north():
    return 'N'


def south():
    return 'S'


def is_left(direction):
    if direction == 'L':
        return 1
    return 0


def is_north(state):
    if state == 'N':
        return 1
    return 0


def is_south(state):
    if state == 'S':
        return 1
    return 0


def is_east(state):
    if state == 'E':
        return 1
    return 0


def is_west(state):
    if state == 'W':
        return 1
    return 0


def is_move(direction):
    if direction == 'M':
        return 1
    return 0

def swap_north(state):
    if state == 'W':
        return east()
    return west()


def swap_east(state):
    if state == 'N':
        return south()
    return north()


def change_north(direction):
    if is_left(direction):
        return west()
    return east()


def change_south(direction):
    return swap_north(change_north(direction))


change_east = lambda direction: north() if is_left(direction) else south()


def change_west(direction):
    return swap_east(change_east(direction))


move = lambda current, direction, func1, func2:  func1(current) and func2(direction)
from_north = lambda current, direction:  move(current, direction, is_north, change_north)
from_south = lambda current, direction:  move(current, direction, is_south, change_south)
from_east = lambda current, direction:  move(current, direction, is_east, change_east)
from_west = lambda current, direction:  move(current, direction, is_west, change_west)

increase = lambda position, index, limit: position[index] + 1 if position[index] < limit else position[index]
decrease = lambda position, index: position[index] - 1 if position[index] > 0 else position[index]

which_side = lambda state, side1, side2: side1(state) or side2(state)
keep = lambda position, side1, side2, index: which_side(position[2], side1, side2) and str(position[index])
change = lambda position, side, index, limit: str(increase(position, index, limit)) if side(position[2]) else str(decrease(position, index))


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


# print(change_east('R'))
print(find_position(position, movement, size[0], size[1]))