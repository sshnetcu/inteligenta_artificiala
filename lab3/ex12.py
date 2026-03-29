squares_dict = {x: x**2 for x in range(1, 11)}

text = "banana"
freq = {c: text.count(c) for c in text}

divisors = {
    x: [d for d in range(1, x+1) if x % d == 0]
    for x in range(1, 11)
}