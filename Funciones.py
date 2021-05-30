# Reusando codigo con funciones
# Siempre se usa snake_case
# --- : ---- Marca el inicio del bloque de código 

def saluda_usuario():            #para definir una función
    print("Buenos días Krillin")   #Puedes realizar cualquier acción
    print("Es hora de entrenar")

# Para llamar la función escribiendo la función  ----- saluda_usuario() --------

def weather_update():
    print ("Weather update")
    print ("Rainy daya are comming")

def rutina_mañanera():

    print ("Levantate")
    print ("Estirate")
    print ("Relajate")
    print ("Bebe mucha agua")


def nombre_completo():      # se pueden guaradar variables dentro de una función
    nombre = ("Jorge")
    apellido = (" Rocha")
    print (nombre + apellido)
    
    
def saluton():
    nomo = "Ludwing"
    print (f"Saluton, {nomo}")

def saluti(Nomo):
    print(f"Hello, {Nomo}")
saluti("Samenhoff") #   -----  recicla la función;; dentro del parentesis sustituye a {Nomo}

def USUARIO():
    estado = "Activo"
    usantnomo = "Bob"
    print(f"{usantnomo} is {estado}")


def usant_nomo(estas):
    print(f"Bob: {estas}")
usant_nomo("Activista")
usant_nomo("Pacifista")


def duono(nombro):      # Para dividir un número entre 2 
    micha = nombro / 2
    print(micha)

def multiplicar(nombro):    # Para multiplicar un número entre 2 
    doble = nombro * 2
    print (doble)
    
# --------- Returning values -----------
# Si no se usa el comando 'return' el programa despliega 'None'

def age_label(age):
    label = "User age: " + age
    return label
print(age_label("22"))
"""
También se puede crear una variable para guardar el resultado
Ej:
result = age_label("22")
print(result)
"""

def quieroDiez():
    return 10

print(quieroDiez())

def enojo(usador):
    basura = "No te quiero volver a ver" + usador + ". Eres terrible."
    return basura

sal = enojo("Peterson")
print(sal)

def multiples_operaciones(numero):
    suma = numero + 96
    resta = suma - 529
    multiplicación = resta * -24
    division = multiplicación / 12
    return division
# Se puede cambiar 'division' de 'return' y poner cualquier otra operación y no se ejecutaran las acciones que hay después, se detiene en la variable que le asignas a 'return'

RESULT = multiples_operaciones(4)    

def el_doble(chichiton):
    dos = 2 * chichiton
    return dos
print(el_doble(20))

# ------------ USANDO MULTIPLES PARAMETROS ------------------

def muestra(unua, lasta):
    print(unua+" "+lasta)
muestra("Luffy", "Monkey")


# ------------

def create_email(name):
    return name + "@outlook.com"
email = create_email("jonas")
print(email)


def is_freezing(temperature):
    return temperature < 0
freezing = is_freezing(6)

def display_item_price(item, price):
    print (f"{item}: ${price}")
display_item_price("Chocolate", 4)

def generate_username(name, character):
    return (f"{name}-/&{character}")
usantnomo = generate_username("Jal", 482)


def get_free_seats(booked, total):
    return total - booked
freeS = get_free_seats(40,56)


def Total_score(score, bonus):
    print(score + bonus)
Total_score(623, 96)

def error_sum(a,b):
    return (a+b)
using_strings= error_sum("53","20")
# Usar strings en lugar de integers generará un error en la operación
# se pueden comparar valores


# Local scope

def add_bonus(SALARY):
    bonus = 200
    print(SALARY + bonus)

add_bonus(2096)    


#Global scope

price = 100
for i in range(2):
    discount = 10
    price = price - discount

print(f"Discount: {discount}")


# DECISIONES CON FUNCIONES
    
def add_shipping(cart):
  if cart < 200:
      #cuando se usa una condicional dentro de una función se pone a 2 espacios del borde inicial    
    print (f"Total: {cart + 10}")
add_shipping(16)

def can_drive(age):
  if age >= 18:
   print (f"Tu edad es: {age} por su pollo puedes")
  else:
   print(f"Tu edad es: {age} no puedes manejar")
can_drive(24)   

def calculate (operator, x, y):
  if operator  == "+":
    print(x+y)
  elif operator == "/":
    print(x/y)  
  else:
      print(f"unknown: {operator}")
calculate ("/",50,8)


def show_status(inbox):
  if inbox > 606:
    print("Inbox full!")
  print("You have new message!")
show_status(67)    
      

# FUNCIONES  +  LISTAS

def is_multiplayer(players):
    print(len(players) > 1 )

players = ["Amy", "Rory", "Dr. Donna"]
is_multiplayer(players)


def movies_forTonight(pelis):
   print("Airing tonight:")
   print(pelis)

The_list = ["Fido", "Guardians", "Troll hunter"]
movies_forTonight(The_list)


def booked(passengers):
  print(len(passengers) > 3)

Pasajeros = ["Juny", "Porfirio", "Stan Lee"]   
booked(Pasajeros)

def the_winner(Best_player):
   winner = Best_player[1]
   print(f"El mejor del mundo es: {winner}")
   
Players = ["Juny", "Porfirio", "Stan Lee"]   
the_winner(Players)   

# PARA SUSTITUIR UN ELEMENTO DE LA LISTA

def sustitution_of_player(leaderboard, player):
    leaderboard[0]=player
    return leaderboard

leaderboard = ["Juny", "Porfirio", "Stan Lee"]
leaderboard = sustitution_of_player(leaderboard,"Teresa")
print(leaderboard)

    
# DENTRO DE UNA FUNCIÓN SE PUEDEN USAR CULQUIER TIPO DE OPERADORES: count(), sum(), len(), replace()


# Loop WHILE

def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
#onboard_passengers(CUALQUIER NÚMERO)

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")
display_progress(5)

def countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")
      

def display_progress():
    for i in range(4):
        print(f"Downloading file {i} out of 3")
display_progress()

def Luffy(total_files):
  for i in range(total_files):
    print(f"Downloading file {i} out of {total_files}")
Luffy(3)    

def halve_price(cart):
    for price in cart:
        print(f"New price: {price/2}")
        
cart_list = [69, 369, 19, 24, 50]
halve_price(cart_list)


def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Rosana"]
    for track in playlist:
        print(f"Next song: {track}")
        
def next_track(playlist):
  for track in playlist:
    print(f"Next song: {track}")
        
songs = ["Hey Jude", "Helter Skelter", "Rosana"]
next_track(songs)
