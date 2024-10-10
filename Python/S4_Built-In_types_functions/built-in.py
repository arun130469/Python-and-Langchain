val = 10
print(id(val))
val2 = val  # does not create a new object but reuses the same object.

if val is val2:
    print("val:", id(val), "  val2:", id(val2))  # print if they have the same ID


str1 = "string1"
str2 = str1

print("str1: ", id(str1), "str2: ", id(str2))  # same id

char1 = "a"
char2 = "a"

print("char1: ", id(char1), "char2: ", id(char2))  # Surprise!! they are same!

longstring1 = "this is a long string"
longstring2 = "this is a long string"

print("ls1: ", id(longstring1), "ls2: ", id(longstring2))  # BUT these are different!!
