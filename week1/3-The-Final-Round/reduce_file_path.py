def reduce_file_path(path):
    path = path.split('..')
    is_two_points = False

    if len(path) > 1:
        is_two_points = True
        path = str(path[0])

    path = ''.join(path)
    path = path.split('.')
    path = ''.join(path)

    if path.count('/') > 1:
        path = path[::-1]
        while path[0] == '/' and path.count('/') > 1:
            path = path[1:]
    path = path[::-1]

    for i in range(len(path) - 1):
        if path[i] == '/' and path[i + 1] == '/':
            path = path[:i] + path[i + 1:]

    if is_two_points:
        path = path[::-1]
        while path[0] != '/':
            path = path[1:]
        path = path[::-1]

    return path

# print(reduce_file_path("/"))
# print(reduce_file_path("/srv/../"))
# print(reduce_file_path("/srv/www/htdocs/wtf/"))
# print(reduce_file_path("/srv/www/htdocs/wtf"))
# print(reduce_file_path("/srv/./././././"))
# print(reduce_file_path("/etc//wtf/"))
# print(reduce_file_path("/etc/../etc/../etc/../"))
# print(reduce_file_path("//////////////"))
# print(reduce_file_path("/../"))
