import os
import unittest
from models import Base, Book, Author, Publisher, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Book(id='1', title = 'TESTONE')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '1').one()
        self.assertEqual(str(r.id), '1')

        session.query(Book).filter_by(id = '1').delete()
        session.commit()

    def test_source_insert_2(self):
        s = Book(id='2', title = 'TESTTWO')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')

        session.query(Book).filter_by(id = '2').delete()
        session.commit()

    def test_source_insert_3(self):
        s = Type(name = "scratch", power = "40", accuracy = "100", type ="normal", pp = "35" )
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(name = "scratch").one()
        self.assertEqual(str(r.id), 'scratch')

        session.query(Book).filter_by(name = 'scratch').delete()
        session.commit()

    def test_source_insert_4(self):
        s = Type(name = "scratch", power = "40", accuracy = "100", type ="normal", pp = "35" )
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(name = "scratch").one()
        self.assertEqual(str(r.id), 'scratch')

        session.query(Book).filter_by(name = 'scratch').delete()
        session.commit()

    def test_source_insert_5(self):
        s = Type(name = "rest", power = "", accuracy = "", type = "psychic", pp = "10")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = "rest").one()
        self.assertEqual(str(r.id), 'rest')

        session.query(Author).filter_by(name = "rest").delete()
        session.commit()

    def test_source_insert_6(self):
        s = Type(name = 'ice-punch', power = "75", accuracy = "100", type = "ice", pp = "15")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = 'ice-punch').one()
        self.assertEqual(str(r.id), 'ice-punch')

        session.query(Author).filter_by(name = 'ice-punch').delete()
        session.commit()

    def test_source_insert_7(self):
        s = Type(name='ghost', half_to = 'dark', half_from = 'poison,bug', double_to = 'ghost,psychic', double_from = 'ghost,dark')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'ghost').one()
        self.assertEqual(str(r.id), 'ghost')

        session.query(Publisher).filter_by(name = 'ghost').delete()
        session.commit()

    def test_source_insert_8(self):
        s = Type(name ='steel', half_to ='steel,fire,water,electric', half_from = 'normal,flying,rock,bug,steel,grass,psychic,ice,dragon,fairy', double_to ='rock,ice,fairy', double_from ='fighting,ground,fire')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'steel').one()
        self.assertEqual(str(r.id), 'steel')

        session.query(Publisher).filter_by(name = 'steel').delete()
        session.commit()

    def test_source_insert_9(self):
        s = Type(name='ice', half_to = 'steel,fire,water,ice', half_from='ice',double_to='flying,ground,grass,dragon',double_from='fighting,rock,steel,fire')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'ice').one()
        self.assertEqual(str(r.id), 'ice')

        session.query(Publisher).filter_by(name = 'ice').delete()
        session.commit()


if __name__ == '__main__':
	unittest.main()
