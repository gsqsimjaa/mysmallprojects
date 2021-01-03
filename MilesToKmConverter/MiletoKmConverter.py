milist = ["Mi", "Meilen", "miles", "meilen", "mi", "Miles"]
kmlist = ["km", "Kilometer", "Km", "kilometer", "KM", "kM"]
kmormi = input("Möchtest du Meilen oder Kilometer umrechnen? Mi oder Km?\n")
if kmormi in milist:
    message=input("\nBitte die Anzahl der Meilen eingeben!\n")
    result=float(message)*1.60934
    print("\n%s Meilen sind %r Kilometer!" % (message, result))

if kmormi in kmlist:
    message2=input("\nBitte die Anzahl der Kilometer eingeben!\n")
    result2 = float(message2) * 0.621371
    print("\n%s Kilometer sind %r Meilen!" % (message2, result2)) 

    






