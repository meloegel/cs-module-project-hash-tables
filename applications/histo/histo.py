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

with open('./applications/histo/robin.txt') as file:
    s = file.read()

cache = word_count(s)
width= max([len(word) for word in cache.keys()]) + 2

cache = sorted(cache.items(), key=lambda x:(-x[1], x[0]))

print(cache)

for count in cache:
    print(f'{count[0].ljust(width)}' + '#' * count[1])