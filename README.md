Python Click House
===

![home](https://github.com/Naategh/PyCk/raw/master/logo.jpeg)

Python Click House is a simple project contains some useful and simple python scripts that may be helpful in penetration testing. 

## Requirements

Python 3.5 or later.

Installation
---

```bash
git clone git@github.com:Wanguy/pyClickHouse.git
cd pyClickHouse
pip3 install --user
```

Usage
---

```python
import ck
from ck import iteration
import pandas as pd

# start a local ClickHouse server
# the default data directory is ~/.ck_data
session = ck.LocalSession()
# use PassiveSession if you just want a ClickHouse client
# session = ck.PassiveSession(host='192.168.xxx.xxx')

# ping the server
# it will return True
print(session.ping())

# make a simple query
# the result will be returned as bytes
print(session.query('select 1'))

# pretty print
print(session.query('select 1 as x, 2 as y format Pretty').decode())

# create a table
session.query('create table test (x Int32) engine=Memory')

# read data from a file
session.query(
    'insert into test format CSV',
    gen_in=iteration.file_in('1.csv')
)

# write data to a file
session.query(
    'select * from test format CSV',
    gen_out=iteration.file_out('2.csv')
)
```

## License

This project is licensed under the [MIT LICENSE](https://github.com/Wanguy/pyClickHouse/blob/master/LICENSE). But you can do what you want with it yet, there is no problem.