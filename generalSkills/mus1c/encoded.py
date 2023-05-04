ASCII_encoded_song= "114 114 114 111 99 107 110 114 110 48 49 49 51 114"

print("picoCTF{", end='')
for c in ASCII_encoded_song.split():
        print(chr(int(c)), end='')
print("}")
