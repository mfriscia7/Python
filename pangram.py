def pangram(phrase):
    for i in range(65,90):
        if unichr(i) not in phrase and unichr(i+32) not in phrase:
            return 'not pangram'
    return 'pangram'


phrase = 'the quick brown fox jumps over the lazy dog'
phrase1 = 'this phrase is not a pangram'

print pangram(phrase)
print pangram(phrase1)