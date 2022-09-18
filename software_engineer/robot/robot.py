def set_position(position: list, direction: int, distance: int):
    if direction == 0:
        position[1] += distance
    elif direction == 90:
        position[0] += distance
    elif direction == 180:
        position[1] += -distance
    elif direction == 270:
        position[0] += -distance


def exec_command(s: str) -> tuple:
    direction = 0
    position = [0, 0]
    is_moving = False
    dig = ""
    l = len(s)
    for i in range(l):
        ch = s[i]
        # print(is_moving and not ch.isdigit())
        # Move state
        if is_moving and ch.isdigit() and i == l-1:
            distance = int(dig+ch)
            set_position(position, direction, distance)
        elif is_moving and ch.isdigit():
            dig += ch
        elif is_moving and not ch.isdigit():  # exec move and end
            distance = int(dig)
            set_position(position, direction, distance)
            dig = ""
            is_moving = False

        # Turning state
        if ch == 'R':
            direction = (direction + 90) % 360
        elif ch == 'L':
            direction = (direction - 90) % 360
        elif ch == "W":  # start Move
            is_moving = True

    return position, direction
