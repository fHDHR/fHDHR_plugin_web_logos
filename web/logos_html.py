from flask import request, render_template_string, session
import os
import pathlib
from io import StringIO

import urllib.parse


class Logos_html():
    endpoints = ["/logos", "/logos.html"]
    endpoint_name = "page_logos_html"
    endpoint_category = "pages"
    pretty_name = "Logos"

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.logo_files = pathlib.Path(plugin_utils.path).joinpath('logos')

        self.template_file = pathlib.Path(plugin_utils.path).joinpath('logos.html')
        self.template = StringIO()
        self.template.write(open(self.template_file).read())

    def __call__(self, *args):
        return self.handler(*args)

    def handler(self, *args):

        logo_list = self.list_logos
        logo_dicts = []
        for logo in logo_list:
            logo_dicts.append({
                "name": logo.split(".")[0],
                "url": "/api/logos?logo_name=%s" % urllib.parse.quote(logo.split(".")[0])
            })

        return render_template_string(self.template.getvalue(), request=request, session=session, fhdhr=self.fhdhr, logo_dicts=logo_dicts, list=list, origin=self.plugin_utils.namespace)

    @property
    def list_logos(self):
        return os.listdir(self.logo_files)
