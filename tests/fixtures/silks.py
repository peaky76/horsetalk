from horsetalk.silks import Silks

c = Silks.Colour
p = Silks.Pattern

SILKS_INPUT = [
    "Beige and black hoops, white sleeves, beige cap, black star",
    "Beige, dark blue cross of lorraine and sleeves, dark blue cap, beige star",
    "Black and orange (quartered), white sleeves, black cap",
    "Black, black and white check sleeves",
    "Brown, brown cap, beige star",
    "Brown, light green epaulets",
    "Dark blue and yellow check, yellow sleeves",
    "Dark blue, beige striped sleeves",
    "Dark blue, large white spots, dark blue and white chevrons on sleeves, dark blue and white striped cap",
    "Dark blue, pink cross sashes, pink stars on sleeves, dark blue cap",
    "Dark blue, red stripe, halved sleeves, red cap",
    "Dark blue, white chevron, halved sleeves, dark blue cap",
    "Dark blue, white cross belts, chevrons on sleeves",
    "Dark blue, white disc",
    "Dark blue, white seams, dark blue sleeves, royal blue armlets, dark blue cap",
    "Dark blue, yellow star, checked sleeves, yellow cap",
    "Dark green, brown armlets, brown cap",
    "Emerald green, emerald green and white check sleeves, white cap",
    "Emerald green, grey braces and sleeves, hooped cap",
    "Emerald green, red hoops, quartered cap",
    "Emerald green, red inverted triangle, red cap",
    "Emerald green, red stars, white sleeves, red armlets, emerald green cap",
    "Grey, dark blue epaulets, dark blue cap",
    "Grey, pink and grey halved sleeves, pink cap",
    "Light blue, dark blue epaulets, white sleeves",
    "Light blue, yellow chevron, white sleeves, black stars, yellow cap",
    "Light green, red diamond and sleeves, quartered cap",
    "Maroon and yellow chevrons, maroon sleeves, yellow cuffs, yellow star on cap",
    "Orange, brown seams, emerald green and yellow quartered cap",
    "Orange, brown seams, green cap",
    "Orange, brown seams, orange cap",
    "Orange, red sleeves",
    "Pink and emerald green quartered, check sleeves, pink cap",
    "Pink, black cross of lorraine, white sleeves and cap",
    "Pink, orange triple diamond, pink sleeves, orange seams, pink cap, orange diamond",
    "Pink, royal blue hoops, royal blue and pink diabolo on sleeves, pink cap, royal blue star",
    "Purple and yellow diamonds, yellow sleeves, purple cap",
    "Purple, beige star, hooped sleeves and stars on cap",
    "Purple, beige striped sleeves",
    "Purple, light green striped sleeves",
    "Purple, pink seams, purple sleeves, pink star on cap",
    "Purple, white disc, purple sleeves, white spots, hooped cap",
    "Purple, yellow sleeves, red and yellow striped cap",
    "Purple, yellow stars and sleeves, yellow cap, purple stars",
    "Red and white stripes, red sleeves, quartered cap",
    "Red, dark green hoop",
    "Red, royal blue star, royal blue chevrons on sleeves, royal blue star on cap",
    "Red, royal blue stars, red cap",
    "Red, yellow chevron, yellow sleeves, red armlets",
    "Royal blue, brown diamond, brown cap",
    "Royal blue, grey seams, sleeves and cap",
    "Royal blue, royal blue cap, yellow star",
    "Royal blue, white stars, white sleeves, white star on cap",
    "White and royal blue (quartered), white and red striped sleeves, red cap",
    "White, maroon panel and sleeves, royal blue and yellow striped cap",
    "White, purple panel, check cap",
    "White, red stripe, striped sleeves, quartered cap",
    "White, royal blue epaulets, royal blue sleeves, light blue stars, royal blue cap, light blue star",
    "White, royal blue stars, royal blue armlet, royal blue cap",
    "White, royal blue stars, white and maroon striped sleeves, maroon cap",
    "White, yellow chevron, royal blue sleeves, yellow stars, royal blue cap, yellow star",
    "White, yellow star, red armlet, white cap, emerald green star",
    "Yellow, purple disc, purple spots on sleeves, quartered cap",
    "Yellow, white epaulets",
]

SILKS_OUTPUT = [
    [
        (c.BEIGE, c.BLACK, p.HOOPS),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.BEIGE, c.BLACK, p.STAR),
    ],
    [
        (c.BEIGE, c.DARK_BLUE, p.CROSS_OF_LORRAINE),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
        (c.DARK_BLUE, c.BEIGE, p.STAR),
    ],
    [
        (c.BLACK, c.ORANGE, p.QUARTERED),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.BLACK, c.BLACK, p.PLAIN),
    ],
    [
        (c.BLACK, c.BLACK, p.PLAIN),
        (c.BLACK, c.WHITE, p.CHECK),
        (c.BLACK, c.BLACK, p.PLAIN),
    ],
    [
        (c.BROWN, c.BROWN, p.PLAIN),
        (c.BROWN, c.BROWN, p.PLAIN),
        (c.BROWN, c.BEIGE, p.STAR),
    ],
    [
        (c.BROWN, c.LIGHT_GREEN, p.EPAULETS),
        (c.BROWN, c.BROWN, p.PLAIN),
        (c.BROWN, c.BROWN, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.YELLOW, p.CHECK),
        (c.YELLOW, c.YELLOW, p.PLAIN),
        (c.DARK_BLUE, c.YELLOW, p.CHECK),
    ],
    [
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
        (c.DARK_BLUE, c.BEIGE, p.STRIPES),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.WHITE, p.LARGE_SPOTS),
        (c.DARK_BLUE, c.WHITE, p.CHEVRONS),
        (c.DARK_BLUE, c.WHITE, p.STRIPES),
    ],
    [
        (c.DARK_BLUE, c.PINK, p.CROSS_SASHES),
        (c.DARK_BLUE, c.PINK, p.STARS),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.RED, p.STRIPE),
        (c.DARK_BLUE, c.RED, p.HALVED),
        (c.RED, c.RED, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.WHITE, p.CHEVRON),
        (c.DARK_BLUE, c.WHITE, p.HALVED),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.WHITE, p.CROSS_BELTS),
        (c.DARK_BLUE, c.WHITE, p.CHEVRONS),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.WHITE, p.DISC),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.WHITE, p.SEAMS),
        (c.DARK_BLUE, c.ROYAL_BLUE, p.ARMLETS),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.DARK_BLUE, c.YELLOW, p.STAR),
        (c.DARK_BLUE, c.YELLOW, p.CHECK),
        (c.YELLOW, c.YELLOW, p.PLAIN),
    ],
    [
        (c.DARK_GREEN, c.DARK_GREEN, p.PLAIN),
        (c.DARK_GREEN, c.BROWN, p.ARMLET),
        (c.BROWN, c.BROWN, p.PLAIN),
    ],
    [
        (c.EMERALD_GREEN, c.EMERALD_GREEN, p.PLAIN),
        (c.EMERALD_GREEN, c.WHITE, p.CHECK),
        (c.WHITE, c.WHITE, p.PLAIN),
    ],
    [
        (c.EMERALD_GREEN, c.GREY, p.BRACES),
        (c.GREY, c.GREY, p.PLAIN),
        (c.EMERALD_GREEN, c.GREY, p.HOOPS),
    ],
    [
        (c.EMERALD_GREEN, c.RED, p.HOOPS),
        (c.EMERALD_GREEN, c.RED, p.HOOPS),
        (c.EMERALD_GREEN, c.RED, p.QUARTERED),
    ],
    [
        (c.EMERALD_GREEN, c.RED, p.INVERTED_TRIANGLE),
        (c.EMERALD_GREEN, c.EMERALD_GREEN, p.PLAIN),
        (c.RED, c.RED, p.PLAIN),
    ],
    [
        (c.EMERALD_GREEN, c.RED, p.STARS),
        (c.WHITE, c.RED, p.ARMLETS),
        (c.EMERALD_GREEN, c.EMERALD_GREEN, p.PLAIN),
    ],
    [
        (c.GREY, c.DARK_BLUE, p.EPAULETS),
        (c.GREY, c.GREY, p.PLAIN),
        (c.DARK_BLUE, c.DARK_BLUE, p.PLAIN),
    ],
    [
        (c.GREY, c.GREY, p.PLAIN),
        (c.PINK, c.GREY, p.HALVED),
        (c.PINK, c.PINK, p.PLAIN),
    ],
    [
        (c.LIGHT_BLUE, c.DARK_BLUE, p.EPAULETS),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.LIGHT_BLUE, c.LIGHT_BLUE, p.PLAIN),
    ],
    [
        (c.LIGHT_BLUE, c.YELLOW, p.CHEVRON),
        (c.WHITE, c.BLACK, p.STARS),
        (c.YELLOW, c.YELLOW, p.PLAIN),
    ],
    [
        (c.LIGHT_GREEN, c.RED, p.DIAMOND),
        (c.RED, c.RED, p.PLAIN),
        (c.LIGHT_GREEN, c.RED, p.QUARTERED),
    ],
    [
        (c.MAROON, c.YELLOW, p.CHEVRONS),
        (c.MAROON, c.YELLOW, p.CUFFS),
        (c.MAROON, c.YELLOW, p.STAR),
    ],
    [
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.EMERALD_GREEN, c.YELLOW, p.QUARTERED),
    ],
    [
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.GREEN, c.GREEN, p.PLAIN),
    ],
    [
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.ORANGE, c.BROWN, p.SEAMS),
        (c.ORANGE, c.ORANGE, p.PLAIN),
    ],
    [
        (c.ORANGE, c.ORANGE, p.PLAIN),
        (c.RED, c.RED, p.PLAIN),
        (c.ORANGE, c.ORANGE, p.PLAIN),
    ],
    [
        (c.PINK, c.EMERALD_GREEN, p.QUARTERED),
        (c.PINK, c.EMERALD_GREEN, p.CHECK),
        (c.PINK, c.PINK, p.PLAIN),
    ],
    [
        (c.PINK, c.BLACK, p.CROSS_OF_LORRAINE),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.WHITE, c.WHITE, p.PLAIN),
    ],
    [
        (c.PINK, c.ORANGE, p.TRIPLE_DIAMOND),
        (c.PINK, c.ORANGE, p.SEAMS),
        (c.PINK, c.ORANGE, p.DIAMOND),
    ],
    [
        (c.PINK, c.ROYAL_BLUE, p.HOOPS),
        (c.ROYAL_BLUE, c.PINK, p.DIABOLO),
        (c.PINK, c.ROYAL_BLUE, p.STAR),
    ],
    [
        (c.PURPLE, c.YELLOW, p.DIAMONDS),
        (c.YELLOW, c.YELLOW, p.PLAIN),
        (c.PURPLE, c.PURPLE, p.PLAIN),
    ],
    [
        (c.PURPLE, c.BEIGE, p.STAR),
        (c.PURPLE, c.BEIGE, p.HOOPED),
        (c.PURPLE, c.BEIGE, p.STARS),
    ],
    [
        (c.PURPLE, c.PURPLE, p.PLAIN),
        (c.PURPLE, c.BEIGE, p.STRIPES),
        (c.PURPLE, c.PURPLE, p.PLAIN),
    ],
    [
        (c.PURPLE, c.PURPLE, p.PLAIN),
        (c.PURPLE, c.LIGHT_GREEN, p.STRIPES),
        (c.PURPLE, c.PURPLE, p.PLAIN),
    ],
    [
        (c.PURPLE, c.PINK, p.SEAMS),
        (c.PURPLE, c.PURPLE, p.PLAIN),
        (c.PURPLE, c.PINK, p.STAR),
    ],
    [
        (c.PURPLE, c.WHITE, p.DISC),
        (c.PURPLE, c.WHITE, p.SPOTS),
        (c.PURPLE, c.WHITE, p.HOOPED),
    ],
    [
        (c.PURPLE, c.PURPLE, p.PLAIN),
        (c.YELLOW, c.YELLOW, p.PLAIN),
        (c.RED, c.YELLOW, p.STRIPES),
    ],
    [
        (c.PURPLE, c.YELLOW, p.STARS),
        (c.YELLOW, c.YELLOW, p.PLAIN),
        (c.YELLOW, c.PURPLE, p.STARS),
    ],
    [
        (c.RED, c.WHITE, p.STRIPES),
        (c.RED, c.RED, p.PLAIN),
        (c.RED, c.WHITE, p.QUARTERED),
    ],
    [(c.RED, c.DARK_GREEN, p.HOOP), (c.RED, c.RED, p.PLAIN), (c.RED, c.RED, p.PLAIN)],
    [
        (c.RED, c.ROYAL_BLUE, p.STAR),
        (c.RED, c.ROYAL_BLUE, p.CHEVRONS),
        (c.RED, c.ROYAL_BLUE, p.STAR),
    ],
    [(c.RED, c.ROYAL_BLUE, p.STARS), (c.RED, c.RED, p.PLAIN), (c.RED, c.RED, p.STAR)],
    [
        (c.RED, c.YELLOW, p.CHEVRON),
        (c.YELLOW, c.RED, p.ARMLETS),
        (c.RED, c.RED, p.PLAIN),
    ],
    [
        (c.ROYAL_BLUE, c.BROWN, p.DIAMOND),
        (c.ROYAL_BLUE, c.ROYAL_BLUE, p.PLAIN),
        (c.BROWN, c.BROWN, p.PLAIN),
    ],
    [
        (c.ROYAL_BLUE, c.GREY, p.SEAMS),
        (c.GREY, c.GREY, p.PLAIN),
        (c.GREY, c.GREY, p.PLAIN),
    ],
    [
        (c.ROYAL_BLUE, c.ROYAL_BLUE, p.PLAIN),
        (c.ROYAL_BLUE, c.ROYAL_BLUE, p.PLAIN),
        (c.ROYAL_BLUE, c.YELLOW, p.STAR),
    ],
    [
        (c.ROYAL_BLUE, c.WHITE, p.STARS),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.ROYAL_BLUE, c.WHITE, p.STAR),
    ],
    [
        (c.WHITE, c.ROYAL_BLUE, p.QUARTERED),
        (c.WHITE, c.RED, p.STRIPES),
        (c.RED, c.RED, p.PLAIN),
    ],
    [
        (c.WHITE, c.MAROON, p.PANEL),
        (c.MAROON, c.MAROON, p.PLAIN),
        (c.ROYAL_BLUE, c.YELLOW, p.STRIPES),
    ],
    [
        (c.WHITE, c.PURPLE, p.PANEL),
        (c.WHITE, c.WHITE, p.PLAIN),
        (c.WHITE, c.PURPLE, p.CHECK),
    ],
    [
        (c.WHITE, c.RED, p.STRIPES),
        (c.WHITE, c.RED, p.STRIPES),
        (c.WHITE, c.RED, p.QUARTERED),
    ],
    [
        (c.WHITE, c.ROYAL_BLUE, p.EPAULETS),
        (c.ROYAL_BLUE, c.LIGHT_BLUE, p.STARS),
        (c.ROYAL_BLUE, c.LIGHT_BLUE, p.STARS),
    ],
    [
        (c.WHITE, c.ROYAL_BLUE, p.STARS),
        (c.WHITE, c.ROYAL_BLUE, p.ARMLET),
        (c.ROYAL_BLUE, c.ROYAL_BLUE, p.PLAIN),
    ],
    [
        (c.WHITE, c.ROYAL_BLUE, p.STARS),
        (c.WHITE, c.MAROON, p.STRIPED),
        (c.MAROON, c.MAROON, p.PLAIN),
    ],
    [
        (c.WHITE, c.YELLOW, p.CHEVRON),
        (c.ROYAL_BLUE, c.YELLOW, p.STARS),
        (c.ROYAL_BLUE, c.YELLOW, p.STAR),
    ],
    [
        (c.WHITE, c.YELLOW, p.STAR),
        (c.WHITE, c.RED, p.ARMLET),
        (c.WHITE, c.EMERALD_GREEN, p.STAR),
    ],
    [
        (c.YELLOW, c.PURPLE, p.DISC),
        (c.YELLOW, c.PURPLE, p.SPOTS),
        (c.YELLOW, c.PURPLE, p.QUARTERED),
    ],
    [
        (c.YELLOW, c.WHITE, p.EPAULETS),
        (c.YELLOW, c.YELLOW, p.PLAIN),
        (c.YELLOW, c.YELLOW, p.PLAIN),
    ],
]
