class userService(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = {
            "imanakelompok10@gmail.com" : {
                "email"     : "imanakelompok10@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },
            "erlinkelompok10@gmail.com" : {
                "email"     : "erlinkelompok10@gmail.com",
                "password"  : "12345",
                "role"      : "user"
            }
        }

    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'])
        else:
            print("\nInvalid Login!\n")

    def checkCredentials(self):
        for value in self.data:
            if value == self.email:
                get_data_user = self.data[value] 
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    def showHistory(self) : 
        print(self.email + " Meminjam Buku:")
        for x in self.history[self.email]["pinjam_buku"] :
            print(x)
        print("date:\n" + self.history[self.email]["tgl_pinjam"] + "\n")


