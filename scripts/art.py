from pathlib import Path

import click
from artpanda.art import ImageDrawer


@click.command()
@click.option('--output_path',
              default='./output',
              help='The path where the images will be saved.')
@click.option('--subject',
              prompt='Enter the subject you wish to drew. Example: "a black and white panda standing in front of a canvas and painting"',
              help='The subject to draw.',
              default=None, show_default=False, required=False)
@click.option('--style', multiple=True, default=['flat', 'modernist', 'line art', 'pop-art'],
              help='A list of styles to generate images in.')
@click.option('--n', default=1, type=int,
              help='Number of images to generate. Default is 1.')
def generate_images(subject, style, n, output_path):
    """
    CLI for generating images using a specified subject, styles, and number of images.
    The asset_name is hardcoded to 'svg'.
    """
    # Instantiate the ImageDrawer class (assuming it's defined elsewhere)
    drawer = ImageDrawer(Path(output_path))

    # Loop through each style provided
    for s in style:
        res = drawer.run(subject,
                         style_name=s,
                         asset_name='svg',
                         n=n,
                         )
        print(f'Generated images in style {s}')
        print([str(s.absolute()) for s in res])


if __name__ == '__main__':
    generate_images()
