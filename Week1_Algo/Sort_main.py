from Week1_Algo.Utility2 import Utility2
no = 8
while no != 7:
    no = int(input("Enter ur choice:\n1: binarySearch method for integer\n2: binarySearch method for String\n3: insertionSort method for integer\n4: insertionSort method for String\n5: bubbleSort method for integer\n6: bubbleSort method for String\n7: exit"))
    if no ==1:
        arr = Utility2.binarySearchInt()
    elif no == 2:
        arr = Utility2.binarySearchString()
    elif no == 3:
        arr = Utility2.insertionSortInt()
    elif no == 4:
        arr = Utility2.insertionSortString()
    elif no == 5:
        arr = Utility2.bubbleSortInt()
    elif no == 6:
        arr = Utility2.bubbleSortString()
    else:
        if no == 7:
            break
        else:
            print("Wrong Input....Enter Valid i/p")
