from abc import ABC

import pytest

from inventory_report.importers import CsvImporter, Importer, JsonImporter
from inventory_report.product import Product

PRODUCTS = [
    Product(**product)
    for product in [
        {
            "id": "1",
            "product_name": "Nicotine Polacrilex",
            "company_name": "Target Corporation",
            "manufacturing_date": "2021-02-18",
            "expiration_date": "2023-09-17",
            "serial_number": "CR25 1551 4467 2549 4402 1",
            "storage_instructions": "instrucao 1",
        },
        {
            "id": "2",
            "product_name": "fentanyl citrate",
            "company_name": "Target Corporation",
            "manufacturing_date": "2020-12-06",
            "expiration_date": "2023-12-25",
            "serial_number": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "storage_instructions": "instrucao 2",
        },
        {
            "id": "3",
            "product_name": "NITROUS OXIDE",
            "company_name": "Galena Biopharma",
            "manufacturing_date": "2020-12-22",
            "expiration_date": "2024-11-07",
            "serial_number": "CZ09 8588 0858 8435 9140 2695",
            "storage_instructions": "instrucao 3",
        },
        {
            "id": "4",
            "product_name": "Norepinephrine Bitartrate",
            "company_name": "Cantrell Drug Company",
            "manufacturing_date": "2020-12-24",
            "expiration_date": "2025-08-19",
            "serial_number": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
            "storage_instructions": "instrucao 4",
        },
        {
            "id": "5",
            "product_name": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
            "company_name": "Moore Medical LLC",
            "manufacturing_date": "2021-04-14",
            "expiration_date": "2025-01-14",
            "serial_number": "LV23 ELDS 2GD5 X19P VCSI K",
            "storage_instructions": "instrucao 5",
        },
        {
            "id": "6",
            "product_name": "Silicea Belladonna",
            "company_name": "Cantrell Drug Company",
            "manufacturing_date": "2021-07-18",
            "expiration_date": "2024-10-05",
            "serial_number": "FR57 7414 7254 046O IHVX AV6L H71",
            "storage_instructions": "instrucao 6",
        },
        {
            "id": "7",
            "product_name": "Spironolactone",
            "company_name": "REMEDYREPACK",
            "manufacturing_date": "2021-07-17",
            "expiration_date": "2023-11-18",
            "serial_number": "SM28 B981 5118 903W JY0C 5KVO 3QD",
            "storage_instructions": "instrucao 7",
        },
        {
            "id": "8",
            "product_name": "Aspirin",
            "company_name": "Galena Biopharma",
            "manufacturing_date": "2021-02-22",
            "expiration_date": "2024-03-14",
            "serial_number": "KZ63 800H NM4B ZOWB YYUI",
            "storage_instructions": "instrucao 8",
        },
        {
            "id": "9",
            "product_name": "eucalyptus globulus",
            "company_name": "Target Corporation",
            "manufacturing_date": "2020-09-06",
            "expiration_date": "2024-05-21",
            "serial_number": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
            "storage_instructions": "instrucao 9",
        },
        {
            "id": "10",
            "product_name": "Titanium Dioxide",
            "company_name": "Target Corporation",
            "expiration_date": "2023-12-08",
            "serial_number": "FR29 5791 5333 58XR G4PR IG28 D08",
            "manufacturing_date": "2020-12-08",
            "storage_instructions": "instrucao 10",
        },
    ]
]


@pytest.mark.dependency
def test_importer_is_abstract() -> None:
    assert issubclass(Importer, ABC)


@pytest.mark.dependency
def test_importer_init_is_not_abstract() -> None:
    with pytest.raises(
        AttributeError,
        match="'function' object has no attribute '__isabstractmethod__'",
    ):
        Importer.__init__.__isabstractmethod__  # type:ignore


@pytest.mark.dependency
def test_importer_init_receive_self_and_path() -> None:
    importer_init_params = Importer.__init__.__code__.co_varnames
    assert "self" in importer_init_params
    assert "path" in importer_init_params
    assert len(importer_init_params) == 2


@pytest.mark.dependency
def test_importer_init_path_is_str() -> None:
    assert Importer.__init__.__annotations__["path"] == str


@pytest.mark.dependency
def test_importer_import_data_is_abstractmethod() -> None:
    assert Importer.import_data.__isabstractmethod__  # type:ignore


@pytest.mark.dependency
def test_importer_import_data_receive_self() -> None:
    importer_import_data_params = Importer.import_data.__code__.co_varnames
    assert "self" in importer_import_data_params
    assert len(importer_import_data_params) == 1


@pytest.mark.dependency
def test_importer_import_data_return_list_of_products() -> None:
    assert (
        str(Importer.import_data.__annotations__["return"])
        .lower()
        .replace("typing.", "")
        == "list[inventory_report.product.product]"
    )


# Teste do requisito 3
@pytest.mark.dependency(
    depends=[
        "test_importer_is_abstract",
        "test_importer_init_is_not_abstract",
        "test_importer_init_receive_self_and_path",
        "test_importer_init_path_is_str",
        "test_importer_import_data_is_abstractmethod",
        "test_importer_import_data_receive_self",
        "test_importer_import_data_return_list_of_products",
    ]
)
def test_importer_final() -> None:
    pass


@pytest.mark.dependency
def test_json_importer_extends_importer() -> None:
    assert issubclass(JsonImporter, Importer)


# Teste do requisito 4
@pytest.mark.dependency(depends=["test_json_importer_extends_importer"])
def test_validate_json_importer() -> None:
    report = JsonImporter("tests/mocks/inventory.json").import_data()
    assert report == PRODUCTS


@pytest.mark.dependency
def test_csv_importer_extends_importer() -> None:
    assert issubclass(CsvImporter, Importer)


# Teste do requisito 8
@pytest.mark.dependency(depends=["test_csv_importer_extends_importer"])
def test_validate_csv_importer() -> None:
    report = CsvImporter("tests/mocks/inventory.csv").import_data()
    assert report == PRODUCTS
