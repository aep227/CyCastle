import pygame


pygame.init()
window = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()
pygame.display.set_caption("PyCastle")

class game_info:
    tile_size = 32
    move = 1


class player:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


inst_game_info = game_info()
inst_player = player(2,2)

# player_graphic = pygame.image.load("./graphics/player_male.png")
player_graphic = pygame.image.load("./graphics/player_male_cyber.png")
#player_graphic.convert()
player_graphic.convert_alpha()

# floor_graphic = pygame.image.load("./graphics/floor.png")
floor_graphic = pygame.image.load("./graphics/floor_cyber.png")
floor_graphic.convert_alpha()

# door_closed_graphic = pygame.image.load("./graphics/door_closed.png")
door_closed_graphic = pygame.image.load("./graphics/door_closed_cyber.png")
door_closed_graphic.convert_alpha()



run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # window.fill((255,255,255))
    window.fill((0,0,0))

    W = 'wall'
    F = 'floor'
    P = 'player'
    D = 'door_closed'
    tile_map = [[W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,W,W,W,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,F,F,F,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,F,F,F,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,F,F,F,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,F,F,F,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,F,F,F,D,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,W,W,W,W,W,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,W],
                [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W] ]

    tile_map[inst_player.y][inst_player.x] = P

    x = 0
    y = 0
    for h_row in tile_map:
        x = 0
        for tile in h_row:
            if tile == W:
                # pygame.draw.rect(window,
                #                  (192, 192, 192),
                #                  (x*inst_game_info.tile_size,
                #                   y*inst_game_info.tile_size,
                #                   inst_game_info.tile_size,
                #                   inst_game_info.tile_size)
                #                 )
                pygame.draw.rect(window,
                                 (107, 107, 107),
                                 (x*inst_game_info.tile_size,
                                  y*inst_game_info.tile_size,
                                  inst_game_info.tile_size,
                                  inst_game_info.tile_size)
                                )
            elif tile == P:
                window.blit(floor_graphic, (x*inst_game_info.tile_size, y*inst_game_info.tile_size))
                window.blit(player_graphic, (x*inst_game_info.tile_size, y*inst_game_info.tile_size))
            elif tile == F:
                window.blit(floor_graphic, (x*inst_game_info.tile_size, y*inst_game_info.tile_size))
            elif tile == D:
                window.blit(door_closed_graphic, (x*inst_game_info.tile_size, y*inst_game_info.tile_size))
            x += 1
        y += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if inst_player.x > 0:
            if tile_map[inst_player.y][inst_player.x-1] != W:
                inst_player.x -= inst_game_info.move
    if keys[pygame.K_RIGHT]:
        if inst_player.x < 19:
            if tile_map[inst_player.y][inst_player.x+1] != W:
                inst_player.x += inst_game_info.move
    if keys[pygame.K_UP]:
        if inst_player.y > 0:
            if tile_map[inst_player.y-1][inst_player.x] != W:
                inst_player.y -= inst_game_info.move
    if keys[pygame.K_DOWN]:
        if inst_player.y < 19:
            if tile_map[inst_player.y+1][inst_player.x] != W:
                inst_player.y += inst_game_info.move


    pygame.display.update()

    clock.tick(60) # limits FPS

pygame.quit()