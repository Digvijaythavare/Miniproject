def count_vowels(userInput):
    Vowels = "aeiouAEIOU"


    countVowels = 0
    countConst = 0

    for eachChar in userInput: 
         if(eachChar.isalpha):
                if eachChar in Vowels:
                     countVowels += 1
                else:
                     countConst += 1
    return countVowels,countConst


vowel , costrn =    count_vowels("Digvijay Thavare")
print("Vowels: ",vowel)
print("Consonants: ",costrn)
