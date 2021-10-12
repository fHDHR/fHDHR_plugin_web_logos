from flask import request, render_template_string, session
import pathlib
from io import StringIO


class Logos_html():
    endpoints = ["/logos", "/logos.html"]
    endpoint_name = "page_logos_html"
    endpoint_category = "pages"
    pretty_name = "Logos"

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.template_file = pathlib.Path(plugin_utils.path).joinpath('logos.html')
        self.template = StringIO()
        self.template.write(open(self.template_file).read())

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        return render_template_string(self.template.getvalue(), request=request, session=session, fhdhr=self.fhdhr, list=list, origin=self.plugin_utils.namespace)
