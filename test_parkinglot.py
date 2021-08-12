import unittest
from parkinglot import parkinglot
class TestParkingLot(unittest.TestCase):
	

	def test_create_parking_lot(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)		
		self.assertEqual(6,res)

	def test_park(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		self.assertNotEqual(-1,res)	
	def test_leave(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.leave(1)
		self.assertEqual(True,res)

	def test_getRegNoFromColor(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-1235","White")
		regnos = parkingLot.getRegNoFromColor("White")
		self.assertIn("KA-01-HH-1234",regnos)
		self.assertIn("KA-01-HH-1234",regnos)
	
	def test_getSlotNoFromRegNo(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.getSlotNoFromRegNo("KA-01-HH-1234")
		self.assertEqual(1,res)

	def test_getslotNoFromColor(self):
		parkingLot = parkinglot()
		res = parkingLot.createparkinglot(6)
		res = parkingLot.park("KA-01-HH-1234","White")
		res = parkingLot.park("KA-01-HH-1235","White")
		slotnos = parkingLot.getslotNoFromColor("White")
		self.assertIn(str(1),slotnos)
		self.assertIn(str(2),slotnos)
	

if __name__ == '__main__':
	unittest.main()