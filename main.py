def on_received_number(receivedNumber):
    global lost, ableToPlay
    if inGame:
        if receivedNumber == (rps + 1) % 3:
            # lose
            lost = 1
        else:
            if receivedNumber == rps:
                # tie
                lost = 0
            else:
                # win
                lost = 2
        # if (choosing && receivedNumber == radId) {
        # choosing = false
        # }
        endGame()
    else:
        if receivedNumber == radId:
            ableToPlay = True
            basic.show_string("")
        elif receivedNumber == radId + 100:
            ableToPlay = True
            startGame()
radio.on_received_number(on_received_number)

def menu():
    global radId, inGame
    radId = 0
    inGame = False
    while not (inGame):
        radId = abs(radId % 10)
        basic.show_number(radId, 0)
    inGame = False
    radio.set_group(Math.floor(radId / 10))
    radio.send_number(radId)
    while not (ableToPlay):
        basic.show_string("", 0)
    radio.send_number(radId + 100)
def endGame():
    global inGame
    if lost == 0:
        basic.show_leds("""
            # . # # .
            # # # # .
            # # # . .
            # . . . .
            # . . . .
            """)
    elif lost == 1:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    else:
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # . .
            # . # . .
            . # . . .
            """)
    basic.pause(1000)
    inGame = False
    # Ensure inGame is set to false to break the menu loop
    menu()
def startGame():
    global inGame, choosing, rps
    inGame = True
    choosing = True
    while choosing:
        rps = rps % 3
        showRpsLeds(rps)
    # choosing = true
    # while (choosing) {
    # basic.pause(10)
    # }
    # basic.showNumber(3, 120)
    # basic.showNumber(2, 120)
    # basic.showNumber(1, 120)
    # basic.showNumber(0, 120)
    showRpsLeds(rps)
    # basic.pause(500)
    radio.send_string("now")

def on_button_pressed_a():
    global radId, rps
    radId -= 1
    rps -= 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global inGame, choosing
    inGame = True
    # radio.sendString("WWAIIT")
    if choosing:
        choosing = False
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "now":
        radio.send_number(rps)
    if receivedString == "WWAIIT":
        radio.send_number(radId)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global radId, rps
    radId += 1
    rps += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

ableToPlay = False
lost = 0
rps = 1000
inGame = False
radId = 0
choosing = False
inGame = False
menu()
def showRpsLeds(choice: number):
    if choice == 0:
        basic.show_leds("""
                . . . . .
                # . # # #
                . # . . .
                # . # # #
                . . . . .
                """,
            0)
    if choice == 1:
        basic.show_leds("""
                . . . . .
                . . # # .
                . # # # #
                # # # # #
                . . . . .
                """,
            0)
    if choice == 2:
        basic.show_leds("""
                . # # . .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                """,
            0)