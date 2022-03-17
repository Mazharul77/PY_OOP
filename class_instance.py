print("=== Class instance, instantiation, Object & inheritance implementation with Python ===\n")


class ItIndustry:
    emp_name = "Bhuiyan"
    designation = "Software-Engineer"

    def __init__(self):
        self.hours = 7
        self.minute = self.hours * 60
        self.office_hours = 8
        self.service_perform_rate = (self.minute / (self.office_hours * 60)) * 100

    def emp_activity(self):
        print("Performance Rate of", it_object.emp_name, "is:", self.service_perform_rate, "%")
        return self.service_perform_rate


# Inherited class to new class(below):
class University(ItIndustry):
    uni_name = " "
    uni_location = "Oxford"

    def __init__(self, v_name):
        super().__init__()
        self.varsity_name = v_name

    def tech_tutoring(self):
        print("Welcome to", self.varsity_name)


# Another Test-Class
class TestClass:
    pass


institution = input("Enter University Name Please:")
it_object = ItIndustry()
uni_object = University(institution)
print("The Employee Name: ", it_object.emp_name)
print("Employee's Designation:", it_object.designation)
print(it_object.emp_activity())

print("\n\t", uni_object.tech_tutoring())
print("\n\t The University Name Was:", uni_object.uni_location)
print("\n\t University Class Hours:", uni_object.hours)
print("\n\t The Performance Rate Of Students: %.2f" % (uni_object.emp_activity()*.70), "%")

print("\n\t========== Py-OOP Class Concept is Partially Ended =============")