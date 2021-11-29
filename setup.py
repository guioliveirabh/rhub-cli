from setuptools import setup, find_packages

setup(
    name='rhub_cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cement',
        'click',
        'fire',
        'requests',
        'typer[all]',
    ],
    entry_points={
        'console_scripts': [
            'poc_click = rhub_cli.click.main:cli',
            'poc_fire = rhub_cli.fire.main:main',
        ],
    },
)
