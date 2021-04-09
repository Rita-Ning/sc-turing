"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This is a Breakout game, player will move the paddle left or right to let the ball hits as much bricks as possible.
Player wins the game by hitting all the bricks or loses the game by letting the ball drops 3 times.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

#constant
FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    bx = graphics.get_speedx()
    by = graphics.get_speedy()
    while True:
        is_playing = graphics.get_isplaying()
        if is_playing:

            if graphics.break_hit == graphics.brick_cols * graphics.brick_rows:
                break

            #ball runs over the paddle to border of the window
            if graphics.ball_drop():
                graphics.end_game()
                lives -= 1
                if lives > 0:
                    graphics.set_ball_position()
                else:
                    break

            if graphics.ball_hit():
                if graphics.ball.y + graphics.ball.height >= graphics.paddle.y:
                    if by > 0:
                        by = -by
                elif graphics.ball.y <= graphics.brick.y + graphics.brick.height or graphics.ball.y + \
                        graphics.ball.height >= graphics.brick.y:
                    by = -by
                    graphics.remove_brick()
                elif graphics.ball.x <= graphics.brick.x + graphics.brick.width or graphics.ball.x + \
                        graphics.ball.width >= graphics.brick.x:
                    bx = -bx
                    graphics.remove_brick()

            graphics.ball.move(bx, by)
            # Check
            if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                bx = -bx
            if graphics.ball.y < 0:
                by = -by
        pause(FRAME_RATE)









if __name__ == '__main__':
    main()
