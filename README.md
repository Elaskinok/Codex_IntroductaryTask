# Codex_IntroductaryTask

This application allows to draw lines and rectangles on canvas. Also it allows fill closed area.
All these actions can be displayed by pseudographics(in file "output.txt").

## Running Application

For running application you must create a file with name "input.txt". The file must contain commands.

## Application features

- ### Create canvas 

        C w h

w - width

h - heigth

- ### Draw line

        L x1 y1 x2 y2

x1, y1 - coordinates of 1st point

x2, y2 - coordinates of 2nd point

- ### Draw Rectangle

        R x1 y1 x2 y2
x1, y1 - coordinates of 1st point

x2, y2 - coordinates of 2nd point

- ### Bucket fill (fill area)

        B x y
x, y - coordinates of point, which contained into field, which will be filled


## Tests

For running tests you must be in root directory (which contain README).

Execute next command:

    $ python3.x -m Tests.test_command_executor

