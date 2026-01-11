def is_palindrome(text:str) -> bool:
    text_clear = ''
    for char in text:
        if char.isalnum():
            text_clear += char.lower()

    rev_text_clear = ''
    for char in text_clear:
        rev_text_clear = char+rev_text_clear

    return text_clear == rev_text_clear

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
