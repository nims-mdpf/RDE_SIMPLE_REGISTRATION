import os
import shutil
from pathlib import Path

import cairosvg
import magic
from pdf2image import convert_from_path
from PIL import Image
from rdetoolkit.models.rde2types import RdeOutputResourcePath


class GraphPlotter:
    """Template class generates image files.

    This class generates main image file and other image files as needed.
    It does not create graph images.
    """

    def _create_main_image(self, image_from: str, image_to: Path, raw_folder: str, first_file: str) -> None:
        """Create main image

        Args:
            image_from(str): main image source file
            image_to(Path): main image destination file
            raw_folder(str): raw folder (In case the image could not be created)
            first_file(str): first image (In case the image could not be created)

        Returns:
            None
        """
        try:
            mymime = magic.from_file(image_from, mime=True)
            if mymime == "image/jpeg" or mymime == "image/png" or mymime == "image/gif":
                shutil.copy(image_from, image_to)
            elif mymime == "application/pdf":
                pdf_path = Path(image_from)
                img_path = Path(image_to)
                pages = convert_from_path(pdf_path, dpi=350, last_page=1)
                if len(pages) == 1:
                    pages[0].save(str(img_path.joinpath(Path(pdf_path).stem + ".png")))
            elif mymime == "image/svg+xml":
                svg_path = Path(image_from)
                basename = Path(image_from).stem
                save_main_path = str(image_to.joinpath(basename + ".png"))
                os.environ['LC_CTYPE'] = "ja_JP.UTF-8"
                cairosvg.svg2png(url=str(svg_path), write_to=save_main_path)
            else:
                img = Image.open(image_from)
                img.save(str(image_to.joinpath(Path(image_from).stem + ".png")))
        except Exception:
            pass  # before v5
            # shutil.copy(os.path.join(raw_folder, first_file), image_to)  # v6 or later

    def _create_other_image(self, images_from: list, image_to: Path) -> None:
        """Create other image

        Args:
            images_from(list): image files list
            image_to(Path): other image destination folder

        Returns:
            None
        """
        for image_from in images_from:
            src_base_name = os.path.basename(image_from)
            mymime = magic.from_file(image_from, mime=True)
            if mymime == "image/jpeg" or mymime == "image/png" or mymime == "image/gif":
                shutil.copy(image_from, os.path.join(image_to, src_base_name))
            elif mymime == "application/pdf":
                pdf_path = Path(image_from)
                img_path = Path(image_to)
                pages = convert_from_path(pdf_path, dpi=350, last_page=1)
                if len(pages) == 1:
                    pages[0].save(str(img_path.joinpath(Path(pdf_path).stem + ".png")))
            elif mymime == "image/svg+xml":
                svg_path = Path(image_from)
                img_path = Path(os.path.join(image_to, src_base_name))
                basename = Path(img_path).stem
                save_other_path = str(image_to.joinpath(basename + ".png"))
                os.environ['LC_CTYPE'] = "ja_JP.UTF-8"
                cairosvg.svg2png(url=str(svg_path), write_to=save_other_path)
            else:
                img = Image.open(image_from)
                img.save(str(image_to.joinpath(Path(image_from).stem + ".png")))

    def create_image(self, main_image_file: str, other_files: list, first_file: str, resource_paths: RdeOutputResourcePath) -> None:
        """Create a main image and other images.

        Args:
            main_image_file (str): source file
            other_files (Path): destination folder
            first_file (str): first file (In case the image could not be created)
            resource_paths (RdeOutputResourcePath): Paths to input source files (In case the image could not be created)
        """
        self._create_main_image(main_image_file, resource_paths.main_image, str(resource_paths.raw), first_file)
        self._create_other_image(other_files, resource_paths.other_image)
