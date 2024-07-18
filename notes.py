def easy_duplicate_check():
    st = set(nums)
    return len(st) != len(nums)

def access_map():
    res = seen.get(num, 0)

# Sorting is always a solution if there

def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())