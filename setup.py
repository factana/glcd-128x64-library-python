from glcd_jhd128x64e import metadata
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "readme.md").read_text()

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
  	long_description_content_type='text/markdown'
	classifiers=[
          'License :: MIT License',
          'Operating System :: LINUX',
          'Programming Language :: Python,
          'Topic :: System :: Hardware :: Hardware Drivers',
          'Topic :: Software Development :: Libraries :: Python Modules',
	]
)
