class MyClass:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # setter to set the value
    def set_description(self, new_description):
        self.description = new_description

    # getter to get the current property value
    def get_description(self):
        return self.description

    # what is instance
    def what_is_instance(self):
        result_str = f"This instance is a {self.name}"
        return result_str

my_class_ref = MyClass("Andrew", "me")
my_class_ref2 = MyClass("Ben", "a ben")
print(f"My name is {my_class_ref.name} and I'm {my_class_ref.description}!!")
my_class_ref.set_description("your dad")
print(f"My name is {my_class_ref2.name} and I'm {my_class_ref2.get_description()}!!")
print(my_class_ref.what_is_instance())
