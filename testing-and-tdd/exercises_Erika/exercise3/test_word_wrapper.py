import pytest


from word_wrapper import wrap_words

# test that the output is list

# If the row-length is 60, and the input string is 30, the result is just the input string
def test_input_string_shorter_than_length():
test_string = "Hello World!"
test_row_length = 20
assert len(wrap_words(test_string,test_row_length)) == 1
assert wrap_words(test_string,test_row_length)[0] == test_string


# If the row-length is 3, and the input string is "abc def" the result is ["abc", "def"]
# If the row-length is 3, and the input string is "abcdef" the result is ["abc", "def"]
# If the row-length is 3, and the input string is "abcdef abc" the result is ["abc", "def", "abc"]
# With row length 3 and "a b c d e f" the result is ["a b", "c d", "e f"] 
