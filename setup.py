from setuptools import setup, find_packages

setup(
    name='dino-terminal',
    version='1.0.0',
    description="Chrome Dino game in your terminal",
    author="Alabi Busayo",
    author_email="busayo_jee@yahoo.com",
    url="https://github.com/busayojee/games/tree/master/dino-terminal",
    classifiers=[
        "Environment :: Console :: Curses",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    install_requires=[
       "curses-menu>=0.7.1",
       "click==8.1.7"
    ],
    entry_points={
        'console_scripts': [
            'dino-terminal = dinoterm.main:main',
        ],
    },
)
