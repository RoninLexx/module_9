def all_variants(text):
    n = len(text)
    for k in range(n):
        for j in range(k + 1, n + 1):
            yield text[k:j]



a = all_variants("abc")
for i in a:
    print(i)

