import sys
import re


class WordFrequencies:
    def __init__(self, file_name):
        self.file_name = file_name #name of file
        self.word_list = [] #list to hold all words in the file split
        self.str = "" #string that data is read into
        self.D = {} #dictionary to hold (key: value) pairs of (word: count)

    def print_name_of_file(self):
        ## Prints name of the file
        print("File name: ")
        print(self.file_name)

    def read_file_into_string(self):
        ## Opens file and reads into a string. It then strips the string of everything except
        ## alphanumeric characters (A_-Z,a-z, 0-9)
        with open(self.file_name, 'r') as myFile:
            data = myFile.read()
        self.str = re.sub('[^A-Za-z0-9 ]+', ' ', data)



    def split_string_into_word_list(self):
        ## Splits string into a list of words
        self.word_list = self.str.lower().split()


    def put_words_into_dictionary(self):
        ## Puts the words from the list into a dictionary based on count of words
        for index in range(len(self.word_list)):
            if self.word_list[index] in self.D.keys():
                self.D[self.word_list[index]] += 1
            else:
                self.D[self.word_list[index]] = 1


    def print_result(self):
        ## Sorts dictionary and prints out key, value (word, count) pairs
        print("-------- RESULT --------")
        self.D = sorted(self.D.items(), key=lambda t: (-t[1], t[0]))
        for key, value in self.D:
            print("{} - {}".format(key, value))
        print("\n")







if __name__ == "__main__":
    test = WordFrequencies(sys.argv[1])
    test.read_file_into_string()
    test.split_string_into_word_list()
    test.put_words_into_dictionary()
    test.print_result()


