# Bing Image Creator 🎨

A Python package for generating images using Bing Image Creator powered by DALL-E 3.

[![PyPI version](https://badge.fury.io/py/bing-image-creator.svg)](https://badge.fury.io/py/bing-image-creator)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 📦 Installation

```bash
pip install bing-image-creator
```

## 🚀 Quick Start

### ⚡ Asynchronous Usage
```python
import asyncio
from bing_image_creator import BingImageCreator

async def main():
    creator = BingImageCreator(cookies=["your_cookie_value"])
    
    # Generate and get image URLs only
    images = await creator.generate_images(
        prompt="a cute cat playing with yarn",
        model="dall-e-3"
    )
    print(images)

asyncio.run(main())
```

### 🔄 Synchronous Usage
```python
from bing_image_creator import BingImageCreator

creator = BingImageCreator(cookies=["your_cookie_value"])
images = creator.generate_images_sync(
    prompt="a cute cat playing with yarn",
    model="dall-e-3"
)
print(images)
```

## 🔑 Authentication

To use this package, you need to provide Bing authentication cookies:

1. Visit [Bing Image Creator](https://www.bing.com/images/create)
2. Log in to your account
3. Open browser developer tools (F12)
4. Navigate to Application > Cookies
5. Find the `_U` cookie value
6. Use this value in the `cookies` parameter when initializing `BingImageCreator`

## ✨ Features

- ⚡ Asynchronous image generation
- 🎨 Support for DALL-E 3 model
- 🖼️ Multiple images per prompt
- 💾 Automatic image saving
- 🔄 Error handling and retries

## 📝 Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `prompt` | str | Text description of the desired image | Required |
| `model` | str | AI model to use | "dall-e-3" |
| `output_dir` | str | Directory path for saving images | None |

## 📂 Output Format

When saving images locally:
- File naming: `{prompt}_{index}{extension}`
- Prompt is truncated to 50 characters
- Original extensions preserved (defaults to .jpg)
- Example: `a_cute_cat_playing_with_yarn_0.jpg`

Returns a list of image URLs regardless of local saving.

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
