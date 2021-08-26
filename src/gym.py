import csv
from typing import List

from .person import Customer, Employee


class Gym:
    DEFAULT_VISIT_PRICE = 3.9

    def __init__(self, address, name) -> None:
        self._address = address
        self._name = name
        self._employees: List[Employee] = []
        self._customers: List[Customer] = []
    
    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def add_customer(self, customer: Customer):
        self._customers.append(customer)

    def export_employees_info(self, file_path):
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['full_name', 'age', 'gender', 'position']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for employee in self._employees:
                writer.writerow({
                    'full_name': employee.full_name,
                    'age': employee.age,
                    'gender': employee.gender.value,
                    'position': employee.position.value
                })

    def export_customers_info(self, file_path):
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['full_name', 'age', 'gender',\
                'remaining_visits', 'total_visits']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for customer in self._customers:
                writer.writerow({
                    'full_name': customer.full_name,
                    'age': customer.age,
                    'gender': customer.gender.value,
                    'remaining_visits': int(customer._remaining_visits),
                    'total_visits': int(customer._total_visits)
                })