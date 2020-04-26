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
        self.history = {
            "imanakelompok10@gmail.com" : {
                "pinjam_buku" : {"- Kalkulus" , "- Sistem Digital"},
                "tgl_pinjam" : "26-04-2020"
                },
            "erlinkelompok10@gmail.com" : {
                "pinjam_buku" : {"- Pendidikan Pancasila","- Kecakapan Antar Personal"},
                "tgl_pinjam" : "26-04-2020"
                },
            }

    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nWelcome ",get_data['role'])
            print("Logged it as user email: ",get_data['email'])
            print("----------------")
            print(self.email + " Meminjam Buku:")
            for x in self.history[self.email]["pinjam_buku"] :
                print(x)
            print("date:\n" + self.history[self.email]["tgl_pinjam"] + "\n")
        else:
            print("\nInvalid Login!\n")

    def showHistory(self) : 
        print(self.email + " Meminjam Buku:")
        for x in self.history[self.email]["pinjam_buku"] :
            print(x)
        print("date:\n" + self.history[self.email]["tgl_pinjam"] + "\n")


