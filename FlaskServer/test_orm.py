'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_orm.py
@time: 2021/5/14 11:09
@Email: Warron.Wang
'''


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = ''
user = ''
password = ''
db = 'hogwarts_python'
charset = 'utf8mb4'

Base = declarative_base()

class User(Base):
    __tablename__ = 'warron_user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

def test_orm():
    engine = create_engine(
      'mysql+pymysql://{user}:{password}@{host}/{db}'.format(
          host=host, db=db, user=user, password=password),
        echo=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # 数据的插入
    u1 = User(
        username="warron02",
        password="password02",
        email="warron02@admin.com"
    )
    session.add(u1)
    session.commit()

    # 查询
    u2 = session.query(User).filter_by(username="warron02").first()
    print(u2.username)
    assert u2.username == u1.username