def longest_substring(st,template):
    s=st.lower()
    right = -1
    result = ''
    while right < len(s) - 1:
        res = ''
        right += 1  
        for i in template:            
            while i == s[right]:                
                res += i                
                if right < len(s)-1:
                    right += 1 
                else:
                    break                
        if len(result) < len(res):
            result = res     
    return(result)  


print(longest_substring('abbaaaaaaazacc', 'abca')=='abbaaaaaaa')
print(longest_substring('aaabbaabhtrabcddddb', 'abab') == 'aaabbaab')
print(longest_substring('AAABBAABhtrabcddddb', 'abab') ==  'aaabbaab')
