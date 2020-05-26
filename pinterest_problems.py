# Q1 At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 
# To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

# Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

def knows(known, a, b):
    return b in known[a]


def get_celeb(known):
    celeb_candidates = set(known.keys())

    while celeb_candidates:
        sample = next(iter(celeb_candidates))
        celeb_candidates.remove(sample)
        count = len(celeb_candidates)
        for other in celeb_candidates:
            if not knows(known, sample, other):
                count -= 1
        if count == 0:
            return sample

known = {'a': {'b', 'c'},
         'b': {'c'},
         'c': {'a'},
         'd': set()}

print(get_celeb(known))
