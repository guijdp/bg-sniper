import random

from sqlalchemy.orm import sessionmaker

import conn

Session = sessionmaker(bind=conn.engine)
session = Session()

for t in range(10, 20):
    tr = conn.Boardgame(name="SQUASH")
    session.add(tr)

session.commit()
