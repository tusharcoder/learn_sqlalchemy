from sqlalchemy import Column, Table, MetaData, Integer, String, ForeignKey, create_engine
from sqlalchemy import select

engine = create_engine("sqlite:///:memory:",echo=True) #using the inmemory sql database, also echo for outputing the raw sql statements
metadata = MetaData()

users = Table("users",metadata,
Column("id",Integer, primary_key = True),
Column("name",String),
Column("full_name",String),
)

addresses = Table("addresses",metadata,
Column("id",Integer,primary_key=True),
Column("user_id",None,ForeignKey("users.id")),
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

address_ins = addresses.insert()
con.execute(address_ins, [
{"user_id" : 1,"email_address":"foo1@somewhere.com"},

{"user_id" : 1,"email_address":"foo1email2@somewhere.com"},

{"user_id" : 2,"email_address":"foo2email1@somewhere.com"},

{"user_id" : 3,"email_address":"foo3email1@somewhere.com"},

{"user_id" : 4,"email_address":"foo4email1@somewhere.com"},

{"user_id" : 5,"email_address":"foo5email1@somewhere.com"},

]) #executing the bulk insert using multiple data dictionaries in the execute statement


#select statements

select_st = select([users.c.name,users.c.full_name]) #specify the columns using the c attribute of the table object where columns of the table are the attributes of the c object
result = con.execute(select_st)
for row in result:
    print("name: %s, full_name: %s"% (row["name"],row["full_name"])) #print the values in the row by the named columns we can also use the indexes like

result.close() #its good to close the result to discard the pending rows

result = con.execute(select_st)
for row in result:
    print("name: %s, full_name: %s"% (row[0], row[1])) # print the rows using the indexes

result.close()

#select statement with join
select_st = select([users.c.name, users.c.full_name, addresses.c.user_id, addresses.c.email_address]).where(users.c.id==addresses.c.user_id) #here without the where clause will give the Cartesian product of the users with that of the addresses.
#selecting with the join
result = con.execute(select_st)
for row in result:
    print("name: %s, full_name: %s, user_id: %s, email_address: %s"% (row["name"], row["full_name"], row["user_id"], row["email_address"])) # print the rows using the indexes

result.close() #closed the result



