# Python3.7.3
# Abstract Factory example. A big thank you to https://refactoring.guru.com

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    An abstract factory interface declares a set of methods that return
    different abstract products. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another."""

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the concrete factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """Each concrete factory has a corresponding product variant."""

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """Each distinct product of a product family should have a base interface.
    All variants of the product must implement this interface."""

    @abstractmethod
    def useful_function_a(self) -> str:
        pass
    

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """The base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products
    of the same concrete variant."""
    
    @abstractmethod
    def useful_function_b(self) -> None:
        """Product B is able to do its own thing..."""
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """It can also collaborate with ProductA.
        The Abstract Factory makes sure all products it creates are of the
        same variant and compatible."""
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of thr product B1."

    """The variant, Product B1, is only able to work correctly with Product A1.
    And it accepts any instance of AbstractProductA as an argument."""

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaboration with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
