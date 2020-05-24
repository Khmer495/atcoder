import sys
inf = 10**9
sys.setrecursionlimit(inf)


def connect(signs, to_room, from_room):
    signs[to_room][2].add(from_room)
    signs[from_room][2].add(to_room)
    return signs


def update(signs, to_room, from_room):
    """
    1. fromの距離を記憶
    2. fromの行き先を記憶
    3. toの来るリストにfromを追加
    4. fromの行き先にtoを追加
    5. fromの距離をto+1に変更
    6. もともとのfromの距離がinfなら
        a. fromの来るリスト(fromfrom)の行き先をfromにする
        b. fromfromの来るリストからfromを削除
        c. 1から始める
    7. fromの新しい距離がもともとのfromの行き先(fromto)の距離がより短いなら、
        a. 1から始める
    """
    # from_room_dist = signs[from_room][0]
    # from_to_rooms = signs[from_room][1]
    # signs[to_room][2].add(from_room)
    # signs[to_room][2].discard(from_room)
    signs[from_room][0] = signs[to_room][0] + 1
    signs[from_room][1] = to_room
    # signs[from_room][2].discard(to_room)
    for from_from_room in signs[from_room][2]:
        if signs[from_room][0] < signs[from_from_room][0] - 1:
            signs = update(signs, from_room, from_from_room)
    # if from_room_dist == inf:
    #     for from_from_room in signs[from_room][1]:
    #         signs[from_from_room][1].discard(from_room)
    #         signs = update(signs, from_room, from_from_room)
    for from_to_room in signs[from_room][2]:
        if from_to_room and signs[from_room][0] < signs[from_to_room][0] - 1:
            signs = update(signs, from_room, from_to_room)
        # print(signs)
    return signs


def main():
    n, m, *ab = map(int, open(0).read().split())
    ab = [ab[2 * i:2 * (i + 1)] for i in range(m)]

    to = [[] for _ in range(n)]
    for a, b in ab:
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)

    dist = [inf] * n
    pre = [None] * n
    queue = [0]
    while queue:
        v = queue.pop(0)
        for u in to[v]:
            if dist[u] != inf:
                continue
            dist[u] = dist[v] + 1
            pre[u] = v
            queue.append(u)

    pre = [i + 1 for i in pre]
    ans = '\n'.join([str(i) for i in ['Yes'] + pre[1:]])

    print(ans)
    return(ans)


if __name__ == '__main__':
    main()
