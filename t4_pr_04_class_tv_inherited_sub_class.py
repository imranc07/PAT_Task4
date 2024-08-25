'''
Q4:
TV class
TVClass - Base class
LedTV class
PlasmaTV class
Part - A

Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. 
Specify brand in a constructor parameter. Channel should be 1 by default.
Volume should be 50 by default.
Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.
Add a method to set the channel. Let's say the TV has only 50 channels so if you try 
to set channel 60 the TV will stay at the current channel.
Add a method to reset TV so it goes back to channel 1 and volume 50.
(Hint: consider using it from the constructor).
It's useful to write a status that returns info about the TV status 
like: "Panasonic at channel 8, volume 75".

Part - B : LED , Plasma
Inherit a TV class add additional properties like screen thickness, energy usage , 
Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails ,
which displays the detailed features of the TV
'''

'''
Input:
1. Base Class = TV
2. Sub classes = ledTV, PlasmaTV

logic:
1. Base class = TV
2. Methods = increase_volume, decrease_volume, reset, display_channel, TV_status & Additional_features
2. Inherited classe = ledTV, PlasmaTV

Output = print (increasevolume(), decreasevolume(), channel(), status(), resetTv(), display())
'''


#Parent class or Base Class tv
class tv:
    def __init__(sony,price,inches,OnOffstatus,volume,channel,v=50,c=1):
        sony.price=price
        sony.inches=inches
        sony.OnOffstatus=OnOffstatus
        sony.volume=volume
        sony.channel=channel
        sony.v=1
        sony.c=50

    #The method to decrease the volume of the TV
    def decreasevolume(sony):
        if sony.volume>=100:
            sony.volume=sony.volume-10
            print("Decreased the tv volume")

    # The method to increase voulme of the TV
    def increasevolume(sony):
        if sony.volume>=0 & sony.volume<=100:
            sony.volume=sony.volume+10
            print("\nIncreased the tv volume to",sony.volume)

    # The Method to display the channel number of the YV
    def cha(sony):
        if sony.channel<=50:
            print("Channel number is",sony.channel)
        else:
            print("You have entered the invalid channel number")
    
    # The Method to reset the TV
    def resetTv(sony):
        print("\nTV is reset to default volume and channel")
        print("The default volume of tv is",sony.v)
        print("The default channel of tv is",sony.c)

    # The Method to display the status of the TV
    def status(sony):
        print("\nThe SONY tv is at channel number", sony.channel , "and volume is",sony.volume)

# Subclass Led and use of concept of inheritance
class Led(tv):
    def __init__(sony,price,inches,ONOffstatus,volume,channel,screenthickness,energyusage,lifespan,refreshrate,viewingangle,backlight):
        super().__init__(price,inches,ONOffstatus,volume,channel)
        sony.screenthickness=screenthickness
        sony.energyusage=energyusage
        sony.lifespan=lifespan
        sony.refreshrate=refreshrate
        sony.viewingangle=viewingangle
        sony.backlight=backlight

    # The Method to display the additional features of the TV  
    def display(sony):
        print("\nThe additional features of tv are")
        print("Screen thickness is",sony.screenthickness)
        print("Energy usage of tv is ",sony.energyusage)
        print("Life span of tv is",sony.lifespan)
        print("Refreshrate of tv is",sony.refreshrate)
        print("Viewing angle of tv is",sony.viewingangle)
        print("Backlight of tv is",sony.backlight)

# Subclass plasma and use of concept of inheritance
class plasma(Led):
    pass   
new_tv=plasma(50000,55,'onoff',10,30,1,'20kw','20years','0.5sec','31degress','75percent')  

# calling the methods of class
new_tv.increasevolume()
new_tv.decreasevolume()
new_tv.cha()
new_tv.status()
new_tv.resetTv()
new_tv.display()