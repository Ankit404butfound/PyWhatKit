from distutils.core import setup

import setuptools


def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README


with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f]


setup(
    name="pywhatkit",
    packages=setuptools.find_packages(),
    version="5.4.1",
    license="MIT",
    description="PyWhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features",
    author="Ankit Raj Mahapatra",
    author_email="ankitrajjitendra816@gmail.com",
    url="https://github.com/Ankit404butfound/PyWhatKit",
    download_url="https://github.com/Ankit404butfound/PyWhatKit/archive/refs/tags/5.2.1.zip",
    keywords=["sendwhatmsg", "info", "playonyt", "search", "watch_tutorial"],
    install_requires=reqs,
    package_data={"pywhatkit": ["py.typed"]},
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
