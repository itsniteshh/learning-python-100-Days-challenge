from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

is_active = True
while is_active:
    options = menu.get_items()
