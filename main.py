import pygame
import os
from const import DISPLAY_SIZE, BLACK, LON, LAT
from landsat import LandsatBisector
from actions import bisect, confirm

os.environ.setdefault(
    'NASA_API_KEY',
    'xkPcYAoU93O1PeqPrKXyjpGChT1FkQ8TjA7Neg7V',
)

# keep only main here
def main():
    """
    Runs a bisection algorithm on a series of Landsat pictures in order
    for the user to find the approximative date of the fire.

    Images are displayed using pygame, but the interactivity happens in
    the terminal as it is much easier to do.
    """

    pygame.init()

    bisector = LandsatBisector(LON, LAT)
    disp = pygame.display.set_mode(DISPLAY_SIZE)

    def mapper(n):
        """
        In that case there is no need to map (or rather, the mapping
        is done visually by the user)
        """

        return n

    def tester(n):
        """
        Displays the current candidate to the user and asks them to
        check if they see wildfire damages.
        """

        bisector.index = n
        disp.fill(BLACK)
        bisector.blit(disp)
        pygame.display.update()

        return confirm(bisector.date)

    culprit = bisect(bisector.count, mapper, tester)
    bisector.index = culprit

    print(f"Found! First apparition = {bisector.date}")

    pygame.quit()
    exit()


if __name__ == '__main__':
    main()
