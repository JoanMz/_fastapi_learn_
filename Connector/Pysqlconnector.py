from decouple import config
from sqlalchemy import Column, Integer, Float, String, Datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/config("DB_DATABASE")")
base = declarative_base()

class Users(base):
    __tablename__ = config("DB_TABLE1")
    id = Column(Integer(), Primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    password = Column(Integer())

    def __str__(self):
        self.username


class Orders(base):
    __tablename__ = config("DB_TABLE2")
    id = Column(Integer(), Primary_key=True)
    user_id = Column(Integer(), ForeignKey("Users.id"))
    order = Column()
    order_price = Column()
    
    def __str__(self):
        self.username
    
class Products(base):
    __tablename__ = config("DB_TABLE3")
    id = Column(Integer(), Primary_key=True)
    product = Column(String(50), nullable=False)
    product_desc = Column(String(200))
    product_price =Column(Integer(), nullable=False)

    def __str__(self):
        self.username

Session = sessionmaker(engine)
session = Session()



if __name__ = "__main__":
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
