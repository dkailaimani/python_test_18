# Problem Statement: You are required to build a Personal Budget Management
# application. The application will manage budget categories like food, 
# entertainment, utilities, etc., ensuring that budget details remain private 
# and are accessed or modified through public methods.

# Task 1: Define Budget Category Class

# Create a class BudgetCategory with private attributes for category name and allocated budget.
# Initialize these attributes in the constructor.
# Expected Outcome: A BudgetCategory class capable of storing category details securely.

print("{:>85}".format("*********BUDGET CATEGORY*********"))
class BudgetCategory:
    def __init__(self, categoryName, allocatedBudget):
        self.__categoryName = categoryName
        self.__allocatedBudget = allocatedBudget

    def getCategoryName(self):
        return self.__categoryName

    def getAllocatedBudget(self):
        return self.__allocatedBudget

    def setAllocatedBudget(self, allocatedBudget):
        self.__allocatedBudget = allocatedBudget


category1 = BudgetCategory("ENTERTAINMENT", 250)
print("CATEGORY:", category1.getCategoryName())
print("BUDGET:", category1.getAllocatedBudget())

category1.setAllocatedBudget(475)
print("BUDGET UPDATE:", category1.getAllocatedBudget())


# Task 2: Implement Getters and Setters

# Write getter and setter methods for both the category name and the allocated budget.
# Ensure that the setter methods include validation 
# (e.g., budget should be a positive number).
# Expected Outcome: Methods that allow controlled access 
# and modification of the private attributes, with validation checks in place.

print("{:>92}".format("*********BUDGET CATEGORY WITH VALIDATION*********"))

class BudgetCategory:
    def __init__(self, categoryName, allocatedBudget):
        self.__categoryName = categoryName
        self.__allocatedBudget = allocatedBudget

    def getCategoryName(self):
        return self.__categoryName

    def getAllocatedBudget(self):
        return self.__allocatedBudget

    def setAllocatedBudget(self, allocatedBudget):
        if allocatedBudget > 0:
            self.__allocatedBudget = allocatedBudget
        else:
            print("ERROR: BUDGET MUST BE POSITIVE!")


category1 = BudgetCategory("ENTERTAINMENT", 250)
print("CATEGORY:", category1.getCategoryName())
print("BUDGET:", category1.getAllocatedBudget())

category1.setAllocatedBudget(475)
print("BUDGET UPDATE:", category1.getAllocatedBudget())

category1.setAllocatedBudget(-550)

# Task 3: Add Budget Functionality

# Implement a method to add expenses to a category and adjust the budget accordingly.
# Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

print("{:>100}".format("*********BUDGET CATEGORY WITH EXPENSES AND VALIDATION*********"))

class BudgetCategory:
    def __init__(self, categoryName, allocatedBudget):
        self.__categoryName = categoryName
        self.__allocatedBudget = allocatedBudget
        self.__expenses = 0  # Initialize expenses to 0

    def getCategoryName(self):
        return self.__categoryName

    def getAllocatedBudget(self):
        return self.__allocatedBudget

    def getExpenses(self):
        return self.__expenses

    def setAllocatedBudget(self, allocatedBudget):
        if allocatedBudget > 0:
            self.__allocatedBudget = allocatedBudget
        else:
            print("ERROR: BUDGET MUST BE POSITIVE!")

    def addExpense(self, expense):
        if expense > 0:
            self.__expenses += expense
            print(f"EXPENSE ADDED AT: {expense}")
            self.__updateRemainingBudget()
        else:
            print("ERROR: EXPENSE MUST BE POSITIVE!")

    def __updateRemainingBudget(self):
        remaining_budget = self.__allocatedBudget - self.__expenses
        print("REMAINING BUDGET:", remaining_budget)

category1 = BudgetCategory("ENTERTAINMENT", 500)
print("CATEGORY:", category1.getCategoryName())
print("BUDGET:", category1.getAllocatedBudget())


category1.addExpense(60)
category1.addExpense(85)
category1.setAllocatedBudget(600)

category1.addExpense(-50)

# Problem Statement: An e-commerce platform requires a system to manage 
# different types of products, such as books, electronics, and clothing. 
# Each product type shares some common characteristics but also has unique features. 
# The system should be able to display information about each product appropriately.

# Task 1: Create Base Product Class

# Develop a base class Product with common attributes like product ID, name, 
# price, and a method to display product information.
# Expected Outcome: A Product class that can hold general information 
# about a product and display it.

print("{:>85}".format("*********ECCOMERCE PRODUCT CLASS*********"))

class Product:
    def __init__(self, productId, name, price):
        self.productId = productId
        self.name = name
        self.price = price

    def displayProductInfo(self):
        print("PRODUCT ID:", self.productId)
        print("NAME:", self.name)
        print("PRICE:", self.price)


product1 = Product("100", "LAPTOP", 2500)
product1.displayProductInfo()


# Task 2: Implement Subclasses for Specific Products

# Create subclasses Book, Electronic, and Clothing that inherit from Product.
# Each subclass should have additional attributes relevant to its category 
# (e.g., author for books, specs for electronics, size for clothing).
# Expected Outcome: Each subclass contains both inherited attributes 
# from Product and new attributes specific to the product type.

# Task 3: Override Display Method in Subclasses

# Override the method to display product information in
# each subclass to include specific attributes.
# For example, the Book class should display the author, 
# Electronic should display specs, etc.
# Expected Outcome: Calling the display method on an 
# instance of any subclass shows both common and specific product details.

class Product:
    def __init__(self, productId, name, price):
        self.productId = productId
        self.name = name
        self.price = price

    def displayProductInfo(self):
        print("ID:", self.productId)
        print("NAME:", self.name)
        print("PRICE:", self.price)

class Book(Product):
    def __init__(self, productId, name, price, author, genre):
        super().__init__(productId, name, price)
        self.author = author
        self.genre = genre

    def displayProductInfo(self):
        super().displayProductInfo()
        print("AUTHOR:", self.author)
        print("GENRE:", self.genre)


class Electronic(Product):
    def __init__(self, productId, name, price, brand, specs):
        super().__init__(productId, name, price)
        self.brand = brand
        self.specs = specs

    def displayProductInfo(self):
        super().displayProductInfo()
        print("BRAND:", self.brand)
        print("SPECS:", self.specs)


class Clothing(Product):
    def __init__(self, productId, name, price, size, color):
        super().__init__(productId, name, price)
        self.size = size
        self.color = color

    def displayProductInfo(self):
        super().displayProductInfo()
        print("SIZE:", self.size)
        print("COLOR:", self.color)


book1 = Book("T200", "HARRY POTTER", 27.99, "J.K. ROWLING", "FICTION")
book1.displayProductInfo()

electronic1 = Electronic("T220", "IPAD", 299.99, "APPLE", "13 IN. DISPLAY, 8GB RAM")
electronic1.displayProductInfo()

clothing1 = Clothing("T707", "HAT", 15.99, "XL", "BLACK")
clothing1.displayProductInfo()


# Task 4: Test Product Catalog Functionality

# Instantiate objects of each subclass and call their display 
# methods to ensure correct information is shown.
# Expected Outcome: The system should accurately display detailed 
# information for each type of product, demonstrating inheritance and method overriding.

class Product:
    def __init__(self, productId, name, price):
        self.productId = productId
        self.name = name
        self.price = price

    def displayProductInfo(self):
        print("ID:", self.productId)
        print("NAME:", self.name)
        print("PRICE:", self.price)

class Book(Product):
    def __init__(self, productId, name, price, author, genre):
        super().__init__(productId, name, price)
        self.author = author
        self.genre = genre

    def displayProductInfo(self):
        super().displayProductInfo()
        print("AUTHOR:", self.author)
        print("GENRE:", self.genre)


class Electronic(Product):
    def __init__(self, productId, name, price, brand, specs):
        super().__init__(productId, name, price)
        self.brand = brand
        self.specs = specs

    def displayProductInfo(self):
        super().displayProductInfo()
        print("BRAND:", self.brand)
        print("SPECS:", self.specs)


class Clothing(Product):
    def __init__(self, productId, name, price, size, color):
        super().__init__(productId, name, price)
        self.size = size
        self.color = color

    def displayProductInfo(self):
        super().displayProductInfo()
        print("SIZE:", self.size)
        print("COLOR:", self.color)


book1 = Book("T200", "HARRY POTTER", 27.99, "J.K. ROWLING", "FICTION")
book1.displayProductInfo()

electronic1 = Electronic("T220", "IPAD", 299.99, "APPLE", "13 IN. DISPLAY, 8GB RAM")
electronic1.displayProductInfo()

clothing1 = Clothing("T707", "HAT", 15.99, "XL", "BLACK")
clothing1.displayProductInfo()

