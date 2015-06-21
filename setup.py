from distutils.core import setup
from smart_getenv import __version__



setup(
    name='smart-getenv',
    version=__version__,
    author='Valentyn Barmashyn',
    author_email='valpreacher@gmail.com',
    url='https://github.com/Va1/python-smart-getenv',
    license='Apache License 2.0',
    description="Wrapper for os.getenv that achieves return values of a specified type ",
    long_description="Since environment variables in os.environ are strings, "
                     "it often appears inconvenient to store and retrieve other "
                     "data types such as bool or list. The package provides a single function "
                     "that wraps os.getenv and allows you to specify the desired variable type.",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System',
        'Topic :: Utilities'
    ],
    py_modules=['smart_getenv'],
    test_suite='tests'
)
