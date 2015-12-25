print "Decision"
print "Situasi dimana jika cuaca buruk atau tidak"
print ""
ulang = True
while ulang :
	a = raw_input("bagaimana situasi diluar apakah hujan?(ya atau tidak) ")
	if a == "ya":
		print "tetap dirumah untuk coding"
		ulang = False
	elif a == "tidak":
		print "ke warkop untuk coding"
		ulang = False
	else:
		print "masukkan ya atau tidak"
		ulang = True
		