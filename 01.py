#write a program to take string "Aptech Learning" and print the string as "ApTech LeArning"
s="Aptech Learning"

result= s.replace("t", "T", 1).replace("a", "A", 1)
print(result)