# LAMP Visualization Box

## Components
* 3D printed components
    * CE3_lampBOX circuit tray v1.gcode (Ender 3 specific gcode)
    * Upiece.stl
    * lampBOX circuit tray v1.stl
    * slider.stl
    * VisBox.stl
* 5V/12V breadboard powersupply
* small piece of insulated wire
* 4 x 100ohm Resistors
* 4 x Clear Blue LEDs
* 6cm x 8cm prototyping PCB
* Light filter gels
    * 2 x orange gel
    * 1 x yellow gel
## Links to components
* [100 ohm Resistors](https://www.amazon.com/100-Ohm-Resistors-Watt-Pieces/dp/B07JJQY958/ref=sr_1_5?crid=3UTUWQAA1N2VT&keywords=100+ohm+resistor+1%2F4+watt&qid=1578514668&sprefix=100+ohm%2Caps%2C190&sr=8-5)
* [Breadboard Powersupply](https://www.amazon.com/HiLetgo-Supply-Module-Prototype-Breadboard/dp/B00HJ6AE72/ref=sxin_2_ac_d_rm?ac_md=0-0-YnJlYWRib2FyZCBwb3dlciBzdXBwbHk%3D-ac_d_rm&crid=3J5C8DEBMW3ML&cv_ct_cx=breadboard+power+supply&keywords=breadboard+power+supply&pd_rd_i=B00HJ6AE72&pd_rd_r=70b07c48-81e5-4840-aad6-6a416c62ceee&pd_rd_w=lLqGs&pd_rd_wg=Hg29M&pf_rd_p=e2f20af2-9651-42af-9a45-89425d5bae34&pf_rd_r=PQ1VN9FW095VK0XPPVM3&psc=1&qid=1578514849&sprefix=breadboard+power%2Caps%2C190)
* [UV/Blue LEDs](https://www.amazon.com/microtivity-IL041-Clear-Blue-Pack/dp/B004JO4JPA/ref=sr_1_1?keywords=Clear+blue+leds&qid=1578515012&s=electronics&sr=1-1)
* [prototype PCB](https://www.amazon.com/Lheng-Double-Sided-Prototyping-Universal-Electronic/dp/B07PCQYV4M/ref=sr_1_2?keywords=6+x+8+PCB&qid=1578515408&s=electronics&sr=1-2)
## Tools
* Wire cutters
* Soldering Iron

## Assembly Instructions
1. 3D print a single copy of all items (STL files)
2. You should end with 4 3D printed pieces
3. gather your electronic components:
    * 1 x 5V/12V breadboard powersupply
    * 1 x small piece of insulated wire
    * 4 x 100ohm Resistors
    * 4 x Clear Blue LEDs
    * 1 x (6cm x 8cm) prototyping PCB
4. Along one of the short sides of the PCB, press fit the breadboard powersupply into the PCB perforations so that the pins closest to the edge are 3 holes from the edge
    * if the bottom pins bend its okay, the hole spacing is slightly different from the pin spacing
5. Take note of which pins on the bottom are ground and which pins are positive, pins of the same polarity are aligned
6. Following the PCB holes inline with the positive pins, with the LED on the same side as the powersupply, place the longer leg of an LED in the aligned hole, at least 5 holes from the pin (when looking underneath)
    * Skip 3 holes and place another LED inline with the first
    * Skip 2 holes and place another LED inline with the others
    * Skip 3 holes and place another LED inline with the others
    * See image for top view
7. To keep LEDs in place while soldering, feed the negative (short) leg of the LED back to the the powersupply side of the PCB and fold it
