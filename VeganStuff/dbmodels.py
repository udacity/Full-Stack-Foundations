import os
import sys
from sqlalchemy import Column, ForeignKey, NVARCHAR, INTEGER, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# TODO: Add picture path and add CRUD functionality, refer to those videos!


class Category(Base):
	__tablename__ = 'category'
	
	id = Column(INTEGER, primary_key=True, nullable=False)
	name = Column(NVARCHAR, nullable=False)
	description = Column(NVARCHAR, nullable=False)
	
	@property
	def serialize(self):
		"""Return object in easily serializable format"""
		return {
			'name':        self.name,
			'description': self.description,
			'Unique id':   self.id
		}


class Manufacturer(Base):
	__tablename__ = 'manufacturer'
	name = Column(NVARCHAR, primary_key=True, nullable=False)
	description = Column(NVARCHAR, nullable=False)
	
	@property
	def serialize(self):
		"""Return object in easily serializable format"""
		return {
			'name and unique id': self.name,
			'description':        self.description,
		}
	
	
class Shop(Base):
	__tablename__ = 'shop'
	id = Column(INTEGER, primary_key=True, nullable=False)
	name = Column(NVARCHAR, nullable=False)
	description = Column(NVARCHAR, nullable=False)
	
	def serialize(self):
		"""Return object in easily serializable format"""
		return {
			'name':        self.name,
			'description': self.description,
		}
	
	
class Item(Base):
	__tablename__ = 'item'
	id = Column(INTEGER, primary_key=True, nullable=False)
	type = Column(BOOLEAN, nullable=False)
	name = Column(NVARCHAR, nullable=False)
	category = Column(INTEGER, ForeignKey('category.id'), nullable=False)
	accidentally_vegan = Column(BOOLEAN, nullable=False)
	ingredients = Column(NVARCHAR)
	m_id = Column(NVARCHAR, ForeignKey('manufacturer.name'), nullable=False)
	s_id = Column(INTEGER, ForeignKey('shop.id'), nullable=False)
	# Make relationships so the tables know each other or something like that.
	Category_id = relationship(Category)
	Manufacturer_id = relationship(Manufacturer)
	Shop_id = relationship(Shop)
	
	@property
	def serialize(self):
		"""Return object in easily serializable format"""
		return {
			'name':            self.name,
			'category':        self.category,
			'description':     self.description,
			'shop id':         self.s_id,
			'manufacturer': self.m_id,
			'unique id':       self.id,
		}

# Make the database
engine = create_engine('sqlite:///models.db')

Base.metadata.create_all(engine)
