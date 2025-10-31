def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, [3, 4], [5, [6]]], 7]))
