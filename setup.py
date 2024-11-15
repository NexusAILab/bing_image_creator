from setuptools import setup, find_packages

setup(
    name="bing-image-creator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "beautifulsoup4",
    ],
    author="NexusAI",
    author_email="tempnexusai@gmail.com",
    description="A Python package for generating images using Bing Image Creator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NexusAILab",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 