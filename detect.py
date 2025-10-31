def remove_duplicates(data):
    seen = set()
    unique = []
    for d in data:
        t = tuple(sorted(d.items()))
        if t not in seen:
            seen.add(t)
            unique.append(d)
    return unique

data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"}
]
print(remove_duplicates(data))
