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


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
Base = declarative_base()

class Pokemon(Base):
	__tablename__ = 'pokemonname'
	
	name = Column(String(20), nullable = False, primary_key = True)
	type = Column(String(20), nullable = False)
	move = Column(String(5000), nullable = False)
	attack = Column(Integer, nullable = False)
	defense = Column(Integer, nullable = False)
	spdefense = Column(Integer, nullable = False)
	specialattack = Column(Integer, nullable = False)
	image = Column(String(500), nullable = False)

class Move(Base):
	__tablename__ = 'move'
	
	name = Column(String(30), nullable = False, primary_key = True)
	power = Column(Integer)
	accuracy = Column(Integer)
	type = Column(String(30))
	pp = Column(Integer)

class Type(Base):
	__tablename__ = 'type'
	
	name = Column(String(8), nullable = False, primary_key = True)
	half_to = Column(String(63))
	half_from = Column(String(63))
	double_to = Column(String(63))
	double_from = Column(String(63))
	

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:password@localhost/newdb')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
