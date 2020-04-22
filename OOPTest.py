# A class is basically a custom data type #

class User:                                         # Declare a class and give it name User #
    def __init__(self, username, email_address):    # Now we have 2 parms, excluding "self" #
        self.name = username                        # We use the values passed in to set the name and email attr, account bal is 0, so no need for a third param #
        self.email = email_address                  # Attributes are characteristics that are shared by all instances of the same class type #
        self.account_balance = 0                    # Follow this pattern: self.<<attribute_name_of_your_choosing>> #
    # adding the deposit method #
    def make_deposit (self, amount):                # takes an argument that is the amount of the deposit, remember first param is always "self" #
        self.account_balance += amount              # the specific user's account increases by the amount of the value received #

# guido = User() #  # This is how to create a new instance of the class #
# monty = User() #  # This is how to create a new instance of the class #

guido = User("Guido van Rossum", "guido@python.com")  # This is how to create a new instance of the class, with params #
monty = User("Monty Python", "monty@python.com")  # This is how to create a new instance of the class, with params #

# guido.name = "Guido" #   # This is how to set certain values of a class #
# monty.name = "Monty" #   # This is how to set certain values of a class #

print(guido.name)   # This is how to access the instances' attributes #
print(monty.name)   # This is how to access the instances' attributes #

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.account_balance)
print(monty.account_balance)



# Methods are the actions that the objects can perform #