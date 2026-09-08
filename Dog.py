class Dog:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof! Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! {self.name} is now {self.age} years old.")

    def get_info(self) -> str:
        return f"Dog Name: {self.name}, Age: {self.age}"


if __name__ == "__main__":
    my_dog = Dog("Max", 5)
    my_dog.bark()
    my_dog.celebrate_birthday()
    print(my_dog.get_info())
