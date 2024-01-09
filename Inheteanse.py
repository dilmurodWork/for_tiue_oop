from main import Post


class NewPost(Post):
    author: str
    likes: int
    dislikes: int

    def __init__(self, title, description, publish, author, likes, dislikes):
        super().__init__(title, description, int(likes / (likes + dislikes) * 10), publish)
        self.author = author

    def __str__(self):
        return super().__str__() + f'\nAuthor: {self.author}'


if __name__ == '__main__':
    np = NewPost('Breaking news', 'Munisa geted maried', True, 'Tom Holand', 5, 15)

    print(np)
