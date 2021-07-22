news = []


def add_news():
    title = input('Title: ')
    body = input('Body: ')
    news.append({'title': title,
                 'body': body})

def read_news():
    print(news)


def work():
    for i in range(3):
        add_news()
    read_news()

work()