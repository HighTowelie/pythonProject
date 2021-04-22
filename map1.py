def get_distance(point):
    x = point[0]
    y = point[1]
    return (x ** 2 + y ** 2) ** 0.5

lambda point: (point[0] ** 2 + point[1] ** 2) ** 0,5

if __name__ == '__main__':
    pts = [
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]

    print(max(map(get_distance, pts)))


    aw = [(number_1[0] ** 2 + number_1[1] ** 2) ** 0.5 for number_1 in pts]
    print(max(aw))
    print(max(map(lambda point: (point[0] ** 2 + point[1] ** 2) ** 0.5, pts)))