from abc import abstractmethod, ABC

class Person(ABC):
    def __init__(self,name,yob):
        self._name=name
        self._yob = yob
    def getYoB(self):
        return self._yob
    @abstractmethod
    def describe(self):
        return f"Student - Name : {self._name} - YoB: {self._yob}"
    
class Student(Person):
    def __init__(self,name,yob,grade):
        super().__init__(name,yob)
        self.__grade=grade

    def describe(self):
        print( f"Student - Name : {self._name} - YoB: {self._yob} - Grade: {self.__grade}")
class Teacher(Person):
    def __init__(self,name,yob,subject):
        super().__init__(name,yob)
        self.__subject=subject

    def describe(self):
        print(  f"Student - Name : {self._name} - YoB: {self._yob} - Subject: {self.__subject}")

class Doctor(Person):
    def __init__(self,name,yob,specialist):
        super().__init__(name,yob)
        self.__specialist=specialist

    def describe(self):
        print( f"Student - Name : {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")

class Ward:
    def __init__(self,name:str):
        self.__name=name
        self.__list_people=[]
    
    def add_person(self,person:Person):
        self.__list_people.append(person)
    
    def describe(self):
        print(f'Ward Name: {self.__name}')
        for i in self.__list_people:
            i.describe()
    
    def count_doctor(self):
        count=0
        for i in self.__list_people:
            if isinstance(i,Doctor):
                count +=1
        return count         
    def sort_age(self):
        self.__list_people.sort(key=lambda x: x.getYoB(),reverse=True)
    def compute_average(self):
        for i in self.__list_people:
            total_yob=0
            count_teacher=0
            if isinstance(i,Teacher)==True:
                total_yob+=i.getYob()
                count_teacher+=1
        return total_yob/count_teacher

        #test
teacher2 = Teacher( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward( name =" Ward1")
ward1.add_person( doctor2 )
ward1.add_person( teacher2 )
ward1.describe()
ward1.sort_age()
ward1.describe()
