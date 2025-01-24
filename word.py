"""
8. Write a function that searches an list of names (unsorted) for the name &quot;Bob&quot; and returns the
location in the list. If Bob is not in the list, return -1.

Examples
find_bob([&quot;Jimmy&quot;, &quot;Layla&quot;, &quot;Bob&quot;]) ➞ 2"""

def find_bob(names):
    for index, name in enumerate(names):
        if name =="bob":
            return index
        
    return -1
print(find_bob(["Jimmy", "Layla", "Bob"]))