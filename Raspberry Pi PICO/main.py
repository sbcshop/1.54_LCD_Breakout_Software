from machine import Pin, UART,SPI
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font


spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=0)#SPI interface for tft screen

def main():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"SB COMPONENTS", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"1.54 INCH TFT", 10,100,st7789.GREEN)
    tft.fill_rect(0, 140, 240,10, st7789.RED)
    
    tft.text(font,"BREAKOUT", 10,170,st7789.GREEN)
    tft.fill_rect(0, 210, 240,10, st7789.RED)
    
time.sleep(1)
main()
