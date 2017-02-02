# -*- coding: utf-8 -*-
import json


def get_forbes_json():
    """Return forbes json."""
    with open('./forbes.json') as data_file:
        forbes_json = json.load(data_file)
    return forbes_json
