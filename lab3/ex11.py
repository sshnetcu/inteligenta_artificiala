even_set = {x for x in range(0, 20, 2)}

text = "hello world"
letters = {c for c in text if c != " "}

text = "Acesta este un exemplu simplu pentru testare"
words = {word for word in text.split() if len(word) >= 5}