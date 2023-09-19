def longestPalindrome(s: str) -> str:
    length = 0
    palindrome = ""

    for i in range(len(s)):
        l, r = i, i
        while l > -1 and r < len(s) and s[l] == s[r]:
            if len(s[l : r + 1]) > length:
                palindrome = s[l : r + 1]
                length = len(palindrome)
            l -= 1
            r += 1

        l, r = i, i + 1
        while l > -1 and r < len(s) and s[l] == s[r]:
            if len(s[l : r + 1]) > length:
                palindrome = s[l : r + 1]
                length = len(palindrome)
            l -= 1
            r += 1
    return palindrome


print(longestPalindrome("babad"))
