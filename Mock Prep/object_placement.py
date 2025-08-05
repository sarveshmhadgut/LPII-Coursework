import heapq
import os
from copy import deepcopy

ROOM_WIDTH, ROOM_HEIGHT = 6, 7

RECT_OBJ = [(f"r{i+1}", (3, 2)) for i in range(5)]
SQUARE_OBJ = [(f"s{i+1}", (2, 2)) for i in range(4)]
ALL_OBJECTS = RECT_OBJ + SQUARE_OBJ


class Node:
    def __init__(self, room, remaining_objects, placed, g):
        self.room = room
        self.remaining_objects = remaining_objects
        self.placed = placed
        self.g = g
        self.h = len(remaining_objects) * 5
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f


def can_place(room, width, height, x, y):
    if x + width > ROOM_WIDTH or y + height > ROOM_HEIGHT:
        return False
    for dx in range(width):
        for dy in range(height):
            if room[y + dy][x + dx] != "":
                return False
    return True


def place_object(room, label, width, height, x, y):
    new_room = deepcopy(room)
    for dx in range(width):
        for dy in range(height):
            new_room[y + dy][x + dx] = label
    return new_room


def astar_place_objects():
    initial_room = [[""] * ROOM_WIDTH for _ in range(ROOM_HEIGHT)]
    start_node = Node(initial_room, ALL_OBJECTS, [], 0)
    frontier = []
    heapq.heappush(frontier, start_node)

    while frontier:
        current = heapq.heappop(frontier)

        if not current.remaining_objects:
            return current.room, current.placed

        label, (w, h) = current.remaining_objects[0]
        rest = current.remaining_objects[1:]

        for y in range(ROOM_HEIGHT):
            for x in range(ROOM_WIDTH):
                for w_try, h_try in [(w, h), (h, w)]:
                    if can_place(current.room, w_try, h_try, x, y):
                        new_room = place_object(current.room, label, w_try, h_try, x, y)
                        new_node = Node(
                            new_room,
                            rest,
                            current.placed + [(label, x, y, w_try, h_try)],
                            current.g + 1,
                        )
                        heapq.heappush(frontier, new_node)

    return None, None


print("Processing...")
final_room, placements = astar_place_objects()
os.system("clear")

if final_room:
    print("Final Room Layout:")
    for row in final_room:
        print(" ".join(cell.rjust(3) if cell else " . " for cell in row))

    print("\nObject Placements:")
    for label, x, y, w, h in placements:
        print(f"{label}: at ({x},{y}) size ({w}×{h})")
else:
    print("No arrangement possible.")
