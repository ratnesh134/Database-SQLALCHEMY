from sqlalchemy import create_engine , MetaData, Table, Column, Integer, String, insert

engine = create_engine('sqlite:///mydatabase.db',echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id",Integer, primary_key=True),
    Column('name', String,nullable=False),
    Column('age',Integer)

)

meta.create_all(engine)

conn = engine.connect()

insert_statement = insert(people).values(name='Jane',age=35)
result = conn.execute(insert_statement)
conn.commit()

