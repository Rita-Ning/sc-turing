"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This is a Breakout game, player will move the paddle left or right to let the ball hits as much bricks as possible.
Player wins the game by hitting all the bricks or loses the game by letting the ball drops 3 times.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

# Global Variable
is_playing = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        self.brick_offset = brick_offset

        #win condition- for bricks hitted
        self.break_hit = 0

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=(self.window.height - paddle_offset))
        self.paddle.filled = True
        self.window.add(self.paddle)

        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.paddle_offset = paddle_offset

        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing), y=(brick_offset + brick_height) +
                                                                                   i * (brick_height + brick_spacing))

                if i < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif 1 < i < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 3 < i < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 5 < i < 8:
                    self.brick.fill_color = 'seagreen'
                    self.brick.color = 'seagreen'
                elif 7 < i < 10:
                    self.brick.fill_color = 'royalblue'
                    self.brick.color = 'royalblue'
                elif 9 < i < 12:
                    self.brick.fill_color = 'midnightblue'
                    self.brick.color = 'midnightblue'
                elif 11 < i < 14:
                    self.brick.fill_color = 'purple'
                    self.brick.color = 'purple'
                else:
                    self.brick.fill_color = 'silver'
                    self.brick.color = 'silver'

        # Center a filled ball in the graphical window.
        self.ball_r = ball_radius
        self.ball = GOval(self.ball_r * 2, self.ball_r * 2, x=(self.window.width - self.ball_r * 2) / 2,
                          y=(self.window.height - self.ball_r * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__bx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__bx = -self.__bx
        self.__by = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmouseclicked(self.start_game)
        onmousemoved(self.move_paddle)

    def start_game(self, click):
        global is_playing
        is_playing = True

    # if ball drops, game needs to restart
    def end_game(self):
        global is_playing
        is_playing = False

    def move_paddle(self, mouse):
        if self.paddle.width / 2 <= mouse.x <= self.window.width - self.paddle.width / 2:
            self.window.add(self.paddle, x=mouse.x - self.paddle.width / 2, y=self.window.height - self.paddle_offset)
        elif self.paddle.width / 2 >= mouse.x:
            self.window.add(self.paddle, x=0, y=self.window.height - self.paddle_offset)
        elif mouse.x >= self.window.width - self.paddle.width / 2:
            self.window.add(self.paddle, x=self.window.width - self.paddle.width,
                            y=self.window.height - self.paddle_offset)

    # to know if the ball hit on sth or not
    def ball_hit(self):
        is_ball1point_hit = self.window.get_object_at(self.ball.x, self.ball.y) is not None
        is_ball2point_hit = self.window.get_object_at(self.ball.x + 2 * self.ball_r, self.ball.y) is not None
        is_ball3point_hit = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_r) is not None
        is_ball4point_hit = self.window.get_object_at(self.ball.x + 2 * self.ball_r,
                                                      self.ball.y + 2 * self.ball_r) is not None

        return is_ball1point_hit or is_ball2point_hit or is_ball3point_hit or is_ball4point_hit

    # to remove brick
    def remove_brick(self):
        global is_playing
        ball1point_brick = self.window.get_object_at(self.ball.x, self.ball.y)
        ball2point_brick = self.window.get_object_at(self.ball.x + 2 * self.ball_r, self.ball.y)
        ball3point_brick = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_r)
        ball4point_brick = self.window.get_object_at(self.ball.x + 2 * self.ball_r, self.ball.y + 2 * self.ball_r)

        if ball1point_brick is not None and ball1point_brick is not self.paddle:
            self.window.remove(ball1point_brick)
            self.break_hit += 1
        if ball2point_brick is not None and ball2point_brick is not self.paddle:
            self.window.remove(ball2point_brick)
            if ball1point_brick != ball2point_brick:
                self.break_hit += 1
        if ball3point_brick is not None and ball3point_brick is not self.paddle:
            self.window.remove(ball3point_brick)
            self.break_hit += 1
        if ball4point_brick is not None and ball4point_brick is not self.paddle:
            self.window.remove(ball4point_brick)
            if ball3point_brick != ball4point_brick:
                self.break_hit += 1

        return self.break_hit


    # to check if ball drop
    def ball_drop(self):
        is_ball_drop = self.ball.y + self.ball.height >= self.window.height
        return is_ball_drop

    # let the ball back to initial point
    def set_ball_position(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width - self.ball_r * 2) / 2,
                        y=(self.window.height - self.ball_r * 2) / 2)


    # getters
    def get_speedx(self):
        return self.__bx

    def get_speedy(self):
        return self.__by

    def get_isplaying(self):
        return is_playing




