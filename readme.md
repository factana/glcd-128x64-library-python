# JHD128x64E
A simple library for JHD128x64E GLCD, This library is used to drive JHD128x64E GLCD which has 2 KS0108 Chips, This library can display all Alphabets in English language both CAPS and small, numbers from 0 to 9 and and standard special characters.

# Datasheet of JHD128X64E GLCD

![Screenshot (9)](https://user-images.githubusercontent.com/101356753/166966236-b1e28cfe-5308-448c-996c-f09271cd8e70.png)

# Installation 
To install the library just type:
```
pip install glcd-jhd128x53e
```

# Hardware support
* Supports only Raspberry Pi GPIO pins

# Limitations:

* Cannot display any kind of images
* Does not support devices other that JHD128X64E GLCD
* No scroll option available
* Can only be used for Raspberry Pi

# Usage Examples
In this program a string and a character is displayed on the GLCD continuously starting chip 0, line 0 and cursor 0

```
import glcd_jhd128x64e    

      
def main():
    GLCD = glcd_jhd128x64e.KS0108(rs=4, rw=7, en=8, d0=9, d1=10, d2=11, d3=14, d4=15, d5=17, d6=18, d7=25, chip_set0=22, chip_set1=23,
                  reset=24)
    GLCD.start()
    GLCD.set_cursor(0, 0, 0)
    GLCD.print_str("Hello! How are you")
    GLCD.print_chr("?")
        
            
if __name__ == "__main__":
    main()
```
