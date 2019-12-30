""""""


VERTICAL_BORDER = '|'
HORIZONTAL_BORDER = '-'
LINE_ELEM = 'x'
BUCKET_FILL_ELEM = 'o'


class Canvas:
    """Canvas, which allows draw lines and rectangles and fill area as bucket fill."""

    def __init__(self, width: int, heigth: int):
        self.width = width + 2
        self.heigth = heigth + 2

        self.canvas = []
        for line in range(self.heigth):
            self.canvas.append([' ' for elem in range(self.width)])

        self._make_borders()

    def _make_borders(self) -> None:
        for column in range(self.width):
            self.canvas[0][column] = HORIZONTAL_BORDER
            self.canvas[self.heigth - 1][column] = HORIZONTAL_BORDER

        for line in range(self.heigth - 2):
            self.canvas[line + 1][0] = VERTICAL_BORDER
            self.canvas[line + 1][self.width - 1] = VERTICAL_BORDER

    def draw_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Drawing line by 2 points."""
        if x1 <= 0 or x1 >= self.width - 1 or \
           x2 <= 0 or x2 >= self.width - 1 or \
           y1 <= 0 or y1 >= self.heigth - 1 or \
           y2 <= 0 or y2 >= self.heigth - 1:
           raise IndexError()

        if x1 - x2 == 0:  # vertical
            if y1 < y2:
                while True:
                    self.canvas[y1][x1] = LINE_ELEM

                    if y2 - y1 == 0:
                        break

                    y1 += 1
            else:
                while True:
                    self.canvas[y2][x1] = LINE_ELEM

                    if y2 - y1 == 0:
                        break

                    y2 += 1
        elif y1 - y2 == 0:  # horizontal
            if x1 < x2:
                while True:
                    self.canvas[y1][x1] = LINE_ELEM

                    if x2 - x1 == 0:
                        break

                    x1 += 1
            else:
                while True:
                    self.canvas[y1][x2] = LINE_ELEM

                    if x2 - x1 == 0:
                        break

                    x2 += 1

        else:
            return False

        return True

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        """Drawing rectangle by 2 points."""

        # draw vertical lines
        if not self.draw_line(x1=x1, y1=y1, x2=x1, y2=y2):
            return False
        if not self.draw_line(x1=x2, y1=y1, x2=x2, y2=y2):
            return False

        # draw horizontal lines
        if not self.draw_line(x1=x1, y1=y1, x2=x2, y2=y1):
            return False
        if not self.draw_line(x1=x1, y1=y2, x2=x2, y2=y2):
            return False

        return True

    def _recursion_fill_area(self, x: int, y: int, symbol: str) -> None:
        if x > 0 and x < self.width - 1 and \
           y > 0 and y < self.heigth - 1 and \
           self.canvas[y][x] != VERTICAL_BORDER and \
           self.canvas[y][x] != HORIZONTAL_BORDER and \
           self.canvas[y][x] != LINE_ELEM and \
           self.canvas[y][x] != symbol:

            self.canvas[y][x] = symbol

            self._recursion_fill_area(x + 1, y, symbol)
            self._recursion_fill_area(x, y + 1, symbol)
            self._recursion_fill_area(x - 1, y, symbol)
            self._recursion_fill_area(x, y - 1, symbol)

    def bucket_fill(self, x: int, y: int, symbol: str) -> bool:
        """Fill area, which contain point (x,y) with 'color' - symbol(char)."""
        if x <= 0 or x >= self.width - 1 or \
           y <= 0 or y >= self.heigth - 1:
           raise IndexError()
        elif self.canvas[y][x] == LINE_ELEM:
            return False

        self._recursion_fill_area(x, y, symbol)
        return True

    def __str__(self) -> str:
        return '\n'.join(''.join(line) for line in self.canvas)
