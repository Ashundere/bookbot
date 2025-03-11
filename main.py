import sys
from stats import (
	get_word_count,
	get_char_count,
	get_book_text,
	char_sorted_list
)


def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path = sys.argv[1]
	text = get_book_text(path)
	num_words = get_word_count(text)
	char_count = get_char_count(text)
	chars_sorted_list = char_sorted_list(char_count)
	print_report(path, num_words, chars_sorted_list)


def print_report(path, num_words, chars_sorted_list):
	print("========== BOOKBOT ==========")
	print(f"Analyzing book found at {path}...")
	print("---------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("---------- Character Count ---------")
	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print("========== END ==========")

main()
