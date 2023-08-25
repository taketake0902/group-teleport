def on_received_number(receivedNumber):
    global hasDuck
    if receivedNumber == ID:
        hasDuck = True
        basic.show_icon(IconNames.DUCK)
    else:
        hasDuck = False
radio.on_received_number(on_received_number)

def on_gesture_shake():
    global SendTo, hasDuck
    if hasDuck:
        SendTo = randint(1, players)
        if SendTo != ID:
            hasDuck = False
            basic.clear_screen()
            radio.send_number(SendTo)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

SendTo = 0
hasDuck = False
ID = 0
players = 0
radio.set_group(42)
players = 4
ID = 4
basic.show_number(ID)
if ID == 1:
    hasDuck = True
else:
    hasDuck = False