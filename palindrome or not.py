# palindrome or not
s = "A man, a plan, a canal: Panama"
st = ""
for ch in s :
    if ch.isalnum():
        st+=(ch.lower())

print(True if st[::-1]== st else False)
