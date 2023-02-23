# attendence system using raspberry pi pico and pico barcode hat and security system using barcode
from machine import Pin, UART,SPI
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font


# this create the data.txt file inside the raspberry pi pico

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,135,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=3)#SPI interface for tft screen

def main():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"HELLO WORLD!!", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
    
    #tft.text(font,"ETHERNET HAT", 10,120,st7789.GREEN)
    #tft.fill_rect(0, 152, 240,10, st7789.RED)
    
    
time.sleep(1)
main()