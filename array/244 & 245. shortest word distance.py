# 244: create a class for the word list
class WordDistance():

    def __init__(self,words):
        # create a dictionary to store the pattern ---> word: index of the word

        self.dict = {}
        self.size = len(words)

        # a method to store the word smartly:
        # dictionary.get('key','default') returns the value of the key or if the key not exists,return default
        for idx,word in enumerate(words):
            # if the the vale corresponding to the key:'word' can not be found in the dictionary, return []+[idx]
            # if such value can be found, return the already existing index + new index
            self.dict[word] = self.dict.get(word,[])+[idx]

    def shortest(self,word1,word2):
        # attention: l1 and l2 are both already sorted lists.
        l1,l2 = self.dict[word1],self.dict[word2]
        result = self.size
        # a,b are pointers used in the two word list(maybe more than 1 index for a word)
        a,b = 0,0
        while a<len(l1) and b<len(l2):
            result = min(result,abs(l1[a]-l2[b]))
            # increase which ever is less
            if l1[a] < l2[b]:
                a+=1
            else:
                b+=1
        return result


# obj = WordDistance(['a','c','d','c','b','c','a','a','c','d','b'])
# print(obj.dict)
# print(obj.shortest('a','b'))


# 245: the two words maybe same
def getshortest(words,word1,word2):
    dict = {}
    for idx, word in enumerate(words):
        dict[word] = dict.get(word, []) + [idx]

    list1 = dict[word1]
    list2 = dict[word2]
    a, b = 0, 0
    result = len(words)
    # if the two words are same, just calculate the shortest distance one by one since it is sorted
    if list1 == list2:
        for i in range(1, len(list1)):
            result = min(result, abs(list1[i] - list1[i - 1]))
    else:
        while a < len(list1) and b < len(list2):
            result = min(result, abs(list1[a] - list2[b]))
            if list1[a] < list2[b]:
                a += 1
            else:
                b += 1
    return result
