map = [800, 600]
polygon = [
    [167, 104],
    [257, 108],
    [333, 137],
    [327, 200],
    [274, 270],
    [203, 286],
    [144, 246],
    [101, 200]
]

shape = [
    [7, 9], [57, 156], [96, 194], [118, 128], [162, 99], [111, 43], [40, 236], [56, 282], [137, 238],
    [188, 160],
    [252, 103], [243, 51], [300, 59], [114, 35], [58, 352], [135, 357], [192, 277], [206, 214], [255, 155],
    [262, 214],
    [327, 132], [325, 195], [269, 265], [262, 313], [345, 241], [408, 214], [396, 155], [466, 158], [392, 86],
    [486, 61], [520, 110], [547, 77], [519, 161], [485, 212], [438, 275], [366, 319], [220, 365], [342, 371],
    [465, 339], [452, 395], [540, 313], [540, 257], [317, 426], [559, 401], [655, 349], [632, 210],
    [642, 274]]


def polygone(x_point, y_point, polygon):
    v_polygone = False

    x = x_point
    y = y_point
    for i in range(len(polygon)):
        x_poly = polygon[i][0]
        y_poly = polygon[i][1]
        xp_s_szadi = polygon[i - 1][0]
        yp_s_szadi = polygon[i - 1][1]
        if (((y_poly <= y and y < yp_s_szadi) or (yp_s_szadi <= y and y < y_poly)) and (
                x > (xp_s_szadi - x_poly) * (y - y_poly) / (yp_s_szadi - y_poly) + x_poly)):
            v_polygone = not v_polygone

    if v_polygone:
        print(f'v_poligone: {v_polygone},   point: {[x, y]}')


def points_(points):
    for point in points:
        x = point[0]
        y = point[1]
        polygone(x, y, polygon)


points_(shape)
