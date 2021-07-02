import re

text = 'Egor "flamie" Vasyliev left NAVI team after 10 years playing for them'
spam_words = ['amie', 'eft', 'them']
# coincidence = False
# space_around = True
# count = 0
# if not space_around:
#     for i in spam_words:
#         if i in text:
#             count += 1
#     if count:
#         coincidence = True
#     else:
#         coincidence = False
# else:
#     for i in spam_words:
#         result = re.findall(fr'\W{i}\W|\W{i}\W?', text)
#         if result:
#             count += 1
#     if count:
#         coincidence = True
#     else:
#         coincidence = False
# print(coincidence)


def is_spam_words(text, spam_words, space_around=False):

    count = 0
    if not space_around:
        for i in spam_words:
            if i in text:
                count += 1
        if count:
            coincidence = True
        else:
            coincidence = False
    else:
        for i in spam_words:
            result = re.findall(fr'\W{i}\W|\W{i}\W?', text)
            if result:
                count += 1
        if count:
            coincidence = True
        else:
            coincidence = False
    return coincidence

