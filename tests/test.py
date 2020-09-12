
# TODO
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import random
import pandola as pd

values = [

    {
        'user_id': i + 1,
        'group_name': 'Group' + ('A' if (random.randint(0, 1) == 0) else 'B'),
        'user_name': 'user' + str(i + 1),
        'email': 'user' + str(i + 1) + '@xxx.co.jp'
    }

    for i in range(5)
]


df = pd.DataFrame(values)

print(df.loc[2])

print(df.to_dict('records'))

