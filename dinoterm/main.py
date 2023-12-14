import curses
import play as ply
import click
#from . import VERSION_STRING

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
    return [y,x]

def main_function(stdscr,scr_dimension):           
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
    y,x = curses.getsyx()
    print(y)
    print(x)
    stdscr.timeout(0)
    play = ply.Play(stdscr, scr_dimension, dino)
    play.play()
# def print_version(ctx, param, value):
#     if not value or ctx.resilient_parsing:
#         return
#     #click.echo(VERSION_STRING)
#     ctx.exit()

# @click.command()
# @click.option("-v", "--version", is_flag       =True, callback=print_version,expose_value=False, is_eager=True, help="Show version and exit")
def main():
    stdscr = curses.initscr()
    #curses.wrapper(main_function(stdscr))
    
    main_function(stdscr,getScreen_dimension(stdscr))

if __name__ == '__main__':
    main()