person1 = input("Wie alt bist du?: ")
person2 = input("Wie jung bist du?: ")

print(f"Der Typ von Person1 ist: {type(person1)}")

person1_int = int(person1)
person2_int = int(person2)

addition_person1_person2 = person1 + person2
addition_person1_int_person2_int = person1_int + person2_int


print (f"Die Summe der Jahren /str/ ist: {addition_person1_person2} ")
print (f"Die Summe der Jahren /int/ ist: {addition_person1_int_person2_int} ") 



