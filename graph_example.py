from collections import deque


def search_mango_seller():
    search_queue = deque()

    graph = {'you': ['alice', 'bob', 'claire', 'mango'],
             'alice': ['malkol', 'jack', 'rassel'],
             'jack': ['alice', 'bob', 'smith']
             }

    search_queue += graph['you']

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is mango seller!')
                return True
            elif person in graph:
                search_queue += graph[person]
                searched.append(person)
    print(graph)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


search_mango_seller()

