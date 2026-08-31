class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        groups = {}
        for string in strs:
            profile = {}
            for char in string:
                profile[char] = profile.get(char, 0) + 1
            key = frozenset(profile.items())
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        print(groups)

        output = []
        for key, value in groups.items():
            output.append(value)
        print(output)
        return output


# groups = {}

# for each word:
#     key = representation_of_the_word

#     if key doesn't exist:
#         create an empty group

#     add the word to that group

# return all groups

