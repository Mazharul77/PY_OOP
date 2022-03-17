# Checking Object's classes,Built_in class_Functions ( isinstance(), issubclass() ), and on.....
# [ Note: no Access Modifier in Python like Java/others oop(default, public, private, protected)
# but intelligently can be handled ]
# Python Supports Multiple Inheritances

class Project:
    p_name = "ERP_Solutions"
    pr_desc = "Welcome To New Ai Automation World With Our ERP_Solution!"
    pass


class Software(Project):
    pass


class Module(Software):
    pass


my_project = Project()
ai_hrm = Software()
my_module = Module()

print("The Launched Project:", my_project.p_name)
print(my_module.pr_desc)

# Now Check Individual Object representing class: It utilizes for big project fast handling
print("The Class of Object-my_module is: ", my_module.__class__)
print("The Class of Object-my_project is: ", my_project.__class__)
print("The Class of Object-ai_hrm is: ", ai_hrm.__class__)

"""
    Testing whether which object/instance is belongs which class. returns True or False: isinstance()
    Testing whether A class is Subclass of another(parent) class: issubclass()
"""
print("\n\t Is my_project-object is Instance of Project-class? :", isinstance(my_project, Project))  # True
print("\t Is my_project-object is Instance of Software-class? :", isinstance(my_project, Software))  # False

print("\n\t Is my_project-object is Instance of Module-class? :", isinstance(my_project, Module))  # False

print("\n\t Is my_module-object is Instance of Project-class? :", isinstance(my_module, Project))  # True
print("\t Is my_module-object is Instance of Software-class? :", isinstance(my_module, Software))  # True (Inherited)
print("\t Is my_module-object is Instance of my_project-class? :", isinstance(my_module, Project))  # True (Inherited)

# Testing whether A class is Subclass of another(parent) class: issubclass()
print("\n\t Is Software-class is subclass of Project-class? :", issubclass(Software, Project))  # True (inherited subclass)
print("\t Is Software-class is subclass of Software-class? :", issubclass(Software, Software))  # True (sub of own)
print("\t Is Software-class is subclass of Module-class? :", issubclass(Software, Module))  # False


