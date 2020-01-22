import sys
import os

sys.path.append(os.getcwd() + '/source')

import unittest
from source.command_executor import CommandExecutor

COMMAND_CORRECT_CREATE_CANVAS = 'C 50 20'
COMMANDS_INCORRECT_CREATE_CANVAS = ['C 100 100',
                                    'C -1 0',
                                    'C q w',
                                    'C 1 2 3 4',
                                    'C 5',
                                    'C',]

COMMAND_CORRECT_DRAW_LINE = 'L 3 4 10 4'
COMMANDS_INCORRECT_DRAW_LINE = ['L 100 100 100 100',
                                'L 0 0 0 0',
                                'L q w e r',
                                'L 1 2 3',
                                'L 1 2 3 4 5 6 7 8',
                                'L',
                                'L 1 2 3 4',]

COMMAND_CORRECT_DRAW_RECTANGLE = 'R 1 6 11 16'
COMMANDS_INCORRECT_DRAW_RECTANGLE = ['R 0 0 0 0',
                                     'R -1 -40 5 10',
                                     'R q w e r',
                                     'R 1 2',
                                     'R 1 2 3 4 5',
                                     'R',]

COMMAND_CORRECT_FILL_AREA = 'B 5 4 o'
COMMANDS_INCORRECT_FILL_AREA = ['B o',
                                'B 1 2 3 4 o',
                                'B 1 o',
                                'B q w o',
                                'B -1 0 o',]

class TestCommandExecutor(unittest.TestCase):

    def setUp(self):
        self.command_executor = CommandExecutor()
        self.command_executor.execute_command(COMMAND_CORRECT_CREATE_CANVAS)

    def tearDown(self):
        pass

    def test_create_canvas(self):
        command_executor = CommandExecutor()

        for command in COMMANDS_INCORRECT_CREATE_CANVAS:
            flag = command_executor.execute_command(command)
            self.assertEqual(flag, False)

        # correct
        flag = command_executor.execute_command(COMMAND_CORRECT_CREATE_CANVAS)
        self.assertEqual(flag, True)

    def test_draw_line(self):
        for command in COMMANDS_INCORRECT_DRAW_LINE:
            flag = self.command_executor.execute_command(command)
            self.assertEqual(flag, False)

        # if canvas wasn't created
        command_executor = CommandExecutor()
        flag = command_executor.execute_command(COMMAND_CORRECT_DRAW_LINE)
        self.assertEqual(flag, False)

        # correct
        command_executor.execute_command(COMMAND_CORRECT_CREATE_CANVAS)
        flag = command_executor.execute_command(COMMAND_CORRECT_DRAW_LINE)
        self.assertEqual(flag, True)

    def test_draw_rectangle(self):
        for command in COMMANDS_INCORRECT_DRAW_RECTANGLE:
            flag = self.command_executor.execute_command(command)
            self.assertEqual(flag, False)

        # if canvas wasn't created
        command_executor = CommandExecutor()
        flag = command_executor.execute_command(COMMAND_CORRECT_DRAW_RECTANGLE)
        self.assertEqual(flag, False)

        # correct
        command_executor.execute_command(COMMAND_CORRECT_CREATE_CANVAS)
        flag = command_executor.execute_command(COMMAND_CORRECT_DRAW_RECTANGLE)
        self.assertEqual(flag, True)        

    def test_fill_area(self):
        for command in COMMANDS_INCORRECT_FILL_AREA:
            flag = self.command_executor.execute_command(command)
            self.assertEqual(flag, False)

        # hit to line
        self.command_executor.execute_command(COMMAND_CORRECT_DRAW_LINE)
        flag = self.command_executor.execute_command(COMMAND_CORRECT_FILL_AREA)
        self.assertEqual(flag, False)

        # if canvas wasn't created
        command_executor = CommandExecutor()
        flag = command_executor.execute_command(COMMAND_CORRECT_FILL_AREA)
        self.assertEqual(flag, False)

        # correct
        command_executor.execute_command(COMMAND_CORRECT_CREATE_CANVAS)
        flag = command_executor.execute_command(COMMAND_CORRECT_FILL_AREA)
        self.assertEqual(flag, True)

if __name__ == '__main__':
    unittest.main()
