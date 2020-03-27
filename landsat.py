from nasa import earth
from tqdm import tqdm
import pendulum
from properties import Shot
from constants import MAX_CLOUD_SCORE
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
    
    def generate_image_bytes(self):
        """
        Create an image bytes that can be send to telegram
        Returns:
            Image : Image bytes
        """
        img = self.shot.image
        pil_img = img.image
        image_bytes = BytesIO()
        image_bytes.name = 'image.png'
        pil_img.save(image_bytes, 'PNG')
        image_bytes.seek(0)
        self.image = image_bytes
        return self.image


class LandsatBisector:
    """
    Manages the different assets from landsat to facilitate the bisection
    algorithm.
    """

    def __init__(self, lon, lat):
        self.lon, self.lat = lon, lat
        self.shots = self.get_shots()
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
           
        ## as of now the pendilum is retuning 62 images
        # let limit them to 7 days and check how many results will be returned
        assets = earth.assets(lat=self.lat, lon=self.lon, begin=begin, end=end)

        out = []

        for asset in tqdm(assets):
            img = asset.get_asset_image(cloud_score=True)

            if (img.cloud_score or 1.0) <= MAX_CLOUD_SCORE:
                out.append(Shot(asset, img))

        return out
