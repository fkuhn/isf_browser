import os

from setuptools import find_packages, setup

cur_dir = os.path.dirname(__file__)
readme = os.path.join(cur_dir, 'README.md')
if os.path.exists(readme):
    with open(readme) as fh:
        long_description = fh.read()
else:
    long_description = ''

setup(
    name='isf_browser',
    version='0.1',
    description='Webbasierter Browser für die ISF Datenbank.'
                ' Basierend auf SQLITE-Web (v0.3.5) von Charles Leifner',
    long_description=long_description,
    author='Florian Kuhn',
    author_email='fkuhn@posteo.de',
    url='https://github.com/fkuhn/isf_browser',
    license='MIT',
    install_requires=[
        'flask',
        'peewee>=3.0.0',
        'pygments',
        'flask_wtf'
    ],
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'sqlite_web': [
            'static/*/*',
            'templates/*'
        ],
    },
    entry_points={
        'console_scripts': [
            'sqlite_web = sqlite_web.sqlite_web:main'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
