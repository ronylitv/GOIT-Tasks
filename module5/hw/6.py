import re


# def is_spam_words(text, spam_words, space_around=False):
#     new_list = []
#     if not space_around:
#         for i in spam_words:
#             result = re.search(i, text)
#             new_list.append(result)
#
#         if new_list:
#             return True
#         else:
#             return False
#     else:
#
def is_spam_words(text, spam_words, space_around=False):
    pass


# coincidence = False
# text = 'They have a little moron in his pants'
# spam_words = ['have', 'pan']
# new_list = []
# for i in spam_words:
#     result = re.findall(i + r'\w+', text)
#     if len(result) != len(i):
#         coincidence = False
#     else:
#         coincidence = True
#
#
# print(coincidence)

# print(is_spam_words('Moloh', 'loh'))
# def is_spam_words(text, spam_words, space_around=False):
#     if space_around:
#         result = re.findall(r'\s' + spam_words + '\s', text)
#         return result
#
#     else:
#         pass
#
#
# print(is_spam_words('Moloh loh kuka Rostyk', 'kuk', True))
