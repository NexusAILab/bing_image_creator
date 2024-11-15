# Bing Image Creator

A Python package for generating images using Bing Image Creator.

## Installation

```bash
pip install bing-image-creator
```

## Usage

```python
import asyncio
from bing_image_creator import BingImageCreator

async def main():
    creator = BingImageCreator(cookies=["your_cookie_value"])
    
    images = await creator.generate_images(
        prompt="a cute cat playing with yarn",
        model="dall-e-3", 
    )
    
    # Print the image URLs
    print(images)

# Run the async function
asyncio.run(main())
```

## Authentication

To use this package, you need to provide Bing authentication cookies. You can get these by:

1. Going to `bing.com/images/create`
2. Logging in to your account
3. Opening browser developer tools (F12)
4. Going to Application > Cookies
5. Finding the `_U` cookie value
6. Using this value in the `cookies` parameter when initializing `BingImageCreator`

## Features

- Asynchronous image generation
- Support for DALL-E 3 model
- Multiple images per prompt
- Error handling and retries

## Parameters

- `prompt` (str): The text description of the image you want to generate
- `model` (str, optional): The AI model to use (default: "dall-e-3")


## License

                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
