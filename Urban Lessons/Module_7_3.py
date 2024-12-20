# Найдете везде
import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as f:
                    all_words[file_name] = re.sub("[,.=!?;:-]", "", (f.read().lower())).split()
        return all_words

    def find(self, word):
        dict_result = {}
        for file_mame, words in self.get_all_words().items():
            if word.lower() in words:
                dict_result[file_mame] = words.index(word.lower()) #+ 1
        return dict_result

    def count(self, word):
        dict_result = {}
        for file_mame, words in self.get_all_words().items():
            dict_result[file_mame] = words.count(word.lower())
        return dict_result

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

#END