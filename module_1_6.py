#my_dict ={"Andre": 2001, "Vitek": 1999, "Olga": 1983}
#print(my_dict)
#print(my_dict["Vitek"]) #1
#print (my_dict.get("Vitek"))#2
#print (my_dict.get("Oleg"))
#my_dict.update({"Nik": 1993, "Irina": 1962})
#print(my_dict)
#a = my_dict.pop("Vitek")
#print(a)
#print(my_dict)

my_set = {12, 13, "Krona", True, 12, 13, 14, "Krona", False}
print(my_set)
my_set.update(["New", 33])
print(type, my_set)
my_set.discard(13)
my_set.discard("Krona")
print(my_set)