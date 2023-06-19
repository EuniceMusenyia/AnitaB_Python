# class Student :
#     # name = "Eunice"
#     # age = 22
#     # school = "AkiraChix"
#     # nationality = "Kenyan"

#     # school = "AkiraChix"
#     # def __init__(self, name, age, nationality):
#     #     self.name = name
#     #     self.age = age
#     #     self.nationality = nationality

#     school = "AkiraChix"
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality

#     def greet_student(self):
#         return (f"Hello {self.name} welcome to {self.school}")
    
#     def year_of_birth(self):
#         year = 2023- self.age
#         return f"Hello {self.name}, you were born in {year}"
    
    # Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials
class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def show_full_name(self):
        return (f"My name is{self.first_name} {self.last_name}")
    
    def year_of_birth(self,year):
       birth_year = year - self.age
       return birth_year
    
    def initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"
    



    
