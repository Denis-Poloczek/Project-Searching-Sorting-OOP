class Manager:

    def __init__(self):
        self.methods = {}
        self.methods_details = {}

    def get_available_methods(self):
        print("The following methods are available: ")
        for method in self.methods:
            print(method)

    def get_methods_details(self, method_name):
        if method_name not in self.methods_details.keys():
            return print("This method name is not supported, please try again!")
        print(f"The {method_name} has the {self.methods_details[method_name]}")
