import itertools
import shutil
from datetime import datetime, timedelta
from typing import List

import factory
import pytest
from faker import Faker

from inventory_report.inventory import Inventory
from inventory_report.product import Product

factory.Faker._DEFAULT_LOCALE = "pt_BR"


class ProductFactory(factory.Factory):  # type: ignore
    class Meta:
        model = Product

    id = str(factory.Sequence(int))
    product_name = factory.Faker("word")
    company_name = factory.Faker("company")
    manufacturing_date = factory.Faker("past_date", locale="en.US")
    expiration_date = factory.Faker("future_date", locale="en.US")
    serial_number = str(factory.Sequence(int))
    storage_instructions = factory.Faker("paragraph")


faker = Faker("pt-BR")

OLD_DATE = faker.past_date()
FUTURE_DATE = faker.future_date() + timedelta(days=20)

OLDEST_DATE = OLD_DATE - timedelta(days=30)
CLOSEST_DATE = datetime.today().date() + timedelta(days=10)
COMPANY_WITH_THE_LARGEST_INVENTORY = faker.company()


@pytest.fixture
def products() -> List[Product]:
    return [
        ProductFactory(  # Antigo 2
            company_name=COMPANY_WITH_THE_LARGEST_INVENTORY[
                : len(COMPANY_WITH_THE_LARGEST_INVENTORY) // 2
            ],
            manufacturing_date=str(OLD_DATE),
            expiration_date=str(FUTURE_DATE),
        ),
        ProductFactory(  # Antigo 0
            company_name=COMPANY_WITH_THE_LARGEST_INVENTORY,
            manufacturing_date=str(OLD_DATE),
            expiration_date=str(FUTURE_DATE),
        ),
        ProductFactory(  # Antigo 1
            company_name=COMPANY_WITH_THE_LARGEST_INVENTORY,
            manufacturing_date=str(OLD_DATE),
            expiration_date=str(OLD_DATE),
        ),
        ProductFactory(  # Antigo 3
            company_name=COMPANY_WITH_THE_LARGEST_INVENTORY + " LIMITED",
            manufacturing_date=str(OLDEST_DATE),
            expiration_date=str(CLOSEST_DATE),
        ),
    ]


@pytest.fixture
def inventories(products: List[Product]) -> List[Inventory]:
    return [
        Inventory(list(product))
        for product in itertools.permutations(products)
    ]


def remove_mypy_cache() -> None:
    try:
        shutil.rmtree(".mypy_cache")
    except (FileNotFoundError, OSError):
        pass
