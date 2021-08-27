import os
from src.discount import Discount

from src.gym import Gym
from src.person import Customer, Employee, Person


if __name__ == '__main__':
    gym = Gym(address='Tashkent, Shota Rustavelli, 91', name='Super Sport')
    gym.add_employee(Employee(
        full_name='John Doe',
        age=25,
        gender=Person.Gender.MALE,
        position=Employee.Position.ADMINISTRATOR
    ))
    gym.add_employee(Employee(
        full_name='Alice Cooper',
        age=28,
        gender=Person.Gender.FEMALE,
        position=Employee.Position.INSTRUCTOR
    ))
    gym.add_employee(Employee(
        full_name='Rick Sanchez',
        age=45,
        gender=Person.Gender.MALE,
        position=Employee.Position.INSTRUCTOR
    ))
    gym.add_employee(Employee(
        full_name='Abdulla Abdullaev',
        age=35,
        gender=Person.Gender.MALE,
        position=Employee.Position.LAWYER
    ))
    gym.add_employee(Employee(
        full_name="Ra'no Abdullaeva",
        age=35,
        gender=Person.Gender.FEMALE,
        position=Employee.Position.ACCOUNTANT
    ))

    staff_file_path = os.path.join(os.path.dirname(__file__), 'data/staff.csv')
    gym.export_employees_info(staff_file_path)

    customer = Customer(
        full_name='Jerry Smith',
        age=30,
        gender=Person.Gender.MALE
    )
    gym.add_customer(customer)
    customer.add_visits(1, gym.discounts)
    print(customer.add_visits(100, gym.discounts))

    customer = Customer(
        full_name='Beth Smith',
        age=30,
        gender=Person.Gender.FEMALE
    )
    gym.add_customer(customer)
    customer.add_visits(5, gym.discounts)
    customer.visit_gym()

    try:
        customer.visit_gym()
    except Exception as e:
        print(e)

    customers_file_path = os.path.join(os.path.dirname(__file__), 'data/customers.csv')
    gym.export_customers_info(customers_file_path)

    gym.add_discount(Discount(10, 10))
    gym.add_discount(Discount(20, 50))
    gym.add_discount(Discount(40, 100))
    customer = Customer(
        full_name='Summer Smith',
        age=19,
        gender=Person.Gender.FEMALE
    )
    gym.add_customer(customer)
    change = customer.add_visits(55*gym.DEFAULT_VISIT_PRICE, discounts=gym.discounts)
    print(change)
    for _ in range(5):
        customer.visit_gym()
    print(customer._remaining_visits)
    customer.block()
    try:
        customer.visit_gym()
    except Exception as e:
        print(e)
    customer.unlock()
    customer.visit_gym()
    print(customer._remaining_visits)

    print()
    for customer in gym._customers:
        print(customer.full_name, customer._remaining_visits)
    winner = gym.paly_out_visits()
    print(winner.full_name, winner._remaining_visits)