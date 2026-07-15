#14. Write a recursive function to flatten a nested list (e.g., [1, [2, [3, 4], 5]] → [1, 2, 3, 4, 5]).
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))   # recursive call
        else:
            result.append(item)
    return result
lst = [1, [2, [3, 4], 5]]
print(flatten(lst))