from sqlalchemy import create_engine , MetaData, Table, Column, Integer, String, insert, ForeignKey, Float

engine = create_engine('sqlite:///mydatabase.db',echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id",Integer, primary_key=True),
    Column('name', String,nullable=False),
    Column('age',Integer)

)

things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey(people.id))
)

meta.create_all(engine)

conn = engine.connect()


# select_statement = people.select().where(people.c.age > 30)
# result = conn.execute(select_statement)
# for row in result.fetchall():
#     print(row)

# to update

# update_statement = people.update().where(people.c.name == 'Mike').values(age=50)
# result = conn.execute(update_statement)
# conn.commit()

select_statement = people.select().where(people.c.age > 30)
result = conn.execute(select_statement)
for row in result.fetchall():
    print(row)
