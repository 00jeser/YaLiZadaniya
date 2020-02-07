import sys
from io import BytesIO
import YaMapImgModule
from PIL import Image

Image.open(BytesIO(YaMapImgModule.find(sys.argv[1:]).content)).show()
