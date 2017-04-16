alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']       #Normal order of alphabet
p_alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']     #Permutation order of alphabet

p_text = input("Enter plaintext to be encrypted: ")
c_text = []

for i in range(len(p_text)):
    for p in range(len(alph)):
        if p_text[i] is alph[p]:
            c_text.append(p_alph[p])

print("Your Encrypted data is: " + "".join(c_text))
