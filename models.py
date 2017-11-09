# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base 

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
from sqlalchemy import create_engine


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
Base = declarative_base()

class Pokemon(Base):
	__tablename__ = 'pokemon5'
	
	name = Column(String(15), nullable = False, primary_key = True)
	type = Column(String(10000), nullable = False)
	move = Column(String(10000), nullable = False)
	attack = Column(String(15), nullable = False)
	defense = Column(String(15), nullable = False)
	spdefense = Column(String(15), nullable = False)
	specialattack = Column(String(15), nullable = False)
	image = Column(String(150), nullable = False)

        

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:FreeWilly@localhost/pokemon')
engine = create_engine(SQLALCHEMY_DATABASE_URI)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
