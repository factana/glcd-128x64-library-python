### 128x64 Graphical LCD Display

A simple library for JHD128x64E GLCD, this GLCD consists 2 KS0108 chip which developed by Samsung electronics is a LCD
driver LSl with 64 channel output for dot matrix liquid crystal graphic display system. It has the internal display RAM
for storing the display data transferred from a 8 bit microcontroller and generates the dot matrix Liquid crystal
driving signals corresponding to stored data. This library can display all Alphabets in English language both CAPS and
small, numbers from 0 to 9 and standard special characters.

### Resources

* For datasheets of JHD128x64E and KS0108 please
  refer [Docs](https://github.com/factana/fogwing-glcd-library-python/tree/main/Docs)

### Hardware support

* Raspberry Pi Zero W
* Raspberry Pi 3 B+
* Raspberry Pi 4

### Limitations:

* Cannot display any kind of images
* Does not support display other than JHD128X64E GLCD
* No scroll option available
* Tested only with Raspberry Pi

### Installation

To install the library just type:

```
pip install glcd-jhd128x64
```

### Available methods

* Pinmap

```
GLCD = glcd_jhd128x64e.KS0108(rs=4, rw=7, en=8, d0=9, d1=10, 
                              d2=11, d3=14, d4=15, d5=17, 
                              d6=18, d7=25, chip_set0=22, 
                              chip_set1=23, reset=24)
```

Here the pin numbers can be changed for the user's convenience.

* Initialization

``` 
GLCD.start()
```

This function is used to initialize display, it sends command to turn ON display and clears the memory.

* Setting cursor position

``` 
GLCD.set_cursor()
``` 

This function takes 3 arguments which are: chip to be used, line from where data is to be displayed and from which
column the data must be displayed.

* Line selection

``` 
GLCD.go_to_line()
``` 

This function takes one argument where the user can specify from which line data is to be displayed.

* Shift to next line

```  
GLCD.go_to_nextline()
``` 

This function will shift to next line and display the data.

* Display data

``` 
GLCD.print_str()
``` 

This function will display string or integer or character on the display.

* Display a character

``` 
GLCD.print_chr()
``` 

This function will display a character on the display

### Usage examples

* In this example, a string and a character is displayed on the GLCD continuously starting chip 0, line 0 and cursor 0

```
import glcd_jhd128x64e    

      
def main():
    GLCD = glcd_jhd128x64e.KS0108(rs=4, rw=7, en=8, d0=9, d1=10, 
                              d2=11, d3=14, d4=15, d5=17, 
                              d6=18, d7=25, chip_set0=22, 
                              chip_set1=23, reset=24)
    GLCD.start()
    GLCD.set_cursor(0, 0, 0)
    GLCD.print_str("Hello! How are you")
    GLCD.print_chr("?")
        
            
if __name__ == "__main__":
    main()
```

* In this example DTH11 sensor data is displayed on GLCD, The sentence will be written on line 0, 1, 2 using both the
  chips, temperature is displayed on line 3 of chip 0 and humidity is displayed on line 3 of chip 1

```
import glcd_jhd128x64e
import Adafruit_DHT
import time


def main():
    GLCD = glcd_jhd128x64e.KS0108(rs=4, rw=7, en=8, d0=9, d1=10,
                                  d2=11, d3=14, d4=15, d5=17,
                                  d6=18, d7=25, chip_set0=22,
                                  chip_set1=23, reset=24)
    hum, temp = Adafruit_DHT.read_retry(11, 26)
    time.sleep(2)
    GLCD.start()
    while True:
        GLCD.set_cursor(0, 0, 0)
        GLCD.print_str("This example displays\nTemperature, humidity")
        GLCD.go_to_nextline()
        GLCD.print_str("from DHT11 sensor")
        GLCD.set_cursor(0, 4, 0)
        GLCD.print_str("Temp: ")
        GLCD.print_str(temp)
        GLCD.print_chr("C")
        GLCD.set_cursor(1, 4, 0)
        GLCD.print_str("Hum: ")
        GLCD.print_str(hum)
        GLCD.print_chr("%")


if __name__ == "__main__":
    main()

```

Note: While displaying dynamic data the function used to set cursor potion and to display data must be in while loop, 
"\n" will shift the data to the next line in display.

### Main references

* [Openlab](https://openlabpro.com/guide/ks0108-graphic-lcd-interfacing-pic18f4550-part-2/)
* [ExploreEmbedded](https://github.com/ExploreEmbedded/Tutorials) 

