radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == ID) {
        hasDuck = true
        basic.showIcon(IconNames.Duck)
    } else {
        hasDuck = false
    }
})
input.onGesture(Gesture.Shake, function () {
    if (hasDuck) {
        SendTo = randint(1, players)
        if (SendTo != ID) {
            hasDuck = false
            basic.clearScreen()
            radio.sendNumber(SendTo)
        }
    }
})
let SendTo = 0
let hasDuck = false
let ID = 0
let players = 0
radio.setGroup(42)
players = 4
ID = 4
basic.showNumber(ID)
if (ID == 1) {
    hasDuck = true
} else {
    hasDuck = false
}
