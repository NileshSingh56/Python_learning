def countVowCons(string):
    vowel="aeiouAEIOU"
    countVowel=0
    countConsonant=0

    for eachChar in string:
        if(eachChar.isalpha()):
            if(eachChar in vowel):
                countVowel+=1
            else:
                countConsonant+=1

    return countVowel,countConsonant

Vowels,Consonants=countVowCons("NileshSingh")

print("Vowels:",Vowels)
print("Consonants:",Consonants)