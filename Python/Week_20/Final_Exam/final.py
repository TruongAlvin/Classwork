def main():
    words = []
    with open("dictionary.txt", 'r') as f:
        for line in f:
            words.append(line.strip())
    words.sort()
    print(words)
    print("YABE" in words)


if __name__ == '__main__':
    main()