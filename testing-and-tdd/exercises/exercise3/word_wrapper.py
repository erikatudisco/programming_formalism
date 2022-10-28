
<<<<<<< HEAD
def wrap_words(input_string, row_length):
string_length = len(input_string)
number_blocks = int(string_length/row_length)+1
blocks = []

for i in range(number_blocks):
blocks.append(input_string[0:row_length])
input_string = input_string[row_length:]

return blocks


print(type(wrap_words("Hello World!" , 5)))
print(len(wrap_words("Hello World!" , 5)))
print(wrap_words("Hello World!" , 20)) 
=======
def wrap_words(s, row_length):
    return s
>>>>>>> a4c04e1e41c3cb32507625583558e78fdaea76ed
