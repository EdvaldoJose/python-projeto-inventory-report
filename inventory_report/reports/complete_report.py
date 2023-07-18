from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        companies = ""
        for inventory in self.inventories:
            stock_company = Counter(
                product.company_name for product in inventory.data
            )
        for company, quantity in stock_company.items():
            companies += f"{company}: {quantity}\n"

        return (super().generate() + "Stocked products by company:\n" +
                companies)
