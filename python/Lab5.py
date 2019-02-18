word = input("Please enter a sentence: ")

removedSpacesWord = word.replace(" ", "")

print("Total length of sentence = ", len(removedSpacesWord))

countVowels =0
countConsonants =0

for i in removedSpacesWord:
    if(i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u'
    or i == 'A' or i == 'E' or i == 'I' or i =='O' or i =='U' ):

        countVowels = countVowels + 1
    else:
        countConsonants = countConsonants + 1

print("Total number of vowels = ",countVowels)
print("Total number of Consonants = ",countConsonants)
