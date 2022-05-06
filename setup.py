from jhd128x64e import metadata
from setuptools import setup, find_packages

setup(
	name = metadata.name,
	version = metadata.version,
	description = metadata.description,
	license = metadata.license,
	author = metadata.author,
	author_email = metadata.author_email,
	url = metadata.url,
	packages = find_packages(),
)
