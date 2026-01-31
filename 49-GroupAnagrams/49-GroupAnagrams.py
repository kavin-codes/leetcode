from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort each string to use as a key
        key = ''.join(sorted(s))
        anagram_map[key].append(s)
        
    # Return just the grouped lists
    return list(anagram_map.values())
