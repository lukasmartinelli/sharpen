import collections


def simplify_unix_path(path):
    dotstack = collections.deque()
    segments = path.split('/')
    simplified_segments = collections.deque()

    while len(segments) > 0:
        segment = segments.pop()
        if segment == '.' or segment == '':
            continue
        elif segment == '..':
            dotstack.append(segment)
        else:
            try:
                dotstack.pop()
            except IndexError:
                simplified_segments.appendleft(segment)

    return '/' + '/'.join(simplified_segments)


def test_path():
    assert simplify_unix_path('/a/../b/../') == '/'
    assert simplify_unix_path('/a/./b/../../c') == '/c'
    assert simplify_unix_path('/') == '/'
    assert simplify_unix_path('/a/../b/../c/../d') == '/d'
    assert simplify_unix_path('/var///log') == '/var/log'
    assert simplify_unix_path('/var/log/') == '/var/log'
