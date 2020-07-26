class Solution:
    def toLowerCase(self, str: str) -> str:
        new_str = ''
        for char in str:
            if 'A'<= char <='Z':
                new_str += chr(ord(char)+32)
            else:new_str += char
        return new_str