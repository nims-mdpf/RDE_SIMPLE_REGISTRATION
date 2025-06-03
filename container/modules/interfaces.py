from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, Optional, TypeVar

import pandas as pd
from rdetoolkit.models.rde2types import MetaType, RepeatedMetaType
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

    # @abstractmethod
    # def read(self, srcpaths: tuple[Path, ...]):
    #     raise NotImplementedError


class IStructuredDataProcessor(ABC):
    """Abstract base class (interface) for structured data parsers.

    This interface defines the contract that structured data parser
    implementations must follow. The parsers are expected to transform
    structured data, such as DataFrame, into various desired output formats.

    Methods:
        to_csv: A method that saves the given data to a CSV file.

    Implementers of this interface could transform data into various
    formats like CSV, Excel, JSON, etc.
    """

    @abstractmethod
    def to_csv(self, dataframe: pd.DataFrame, save_path: Path, *, header: Optional[list[str]] = None) -> None:
        raise NotImplementedError


class IMetaParser(Generic[T], ABC):
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
        raise NotImplementedError

    @abstractmethod
    def save_meta(
        self, save_path: Path, Meta: Meta, *, const_meta_info: Optional[MetaType] = None, repeated_meta_info: Optional[RepeatedMetaType] = None
    ) -> None:
        raise NotImplementedError


class IGraphPlotter(Generic[T], ABC):
    """Abstract base class (interface) for graph plotting implementations.
    This interface defines the contract that graph plotting
    implementations must follow. The implementations are expected
    to be capable of plotting a simple graph using a given pandas DataFrame.

    Methods:
        simple_plot: Plots a simple graph using the provided pandas DataFrame.
    """

    # @abstractmethod
    # def plot(self, data: T, save_path: Path, *, title: Optional[str] = None, xlabel: Optional[str] = None, ylabel: Optional[str] = None):
    #    raise NotImplementedError
