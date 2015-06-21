__version__ = '1.0.0'

import os


def getenv(name, **kwargs):
    """
    Retrieves environment variable by name and casts the value to desired type.
    If desired type is list or tuple - uses separator to split the value.
    """
    default_value = kwargs.pop('default', None)
    desired_type = kwargs.pop('type', str)
    list_separator = kwargs.pop('separator', ',')

    value = os.getenv(name, None)

    if value is None:
        if default_value is None:
            return None
        else:
            return default_value

    if desired_type is bool:
        if value.lower() in ['false', '0']:
            return False
        else:
            return bool(value)

    if desired_type is list or desired_type is tuple:
        value = value.split(list_separator)
        return desired_type(value)

    if desired_type is dict:
        return dict(eval(value))

    return desired_type(value)
