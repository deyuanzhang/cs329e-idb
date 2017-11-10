import os
import unittest
from models import Base, Pokemon, Type, Move, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Pokemon(name = "pikachu", type = "electric", move = "bash", attack = "100", defense = "50", spdefense = "50", specialattack = "50", image = "www.pikachu.com")
        session.add(s)
        session.commit()


        r = session.query(Pokemon).filter_by(name = "pikachu").one()
        self.assertEqual(str(r.type), 'electric')

        session.query(Pokemon).filter_by(name = "pikachu").delete()
        session.commit()

    def test_source_insert_2(self):
        s = Pokemon(name = "william", type = "unknown", move = "rest", attack = "100", defense = "100", spdefense = "100", specialattack = "100", image = "www.aol.com")
        session.add(s)
        session.commit()


        r = session.query(Pokemon).filter_by(name = "william").one()
        self.assertEqual(str(r.spdefense), '100')

        session.query(Pokemon).filter_by(name = "william").delete()
        session.commit()

    def test_source_insert_3(self):
        s = Pokemon(name = "deyuan", type = "str8_fire", move = "ancient_power", attack = "101", defense = "101", spdefense = "101", specialattack = "101", image = "www.google.com")
        session.add(s)
        session.commit()


        r = session.query(Pokemon).filter_by(name = "deyuan").one()
        self.assertEqual(str(r.image), 'www.google.com')

        session.query(Pokemon).filter_by(name = "deyuan").delete()
        session.commit()

    def test_source_insert_4(self):
        s = Move(name = "scratch", power = "40", accuracy = "100", type ="normal", pp = "35" )
        session.add(s)
        session.commit()


        r = session.query(Move).filter_by(name = "scratch").one()
        self.assertEqual(str(r.name), 'scratch')

        session.query(Move).filter_by(name = 'scratch').delete()
        session.commit()

    def test_source_insert_5(self):
        s = Move(name = "rest", power = "", accuracy = "", type = "psychic", pp = "10")
        session.add(s)
        session.commit()


        r = session.query(Move).filter_by(name = "rest").one()
        self.assertEqual(str(r.name), 'rest')

        session.query(Move).filter_by(name = "rest").delete()
        session.commit()

    def test_source_insert_6(self):
        s = Move(name = 'ice-punch', power = "75", accuracy = "100", type = "ice", pp = "15")
        session.add(s)
        session.commit()


        r = session.query(Move).filter_by(name = 'ice-punch').one()
        self.assertEqual(str(r.name), 'ice-punch')

        session.query(Move).filter_by(name = 'ice-punch').delete()
        session.commit()

    def test_source_insert_7(self):
        s = Type(name='ghost', half_to = 'dark', half_from = 'poison,bug', double_to = 'ghost,psychic', double_from = 'ghost,dark')
        session.add(s)
        session.commit()


        r = session.query(Type).filter_by(name = 'ghost').one()
        self.assertEqual(str(r.name), 'ghost')

        session.query(Type).filter_by(name = 'ghost').delete()
        session.commit()

    def test_source_insert_8(self):
        s = Type(name ='steel', half_to ='steel,fire,water,electric', half_from = 'normal,flying,rock,bug,steel,grass,psychic,ice,dragon,fairy', double_to ='rock,ice,fairy', double_from ='fighting,ground,fire')
        session.add(s)
        session.commit()


        r = session.query(Type).filter_by(name = 'steel').one()
        self.assertEqual(str(r.name), 'steel')

        session.query(Type).filter_by(name = 'steel').delete()
        session.commit()

    def test_source_insert_9(self):
        s = Type(name='ice', half_to = 'steel,fire,water,ice', half_from='ice',double_to='flying,ground,grass,dragon',double_from='fighting,rock,steel,fire')
        session.add(s)
        session.commit()


        r = session.query(Type).filter_by(name = 'ice').one()
        self.assertEqual(str(r.name), 'ice')

        session.query(Type).filter_by(name = 'ice').delete()
        session.commit()


if __name__ == '__main__':
	unittest.main()
