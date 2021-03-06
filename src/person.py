from enum import Enum
from src.discount import Discount
from typing import List


class Person:
    class Gender(Enum):
        MALE = 'male'
        FEMALE = 'female'

    def __init__(self, full_name, age, gender: Gender) -> None:
        self._full_name = full_name
        self._age = age
        self._gender = gender

    @property
    def full_name(self):
        return self._full_name
    
    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender


class Employee(Person):
    class Position(Enum):
        ADMINISTRATOR = 'administrator'
        INSTRUCTOR = 'instructor'
        LAWYER = 'lawyer'
        ACCOUNTANT = 'accountant'

    def __init__(self,
        full_name,
        age,
        gender: Person.Gender,
        position: Position
    ) -> None:
        super().__init__(full_name, age, gender)
        self._position = position

    @property
    def position(self):
        return self._position


class Customer(Person):

    def __init__(self, full_name, age, gender) -> None:
        super().__init__(full_name, age, gender)
        self._remaining_visits = 0
        self._total_visits = 0
        self._is_active = True

    def add_visits(self, amount, discounts: List[Discount]=[]):
        from .gym import Gym
        visits = amount//Gym.DEFAULT_VISIT_PRICE
        if not visits:
            print('Not enough money to buy visits')
            return amount

        max_persent_discount = None
        for discount in discounts:
            if discount.visits <= visits:
                if max_persent_discount:
                    if max_persent_discount.percent < discount.percent:
                        max_persent_discount = discount
                    else:
                        max_persent_discount = discount
        
        self._remaining_visits += visits
        
        if max_persent_discount:
            return amount%Gym.DEFAULT_VISIT_PRICE + visits*Gym.DEFAULT_VISIT_PRICE*max_persent_discount.percent/100
        return amount%Gym.DEFAULT_VISIT_PRICE

    def visit_gym(self):
        if not self._is_active:
            raise Exception('Block')
        if self._remaining_visits == 0:
            raise Exception('No remaining visits')
        self._remaining_visits -= 1
        self._total_visits += 1
        if self._total_visits%5 == 0:
            self._remaining_visits += 1

    @property
    def is_active(self):
        return self._is_active

    def block(self):
        self._is_active = False

    def unlock(self):
        self._is_active = True
        