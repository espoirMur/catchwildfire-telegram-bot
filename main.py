from constants import LON, LAT
from landsat import LandsatBisector
from actions import bisect, display_current_canditate
from dotenv import load_dotenv
from functools import partial


load_dotenv()


# keep only main here
def main():
    """
    Runs a bisection algorithm on a series of Landsat pictures in order
    for the user to find the approximates date of the fire.

    Images are displayed using pygame, but the interactivity happens in
    the terminal as it is much easier to do.
    """
    bisector = LandsatBisector(LON, LAT)
    culprit = bisect(
        bisector.count,
        lambda x: x,
        partial(
            display_current_canditate,
            bisector=bisector))
    bisector.index = culprit
    print(f"Found! First apparition = {bisector.date}")
    exit()


if __name__ == '__main__':
    main()
