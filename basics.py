from sqlalchemy import create_engine , MetaData, Table, Column, Integer, String, insert, ForeignKey, Float

engine = create_engine('sqlite:///mydatabase.db',echo=True)

meta = MetaData()


conn = engine.connect()


people = Table(
    "people",
    meta,
    Column('id',Integer, primary_key=True),
    Column('name', String,nullable=False),
    Column('age',Integer)

)

things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey(people.c.id))
)

meta.create_all(engine)

# select_statement = people.select().where(people.c.age > 30)
# result = conn.execute(select_statement)
# for row in result.fetchall():
#     print(row)

# to update

# update_statement = people.update().where(people.c.name == 'Mike').values(age=50)
# result = conn.execute(update_statement)
# conn.commit()

# select_statement = people.select().where(people.c.age > 30)
# result = conn.execute(select_statement)
# for row in result.fetchall():
#     print(row)


insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 35},
    {'name': 'Anna', 'age': 38},
    {'name': 'John', 'age': 50},
    {'name': 'Clara', 'age': 42},
])

insert_things = things.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800.50},
    {'owner': 2, 'description': 'Mouse', 'value': 50.50},
    {'owner': 3, 'description': 'Keyboard', 'value': 100.50},
    {'owner': 4, 'description': 'Book', 'value': 10.50},
    {'owner': 5, 'description': 'Speakers', 'value': 80.50},
])

conn.execute(insert_people)
conn.commit()
conn.execute(insert_things)
conn.commit()
