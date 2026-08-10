LEVELS = [
    {
        "grid_width": 16,
        "grid_height": 12,
        "map": [
            "WWWWWWWWWWWWWWWW",
            "W              W",
            "W              W",
            "W  W  KG       W",
            "W  WWWWWWWWWW  W",
            "W              W",
            "D       P      W",
            "W  WWWWWWWWWW  W",
            "W       GK  W  W",
            "W              W",
            "W              W",
            "WWWWWWWWWWWWWWWW"
        ]
    },
    {
        "grid_width": 20,
        "grid_height": 15,
        "map": [
            "WWWWWWWWWWWWWWWWWWWW",
            "WP      W        K W",
            "W WWWWW W WWWWWW   W",
            "W       G      W   W",
            "W WWWWWWWWWWWW W   W",
            "W                D W",
            "WWWWWWWWWWWWWWWWWWWW"
        ]
    }
]

current_level = 0

def load_level(level):
    global MAP, GRID_WIDTH, GRID_HEIGHT, WIDTH, HEIGHT

    MAP = LEVELS[level]["map"]
    GRID_WIDTH = LEVELS[level]["grid_width"]
    GRID_HEIGHT = LEVELS[level]["grid_height"]

    WIDTH = GRID_WIDTH * GRID_SIZE
    HEIGHT = GRID_HEIGHT * GRID_SIZE

    setup_game()

    # at the bottom replace
    setup_game()
    # with
    load_level()



# when player wins... instead of:
game_over = True
player_won = True
# replace with:

if current_level < len(LEVELS) - 1:
    current_level += 1
    load_level(current_level)
else:
    game_over = True
    player_won = True
