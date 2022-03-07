from flask import send_from_directory, redirect, request
import os
import pathlib

from fHDHR.tools import inlist_match


class Logos_API():
    endpoints = ["/api/logos"]
    endpoint_name = "api_logos"

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.logo_files = pathlib.Path(plugin_utils.path).joinpath('logos')

    def __call__(self, *args):
        return self.handler(*args)

    def handler(self, *args):

        logo_name = request.args.get('logo_name', default="", type=str)

        match, matched = inlist_match("%s.png" % logo_name, self.list_logos)
        if matched:
            logo_file_location = pathlib.Path(self.logo_files).joinpath(match)
        else:
            logo_file_location = None

        if logo_file_location:
            logo_file_open = open(logo_file_location, "rb")
            logo_file = logo_file_open.read()
            logo_file_open.close()

            imagemimetype = self.fhdhr.device.images.get_image_type(logo_file)

            return send_from_directory(self.logo_files, match, mimetype=imagemimetype)

        else:
            redirect_url = "/api/images?method=generate&type=channel&message=%s" % logo_name
            return redirect(redirect_url)

    @property
    def list_logos(self):
        return os.listdir(self.logo_files)
