"""
L for lower case letter a-z
U for upper case letter A-Z
D for digits 0-9 
Sample pattern_formats: "LLU", "DLD", "DLLULLD"
Example: 
pattern_format: "LUD"
search_string: "zZ1_example_aA1bB2c" would return "aA1bB2"
"""

class Solution():
  def findLongestRepeatingPattern(self, pattern, string):
    strLen = len(string) 
    patternLen = len(pattern)
    i = end = 0 
    largest = count = 0 
    while (i < strLen):
      flag = self.checkMatch(pattern, string, i, strLen)
      if (flag == True): 
          count += patternLen
          i += patternLen-1
      if (count > largest):
        largest = count 
        end = i 
      if (flag == False): 
        count = 0 
      i += 1 
    start = end - largest + 1 
    
    if (largest == 0): 
      return 'pattern not found'
    else: 
      return string[start:end+1] 
    
  def checkMatch(self, pattern, string, stringIndex, strLen):
    match = True 
    iterStr = stringIndex
    for i in range(len(pattern)):
      if (iterStr < strLen): 
        if ((pattern[i] == 'L' and string[iterStr].islower()) or (pattern[i] == 'U' and string[iterStr].isupper()) or (pattern[i] == 'D' and string[iterStr].isdigit())):
          match = match and True 
        else: 
          match = False
          break 
        iterStr += 1 
      else: 
        match = False 
        break 
    return match 
    
## For testing purpose 
"""
a = Solution()
b = 'LUDD'
#c = 'cC33'
c = 'aAzZ1_example_aA1bB2___aA2bB4aA5bB2'
"""
print(a.findLongestRepeatingPattern(b,c))
