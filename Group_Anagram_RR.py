########## SOLUTION 1 #############################

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
      # using hashmap to store the set() of each words if same then store other number as values 
        temp = defaultdict(list)
        # e.g if cat tac is here so there set  == [c,a,t] thus we store {[c,a,t]:["cat","tac"]} 
        # also keep check of the length otherwise set("tacc") = [c,a,t] and set(tac) == [c,a,t] but they are not anagram 
        for element in strs:
            temp[str(sorted(element))].append(element)
        res = (list(temp.values()))
        return res
