from PIL import ImageGrab
import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.03)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def getImage():
    # First 2 parameters are x and y from the top left corner of the TILES, not the game. The last two are the bottom right corner of the TILES.
    return ImageGrab.grab(bbox=(456,179,894,618))
    
def checkTiles(img):
    tiles = []
    for y in range(0,4):
        for x in range(0,4):
            if img.getpixel((50+(117*x),50+(117*y))) == (0,0,0):
                # 456 and 179 are the x and y displacement values, those are from the grab call in getImage(), (50,50) is the center of the tiles, you might need to change it, 117 is the change between tiles, might need to change this too.
                tiles.append((456+50+(117*x),179+50+(117*y)))
    return tiles

def clickTiles(tiles):
    for tile in tiles:
        click(tile[0],tile[1])
        time.sleep(0.05)

time.sleep(1)
while True:
    clickTiles(checkTiles(getImage()))
