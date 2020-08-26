from distutils.core import setup
import setuptools

def readme():
    with open(r'README.txt') as f:
        README = f.read()
    return README

setup(
    name = 'pywhatkit',
    packages = setuptools.find_packages(),
    version = '2.9',
    license='MIT',
    description = 'pywhatkit is a Python library for Sending whatsapp message at certain time, it has several other features too.',
    author = 'Ankit Raj Mahapatra',
    author_email = 'ankitrajjitendra816@gmail.com',
    url = 'https://github.com/Ankit404butfound/awesomepy',
    download_url = 'https://github.com/Ankit404butfound/awesomepy/archive/1.0.tar.gz',
    keywords = ['sendwhatmsg', 'info', 'playonyt', 'search','watch_tutorial'],
    install_requires=[
          'pyautogui',
          'beautifulsoup4',
          'wikipedia',
          'requests',
          'Pillow',
          'numpy',
          'opencv-python',
          
      ],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)
