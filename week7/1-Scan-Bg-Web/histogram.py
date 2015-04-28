class Histogram:

    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        dictionary_presentation = ""

        for key, count in self.dictionary.items():
            dictionary_presentation += "{}: {} \n".format(key, count)
        dictionary_presentation.strip("\n")

        return dictionary_presentation

    def add(self, element):
        if element not in self.dictionary:
            self.dictionary[element] = 1
        elif element in self.dictionary:
            self.dictionary[element] += 1

    def count(self, element):
        if element in self.dictionary:
            return self.dictionary[element]
        elif element not in self.dictionary:
            return None

    def get_dictionary(self):
        return self.dictionary
