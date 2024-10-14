# creating a class
# syntax
class className:
    code goes here 
    # example:
    pass 
print(person)
<_ _main_ _.person object at 0x10804e510>

# creating an object
p= person()
print(p)

# class Constructor

class person: 
    def __init__(self,firstname , lastname age, country , city
        self.firstname=firstname
        self.lastname=lastname):
        self.name=name
        self.age=age
        self.country=country
        self.city=city

        p= person('Abdulkadir ', 'Mohamud' , 'The Netherlands', 'The Hague')

        # output
        Abdulkadir 
        Mohamud
        230
        The Netherlands 
        The Hague
        
        # object methods
        class person: 
            def __init__(self,firstname , lastname age, country , city
                self.firstname=firstname
                self.lastname=lastname):
                self.name=name
                self.age=age
                self.country=country
                self.city=city
                def person_info(self):
                    return f'{self.firstname} {self.lastname} {self.age} {self.country} {self.city}'

                p= person('Abdulkadir ', 'Mohamud' , 'The Netherlands', 'The Hague')
                print(p.person_info())
                # output
                Abdulkadir Mohamud is 230 he lives in the Hague, in The Netherlands


# Object default methods

# Example:

class person:
    def __init__(self,firstname=  'Abdulkadir',  lastname = 'Mohamud', age = 230,  country = 'The Netherlands', city ='The Hague') :
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.city=city
        def person_info(self):
            return f'{self.firstname} {self.lastname} {self.age} {self.country} {self.city}'

        p1= person()
        print(p1.person_info())
        
        p2= person ('Yaasiin ',  'Ahmed', 17,'' Mogadishu',' Somalia')
        print(p2.person_info())

        # Methods to Modify Class Default Values

        class person:
            def __init__(self,firstname=  'Abdulkadir',  lastname = 'Mohamud', age = 230,  country = 'The Netherlands', city ='The Hague') :
                self.firstname=firstname
                self.lastname=lastname
                self.age=age
                self.country=country
                self.city=city
                self.skills = []
                
                def person_info(self):
                    return f'{self.firstname} {self.lastname} {self.age} {self.country} {self.city}'

                def add_skill(self,skill):
                    self.skills.append(skill)
                    return self.skills

                p1= person()
                print(p1.person_info())
                
                p2= person ('Yaasiin ',  'Ahmed', 17,'' Mogadishu',' Somalia')
                print(p2.person_info())
                # output
                Abdulkadir Mohamud is 230 he lives in the Hague, in The Netherlands
                Yaasiin Ahmed is 17 he lives in Mogadishu, in Somalia

                # Inheritance
                class student (person):
                    pass

                s1= student(Eyup, Yaasiin, 17, Mogadishu, Somalia)
                s2= studeny ('Selin 21 ,  lives in The Hague, The Netherlands')
                print(s1.person_info())
                s1.add_skill(Python, React , C++ , Java)
                s1.add_skill(HTML , CSS , Javascript)
                print(s1.skills)

                print (s2.person_info())
                s2.add_skill(Python, AWS Software Engineer , C++ , Java)
                s2.add_skill(HTML , CSS , Javascript)
                print(s2.skills)
                # output

                # Overriding parent Method

                class student (person):
                    def person_info(self):
                    self.gender = gender
                    super().__init __(firstname, lastname, age, country, city)
                    def person_info(self):
                    gender = 'He' if self.gender == 'M' else 'She'
                    return f'{gender} {self.firstname} {self.lastname} is {self.age} he lives in {self.city}, in {self.country}'

                s1= student(Eyup, Yaasiin, 17, Mogadishu, Somalia)
                s2= studeny ('Selin 21 ,  lives in The Hague, The Netherlands')
                print(s1.person_info())
                s1.add_skill(Python, React , C++ , Java)
                s1.add_skill(HTML , CSS , Javascript)
                print(s1.skills)

                print (s2.person_info())
                s2.add_skill(Python, AWS Software Engineer , C++ , Java)
                s2.add_skill(HTML , CSS , Javascript)
                print(s2.skills)

                # output
                



                    
        


    
    