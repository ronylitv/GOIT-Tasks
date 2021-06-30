import sys

NUM_LINES = 10

if len(sys.argv) != 2:
    print('Ne peredano imya faila dlya prochtenie')
    quit()

try:
    with open(sys.argv[1], 'r', encoding='utf-8') as inf:
        lines = []
        for line in inf:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        for line in lines:
            print(line, end='')

except OSError:
    print('Error in access to file')

