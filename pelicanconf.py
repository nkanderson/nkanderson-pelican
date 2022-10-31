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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

IMAGE_PROCESS = {
    "project-image": {
        "type": "responsive-image",
        "sizes": ("(min-width: 1200px) 800px, " "(min-width: 600px) 500px, " "100vw"),
        "srcset": [
            ("500w", ["scale_in 500 500 False"]),
            ("800w", ["scale_in 800 800 False"]),
        ],
        "default": "800w",
    }
}
