#Task 1
cat_breeds = ['Persian','Bengal','Siamese','Savannah','Ragdoll']
file = open("catbreeds.txt","w")
for i in cat_breeds:
    file.write("%s\n" % )
file.close()
file = open(catbreeds.txt, "r")
print(file.read())
file.close()