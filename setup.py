from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

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
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NexusAILab/bing-image-creator",
    project_urls={
        "Bug Tracker": "https://github.com/NexusAILab/bing-image-creator/issues",
        "Documentation": "https://github.com/NexusAILab/bing-image-creator#readme",
        "Source Code": "https://github.com/NexusAILab/bing-image-creator",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.8",
    keywords="bing, image generation, dall-e, ai, artificial intelligence",
) 