# Phyton Wiki

## Wie starte ich Phyton
Wir öffnen Powershell gehen zu Ubuntu mit "wsl.exe --install" 
danach öffnen wir von Ubuntu Python mit dem Befehl "python3"

## Welche Befehle hatte wir bis jetzt gelernt 

Hier füge ich alle Beispiele ein die ich Unterricht probiert habe

first_name = "Domski"
middle_name = "DnB"
last_name = "Damager"
nickname = "#Domske"
alter = "28"

zahl1 = 99
zahl2 = 66

print(first_name + " " + middle_name + " " + last_name + " " + nickname + " " + alter)

print("zahl1 + zahl2", zahl1 + zahl2)
print("zahl1 * zahl2", zahl1 * zahl2)
print("zahl1 / zahl2", zahl1 / zahl2)

x = input("Domski")

y = input("DnB")

z = input("Damager")

print( x + y + z )

### Anmerkung:
Bei Input kann man z.b. so machen und dafür ist es da 

first_name = input("Wie ist dein Vorname: ") 
middle_name = input("Wie ist dein Zweitname: ")
last_name = input("Wie ist dein Nachname: ")
nickname = input("Was ist dein Spitzname: ")
alter = input("Wie alt bist du: ")

## Python Datentypen

Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType

x = "Hello World" 	                            str 	
x = 20 	                                        int 	
x = 20.5 	                                    float 	
x = 1j 	                                        complex 	
x = ["apple", "banana", "cherry"] 	            list 	
x = ("apple", "banana", "cherry") 	            tuple 	
x = range(6) 	                                range 	
x = {"name" : "John", "age" : 36} 	            dict 	
x = {"apple", "banana", "cherry"} 	            set 	
x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
x = True 	                                    bool 	
x = b"Hello" 	                                bytes 	
x = bytearray(5) 	                            bytearray 	
x = memoryview(bytes(5)) 	                    memoryview 	
x = None                                        NoneType