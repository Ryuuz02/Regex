import re

test_string = "banana"

"""
returns the part of the string with a 'ba'
match = re.search(r"ba", test_string)
"""

"""
Returns the part of the string with 'ab'
match = re.search(r"ab", test_string)
"""

"""
Brackets are basically just any value in that range, so for [abc], as long as that a, b, or c can fit in that spot, it 
will work. Also [a-c] is the same as [abc]
match = re.search(r"[b][a-c]n[abc]n[ac]", test_string)
"""

"""
You can put a caret at the beggining of the bracket to make it an except version. Basically makes it so that as long as
that part of the string is anything but the value in brackets, so [^a] would be any value but a works
match = re.search(r"[^a][^b-z]nana", test_string)
"""

"""
A caret on its own is just the beginning, so this would check if test_string starts with 'ba'
match = re.search(r"^ba", test_string)
"""

"""
Similarly, this tests if test_string starts with 'baa'
match = re.search(r"^baa", test_string)
"""

"""
The dollar sign is the opposite, testing if it ends with the string before it, this would test if it ends in 'anana'
match = re.search(r"anana$", test_string)
"""

"""
Tests if it ends in 'ana'
match = re.search(r"ana$", test_string)
"""

"""
Tests if it ends in 'ban'
match = re.search(r"ban$", test_string)
"""

"""
A dot works for any character except new line (\n). this could be a-z, digits or anything, it all fills that spot
match = re.search(r"......", test_string)
"""

"""
Can be combined as with everything else to say that parts of the string can be any value
match = re.search(r"ba...a", test_string)
"""

"""
The | is an or operator. This one tests if there is an a or b in the test_string
match = re.search(r"a|b", test_string)
"""

"""
Tests if it starts with an a or b and continues with anana
match = re.search(r"(^b|a)anana", test_string)
"""

"""
Takes the ba from 'ba?' and adds a nana on the back and finds the whole banana
match = re.search(r"ba?nana", test_string)
"""

"""
returns none since there is nothing it can do with a p
match = re.search(r"pe?", test_string)
"""

"""
The question mark basically takes as much of the string before it as it can. In this case, the first question mark takes
the 'ba', since it can match that with the first two letters of banana, and the nana from the second question mark for 
the last 4 letters
match = re.search(r"ban?nana?", test_string)
"""

"""
I thought I understood question marks, but now I don't. According to my logic, this should take the 'pin' from pind, and 
the 'e' from epp to give us span=(0, 4) but it returns none
match = re.search(r"(pind?)(epp?)", "pineapple")
"""

"""
Similarly, this should take the 'pin' from pinsir and the 'e' from e to also return a span of (0, 4)
match = re.search(r"(pinsir?)(e?)", "pineapple")
"""

# print(match)
