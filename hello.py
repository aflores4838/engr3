import board
import analogio

motor=analogio.AnalogOut(board.A0)
pot=analogio.AnalogIn(board.A1)
print("sdfg")
while True:
    speed=pot.value
    motor.value=speed
    print(pot.value)