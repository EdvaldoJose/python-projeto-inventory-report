from inventory_report.product import Product


def test_product_report() -> None:
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

    expected = (
        f"The product {id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        f"must be stored according to the following instructions: "
        f"{storage_instructions}."
    )

    assert str(product) == expected
