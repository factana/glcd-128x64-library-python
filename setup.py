from glcd_jhd128x64e import metadata
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
	name = metadata.name,
	version = metadata.version,
	description = metadata.description,
	license = metadata.license,
	author = metadata.author,
	author_email = metadata.author_email,
	url = metadata.url,
	keywords = metadata.keywords,
	packages = find_packages(),
	long_description=long_description,
	long_description_content_type='text/markdown',
	classifiers=[
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3.10',
          'Topic :: System :: Hardware :: Hardware Drivers',
          'Topic :: Software Development :: Libraries :: Python Modules',
	]
)
