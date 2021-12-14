TRANSLATIONS = {
    "bad": "good",
    "horrible": "fantastic",
    "dirty": "clean",
    "disgusting": "sublime",
    "expensive": "affordable",
    "moldy": "flavourful",
    "frozen": "farm-fresh"
}

ADJECTIVES = ['bad', 'horrible', 'dirty', 'disgusting', 'expensive', 'moldy', 'frozen']

TEMPLATES = [
    "The food was #AL ! We waited #N minutes for #AL vegetables and #AL bread. #AU !",
    "This restaurant is #AL ! We found the food #AL ! #AU ...",
    "1 time I went there. They serve #N dishes. The food tasted #AL .",
    "They offer #N dishes, and we waited #N minutes ! #AU !",
    "The wine was #AL . So I ordered #N bottles. ",
    "The clams were #AL . It should be 5 start but it isnt 5",
    "We sat there for #N minutes ! The food tasted #AL . #AU !",
    "I waited for maybe #N minutes . And the toilette was #AL .",
    "We got #AL mushrooms and they prepared it for #N minutes ! #AU"
]

NAMES = ["Lucas", "Louis", "Noah", "Nathan", "Adam", "Arthur", "Mohamed", "Victor",
         "Luka", "David", "Ivan", "Jakov", "Marko", "Petar", "Filip", "Matej",
         "Anna", "Hannah", "Sophia", "Emma", "Marie", "Lena", "Sarah", "Sophie",
         "Emma", "Louise", "Olivia", "Elise", "Alice", "Juliette", "Mila", "Lucie"]


def positivize(review):
    review = review.split()
    review_length = len(review)

    new_review = []
    for i, original_word in enumerate(review):
        lowered = original_word.lower()
        if lowered in TRANSLATIONS:
            translated = TRANSLATIONS[lowered]
            if original_word[0].isupper():
                translated = translated[0].upper() + translated[1:]
            new_review.append(translated)
            continue

        if original_word.isdigit() and i + 1 < review_length:
            if review[i + 1] == "minutes":
                new_review.append("only")
                new_minutes = str(int(int(original_word) / 2))
                new_review.append(new_minutes)
                continue

        new_review.append(original_word)

    return " ".join(new_review)
