"""Module, which cotain class CommandExecutor
and other constants for execute commands and check valid."""

from canvas import Canvas
import logging

COMMAND_CREATE_CANVAS = 'C'
COMMAND_DRAW_LINE = 'L'
COMMAND_DRAW_RECTANGLE = 'R'
COMMAND_BUCKET_FILL = 'B'

CANVAS_MAX_SIZE = 50 * 20  # by empirical :)
# size of canvas mustn't be a huge, because standart python call stack is small

LOG_MSG_NOT_POSITIVE_ARGS = 'incorrect value of arguments (not positive) - command: '
LOG_MSG_RECREATE_CANVAS = 'recreation of canvas - command: '
LOG_MSG_CANVAS_BIG = 'size of canvas is too big - command: '
LOG_MSG_NOT_HOR_VERT_LINE = 'line is not vertical or horizontal- command: '
LOG_MSG_CANVAS_WASNT_CREATED = 'canvas was not created - command: '
LOG_MSG_FILL_HIT_TO_LINE = 'incorrect coordinate(s) - hit to line - command: '
LOG_MSG_UNKNOWN_CMD = 'unknown command - command: '
LOG_MSG_INCORR_TYPE_ARGS = 'incorrect type of argument(s) - command: '
LOG_MSG_INCORR_VALUE_ARGS = 'incorrect value(s) of coordinates - command: '


class CommandExecutor:
    """Class, which allows parse and execute commands."""

    def __init__(self):
        self.canvas = None

    def _positive_check(self, lst: list) -> bool:
        for elem in lst:
            if int(elem) <= 0:
                return False
        return True

    def _exec_create_canvas(self, command_components: str) -> bool:
        if self.canvas:
            logging.warning(LOG_MSG_RECREATE_CANVAS + f"'{' '.join(command_components)}'")
            return False
        else:
            if not self._positive_check(command_components[1:]):
                logging.warning(LOG_MSG_NOT_POSITIVE_ARGS + f"'{' '.join(command_components)}'")
                return False
            elif int(command_components[1]) * int(command_components[2]) > CANVAS_MAX_SIZE:
                logging.warning(LOG_MSG_CANVAS_BIG + f"'{' '.join(command_components)}'")
                return False
            else:
                self.canvas = Canvas(width=int(command_components[1]), heigth=int(command_components[2]))
                return True

    def _exec_draw_line(self, command_components: str) -> bool:
        if not self.canvas.draw_line(x1=int(command_components[1]),
                                     y1=int(command_components[2]),
                                     x2=int(command_components[3]),
                                     y2=int(command_components[4])):
            logging.warning(LOG_MSG_NOT_HOR_VERT_LINE + f"'{' '.join(command_components)}'")
            return False
        return True

    def _exec_draw_reactangle(self, command_components: str) -> bool:
        if not self.canvas.draw_rectangle(x1=int(command_components[1]),
                                          y1=int(command_components[2]),
                                          x2=int(command_components[3]),
                                          y2=int(command_components[4])):
            # logging.warning()
            return False
        return True

    def _exec_fill_area(self, command_components: str) -> bool:
        if not self.canvas:
            logging.warning(LOG_MSG_CANVAS_WASNT_CREATED + f"'{' '.join(command_components)}'")
            return False
        elif not self._positive_check(command_components[1:-1]):
            logging.warning(LOG_MSG_NOT_POSITIVE_ARGS + f"'{' '.join(command_components)}'")
            return False
        else:
            if not self.canvas.bucket_fill(x=int(command_components[1]),
                                           y=int(command_components[2]),
                                           symbol=command_components[3]):
                logging.warning(LOG_MSG_FILL_HIT_TO_LINE + f"'{' '.join(command_components)}'")
                return False

        return True

    def execute_command(self, command: str) -> bool:
        """Parse and execute known command.
        If execution failed - will be returned False."""
        command_components = command.split()
        try:
            # create canvas
            if len(command_components) == 3 and command_components[0] == COMMAND_CREATE_CANVAS:
                return self._exec_create_canvas(command_components)
            # draw line or rectangle
            elif len(command_components) == 5 and \
                 (command_components[0] == COMMAND_DRAW_LINE or command_components[0] == COMMAND_DRAW_RECTANGLE):

                if not self.canvas:
                    logging.warning(LOG_MSG_CANVAS_WASNT_CREATED + f"'{command}'")
                    return False
                if not self._positive_check(command_components[1:]):
                    logging.warning(LOG_MSG_NOT_POSITIVE_ARGS + f"'{command}'")
                    return False
                else:
                    if command_components[0] == COMMAND_DRAW_LINE:
                        return self._exec_draw_line(command_components)
                    else:
                        return self._exec_draw_reactangle(command_components)
            # fill area
            elif len(command_components) == 4 and command_components[0] == COMMAND_BUCKET_FILL:
                return self._exec_fill_area(command_components)
            else:
                logging.warning(LOG_MSG_UNKNOWN_CMD + f"'{command}'")
                return False
        except ValueError:
            logging.warning(LOG_MSG_INCORR_TYPE_ARGS + f"'{command}'")
            return False
        except IndexError:
            logging.warning(LOG_MSG_INCORR_VALUE_ARGS + f"'{command}'")
            return False

    def get_canvas_as_string(self) -> str:
        return self.canvas.__str__()
