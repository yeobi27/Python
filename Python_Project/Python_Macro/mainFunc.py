from typing import Set, TextIO
from io import StringIO


def observe_birds(observations_file: TextIO) -> Set[str]:

    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)

    return birds_observed


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    with open('observations.txt') as observations_file:
        print(observe_birds(observations_file))
