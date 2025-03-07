radio.onReceivedNumber(function (receivedNumber) {
    if (inGame) {
        if (receivedNumber == (rps + 1) % 3) {
            // lose
            lost = 1
        } else {
            if (receivedNumber == rps) {
                // tie
                lost = 0
            } else {
                // win
                lost = 2
            }
        }
        // if (choosing && receivedNumber == radId) {
        //     choosing = false
        // }
        endGame()
    } else {
        if (receivedNumber == radId) {
            ableToPlay = true
            basic.showString("")
        } else if (receivedNumber == radId + 100) {
            ableToPlay = true
            startGame()
        }
    }
})

function menu() {
    radId = 0
    inGame = false
    while (!(inGame)) {
        radId = Math.abs(radId % 10)
        basic.showNumber(radId, 0)
    }
    inGame = false
    radio.setGroup(Math.floor(radId / 10))
    radio.sendNumber(radId)
    while (!(ableToPlay)) {
        basic.showString("", 0)
    }
    radio.sendNumber(radId + 100)
}

function endGame() {
    if (lost == 0) {
        basic.showLeds(`
            # . # # .
            # # # # .
            # # # . .
            # . . . .
            # . . . .
        `)
    } else if (lost == 1) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
        `)
    } else {
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            # . # . .
            . # . . .
        `)
    }
    basic.pause(1000)
    inGame = false  // Ensure inGame is set to false to break the menu loop
    menu()
}

function startGame() {
    inGame = true
    choosing = true
    while (choosing) {
        rps = rps % 3
        showRpsLeds(rps)
    }
    // choosing = true
    // while (choosing) {
    //     basic.pause(10)
    // }
    // basic.showNumber(3, 120)
    // basic.showNumber(2, 120)
    // basic.showNumber(1, 120)
    // basic.showNumber(0, 120)
    showRpsLeds(rps)
    //basic.pause(500)
    radio.sendString("now")
}

input.onButtonPressed(Button.A, function () {
    radId -= 1
    rps -= 1
})

input.onButtonPressed(Button.AB, function () {
    inGame = true
    if (choosing) {
        choosing = false
        //radio.sendString("WWAIIT")
    }
})

radio.onReceivedString(function (receivedString) {
    if (receivedString == "now") {
        radio.sendNumber(rps)
    }
    if (receivedString == "WWAIIT") {
        radio.sendNumber(radId)
    }
})

input.onButtonPressed(Button.B, function () {
    radId += 1
    rps += 1
})

let ableToPlay = false
let lost = 0
let rps = 1000
let inGame = false
let radId = 0
let choosing = false
inGame = false
menu()

function showRpsLeds(choice: number) {
    if (choice == 0) {
        basic.showLeds(`
            . . . . .
            # . # # #
            . # . . .
            # . # # #
            . . . . .
        `,0)
    }
    if (choice == 1) {
        basic.showLeds(`
            . . . . .
            . . # # .
            . # # # #
            # # # # #
            . . . . .
        `, 0)
    }
    if (choice == 2) {
        basic.showLeds(`
            . # # . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
        `, 0)
    }
}