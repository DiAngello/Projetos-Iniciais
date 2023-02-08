from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[31m-=\033[m'* 14)
print(emoji.emojize(':fireworks:', use_aliases=True))
