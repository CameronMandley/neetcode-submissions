class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or s == "":
            return False
        elif len(s) == 1:
            return True
        else:
            i, j = 0, len(s) - 1
            while i <= j:
                if not (s[i].isalpha() or s[i].isnumeric()) or not (s[j].isalpha() or s[j].isnumeric()):
                    if not (s[i].isalpha() or s[i].isnumeric()):
                        i += 1
                    if not (s[j].isalpha() or s[j].isnumeric()):
                        j -= 1
                    continue
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        