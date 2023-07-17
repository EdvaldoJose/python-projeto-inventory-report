import csv
import json
from abc import ABC, abstractmethod
from typing import Dict, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        product_list = []

        try:
            with open(self.path) as file:
                data_products = json.load(file)
            for product in data_products:
                products = Product(
                    product["id"],
                    product["product_name"],
                    product["company_name"],
                    product["manufacturing_date"],
                    product["expiration_date"],
                    product["serial_number"],
                    product["storage_instructions"],
                )
                product_list.append(products)
            return product_list

        except FileNotFoundError:
            raise FileNotFoundError(
                f"missing file: {self.path}"
                )


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        products = []

        try:
            with open(self.path, encoding="utf-8") as file:
                data_products = csv.reader(file, delimiter=",")
                header, *data = data_products
            for line in data:
                new_product = Product(
                    line[0],
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                    line[5],
                    line[6],
                )
                products.append(new_product)

            return products
        except FileNotFoundError:
            raise FileNotFoundError(f"missing file: {self.path}")


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
