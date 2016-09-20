from app.models import User

from www import orm


def test():
    yield from orm.create_pool(user='root', password='123456', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


if __name__ == '__main__':
    for x in test():
        print(x)
