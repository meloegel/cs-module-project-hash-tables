import random

# Read in all the words in one go
with open("./applications/markov/input.txt") as f:
    words = f.read()
    word = words.split()

# TODO: analyze which words can follow other words
def pairUp(arr):
    for i in range(len(arr) - 1):
        yield (arr[i], arr[i + 1])
pairs = pairUp(word)
wordDict = {}
for x, y in pairs:
    if x in wordDict.keys():
        wordDict[x].append(y)
    else:
        wordDict[x] = [y]
first = random.choice(word)
last = random.choice(word)
while first.islower() and first[0] != "'":
    first = random.choice(word)
while last[-1] not in [',', '.']:
    last = random.choice(word)
sentence = [first]
lastWord = [last]
num = 100
for i in range(num):
    sentence.append(random.choice(wordDict[sentence[-1]]))
print(' '.join(sentence + lastWord))


# TODO: construct 5 random sentences
# 1) Looking-glass, that you're the progress of your eye? Well, I could only the edge of the most likely place to have won, if you're the White Queen sitting sulkily among my dear!" And don't think you're a long argument with the side of breath. "Mind you know whether there are getting in it! Let's pretend that came wiggling down the winter: you can see her. "You will, though," the afternoon, and had been doing, I don't keep this one of the Queen cried Alice, catching up in the table behind Alice, dropping the old nurse by its face this led to well,

#2) "What manner of our books, only the door of sticks, Kitty! now we could manage--and then they said. The King looked on the book lying near Alice was so wide open! All the leaves, to the side of worsted Alice had never seen in the room so wide open: and sat very badly") "That's not been reduced at work on with it: it was very like a little mischievous darling! What have to the floor. "Oh! please don't make me laugh so wish it up on getting brown. "Kitty, can just like to purr--no doubt feeling that all ready to see Why,


# 3) Alice had been reduced at the day before--all because I've held up from bar to do at last he slowly than the worsted while she rubbed its ear with one of worsted to tell you never forget!" "You haven't got any whiskers." "The White Knight is sliding down by the table behind the kitten. "Let's pretend." She had done, and for a fire in all come up--the regular way--don't get upon the question: it was the worsted Alice began. "You'd have you squeaked twice while I want so covered with the ball again. "Do you little Lily was the fire. Well middle.

# 4) "So I can tell, you know I'm asking it covers them so much to melt away, just to help, if she rubbed its good. But she could tell you ought!" she called out of the black kitten's neck, just like her. So Alice began. "You'd have to do you couldn't. I saw all the kitten. "Let's pretend we're kings and gently touching the ball rolled down among the ball of frightening them), 'and I'm sure they wake up the kitten had jumped lightly down the old room so much to go the White Queen sitting on getting brown. "Kitty, can hardly him.

# 5) But the White Knight is the summer, Kitty, we'll go without a little kiss to say, "Well, you never forget!" "You make such beautiful things go and began squeaking on with the snow! And here I feel somehow as cross a nice it snowed so, they dress themselves all over his shoulder, and had put him a minute or three faults, Kitty, they dress themselves all ready to know she added, as different on with the kitten wouldn't fold its ear with the Looking-glass House. First, there's a way Dinah was a dear!" And here as cross a memorandum of my ashes,
