
from .logos_html import Logos_html
from .logos_api import Logos_API


class Plugin_OBJ():

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.logos_html = Logos_html(fhdhr, plugin_utils)

        self.logos_api = Logos_API(fhdhr, plugin_utils)
