def number_of_bottles():
    for i in reversed(range(100)):
        if i < 100 and i > 1:
            print(str(i) +" bottles of milk on the wall, "+ str(i)+ " bottles of milk.\n" "Take one down and pass it around, "+ str(i-1) + " bottles")
        elif i == 1:
            print(str(i) +" bottles of milk on the wall, "+ str(i)+ " bottles of milk.\n" "Take one down and pass it around, no more bottles of milk on the wall.")
        else: 
            print("No more bottles of milk on the wall, no more bottles of milk.\n" "Go to the store and buy some more, 99 bottles of milk on the wall.")


number_of_bottles()