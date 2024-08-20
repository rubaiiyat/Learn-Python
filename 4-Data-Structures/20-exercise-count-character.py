sentence = "This is common interview question"
char_cnt = {}
for char in sentence:
    if char in char_cnt:
        char_cnt[char] += 1
    else:
        char_cnt[char] = 1


most_freequency = sorted(char_cnt.items(), key=lambda kv: kv[1], reverse=True)
print(most_freequency[0])
