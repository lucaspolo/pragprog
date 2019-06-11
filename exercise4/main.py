from collections import namedtuple

Command = namedtuple('Command', 'name has_args func')

commands = {
    'P': Command('SELECT_PEN', True, lambda x: print(f'Selecting Pen {x}')),
    'D': Command('PEN_DOWN',  False,   lambda: print(f'Down pen')),
    'W': Command('DRAW_WEST',  True, lambda x: print(f'Drawing to west {x} cm')),
    'N': Command('DRAW_NORTH', True, lambda x: print(f'Drawing to north {x} cm')),
    'E': Command('DRAW_EAST',  True, lambda x: print(f'Drawing to east {x} cm')),
    'S': Command('DRAW_SOUTH', True, lambda x: print(f'Drawing to south {x} cm')),
    'U': Command('PEN_UP',    False,   lambda: print(f'Up pen')),
}

def main():
    with open('commands.txt') as file:
        for line in file:
            line_command, *args = line.split()
            command = commands.get(line_command)
            if command:
                if command.has_args and not args:
                    print(f'Command {line_command} - {command.name} needs args')
                    continue
                command.func(*args)
            else:
                print(f'Command {line_command} not found')

if __name__ == "__main__":
    main()
