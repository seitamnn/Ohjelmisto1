#class kissa:
    #pass
#    def __init__(self, name):
#       self.name = name
#    def __repr__(self):
#        return f"Kissan nimi on {self.name}"
    #def __str__(self):
    #    return f"{self.name}"

#kissa1 = kissa("Jalmari")
#kissa2 = kissa("Sylvi")
#print(kissa1)
#print(kissa2)
#kissa2 = kissa()

#kissa1.name = "Jalmari"
#kissa2.name = "Jallu"

#print(kissa1.name) #name vaaditaan. tulostaa muistipaikan jos ei määritellä
#print(kissa2.name)

#class ostoslista:
#    def __init__(self, lista):
#        self.lista = lista
#    def __repr__(self):
#        return str(self.lista)

#lista1 = ostoslista(['laku', 'omppu', 'korppu'])

#print(lista1)

#class school:
#    def __init__(self, name):
#        self.name = name

#class student:
#    def __init__(self, name, school):
#        self.name = name
#        self.school = school

#school1 = school('Metropolia')
#school2 = school('Aalto yliopisto')

#student1 = student('Pekka', school1.name)
#student2 = student('Ursula', school2.name)
#print(f"{student1.name} is student in {student1.school}")

#print(student1)
#print(student2)


#class book:
#    def __init__(self, name, title):
#        self.name = name
#        self.title = title

#class library:
#    def __init__(self, name):
#        self.name = name
#        self.books = []

#    def add_book(self, book):
#       self.books.append(book)
#        return print(f'{book.name} added to library ')

#    def remove_book(self, book):
#        self.books.remove(book)
#        return print(f'{book.name} removed from {self.name}')

#    def display_books(self):
#        print(f'\nBooks in {self.name}: ')
#        for book in self.books:
#            print(f'{book.name}')

#book1 = book('IT', 'clown kills people')
#book2 = book('Shining', 'crazy man kills family')
#book3 = book('Pet semetary', 'dead animals kill people')
#book4 = book('Carrie', 'girl kills people in girly way')
#print(f'{book1.name}, {book1.title}')
#print(f'{book2.name}, {book2.title}')

#library1 = library('First libary')
#library2 = library('Second library')

#library1.add_book(book1)
#library1.add_book(book2)
#library1.add_book(book3)
#library1.add_book(book4)

#library2.add_book(book3)
#library2.add_book(book4)
#library1.remove_book(book1)

#library1.display_books()
#library2.display_books()


#class Student:
    #def __init__(self, name):
     #   self.name = name
    #    self.courses = []

   # def enroll(self, course):
  #      self.courses.append(course)
 #       course.students.append(self)


#class Course:
#    def __init__(self, name):
#        self.name = name
#        self.students = []


#student1 = Student('Pekka')
#course1 = Course('How to choose a cat')
#course2 = Course('Does my cat love me?')
#student1.enroll(course1.name)
#student1.enroll(course2.name)
#print(f'{student1.name} is on  courses: {student1.courses}')
#print(f'{course1}')

#class Koira:
#    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
#        self.nimi = nimi
 #       self.syntymävuosi = syntymävuosi
  #      self.haukahdus = haukahdus

   # def hauku(self, kerrat):
    #    for i in range(kerrat):
     #       print(self.nimi + " haukkuu: " + self.haukahdus)
      #  return

#class Hoitola:
 #   def __init__(self):
  #      self.koirat = []

   # def koira_sisään(self, koira):
    #    self.koirat.append(koira)
     #   print(koira.nimi + " kirjattu sisään")
      #  return

    #def koira_ulos(self, koira):
     #   self.koirat.remove(koira)
      #  print(koira.nimi + " kirjattu ulos")
       # return

    #def tervehdi_koiria(self):
     #   for koira in self.koirat:
      #      koira.hauku(1)

# Pääohjelma

#koira1 =Koira('Kille', 1999, 'miu miu')
#koira2 = Koira('Julle', 2022, 'muu muu')
#koira1.hauku(5)

#hoitola = Hoitola()

#hoitola.koira_sisään(koira1)
#hoitola.koira_sisään(koira2)
#hoitola.tervehdi_koiria()

#hoitola.koira_ulos(koira1)
#hoitola.tervehdi_koiria()

#class Animal:
 #   def __init__(self, species):
  #      self.species = species

#class Cat:
 #   def __init__(self, species, breed):
  #      self.breed = breed
   #     super().__init__(species)

#animal1 = Animal('cat')
#animal2 = Animal('dog')

#cat1 = Cat('cat', 'orange')
#print(f'Cat 1: {cat1.species}, {cat1.breed}')

#class Henkilö:
 #   def __init__(self, name, age):
  #      self.name = name
   #     self.age = age

    #def tervehdys(self):
     #   print(f'Terve! Nimeni on {self.name} ja olen {self.age} v vanha')

#class Opiskelija(Henkilö):
  #  def __init__(self, name, age, opnro):
   #     self.opnro = opnro
    #    super().__init__(name, age)

    #def tervehdys(self):
     #   super().tervehdys()
      #  print(f'Mun opiskelijanumeroni on {self.opnro}')

#hlö1 = Henkilö('Pirjo', 70)
#hlö1.tervehdys()
#oppilas1 = Opiskelija(hlö1.name, hlö1.age, 1312)
#oppilas2 = Opiskelija('Pekka', 22, 666)

#oppilas2.tervehdys()

class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in työntekijät:
    t.tulosta_tiedot()
