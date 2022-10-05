import unittest

from software_engineer.robot import robot


class TestDo(unittest.TestCase):

    def test_head_south(self):
        pos, heading = robot.exec_command("RRW100")
        self.assertEqual([0, -100], pos)
        self.assertEqual(180, heading)

    def test_head_east(self):
        pos, heading = robot.exec_command("RW100")
        self.assertEqual([100, 0], pos)
        self.assertEqual(90, heading)

    def test_move_with_back_direction(self):
        pos, heading = robot.exec_command("RB100")
        self.assertEqual([-100, 0], pos)
        self.assertEqual(90, heading)


if __name__ == '__main__':
    unittest.main()
