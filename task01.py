name = input("ismingizni kiriting: ")
age = input("yoshingizni kiriting: ")

f = open("data.txt", "a")
data = f"{name.capitalize()} - {age}\n"
f.write(data)
print("Ma'lumot faylga yozildi.")
