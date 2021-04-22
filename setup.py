from setuptools import setup

setup(
    name='mpk-m2-editor',
    packages=['ui'],
    install_requires=['python-rtmidi', 'pyqt5'],
    scripts=['mpk-m2-editor.py']
)
