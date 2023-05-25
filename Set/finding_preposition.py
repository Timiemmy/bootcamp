'''
Implement a function which takes a quote as a parameter to find out which given prepositions have been used in the quote.
The function should return the set of prepositions that are used in the quote.
'''

prep = {"as", "but", "by", "for", "in", "of", "on", "to", "with"}
'''
def find_prep(quote):
    found_prep = set()
    for words in prep:
        if words in quote.strip():
            found_prep.add(words)
    return found_prep
'''

def find_prep(quote):
    words = quote.split()
    preps_used = prep.intersection(words)
    return preps_used

quote = """Success is no accident. It is hard work, perseverance, learning, studying, 
            sacrifice and most of all, love of what you are doing or learning to do."""

print(find_prep(quote))