import io
import logging
import os
from pathlib import Path
from typing import List

import dotenv
import openai
import requests
from PIL import Image

from artpanda import prebuilts
from artpanda.const import Paths

# set logging to info level
# logging.getLogger().setLevel(logging.INFO)

dotenv.load_dotenv()


class ImageDrawer(object):
    def __init__(self, output_folder: Path = Path('output')):
        self.openai = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                                    organization=os.getenv("OPENAI_ORG"))
        self.prompt_template = open(Paths.generic_prompt).read()
        self.output_folder = output_folder
        self.output_folder.mkdir(exist_ok=True)

    def run(self,
            subject_detailed: str,
            style_name: str = 'flat',
            asset_name: str = 'svg',
            n=5):
        asset_text = prebuilts.asset_types[asset_name]
        style_text = prebuilts.styles[style_name]

        out_subfolder = self.output_folder  / style_name
        out_subfolder.mkdir(exist_ok=True, parents=True)

        generated_images = []
        for n in range(n):
            res = self.run_prompt(style_text, subject_detailed, asset_text, out_subfolder / f'img{n}.jpg')
            generated_images.extend(res)

        return generated_images

    def run_prompt(self, style: str, subject: str, asset: str, out_path: Path) -> List[Path]:
        prompt = self.prompt_template.format(asset=asset,
                                             style=style,
                                             subject=subject,
                                             )
        logging.info(f'generating image with prompt\n {prompt}')

        data = self.openai.images.generate(prompt=prompt, n=1, model="dall-e-3").data
        img_paths = []

        for i, image in enumerate(data):
            print()
            img_url = image.url
            # get the image content and save it to a file

            image_path = out_path
            img_content = requests.get(img_url).content

            # read the image into PIL, and save it as a 90 quality jpg
            bytes = io.BytesIO(img_content)
            img = Image.open(bytes)
            img.save(image_path, 'jpeg', quality=90)

            img_paths.append(image_path)
            logging.info(f'Image {i} saved to {image_path}')

        return img_paths


def main():
    drawer = ImageDrawer()
    for style in ['pop-art']:
        res = drawer.run("A whimsical friendly black and white panda running very fast",
                         style_name=style,
                         asset_name='svg',
                         run_name='fast panda',
                         n=5,
                         )


if __name__ == '__main__':
    main()
