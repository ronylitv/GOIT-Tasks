import re
# def is_spam_words(text, spam_words, space_around=False):
#     word_list = []
#     if space_around:
#         for i in spam_words:
#             result = re.findall(r'\W' + i + r'\W?', text)
#             word_list.extend(result)
#         if word_list:
#             return True
#         else:
#             return False
#
#     else:
#         for i in spam_words:
#             result = re.findall(i, text)
#             word_list.extend(result)
#         if word_list:
#             return True
#         else:
#             return False
#


def is_spam_words(text, spam_words, space_around=False):
    pass

text = 'Egor "flamie" Vasyliev left NAVI team after 10 years playing for them'
spam_words = ['maie', 'lef', 'them']
count = 0
coincidence = False
for i in spam_words:
    if i in text:
        count += 1

if count:
    coincidence = True
else:
    coincidence = False

print(count, coincidence, end=' ')
















