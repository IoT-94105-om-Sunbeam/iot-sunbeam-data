from operations import arithmetic, string_ops

print("addition:", arithmetic.add(10, 5))
print("multiplication:", arithmetic.multiply(4, 3))

text = "today is a good day"
print("reversed String:", string_ops.reverseString(text))
print("vowel Count:", string_ops.countVowels(text))