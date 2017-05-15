from setuptools import setup

setup(
	name="ColorsOfTheRegion",
	packages=["cotr"],
	include_package_data=True,
	install_requires=[
		"flask",
		"flask-sqlalchemy",
		"flask-wtforms",
		"flask-bcrypt"
	]
)
