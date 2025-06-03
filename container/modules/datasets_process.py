import os
import shutil

from rdetoolkit.models.rde2types import RdeInputDirPaths, RdeOutputResourcePath
from rdetoolkit.rde2util import Meta

from modules.graph_handler import GraphPlotter
from modules.inputfile_handler import FileReader
from modules.meta_handler import MetaParser


class SimpleRegistrationProcessingCoordinator:
    """Coordinator class for managing simple registration processing modules.

    This class serves as a coordinator for simple registration processing modules,
    facilitating the use of various components such as file reading, creating images.
    It is responsible for managing these components and providing
    an organized way to execute the required tasks.

    Args:
        file_reader (FileReader): An instance of the file reader component.
        meta_parser (MetaParser): An instance of the metadata parsing component.
        graph_plotter (GraphPlotter): An instance of the graph plotting component.

    Attributes:
        file_reader (FileReader): The file reader component for reading input data.
        meta_parser (MetaParser): The metadata parsing component for processing metadata.
        graph_plotter (GraphPlotter): The graph plotting component for visualization.

    Example:
        module = SimpleRegistrationProcessingCoordinator(FileReader(), MetaParser(), GraphPlotter())
        # Note: The method 'execute_processing' hasn't been defined in the provided code,
        #       so its usage is just an example here.
        module.execute_processing(srcpaths, resource_paths)
    """

    def __init__(
        self,
        file_reader: FileReader,
        meta_parser: MetaParser,
        graph_plotter: GraphPlotter,
    ):
        self.file_reader = file_reader
        self.meta_parser = meta_parser
        self.graph_plotter = graph_plotter


def simple_registration_module(srcpaths: RdeInputDirPaths, resource_paths: RdeOutputResourcePath) -> None:
    """Not execute structured text processing, metadata extraction, and visualization.
    Simply copy and generate the image files.

    Args:
        srcpaths (RdeInputDirPaths): Paths to input resources for processing.
        resource_paths (RdeOutputResourcePath): Paths to output resources for saving results.

    Returns:
        None
    """
    module = SimpleRegistrationProcessingCoordinator(FileReader(), MetaParser(), GraphPlotter())
    # Divide input File
    main_image_file, other_images, first_file = module.file_reader.divide(resource_paths, srcpaths)
    # Meta (empty)
    module.meta_parser.save_meta(resource_paths.meta.joinpath("metadata.json"), Meta(srcpaths.tasksupport.joinpath("metadata-def.json")))
    # Invoice
    shutil.copy(resource_paths.invoice.joinpath("invoice.json"), os.path.join(resource_paths.struct, "invoice_org.json"))
    # Graph (or rather image creation)
    if main_image_file is not None and first_file is not None:
        module.graph_plotter.create_image(main_image_file, other_images, first_file, resource_paths)


# @catch_exception_with_message("ERROR: failed in data processing")
def dataset(srcpaths: RdeInputDirPaths, resource_paths: RdeOutputResourcePath) -> None:
    """wrapper function for structured processing

    Args:
        srcpaths (RdeInputDirPaths): Paths to input resources for processing.
        resource_paths (RdeOutputResourcePath): Paths to output resources for saving results.

    Returns:
        None
    """
    simple_registration_module(srcpaths, resource_paths)
