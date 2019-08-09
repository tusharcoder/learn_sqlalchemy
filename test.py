from sqlalchemy import Column, Table, MetaData, Integer, String, ForeignKey, create_engine

engine = create_engine("sqlite:///:memory:",echo=True) #using the inmemory sql database, also echo for outputing the raw sql statements
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

ins = users.insert()#targeting the users table while providing the values

con = engine.connect() #connecting to the database actually
con.execute(ins, [
{"name" : "foo","full_name":"foo bar"},
{"name" : "foo 1","full_name":"foo bar 1"},
{"name" : "foo 2","full_name":"foo bar 2"},
{"name" : "foo 3","full_name":"foo bar 3"},
{"name" : "foo 4","full_name":"foo bar 4"}
]) #executing the bulk insert using multiple data dictionaries in the execute statement
