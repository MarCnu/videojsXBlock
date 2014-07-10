"""Setup for videojsXBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='videojs-xblock',
    version='0.1',
    description='XBlock to use the Video.js player in edX, instead of the default one.',
    packages=[
        'videojs',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'videojs = videojs:videojsXBlock',
        ]
    },
    package_data=package_data("videojs", "static"),
)