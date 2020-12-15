# -*- coding：utf-8 -*-
import mimetypes
import os
from flask import send_from_directory, make_response


def yds(filename):
    path = os.getcwd() + "/files/" + filename
    def file_iterator(filename, chunk_size=512):
        with open(filename) as f:
            b = f.read(chunk_size)
            return b

    try:
        response = make_response(file_iterator(path))
        mime_type = mimetypes.guess_type(filename)[0]
        response.headers['Content-Type'] = mime_type
        response.headers[
            'Content-Disposition'] = 'attachment; filename={}'.format(
            filename.encode().decode('latin-1'))

        return response

    except:
        return "something error"



