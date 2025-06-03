import json
import os
import shutil
from typing import Union, List


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


class TestMetaInvoiceNoImage:
    """case1
    インボイスモード(画像なし)のテスト:
        "MIDATA001.108.spe"
    """

    inputdata: Union[str, List[str]] = [
        "MIDATA001.108.spe"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_no-image")

    def test_metadata_constant(self, setup_main, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        for k in contents["constant"].keys():
            constant_meta_key = setup_metadatadef_json.get(k)
            assert constant_meta_key

    def test_metadata_variable(self, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        result_variable_keys = [k for item in contents["variable"] for k in item.keys()]
        for k in result_variable_keys:
            # metadata.json: variable
            variable_meta_key = setup_metadatadef_json.get(k)
            # check defined variable = 1
            except_variable_flag = setup_metadatadef_json[k].get("variable")

            assert (all(variable_meta_key)) and (except_variable_flag is not None)


class TestMetaInvoiceWithImage:
    """case2
    インボイスモード(画像あり)のテスト:
        "Mo50Ti15C-20230111-10mN-00.tif"
        "f27.bmp"
        "report.pdf"
        "materials.svg"
    """

    inputdata: Union[str, List[str]] = [
        "Mo50Ti15C-20230111-10mN-00.tif",
        "f27.bmp",
        "report.pdf",
        "materials.svg"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_with-image")

    def test_metadata_constant(self, setup_main, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        for k in contents["constant"].keys():
            constant_meta_key = setup_metadatadef_json.get(k)
            assert constant_meta_key

    def test_metadata_variable(self, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        result_variable_keys = [k for item in contents["variable"] for k in item.keys()]
        for k in result_variable_keys:
            # metadata.json: variable
            variable_meta_key = setup_metadatadef_json.get(k)
            # check defined variable = 1
            except_variable_flag = setup_metadatadef_json[k].get("variable")

            assert (all(variable_meta_key)) and (except_variable_flag is not None)


class TestMetaMultiDataTile:
    """case3
    マルチデータタイルのテスト:
        "Mo50Ti15C-20230111-10mN-00.tif"
        "f27.bmp"
        "report.pdf"
        "materials.svg"
    """

    inputdata: Union[str, List[str]] = [
        "Mo50Ti15C-20230111-10mN-00.tif",
        "f27.bmp",
        "report.pdf",
        "materials.svg"
    ]

    def test_setup(self):
        setup_inputdata_folder(self.inputdata, "invoice_multidatatile")

    def test_metadata_constant(self, setup_main, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        for k in contents["constant"].keys():
            constant_meta_key = setup_metadatadef_json.get(k)
            assert constant_meta_key

    def test_metadata_variable(self, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        result_variable_keys = [k for item in contents["variable"] for k in item.keys()]
        for k in result_variable_keys:
            # metadata.json: variable
            variable_meta_key = setup_metadatadef_json.get(k)
            # check defined variable = 1
            except_variable_flag = setup_metadatadef_json[k].get("variable")

            assert (all(variable_meta_key)) and (except_variable_flag is not None)


class TestMetaExcelInvoiceFile:
    """case4
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

    def test_metadata_constant(self, setup_main, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        for k in contents["constant"].keys():
            constant_meta_key = setup_metadatadef_json.get(k)
            assert constant_meta_key

    def test_metadata_variable(self, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        result_variable_keys = [k for item in contents["variable"] for k in item.keys()]
        for k in result_variable_keys:
            # metadata.json: variable
            variable_meta_key = setup_metadatadef_json.get(k)
            # check defined variable = 1
            except_variable_flag = setup_metadatadef_json[k].get("variable")

            assert (all(variable_meta_key)) and (except_variable_flag is not None)


class TestMetaExcelInvoiceFolder:
    """case5
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

    def test_metadata_constant(self, setup_main, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        for k in contents["constant"].keys():
            constant_meta_key = setup_metadatadef_json.get(k)
            assert constant_meta_key

    def test_metadata_variable(self, setup_metadatadef_json):
        metadata = "metadata.json"
        result_metadata_filepath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "meta", metadata
        )

        with open(result_metadata_filepath, mode="r", encoding="utf-8") as f:
            contents = json.load(f)

        result_variable_keys = [k for item in contents["variable"] for k in item.keys()]
        for k in result_variable_keys:
            # metadata.json: variable
            variable_meta_key = setup_metadatadef_json.get(k)
            # check defined variable = 1
            except_variable_flag = setup_metadatadef_json[k].get("variable")

            assert (all(variable_meta_key)) and (except_variable_flag is not None)
