with open('story.txt','r') as f:
    story= f.read()
    
words=set()
start_word = -1
target_start = '<'
target_end = '>'

for i,char in enumerate(story):
   if char == target_start:
       start_word = i

   if char == target_end and start_word != -1:
       word = story[start_word: i+1]
       words.add(word)
       start_word = -1

answer = {}

for word in words:
    ans = input(f'enter a word for {word}: ')
    answer[word] = ans

for word in words:
    story = story.replace(word,answer[word])

print(story)
