# Testing and TDD - exercise 3 - Word-wrapping
([from the TDD Community of Practice - TDD Problems](https://sites.google.com/site/tddproblems/all-problems-1/word-wrapping))

You work with a word editor and there is need for a function which wraps lines which does not fit horizontally 
into several shorter lines.

## Inputs
1. A string to be wrapped
2. A row length, specifying how many characters on row can take

## Output
A list of word-wrapped rows (strings)

## Examples of behaviour

* If the row-length is 60, and the input string is 30, the result is just the input string
* If the row-length is 3, and the input string is "abc def" the result is ["abc", "def"]
* If the row-length is 3, and the input string is "abcdef" the result is ["abc", "def"]
* If the row-length is 3, and the input string is "abcdef abc" the result is ["abc", "def", "abc"]
* With row length 3 and "a b c d e f" the result is ["a b", "c d", "e f"]