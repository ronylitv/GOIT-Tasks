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
    count = 0
    if not space_around:
        for i in spam_words:
            if text.find(i) != -1:
                count += 1
        if count:
            return True
        else:
            return False
    else:
        for i in spam_words:
            if text.find(i) != -1:
                count += 1
        if count:
            return True
        else:
            return False















