from io import BytesIO
from PIL import Image
from datetime import datetime
from collections import namedtuple


def create_test_image():
    file = BytesIO()
    image = Image.open('./images/my_avatar.png')
    image.save(file, 'png')

    file.name = f'image{datetime.now()}'
    Asset = namedtuple('Asset', ['date'])
    asset = Asset(date=datetime.today())
    setattr(file, 'asset', asset)
    file.seek(0)
    return file
