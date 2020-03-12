from constants import DISPLAY_SIZE, BLACK, LON, LAT
from landsat import LandsatBisector
from actions import bisect, confirm
from dotenv import load_dotenv


load_dotenv()


# keep only main here
def main():
    """
    Runs a bisection algorithm on a series of Landsat pictures in order
    for the user to find the approximative date of the fire.

    Images are displayed using pygame, but the interactivity happens in
    the terminal as it is much easier to do.
    """
    bisector = LandsatBisector(LON, LAT)

    def display_current_canditate(candidate, bisector):
        """
        Displays the current candidate to the user and asks them to
        check if they see wildfire damages.
        candidate : the candidate to display
        bisector : the bisector instance
        """

        bisector.index = candidate
        bisector.image.save_image()
        return confirm(bisector.date)

    culprit = bisect(bisector.count, lambda x: x, display_current_canditate)
    bisector.index = culprit
    print(f"Found! First apparition = {bisector.date}")
    exit()


if __name__ == '__main__':
    main()
