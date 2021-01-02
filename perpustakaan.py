import mysql.connector

conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="db_perpustakaan")
cursor=conn.cursor()


class anggota():
    def __init__ (self, ID_Anggota, Nama_Lengkap, Jenis_Kelamin, Tanggal_Lahir, Email, Username, Password):
        self.ID_Anggota = ID_Anggota
        self.Nama_Lengkap = Nama_Lengkap
        self.Jenis_Kelamin = Jenis_Kelamin
        self.Tanggal_Lahir = Tanggal_Lahir
        self.Email = Email
        self.Username = Username
        self.Password = Password
        self.judul_buku_pinjam = ""
        self.jenis_buku_pinjam = ""
        self.nama_pengarang_pinjam = ""
        self.nama_penerbit_pinjam = ""
        self.tahun_terbit_pinjam = ""
    
    def melihat_data(self):
        print("Nama Lengkap = {}\nJenis Kelamin = {}\nTanggal Lahir = {}\nEmail = {}\nUsername = {}\nPassword = {}".format(self.Nama_Lengkap, self.Jenis_Kelamin, self.Tanggal_Lahir, self.Email, self.Username, self.Password))

    def mengubah_data(self):
        print("1. Nama Lengkap")
        print("2. Jenis Kelamin")
        print("3. Tanggal Lahir")
        print("4. Email")
        print("5. Username")
        print("6. Password")
        ubah = int(input("Apa yang ingin diubah?: "))
        
        if ubah==1:
            nama_lengkap_baru=str(input("Nama lengkap baru: "))
            query = "UPDATE tb_anggota SET Nama_Lengkap={} WHERE ID_Anggota={} ".format(nama_lengkap_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
        if ubah==2:
            jenis_kelamin_baru=str(input("Jenis kelamin baru: "))
            query = "UPDATE tb_anggota SET Jenis_Kelamin={} WHERE ID_Anggota={} ".format(jenis_kelamin_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
        if ubah==3:
            tanggal_lahir_baru=str(input("Tanggal lahir baru: "))
            query = "UPDATE tb_anggota SET Tanggal_Lahir={} WHERE ID_Anggota={} ".format(tanggal_lahir_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
        if ubah==4:
            email_baru=str(input("Email baru: "))
            query = "UPDATE tb_anggota SET Email={} WHERE ID_Anggota={} ".format(email_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
        if ubah==5:
            username_baru=str(input("Username baru: "))
            query = "UPDATE tb_anggota SET Username={} WHERE ID_Anggota={} ".format(username_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
        if ubah==6:
            password_baru=str(input("Nama lengkap baru: "))
            query = "UPDATE tb_anggota SET Password={} WHERE ID_Anggota={} ".format(password_baru, self.ID_Anggota)
            cursor.execute(query)
            conn.commit()
    
    def cari_buku(self):
        userInput = int(input("\n1. Cari buku berdasarkan judul\n2. Cari buku berdasarkan jenis buku\n3. Cari buku berdasarkan pengarang\n4. Cari buku berdasarkan penerbit\n5. Cari buku berdasarkan tahun terbit\n6. Back\nInput angka pilihan di atas : "))

        if userInput == 1:
            inputBuku = input("Masukan judul buku : ")
            query = "SELECT * from tb_buku where Judul_Buku = %s"
            value = (inputBuku, )
            cursor.execute(query, value)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])
            except:
                print("\nJudul buku tidak ditemukan") 
        elif userInput == 2:
            inputBuku = str(input("Masukan Jenis Buku : "))
            query = "SELECT * from tb_buku where Jenis_Buku = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])
            except:
                print("\nJenis buku tidak ditemukan") 
        elif userInput == 3:
            inputBuku = str(input("Masukkan Nama Pengarang : "))
            query = "SELECT * from tb_buku where Nama_Pengarang = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])
            except:
                print("\nNama Pengarang buku tidak ditemukan")
        elif userInput == 4:
            inputBuku = str(input("Masukkan Nama Penerbit : "))
            query = "SELECT * from buku where Nama_Penerbit = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])
            except:
                print("\nNama penerbit tidak ditemukan")
        elif userInput == 5:
            inputBuku = str(input("Masukkan Tahun Terbit : "))
            query = "SELECT * from buku where Tahun_Terbit = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])
            except:
                print("\nTahun terbit tidak ditemukan")
        elif userInput == 6:
            return True
    
    def pinjam_buku(self):
        userInput = int(input("\n1. Pinjam buku berdasarkan judul\n2. Pinjam buku berdasarkan jenis buku\n3. Pinjam buku berdasarkan pengarang\n4. Pinjam buku berdasarkan penerbit\n5. Pinjam buku berdasarkan tahun terbit\n6. Kembali\nInput angka pilihan di atas : "))

        if userInput == 1:
            inputBuku = input("Masukan judul buku : ")
            query = "SELECT * from tb_buku where Judul_Buku = %s"
            value = (inputBuku, )
            cursor.execute(query, value)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])

                self.judul_buku_pinjam = dataBuku[1]
                self.jenis_buku_pinjam = dataBuku[2]
                self.nama_pengarang_pinjam = dataBuku[3]
                self.nama_penerbit_pinjam = dataBuku[4]
                self.tahun_terbit_pinjam = dataBuku[5]
                
                total = dataBuku[6]-1
                update = "UPDATE tb_buku SET Stok_Buku=%s where ID_Buku=%s"
                value = (total, dataBuku[0])
                cursor.execute(update, value)
                conn.commit()
                print("Berhasil meminjam buku")
            except:
                print("Judul buku tidak ditemukan")

        elif userInput == 2:
            inputBuku = str(input("Masukan jenis buku : "))
            query = "SELECT * from tb_buku where Jenis_Buku = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])

                self.judul_buku_pinjam = dataBuku[1]
                self.jenis_buku_pinjam = dataBuku[2]
                self.nama_pengarang_pinjam = dataBuku[3]
                self.nama_penerbit_pinjam = dataBuku[4]
                self.tahun_terbit_pinjam = dataBuku[5]
                
                total = dataBuku[6]-1
                update = "UPDATE tb_buku SET Stok_Buku=%s where ID_Buku=%s"
                value = (total, dataBuku[0])
                cursor.execute(update, value)
                conn.commit()
                print("Berhasil meminjam buku")

            except:
                print("Jenis buku tidak ditemukan") 

        elif userInput == 3:
            inputBuku = str(input("Masukan nama pengarang buku : "))
            query = "SELECT * from tb_buku where Nama_Pengarang = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])

                self.judul_buku_pinjam = dataBuku[1]
                self.jenis_buku_pinjam = dataBuku[2]
                self.nama_pengarang_pinjam = dataBuku[3]
                self.nama_penerbit_pinjam = dataBuku[4]
                self.tahun_terbit_pinjam = dataBuku[5]
                
                total = dataBuku[6]-1
                update = "UPDATE tb_buku SET Stok_Buku=%s where ID_Buku=%s"
                value = (total, dataBuku[0])
                cursor.execute(update, value)
                conn.commit()
                print("Berhasil meminjam buku")

            except:
                print("Nama pengarang tidak ditemukan")
            
        elif userInput == 4:
            inputBuku = str(input("Masukan nama penerbit buku : "))
            query = "SELECT * from tb_buku where Nama_Penerbit = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])

                self.judul_buku_pinjam = dataBuku[1]
                self.jenis_buku_pinjam = dataBuku[2]
                self.nama_pengarang_pinjam = dataBuku[3]
                self.nama_penerbit_pinjam = dataBuku[4]
                self.tahun_terbit_pinjam = dataBuku[5]

                total = dataBuku[6]-1
                update = "UPDATE tb_buku SET Stok_Buku=%s where ID_Buku=%s"
                value = (total, dataBuku[0])
                cursor.execute(update, value)
                conn.commit()
                print("Berhasil meminjam buku")

            except:
                print("Nama penerbit tidak ditemukan")

        elif userInput == 5:
            inputBuku = str(input("Masukan tahun terbit buku : "))
            query = "SELECT * from tb_buku where Tahun_Terbit = '{}'".format(inputBuku)
            cursor.execute(query)
            try:
                dataBuku = cursor.fetchall()[0]
                print("Judul Buku :",dataBuku[1])
                print("Jenis Buku : ",dataBuku[2])
                print("Nama Pengarang :",dataBuku[3])
                print("Nama Penerbit :",dataBuku[4])
                print("Tahun Terbit :",dataBuku[5])

                self.judul_buku_pinjam = dataBuku[1]
                self.jenis_buku_pinjam = dataBuku[2]
                self.nama_pengarang_pinjam = dataBuku[3]
                self.nama_penerbit_pinjam = dataBuku[4]
                self.tahun_terbit_pinjam = dataBuku[5]
                
                total = dataBuku[6]-1
                update = "UPDATE tb_buku SET Stok_Buku=%s where ID_Buku=%s"
                value = (total, dataBuku[0])
                cursor.execute(update, value)
                conn.commit()
                print("Berhasil meminjam buku")

            except:
                print("Tahun terbit tidak ditemukan")

        elif userInput == 6:
            return True

    
    def kembalikan_buku(self):
        if self.judul_buku_pinjam == "Belum pinjam":
            print("\nAnda belum meminjam buku apapun")
            return True
        else:
            print("\nData buku yang akan dikembalikan :")
            print("Judul Buku :",self.judul_buku_pinjam)
            print("Jenis Buku: ",self.jenis_buku_pinjam)
            print("Nama Pengarang: ",self.nama_pengarang_pinjam)
            print("Nama Penerbit: ",self.nama_penerbit_pinjam)
            print("Tahun Terbit: ",self.tahun_terbit_pinjam)
            print()
            query = "INSERT into tb_buku values({},'{}','{}','{}','{}')".format(self.judul_buku_pinjam, self.jenis_buku_pinjam, self.nama_pengarang_pinjam, self.nama_penerbit_pinjam, self.tahun_terbit_pinjam)
            cursor.execute(query)
            conn.commit()
            print("Buku berhasil dikembalikan")
            self.judul_buku_pinjam = "Belum pinjam"
            self.jenis_buku_pinjam = "Belum pinjam"
            self.nama_pengarang_pinjam = "Belum pinjam"
            self.nama_penerbit_pinjam = "Belum pinjam"
            self.tahun_terbit_pinjam = "Belum pinjam"
            self.commit()
    
    def commit(self):
        query = "UPDATE tb_peminjaman set judul_buku_pinjam = '{}',jenis_buku_pinjam = '{}',nama_pengarang_pinjam = '{}', nama_penerbit_pinjam = '{}', tahun_terbit_pinjam = '{}' where ID_Anggota = {}".format(self.judul_buku_pinjam, self.jenis_buku_pinjam, self.nama_pengarang_pinjam, self.nama_penerbit_pinjam, self.tahun_terbit_pinjam, self.ID_Anggota)
        cursor.execute(query)
        conn.commit()


def menu():
    userInput = int(input("\n1. Cari buku\n2. Pinjam buku\n3. Kembalikan buku\n4. Melihat data diri\n5. Mengubah data diri\nSilahkan pilih pilihan di atas : "))
    if userInput == 1:
        cari_buku()
    elif userInput == 2:
        pinjam_buku()
    elif userInput == 3:
        kembalikan_buku()
    elif userInput == 4:
        melihat_data()
    elif userInput == 5:
        mengubah_data()

def registrasi():
    Nama_Lengkap = str(input("Nama Lengkap: "))
    Jenis_Kelamin = str(input("Jenis Kelamin: "))
    Tanggal_Lahir = str(input("Tanggal Lahir: "))
    Email = str(input("Email: "))
    Username = str(input("Username: "))
    Password = str(input("Password: "))
    query = "INSERT into tb_anggota values ('', '{}','{}','{}','{}','{}','{}')".format(Nama_Lengkap, Jenis_Kelamin, Tanggal_Lahir, Email, Username, Password)
    cursor.execute(query)
    conn.commit()
    print("\nSelamat, Anda berhasil registrasi")
    menu()
    
data_login = []
def login():
    Username = str(input("Username : "))
    Password = str(input("Password : "))
    query= "SELECT*from tb_anggota where Username='{}' and Password='{}'".format(Username, Password) 
    try:
        cursor.execute(query)
        a=cursor.fetchall()
        for data in a :
            data_login.append(data)
        print("\nSELAMAT DATANG DI PERPUSTAKAAN")

    except:
        print("Username atau password yang Anda masukan salah")


def tampilan_awal():
    while True:
        print("1. Login")
        print("2. Registrasi")
        pilihan = int(input("Pilihlah menu di atas: "))
        if pilihan == 1:
            login()
            anggota_perpus = anggota(data_login[0][0],data_login[0][1],data_login[0][2],data_login[0][3],data_login[0][4],data_login[0][5],data_login[0][6])
            while True:
                userInput = int(input("\n1. Cari buku\n2. Pinjam buku\n3. Kembalikan buku\n4. Melihat data diri\n5. Mengubah data diri\n6. Logout\ninput angka pilihan diatas : "))
                if userInput == 1:
                    anggota_perpus.cari_buku()
                elif userInput == 2:
                    anggota_perpus.pinjam_buku()
                elif userInput == 3:
                    anggota_perpus.kembalikan_buku()
                elif userInput == 4:
                    anggota_perpus.melihat_data()
                elif userInput == 5:
                    anggota_perpus.mengubah_data()
                elif userInput == 6:
                    tampilan_awal()

        elif pilihan == 2:
            registrasi()
        else:
            print("Pilihan tidak tersedia")
    
tampilan_awal()

