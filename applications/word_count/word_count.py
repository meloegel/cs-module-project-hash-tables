def word_count(s):
    cache = {}
    lowS = s.lower()
    symbols = '" : , . - + ; = | \ / { } [ ] ( ) * ^ &'.split(" ")
    for char in symbols:
        lowS = lowS.replace(char, "")
    for x in lowS.split():
        if x == "":
            continue
        if x not in cache:
            cache[x] = 1
        else:
            cache[x] += 1
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))