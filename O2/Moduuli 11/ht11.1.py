class Publication:
    def __init__(self, input_name):
        self.name = input_name


class Book(Publication):
    def __init__(self, input_name,  input_author, input_pages):
        super().__init__(input_name)
        self.author = input_author
        self.pages = input_pages

    def print(self):
        print(f'Kirjan nimi: {self.name}\nKirjoittaja: {self.author}\nSivumäärä: {self.pages}\n')


class Comic(Publication):
    def __init__(self, input_name, input_publisher):
        super().__init__(input_name)
        self.publisher = input_publisher

    def print(self):
        print(f'Lehden nimi: {self.name}\nPäätoimittaja: {self.publisher}\n')


aku_ankka = Comic("Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)
aku_ankka.print()
hytti_nro_6.print()
