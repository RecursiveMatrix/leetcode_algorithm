# given an array of strings, group anagrams together

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs):

    d = {}
    for word in strs:
        key = str(sorted(word))

        # warning: type of key in a dictionary cannot be a list
        # key = sorted(word)

        # result of a sorted object is list
        # print(type(sorted([3, 5, 2, 6, 2]))) ---> list type

        d[key] = d.get(key,[])+ [word]

    return list(d.values())

print(groupAnagrams(input))

