x = float(input())
y = float(input())
h = float(input())
side_walls = 2*(x*y)
side_windows = 2*(1.5*1.5)
side_total = side_walls - side_windows
fb_walls = 2*(x*x)
door = 1.2*2
fb_total = fb_walls - door
total = side_total + fb_total
green_paint = total / 3.4
print(f'{green_paint:.2f}')

roof_rect = 2*(x*y)
roof_tria = 2*(x*h/2)
roof_total=roof_rect + roof_tria
red_paint = roof_total /4.3
print(f'{red_paint:.2f}')