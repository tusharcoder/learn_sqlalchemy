from sqlalchemy import Column, Table, MetaData, Integer, String, ForeignKey, create_engine

engine = create_engine("sqlite:///:memory:",echo=True)
metadata = MetaData()

users = Table("users",metadata,
Column("id",Integer, primary_key = True),
Column("name",String),
Column("full_name",String),
)

addresses = Table("addresses",metadata,
Column("id",Integer,primary_key=True),
Column("user",None,ForeignKey("users.id")),
Column("email_address",String,nullable=False),
)

metadata.create_all(engine) #method to create all the tables

#executing the insert statement

ins = users.insert().values(name = "foo",full_name = "foo bar") #targeting the users table while providing the values

con = engine.connect() #connecting to the database actually
con.execute(ins) #executing the insert statement
