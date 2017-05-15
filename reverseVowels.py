### Reverse only vowels in a string 
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    if not s: return s 

    length = len(s)
    vowel = 'aeiouAEIOU'
    result = ''
    start, end = 0, length-1 
    while start < length: 
        if s[start] not in vowel: 
            result += s[start]
            start += 1 
        else: 
            if s[end] in vowel: 
                result += s[end]
                start += 1 
            end -= 1 
    return result
