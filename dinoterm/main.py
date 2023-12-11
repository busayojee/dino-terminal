import curses
from .play import Play
import click
from . import VERSION_STRING

def main_function(stdscr):
    game_width = 125
    dino = [[' ',' ',' ',' ',' ',' ','*','*','*',' '],
        ['*',' ',' ',' ',' ','*','*',' ','*','*'],
        ['*',' ',' ',' ',' ','*','*','*','*','*'],
        ['*',' ',' ',' ','*','*','*','*',' ',' '],
        ['*','*',' ','*','*','*',' ',' ',' ',' '],
        ['*','*','*','*','*','*','*','*','*','*'],
        [' ','*','*','*','*','*',' ',' ',' ','*'],
        [' ',' ','*',' ',' ','*',' ',' ',' ',' '],
        [' ',' ','*',' ',' ','*',' ',' ',' ',' '],
        [' ',' ','*',' ',' ','*',' ',' ',' ',' ']]
    curses.curs_set(0)
    stdscr.timeout(0)
    play = Play(stdscr, game_width, dino)
    play.play()
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(VERSION_STRING)
    ctx.exit()

@click.command()
@click.option("-v", "--version", is_flag=True, callback=print_version,expose_value=False, is_eager=True, help="Show version and exit")
def main():
    curses.wrapper(main_function)

