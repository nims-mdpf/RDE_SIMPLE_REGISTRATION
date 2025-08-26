import magic
import mimetypes
import os
from typing import Optional

from rdetoolkit.models.rde2types import RdeInputDirPaths, RdeOutputResourcePath
from rdetoolkit.rde2util import read_from_json_file


class FileReader:
    """Template class for dividing input files.

    This class provides the ability to sort the input files into main image files
    and other image files.
    """

    def _extract_image_files(self, files: list) -> list:
        """Extract image files

        Args:
            files(list): all input files

        Returns:
            list: all input image files
        """
        image_files, images_magic, images_mime, pdfs = [], [], [], []

        try:
            for file in files:
                if magic.from_file(file, mime=True)[:5] in ("image"):
                    images_magic.append(file)
                mimetype = mimetypes.guess_type(file)[0]
                if mimetype is None:
                    continue
                if mimetype[:5] in ("image"):
                    images_mime.append(file)
                if mimetype in ("application/pdf"):
                    pdfs.append(file)
            image_files = sorted(list(set(images_magic) | set(images_mime) | set(pdfs)), key=str.lower)
        except Exception:
            image_files.clear()
            pass

        return image_files

    def divide(self, resource_paths: RdeOutputResourcePath, srcpaths: RdeInputDirPaths) -> tuple[Optional[str], list, Optional[str]]:
        """Divide the input file into main image file and other image files.

        Args:
            resource_paths (RdeOutputResourcePath): Paths to input source files.
            srcpaths (RdeInputDirPaths): Paths to input directory.

        Returns:
            Optional[str]: main image
            list: other images
            Optional[str]: first image
        """
        main_image_file = None
        first_file = None
        image_files = []
        files = [str(f) for f in resource_paths.rawfiles]

        # Extract image files
        image_files = self._extract_image_files(files)
        if len(image_files) == 0:
            return main_image_file, image_files, first_file

        # Determine main image
        invoice_obj = read_from_json_file(resource_paths.invoice.joinpath("invoice.json"))
        first_file = os.path.basename(str(image_files[0]))
        main_image_basename = first_file
        if invoice_obj["custom"].get('main_image') is not None:
            main_image_to_select = invoice_obj["custom"]["main_image"]
            if main_image_to_select is not None:
                if srcpaths.config.system.save_nonshared_raw:
                    if os.path.isfile(str(resource_paths.nonshared_raw.joinpath(main_image_to_select.strip()))):
                        main_image_basename = main_image_to_select.strip()
                elif srcpaths.config.system.save_raw:
                    if os.path.isfile(str(resource_paths.raw.joinpath(main_image_to_select.strip()))):
                        main_image_basename = main_image_to_select.strip()
        if srcpaths.config.system.save_nonshared_raw:
            main_image_file = str(resource_paths.nonshared_raw.joinpath(main_image_basename))
        elif srcpaths.config.system.save_raw:
            main_image_file = str(resource_paths.raw.joinpath(main_image_basename))

        # Exclude main image form all image files
        for image_file in image_files:
            src_basename = os.path.basename(image_file)
            if src_basename == main_image_basename:
                image_files.remove(image_file)

        return main_image_file, image_files, first_file
