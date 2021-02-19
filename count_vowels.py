
def count_vowels(string):
    new_string = ""
    vowel_count = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0
    }
    vowels = vowel_count.keys()
    for i in string:
        if i.lower() in vowels:
            vowel_count[i.lower()] += 1
        else:
            new_string += str(i)
    return new_string,vowel_count
if __name__ == "__main__":
    string = input()
    
    print(count_vowels(string))