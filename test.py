from core.DataFrame import DataFrame
import random


values = [

    {
        'user_id': i + 1,
        'group_name': 'Group' + ('A' if (random.randint(0, 1) == 0) else 'B'),
        'user_name': 'user' + str(i + 1),
        'email': 'user' + str(i + 1) + '@xxx.co.jp'
    }

    for i in range(5)
]


df = DataFrame(values)
print(df)

target = ['group_name']
print(df[target])

print(df['user_name'] + df['email'])
