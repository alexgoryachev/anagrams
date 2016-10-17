from collections import Counter

used_word = []

with open('dictionary.txt') as f:
    lines = f.read().splitlines()
# the script removes all anagrams from lines until len(lines) >0
while len(lines) > 0:
    # take the first word from lines
    word = lines[0].rstrip()
    wlen, wset, wcnt = len(word), set(word), Counter(word)
    result = []
    # append it to result
    result.append(word)
    # remove the first word from a lines
    lines.remove(word)
    # Checking if there is an anagram for the  first word
    for temp_thesaurus in lines:
        thesaurus = temp_thesaurus.strip()
        if wlen == len(thesaurus) and wset == set(thesaurus) and wcnt == Counter(thesaurus):
            result.append(thesaurus)
            # append fond an anagram to used words for removal
            used_word.append(thesaurus)
            # remove all found anagrams from line
    lines = [item for item in lines if item not in used_word]
    # print all anagrams for the first word in a file copy     
    print(', '.join(result))
