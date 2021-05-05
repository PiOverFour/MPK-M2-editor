from setuptools import setup

setup(
    name='mpk-m2-editor',
    description='An alternative to the official AKAI MPKMini MkII Editor',
    author='Damien Picard',
    author_email='dam.pic@free.fr',
    url='https://github.com/PiOverFour/MPK-M2-editor',
    packages=['ui'],
    install_requires=['python-rtmidi', 'pyqt5'],
    scripts=['mpk-m2-editor.py'],
    include_package_data=True
)
