from userService import userService

print("PROGRAM PEMINJAMAN BUKU KELOMPOK 10!\n")
email = input("Email: ")
password = input("Password: ")
get_class = userService(email,password)
get_class.login()