from nasa import earth
from tqdm import tqdm
import pendulum
from properties import Shot
from constants import MAX_CLOUD_SCORE
from datetime import datetime
from utils import create_test_image
from io import BytesIO


class LandsatImage:
    """
    Utility class to manage the display of a landsat image using
    """

    def __init__(self):
        self.image = None
        self._shot = None

    @property
    def shot(self):
        return self._shot

    @shot.setter
    def shot(self, value):
        self._shot = value
        self.image = None

    def save_image(self):
        """
        this save the image to a path
        in the bot it will show it to the user

        Args:
            disp ([display]): the display
        """
        if not self.image:
            # TODO : Uncomment in reallife
            # img = self.shot.image
            """image_path = './images/image_{}'.format(datetime.now())
            picture_bytes = BytesIO()
            picture_bytes.name = image_path
            pil_img.save(picture_bytes, 'JPEG')
            picture_bytes.seek(0)
            print(picture_bytes, '=====the image ====')
            self.image = picture_byte"""
            print(self.shot)
            return self.shot


class LandsatBisector:
    """
    Manages the different assets from landsat to facilitate the bisection
    algorithm.
    """

    def __init__(self, lon, lat):
        self.lon, self.lat = lon, lat
        self.shots = self.get_fake_shots()
        self.image = LandsatImage()
        self.index = 0

        print(f'First = {self.shots[0].asset.date}')
        print(f'Last = {self.shots[-1].asset.date}')
        print(f'Count = {len(self.shots)}')

    @property
    def count(self):
        return len(self.shots)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self.image.shot = self.shots[index]
        self._index = index

    @property
    def date(self):
        return self.shots[self.index].asset.date

    def get_shots(self):
        """
        Not all returned assets are useful (some have clouds). This function
        does some filtering in order to remove those useless assets and returns
        pre-computed shots which can be used more easily.
        """

        begin = '2000-01-01'
        end = pendulum.now('UTC').date().isoformat()

        assets = earth.assets(lat=self.lat, lon=self.lon, begin=begin, end=end)

        out = []

        for asset in tqdm(assets):
            img = asset.get_asset_image(cloud_score=True)

            if (img.cloud_score or 1.0) <= MAX_CLOUD_SCORE:
                out.append(Shot(asset, img))

        return out

    def get_fake_shots(self):
        """
        this is for testing purpose
        """
        return [create_test_image() for _ in range(0, 6)]
