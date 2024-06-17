def main():
    print(Subword("word", "wordle"))
    words = []
    with open("dictionary.txt", 'r') as f:
        for line in f:
            words.append(line.strip())
    words.sort()
    print(words)
    print("YABE" in words)
    words_dict={3: [],4: [] ,5: [],6: [],7: [] }
    for word in words:
        words_dict[len(word)].append(word)
    print(words_dict)
def Subword(word_a,word_b):
    for letter in word_a:
        if word_a.count(letter) > word_b.count(letter):
            return False
    return True
def superword(superwords, word_dict):
    subwords = []
    for length, words in word_dict.items():
        for word in words:
            if Subword(words,superwords):
                subwords.append(word)
    return subwords


if __name__ == '__main__':
    main()
