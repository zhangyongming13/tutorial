# coding=utf-8


import hashlib


db1 = {  # 用户名以及对应的密码（密码经过MD5计算才存储）
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(usr, password):
    hash_password = hashlib.md5()
    hash_password.update(password.encode('utf-8'))  # 对输入的密码进行hash
    if db1[usr] == hash_password.hexdigest():  # 判断是否正确
        print('login success!')
    else:
        print('wrong password!')


def cal_md5(password):  # 计算加盐之后hash值
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def add_salt(username, password):  # 进行加盐操作
    result = password + username + 'python'
    return cal_md5(result)


db2 = {  # 创建相应的dict
    'michael': add_salt('michael', '123456'),
    'bob': add_salt('bob', 'abc999'),
    'alice': add_salt('alice', 'alice2008')
}


def login_salt(user, password):
    if db2[user] == add_salt(user, password):
        print('login success!')
    else:
        print('login fail!')


login_salt('michael', '123456')
login_salt('bob', 'abc999')
login_salt('alice', 'alice2008')
login_salt('michael', '1234567')
login_salt('bob', '123456')
login_salt('alice', 'Alice2008')

login('michael', '123456')
login('bob', 'abc999')
login('alice', 'alice2008')
login('michael', '1234567')
login('bob', '123456')
login('alice', 'Alice2008')
