

def  get_book_text(path):
        with open(path) as f:
                file_contents = f.read()
        return file_contents



def get_word_count(text):
        words = text.split()
        num_words = 0
        for word in words:
                num_words += 1
        return num_words

def get_char_count(text):
	words = text.split()
	charDict = {}
	for word in words:
		lowercase = word.lower()
		wordList = list(lowercase)
		for char in wordList:
			if char not in charDict:
				charDict[char] = 1
			else:
				count = (charDict[char]) + 1
				charDict[char] = count
	return charDict

def sort_on(dict):
	return dict["num"]

def char_sorted_list(char_dict):
	sorted_list = []
	for char in char_dict:
		sorted_list.append({"char": char, "num": char_dict[char]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
