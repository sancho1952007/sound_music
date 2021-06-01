from setuptools import setup, find_packages
setup_args=dict(
    name="sound_music",
    version="1.0",
    description="This is a simple module to play music using pygame.",
    long_description="This is a module built by Sancho Godinho using pygame to play music",
    licence="MIT",
    packages=['sound_music'],
    author="Sancho Godinho",
    author_email="sanchogodinho98@gmail.com",
    keywords=['play()'],
    url="https://github.com/sancho1952007/sound_music",
    download_url="https://pypi.org/project/sound_music"
    )
install_requires=[
    'pygame'
    ]

if __name__=="__main__":
    setup(**setup_args, install_requires=install_requires)
