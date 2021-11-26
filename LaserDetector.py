import pigpio
import time
import mcp3204

SPI_CE = 0
SPI_SPEED = 1000000
#ch0の値を読み込む場合、MCP3208だとch8まで指定可能
READ_CHS = [0,1,2,3]
VREF = 3.3
pi = pigpio.pi()
adc = mcp3204.mcp3204( pi, SPI_CE, SPI_SPEED, VREF )

def getLaser(ch:int) :
    return adc.get_volt(adc.get_value(ch))

"""
while True:
    volt0 = adc.get_volt(adc.get_value( READ_CHS[0] ))
    volt1 = adc.get_volt(adc.get_value( READ_CHS[1] ))
    volt2 = adc.get_volt(adc.get_value( READ_CHS[2] ))
    volt3 = adc.get_volt(adc.get_value( READ_CHS[3] ))
    print( "Current [ch0] : {:.8f} mA".format( volt0 ) )
    print( "Current [ch1] : {:.8f} mA".format( volt1 ) )
    print( "Current [ch2] : {:.8f} mA".format( volt2 ) )
    print( "Current [ch3] : {:.8f} mA".format( volt3 ) )
    print("")
    time.sleep( 1 )
"""