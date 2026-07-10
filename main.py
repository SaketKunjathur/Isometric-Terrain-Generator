import pygame, sys, random
from perlin import Perlin
pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ISOMETRIC NOISE")
clock = pygame.time.Clock()

def load_atlas(atlas_path, imgs, scale):
    atlas = pygame.image.load(atlas_path).convert_alpha()
    w, h = atlas.get_width() // imgs[0], atlas.get_height() // imgs[1]
    img_list = []
    for x in range(imgs[0]):
        for y in range(imgs[1]):
            img = atlas.subsurface((x * w, y * h, w, h))
            if pygame.transform.average_color(img) != (0, 0, 0, 0):
                img = pygame.transform.scale(img, (w*scale[0], h*scale[1]))
                img_list.append(img)
    return img_list

tileset = load_atlas('tile_atlas.png', (15, 15), (2, 2))

# for y in range(len(render_map)-1, -1, -1):
#     for z in range(len(render_map[y])):
#         for x in range(len(render_map[y][z])):
#             win.blit(tileset[render_map[y][z][x]], idx_3d_to_iso((x, y, z), tileset[render_map[y][z][x]].get_size()))
def idx_3d_to_iso(idx, dimensions):
    x, y, z = idx
    w, h = dimensions
    a = 0.5 * w
    b = -0.5 * w
    c = 0.25 * h
    d = 0.25 * h
    x_ = (x * a + z * b) + (width / 2 - w / 2)
    y_ = (x * c + z * d) + 10
    for _ in range(y):
        y_ += h // 2
    return x_, y_

def idx_to_iso(idx, dimensions, ht):
    x, z = idx
    w, h = dimensions
    a = 0.5 * w
    b = -0.5 * w
    c = 0.25 * h
    d = 0.25 * h
    x_ = (x * a + z * b) + (width / 2 - w / 2)
    y_ = (x * c + z * d) - (height / 2 - h / 2) + (ht * h//2)
    return x_, y_

# render_map = np.zeros((2, 7, 7), dtype=int) # [
# #     [[0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0]], 
# #     [[0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0],
# #      [0, 0, 0, 0, 0, 0, 0]]
# # ]

p = Perlin(random.randint(0, 1000))

render_map = []
def populate_map(off):
    render = []
    for x in range(30):
        render.append([])
        for y in range(30):
            render[x].append([p.two(off[0] + x, off[1] + y), 0])

    return render

off = [0, 0]
speed = 1
render_map = populate_map(off)

font = pygame.font.Font(None, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill('white')
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        off[1] -= speed
    if keys[pygame.K_DOWN]:
        off[1] += speed
    if keys[pygame.K_LEFT]:
        off[0] -= speed
    if keys[pygame.K_RIGHT]:
        off[0] += speed
    render_map = populate_map(off)
    for x in range(len(render_map)):
        for y in range(len(render_map[x])):
            screen.blit(tileset[render_map[x][y][1]], idx_to_iso((x, y), tileset[render_map[x][y][1]].get_size(), render_map[x][y][0]))
    text = font.render(str(round(clock.get_fps())), False, (0, 0, 0))
    screen.blit(text, (0, 0))
    pygame.display.update()
    clock.tick(10000000)
