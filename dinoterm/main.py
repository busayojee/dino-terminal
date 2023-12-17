import curses
from play import Play
import click
from __init__ import VERSION_STRING
import time

def getScreen_dimension(stdscr):
    y = 0
    x = 0
    while(True):
        try:
            stdscr.addstr(y,0," ")
            stdscr.refresh() 
            y += 1
        except:
            break
    while(True):
        try:
            stdscr.addstr(0,x," ")
            stdscr.refresh()
            x += 1
        except:
            break
    return (y,x)

def main_function(stdscr):           
    scr_dimension = getScreen_dimension(stdscr)
    jump_height = 7
    dino = [[' ',' ',' ',' ',' ',' ','*','*','*',' '],
        ['*',' ',' ',' ',' ','*','*','*','0    ','*'],
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
     
    if(len(dino)+jump_height > scr_dimension[0]):
        stdscr.addstr(int(scr_dimension[0]/2), int(scr_dimension[1]/3),"Ooops! Increase your console/terminal screen height")
        stdscr.refresh()
        time.sleep(5)
        return
    
    play = Play(stdscr, scr_dimension, dino, jump_height)
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
    
if __name__ == '__main__':
    main()
