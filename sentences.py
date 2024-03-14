import random
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == "1":
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"] 
    elif tense == "present" and quantity != "1":
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    word = random.choice(words)
    return word
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    Escriba una función nombrada make_sentencecon el siguiente 
    encabezado y cadena de documentación. Su make_sentencefunción 
    debe llamar a su función get_determiner, get_nouny get_verbuna 
    vez cada una y construir y devolver una oración. Su make_sentencefunción 
    debe escribir en mayúscula la primera letra de la oración y terminarla con un punto (.).
    """
    determiner= get_determiner (quantity)
    noun= get_noun(quantity)
    verb=get_verb(quantity,tense)
    phrase= get_prepositional_phrase(quantity)
    sentence= f"{determiner.capitalize()} {noun} {phrase} {verb}"
    return sentence

def main ():
    quantity = 1
    tense="past"
    sentence= make_sentence(quantity, tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")

    quantity=1
    tense="present"
    sentence= make_sentence(quantity,tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")

    quantity=1
    tense="future"
    sentence= make_sentence(quantity,tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")
    
    quantity = 2
    tense="past"
    sentence= make_sentence(quantity, tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")

    quantity=2
    tense="present"
    sentence= make_sentence(quantity,tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")
    
    quantity=2
    tense="future"
    sentence= make_sentence(quantity,tense)
    phrase= get_prepositional_phrase(quantity)
    print(f"{sentence} {phrase}.")

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words=["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
    quantity: an integer that determines if the
        determiner and noun in the prepositional
        phrase returned from this function should
        be single or pluaral.
    Return: a prepositional phrase.
    """
    determiner= get_determiner (quantity)
    noun= get_noun(quantity)
    preposition=get_preposition()
    phrase= f"{preposition} {determiner} {noun}"
    return phrase

main()

# Within your make_sentence function add another call to get_prepositional_phrase 
# so that each sentence includes two prepositional phrases
    