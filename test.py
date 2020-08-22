from core.DataFrame import DataFrame


class TestSample:
    def __init__(self, user_id, group_name, user_name, email):
        self.user_id = user_id
        self.group_name = group_name
        self.user_name = user_name
        self.email = email


values1 = [
    {
        'user_id': 1,
        'group_name': 'GroupA',
        'user_name': 'user1',
        'email': 'user1@xxx.co.jp'
    },
    {
        'user_id': 2,
        'group_name': 'GroupB',
        'user_name': 'user2',
        'email': 'user2@xxx.co.jp'
    },
    {
        'user_id': 3,
        'group_name': 'GroupB',
        'user_name': 'user3',
        'email': 'user3@xxx.co.jp'
    },
    {
        'user_id': 4,
        'group_name': 'GroupA',
        'user_name': 'user4',
        'email': 'user4@xxx.co.jp'
    },
    {
        'user_id': 5,
        'group_name': 'GroupA',
        'user_name': 'user5',
        'email': 'user5@xxx.co.jp'
    }
]

values2 = [
    TestSample(1, 'GroupA', 'user1', 'user1@xxx.co.jp'),
    TestSample(2, 'GroupB', 'user2', 'user2@xxx.co.jp'),
    TestSample(3, 'GroupB', 'user3', 'user3@xxx.co.jp'),
    TestSample(4, 'GroupA', 'user4', 'user4@xxx.co.jp'),
    TestSample(5, 'GroupA', 'user5', 'user5@xxx.co.jp')
]

df = DataFrame(values2)
print('df生成完了')
print(df)

target = ['group_name']
print(df[target])
