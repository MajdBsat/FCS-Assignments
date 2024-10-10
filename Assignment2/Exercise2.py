Names = ["Maria" , "Hala", "Ghady" , "Ehsan", "Joe", "Zoe"]
str1 = ""

while str1.lower() != "done": 

    str1 = input("Enter a letter or (done) to exit: ").lower()

    if str1.lower == "done":
       break
    else:
        for i in (Names):
            if str1 in i.lower():
                print(i)