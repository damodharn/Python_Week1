from array import array


class Utility2:

    @staticmethod
    def primeno():
        count = 0
        for x in range(2, 1000):
            prime = 1
            count += 1
            for y in range(2, (x // 2) + 1):
                if x % y == 0:
                    prime = 0
                    count -= 1
                    break
            if prime == 1:
                if (count - 1) % 10 == 0:
                    print("\n")
                print(count, ')', x, "", end="")

    # #################################  Prime  Anagram #######################
    @staticmethod
    def primeAnagram(no: object) -> object:                         # Check Prime
        arr = array('i', [])
        arr2 = array('i', [])
        count = 0
        for i in range(2, no + 1):
            prime = 1
            count += 1
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    prime = 0
                    count -= 1
                    break
            if prime == 1:
                arr.append(i)
                arr2.append(i)
            #  ****************************  Anagram checking    ********************************
        print('\n*********************  Prime Anagrams  **************************************\n')
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if len(str(arr[i])) == len(str(arr[j])):
                    var1 = ''.join(sorted(str(arr[i])))
                    var2 = ''.join(sorted(str(arr[j])))
                    if var1 == var2:
                        print(arr[i], 'and', arr[j], 'are Anagrams')

    #  *************************** Pelindrome check   *******************************************
        print('\n**************  Prime Palindromes *********************************************\n')
        for i in range(len(arr2)):
            if arr[i] > 10:
                no = arr[i]
                rev = 0
                temp = 0
                while no != 0:
                    temp = no % 10
                    rev = rev*10+temp
                    no = no // 10
                if arr[i] == rev:
                    print(arr[i], 'is a Palindrome')
        #  *************************  String Anagram  **********************************8
    @staticmethod
    def stringanagram(str1, str2):
        str1 = sorted(str1)
        str2 = sorted(str2)
        if str1 == str2:
            print('Strings are anagram')
        else:
            print('strings are not Anagrams')

    #  *************************** Insertion Sort For Integer  **************************

    @staticmethod
    def insertionsort_int():
        arr=array
