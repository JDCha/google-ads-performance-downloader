from setuptools import setup, find_packages

setup(
    name='google-adwords-performance-downloader',
    version='1.7.1',
    description="Downloads data from the Google Adwords Api to local files",

    install_requires=[
        'googleads==11.0.1',
        'click>=6.0',
        'mara-config>=0.1'

    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={
        'console_scripts': [
            'download-adwords-performance-data=adwords_downloader.cli:download_data',
            'refresh-adwords-api-oauth2-token=adwords_downloader.cli:refresh_oauth2_token'
        ]
    }
)
