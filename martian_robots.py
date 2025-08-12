import sys

# Movement offsets for each direction
DELTA = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

DIRECTIONS = ['N', 'E', 'S', 'W']  # clockwise order


def turn_left(direction):
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx - 1) % 4]


def turn_right(direction):
    idx = DIRECTIONS.index(direction)
    return DIRECTIONS[(idx + 1) % 4]


def main():
    # Read and clean input from stdin
    raw_lines = sys.stdin.read().splitlines()
    lines = []
    for line in raw_lines:
        line = line.strip()
        if line:
            lines.append(line)

    if not lines:
        return

    maxx, maxy = map(int, lines[0].split())
    scents = set()  # (x, y, dir) where a robot fell off
    results = []

    i = 1
    while i < len(lines):
        x, y, d = lines[i].split()
        x, y = int(x), int(y)

        if i + 1 < len(lines):
            program = lines[i + 1]
        else:
            program = ""

        i += 2

        lost = False
        for cmd in program:
            if cmd == 'L':
                d = turn_left(d)
            elif cmd == 'R':
                d = turn_right(d)
            elif cmd == 'F':
                dx, dy = DELTA[d]
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > maxx or ny > maxy:
                    key = (x, y, d)
                    if key in scents:
                        continue  # ignore dangerous forward
                    scents.add(key)
                    lost = True
                    break
                x, y = nx, ny
            # else: ignore unknown commands

        results.append(f"{x} {y} {d}{' LOST' if lost else ''}")

    print("\n".join(results))


if __name__ == "__main__":
    main()
