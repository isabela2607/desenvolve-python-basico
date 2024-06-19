from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = [palavra for palavra in frase.split() if is_anagram(palavra, palavra_objetivo)]
print(f"Anagramas: {anagramas}")