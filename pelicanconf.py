import tinify
from PIL import Image
import io, os

AUTHOR = "Niklas Anderson"
SITENAME = "Niklas Anderson | Software Engineer"
SITEURL = "https://nkanderson.com"
SITEDESCRIPTION = "Niklas Anderson software engineer work and experience"

PATH = "content"

TIMEZONE = "America/Los_Angeles"

DEFAULT_LANG = "en"

THEME = "nik-custom"
DISPLAY_CATEGORIES_ON_MENU = False

# GITHUB_URL = "http://github.com/nkanderson"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 15

RELATIVE_URLS = True


def compress_img(image):
    API_KEY = os.environ["TINYPNG_KEY"]
    tinify.key = API_KEY
    source_data = io.BytesIO()
    image.save(source_data, format="PNG")
    result_data = tinify.from_buffer(source_data.getvalue()).to_buffer()
    return Image.open(io.BytesIO(result_data))


IMAGE_PROCESS = {
    "project-image": {
        "type": "responsive-image",
        "sizes": ("(max-width: 375px) 300px, " "(max-width: 600px) 500px, " "800px"),
        "srcset": [
            ("300w", ["scale_in 300 300 False", compress_img]),
            ("500w", ["scale_in 500 500 False", compress_img]),
            ("800w", ["scale_in 800 800 False", compress_img]),
        ],
        "default": "800w",
    }
}
