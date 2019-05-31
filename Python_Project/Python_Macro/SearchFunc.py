from typing import TextIO, List, Any
from io import StringIO


def count_birds(observations_file: TextIO) -> List[List[Any]]:

    bird_counts = []
    for line in observations_file:
        bird = line.strip()
        found = False

        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
                found = True
        if not found:
            bird_counts.append([bird, 1])

    return bird_counts


if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_counts = count_birds(observations_file)

        for entry in bird_counts:
            print(entry[0], entry[1])
