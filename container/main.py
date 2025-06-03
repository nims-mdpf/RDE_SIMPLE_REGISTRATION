import rdetoolkit
from modules import datasets_process


if __name__ == "__main__":

    rdetoolkit.workflows.run(custom_dataset_function=datasets_process.dataset)
