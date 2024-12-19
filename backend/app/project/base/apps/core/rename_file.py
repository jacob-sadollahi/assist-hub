import os

from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndUniqueFilename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename_start = filename.replace('.' + ext, '')
        filename = "%s__%s.%s" % (filename_start, get_random_string(15), ext)
        return os.path.join(self.path, filename)


rename_document_file = PathAndUniqueFilename('files/documents')
rename_video_file = PathAndUniqueFilename('files/videos')
rename_image_file = PathAndUniqueFilename('files/images')
