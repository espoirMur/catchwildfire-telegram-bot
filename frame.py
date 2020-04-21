import io
from typing import Text
from urllib.parse import quote, urljoin
from httpx import Client
from properties import Video, DISPLAY_SIZE
from config import API_BASE
from PIL import Image


class Frame:
    """
    Wrapper around frame data to help covert it into an image that can be send to telegram
    """

    def __init__(self, data):
        self.data = data
        self.image = None

    def generate_image_bytes(self):
        """
        Create an image bytes that can be send to telegram
        Returns:
            Image : Image bytes
        """
        if not self.image:
            pil_img = Image.new('RGBA', size=DISPLAY_SIZE)
            image_bytes = io.BytesIO(self.data)
            image_bytes.name = 'image.png'
            pil_img.save(image_bytes, 'PNG')
            image_bytes.seek(0)
            self.image = image_bytes
        return self.image


class FrameX:
    """
    Utility class to access the FrameX API
    """

    BASE_URL = API_BASE

    def __init__(self):
        self.client = Client()

    def video(self, video: Text) -> Video:
        """
        Fetches information about a video
        """

        r = self.client.get(urljoin(self.BASE_URL, f"video/{quote(video)}/"))
        r.raise_for_status()
        return Video(**r.json())

    def video_frame(self, video: Text, frame: int) -> bytes:
        """
        Fetches the JPEG data of a single frame
        """

        r = self.client.get(
            urljoin(self.BASE_URL, f'video/{quote(video)}/frame/{quote(f"{frame}")}/')
        )
        r.raise_for_status()
        return r.content


class FrameXBisector:
    """
    Helps managing the display of images from the launch
    """

    BASE_URL = API_BASE

    def __init__(self, name):
        self.api = FrameX()
        self.video = self.api.video(name)
        self._index = 0
        self.image = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, v):
        """
        When a new index is written, download the new frame
        """

        self._index = v
        self.image = Frame(self.api.video_frame(self.video.name, v))

    @property
    def count(self):
        return self.video.frames
