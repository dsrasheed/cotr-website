from setuptools import setup

setup(
	name="ColorsOfTheRegion",
	description=__doc__,
	packages=["cotr"],
	include_package_data=True,
	install_requires=[
		"flask"
	]
)
