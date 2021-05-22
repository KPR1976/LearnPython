"""
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…
"""
def baby_shark_lyrics():
    lyrics, doo, let, e, s  = '', ' doo', 'Let\'s go hunt', '{}!\n', '{},{}\n'
    for f in ['Baby', 'Mommy', 'Daddy', 'Grandma', 'Grandpa']:
        f = f + ' shark'
        lyrics += s.format(f, doo * 6) * 3 + e.format(f)
    return lyrics += s.format(let, doo * 6) * 3 + e.format(let) + 'Run away,…'
    return lyrics

print(baby_shark_lyrics())
