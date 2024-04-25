# setup.py

from setuptools import setup, find_packages

setup(
    name='artpanda',
    version='0.1',
    packages=find_packages(),
    package_data={
        'artpanda': ['prompts/*.md'],
    },
    entry_points={
        'console_scripts': [
            'generate-images=scripts.art:generate_images',
        ],
    },
)