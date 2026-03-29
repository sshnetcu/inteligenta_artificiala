prices = [100, 200, None, 50, None, 300]

filtered = list(filter(lambda x: x is not None, prices))
discounted = list(map(lambda x: x * 0.9, filtered))

print(discounted)  # [90.0, 180.0, 45.0, 270.0]