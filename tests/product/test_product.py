from inventory_report.product import Product


def test_create_product() -> None:
    id = "10"
    product_name = "Titanium Dioxide"
    company_name = "Target Corporation"
    manufacturing_date = "2020-12-08"
    expiration_date = "2023-12-08"
    serial_number = "FR29 5791 5333 58XR G4PR IG28 D08"
    storage_instructions = "instrucao 10"

    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )

    assert product.id == id
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions
