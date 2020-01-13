fp = open('composition.txt')

word_freq = {}

for line in fp:
    words = line.strip().split()#放有单词的数组
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

freq_word = []
for word , freq in word_freq.items():
    freq_word.append((freq,word))

freq_word.sort(reverse = True)#sort和sorted内建函数会优先排序第一个元素,也即现在的频率
print(freq_word)

for freq , word in freq_word[:10]:
    print(word)

fp.close()

d1 = {'zhang':123 , 'wang':456 , 'li':123 , 'zhao':456}
d2 = {}

for name , room in d1.items():
    if room in d2:
        d2[room].append(name)
    else:
        d2[room] = [name]#这样增加信新的键值对

print(d2)