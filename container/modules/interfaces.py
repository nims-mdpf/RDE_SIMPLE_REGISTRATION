from abc import ABC, abstractmethod
from pathlib import Path
from typing import TypeVar

from rdetoolkit.models.rde2types import MetaType, RdeInputDirPaths, RdeOutputResourcePath, RepeatedMetaType
from rdetoolkit.rde2util import Meta

T = TypeVar("T")


class IInputFileParser(ABC):
    """Abstract base class (interface) for input file parsers.

    This interface defines the contract that input file parser
    implementations must follow. The parsers are expected to read files
    from a specified path, parse the contents of the files, and provide
    options for saving the parsed data.

    Methods:
        read: A method expecting a file path and responsible for reading a file.

    Example implementations of this interface could be for parsing files
    of different formats like CSV, Excel, JSON, etc.

    """

    @abstractmethod
    def divide(
        self,
        resource_paths: RdeOutputResourcePath,
        srcpaths: RdeInputDirPaths,
    ) -> tuple[str | None, list, str | None]:
        """Divide the input file into main image file and other image files."""
        raise NotImplementedError


class IMetaParser[T](ABC):
    """Abstract base class (interface) for meta information parsers.

    This interface defines the contract that meta information parser
    implementations must follow. The parsers are expected to save the
    constant and repeated meta information to a specified path.

    Method:
        save_meta: Saves the constant and repeated meta information to a specified path.
        parse: This method returns two types of metadata: const_meta_info and repeated_meta_info.
    """

    @abstractmethod
    def parse(self, data: T) -> tuple[MetaType, RepeatedMetaType]:
        """Parse and extract constant and repeated metadata from the provided data."""
        raise NotImplementedError

    @abstractmethod
    def save_meta(
        self,
        save_path: Path,
        metaobj: Meta,
        *,
        const_meta_info: MetaType | None = None,
        repeated_meta_info: RepeatedMetaType | None = None,
    ) -> None:
        """Save parsed metadata to a file using the provided Meta object."""
        raise NotImplementedError


class IGraphPlotter[T](ABC):
    """Abstract base class (interface) for graph plotting implementations.

    This interface defines the contract that graph plotting
    implementations must follow. The implementations are expected
    to be capable of plotting a simple graph using a given pandas DataFrame.

    Methods:
        simple_plot: Plots a simple graph using the provided pandas DataFrame.

    """

    @abstractmethod
    def create_image(
            self,
            main_image_file: str,
            other_files: list,
            first_file: str,
            resource_paths: RdeOutputResourcePath,
    ) -> None:
        """Create a main image and other images."""
        raise NotImplementedError
