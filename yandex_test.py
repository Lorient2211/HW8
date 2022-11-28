import yadisk
y = yadisk.YaDisk(token='')
print(y.check_token())
y.mkdir('/netology')
y.upload("test.txt",'/netology/test.txt')