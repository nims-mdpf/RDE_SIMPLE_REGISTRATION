import os
import shutil
from typing import List, Union


def setup_inputdata_folder(inputdata_name: Union[str, List[str]], case_name: str):
    """テスト用でdataフォルダ群の作成とrawファイルの準備
    Args:
        inputdata_name (Union[str, List[str]]): rawファイル名
    """
    destination_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(destination_path, exist_ok=True)
    os.makedirs(os.path.join(destination_path, "inputdata"), exist_ok=True)
    os.makedirs(os.path.join(destination_path, "invoice"), exist_ok=True)
    inputdata_original_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "inputdata", "examples", "dt0001", case_name
    )
    if isinstance(inputdata_name, List):
        for item in inputdata_name:
            shutil.copy(
                os.path.join(inputdata_original_path, item),
                os.path.join(destination_path, "inputdata"),
            )
    else:
        shutil.copy(
            os.path.join(inputdata_original_path, inputdata_name),
            os.path.join(destination_path, "inputdata"),
        )
    shutil.copy(
        os.path.join(inputdata_original_path, "invoice.json"),
        os.path.join(destination_path, "invoice"),
    )

    # tasksupport
    os.makedirs(os.path.join(destination_path, "tasksupport"), exist_ok=True)
    tasksupport_original_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "templates", "dt0001", "tasksupport"
    )
    shutil.copy(
        os.path.join(tasksupport_original_path, "default_value.csv"),
        os.path.join(destination_path, "tasksupport"),
    )
    shutil.copy(
        os.path.join(tasksupport_original_path, "invoice.schema.json"),
        os.path.join(destination_path, "tasksupport"),
    )
    shutil.copy(
        os.path.join(tasksupport_original_path, "metadata-def.json"),
        os.path.join(destination_path, "tasksupport"),
    )
    shutil.copy(
        os.path.join(tasksupport_original_path, "rdeconfig.yaml"),
        os.path.join(destination_path, "tasksupport"),
    )
    if case_name == 'invoice_multidatatile':
        shutil.copy(
            os.path.join(inputdata_original_path, "rdeconfig.yaml"),
            os.path.join(destination_path, "tasksupport"),
        )


class TestOutputCaseInvoiceNoImage:
    """case1 invoice_no-image
    インボイスモード(画像なし)のテスト:
        "MIDATA001.108.spe"
    """

    inputdata: Union[str, List[str]] = [
        "MIDATA001.108.spe"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_no-image")

    def test_raw_data(self, setup_main, data_path):
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "MIDATA001.108.spe"))

    def test_main_image(self):
        assert True

    def test_other_image(self):
        assert True

    def test_structured(self):
        assert True

    def test_meta(self, data_path):
        assert os.path.exists(os.path.join(data_path, "meta", "metadata.json"))


class TestOutputCaseInvoiceWithImage:
    """case2 invoice_with-image
    インボイスモード(画像あり)のテスト:
        "image.tif"
        "f27.bmp"
        "report.pdf"
        "materials.svg"
    """

    inputdata: Union[str, List[str]] = [
        "image.tif",
        "f27.bmp",
        "report.pdf",
        "materials.svg"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_with-image")

    def test_raw_data(self, setup_main, data_path):
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "image.tif"))
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "f27.bmp"))
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "report.pdf"))
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "materials.svg"))

    def test_main_image(self, data_path):
        assert os.path.exists(os.path.join(data_path, "main_image", "report.png"))

    def test_other_image(self, data_path):
        assert os.path.exists(os.path.join(data_path, "other_image", "f27.png"))
        assert os.path.exists(os.path.join(data_path, "other_image", "Mo50Ti15C-20230111-10mN-00.png"))
        assert os.path.exists(os.path.join(data_path, "other_image", "materials.png"))

    def test_structured(self):
        assert True

    def test_meta(self, data_path):
        assert os.path.exists(os.path.join(data_path, "meta", "metadata.json"))


class TestOutputCaseMultiDataTile:
    """case3 multiDataTile
    マルチデータタイルのテスト:
        "image.tif"
        "f27.bmp"
        "materials.svg"
        "report.pdf"
    """

    inputdata: Union[str, List[str]] = [
        "image.tif",
        "f27.bmp",
        "materials.svg",
        "report.pdf"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_multidatatile")

    def test_raw_data(self, setup_main, data_path):
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "image.tif"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "nonshared_raw", "f27.bmp"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "materials.svg"))
        assert os.path.exists(os.path.join(data_path, "divided", "0003", "nonshared_raw", "report.pdf"))

    def test_main_image(self, data_path):
        assert os.path.exists(os.path.join(data_path, "main_image", "Mo50Ti15C-20230111-10mN-00.png"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "main_image", "f27.png"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "main_image", "materials.png"))
        assert os.path.exists(os.path.join(data_path, "divided", "0003", "main_image", "report.png"))

    def test_structured(self):
        assert True

    def test_meta(self, data_path):
        assert os.path.exists(os.path.join(data_path, "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0003", "meta", "metadata.json"))


class TestOutputCaseExcelInvoiceFile:
    """case4 excelinvoice_file
    エクセルインボイスモード(ファイル)のテスト:
        "test_3_files.zip"
        "TEST_file_excel_invoice.xlsx"
    """

    inputdata: Union[str, List[str]] = [
        "test_3_files.zip",
        "TEST_file_excel_invoice.xlsx"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "excelinvoice_file")

    def test_raw_data(self, setup_main, data_path):
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "GaP_test_002_DOS.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "nonshared_raw", "GaP_test_002.cif"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_002_BandStr.csv"))

    def test_main_image(self):
        assert True

    def test_other_image(self):
        assert True

    def test_structured(self):
        assert True

    def test_meta(self, data_path):
        assert os.path.exists(os.path.join(data_path, "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "meta", "metadata.json"))


class TestOutputCaseExcelInvoiceFolder:
    """case5 excelinvoice_folder
    エクセルインボイスモード(フォルダ)のテスト:
        "test_3_folders.zip"
        "TEST_folder_excel_invoice.xlsx"
    """

    inputdata: Union[str, List[str]] = [
        "test_3_folders.zip",
        "TEST_folder_excel_invoice.xlsx"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "excelinvoice_folder")

    def test_raw_data(self, setup_main, data_path):
        assert os.path.exists(os.path.join(data_path, "nonshared_raw", "GaP_test_001.cif"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "nonshared_raw", "GaP_test_002_BandStr.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "nonshared_raw", "GaP_test_002_DOS.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "nonshared_raw", "GaP_test_002.cif"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_003 Elastic Constants.txt"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_003_BandStr.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_003_DOS.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_003_PhonDOS.csv"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "nonshared_raw", "GaP_test_003.cif"))

    def test_main_image(self):
        assert True

    def test_other_image(self):
        assert True

    def test_structured(self):
        assert True

    def test_meta(self, data_path):
        assert os.path.exists(os.path.join(data_path, "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0001", "meta", "metadata.json"))
        assert os.path.exists(os.path.join(data_path, "divided", "0002", "meta", "metadata.json"))
