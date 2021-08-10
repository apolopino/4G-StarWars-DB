import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(999), nullable=False)
    favorites = relationship("Favs")

class Planets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    rotation_period = Column(Integer, nullable=False)
    gravity = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    population = Column(Integer, nullable=False)
    inhabitants = relationship("Characters")

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    homeworld = Column(String, ForeignKey('planets.id'))

class Favs(Base):
    __tablename__= 'favorites'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    characters = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    planets = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    user = relationship(User)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')