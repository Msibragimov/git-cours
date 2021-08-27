class Discount:

    def __init__(self, percent: float, visits: int) -> None:
        self._percent = percent
        self._visits = visits

    @property
    def percent(self):
        return self._percent

    @property
    def visits(self):
        return self._visits