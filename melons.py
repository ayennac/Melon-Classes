"""Classes for melon orders."""

import random
from datetime import datetime


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 0
        self.order_time = datetime.today()

    def get_base_price(self):
        self.base_price = random.randint(5, 9)

        if self.order_time.weekday() in [0, 1, 2, 3, 4] and self.order_time.hour in [8, 9, 10]:
            self.base_price += 4

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas":
            self.base_price *= 1.5

        total = (1 + self.tax) * self.qty * self.base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """A domestic melon order"""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, country_code):
        """An international (non-US) melon order."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """A government melon order"""

        super().__init__(species, qty)
        self.order_type = "government"
        self.passed_inspection = False
        self.tax = 0

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
