alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']       #Normal order of alphabet
p_alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']     #Permutation order of alphabet

c_text = input("Enter text to be decrypted: ")
p_text = []

for i in range(len(c_text)):
    for p in range(len(p_alph)):
        if c_text[i] is p_alph[p]:
            p_text.append(alph[p])

print("Your decrypted data is: " + "".join(p_text))