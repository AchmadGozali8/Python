print "implementasi loop dan operator"
print ""
print "Daftar makanan khas bugis"
makanan=[]
banyak_makanan = input("Berapa jenis nama makanan bugis yang akan direkomendasikan: ")
for i in range(banyak_makanan):
	a = raw_input("Masukkan nama makanan yang anda rekomendasikan: ")
	makanan.append(a)
	
print "daftar makanan yang kami rekomendasikan yaitu: ", makanan
