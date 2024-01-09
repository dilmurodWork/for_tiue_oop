from datetime import datetime


class Post:
    title: str
    description: str
    rate: int
    publish: bool
    created: datetime

    def __init__(self, title, desc, rate, publish):
        self.title = title
        self.description = desc
        self.rate = rate
        self.publish = publish
        self.created = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"{self.description}\n"
                f"Rate: {self.rate}\t\t Created: {self.created.ctime()}")


if __name__ == '__main__':

    p = Post('Tashkent v tope', 'Tashkent vishel na 2 mesto po zagreneniye vozduxa', 4, True)

    print(p)
