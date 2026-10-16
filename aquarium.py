import os, random, time, shutil
FISH_R = ["><>", "><(((°>", "><))°>", "><>>"]
FISH_L = ["<><", "<°)))><", "<°((><", "<<><"]
class Fish:
    def __init__(s, w, h):
        s.dir = random.choice([1, -1]); s.y = random.randint(1, h - 3)
        s.x = 0 if s.dir == 1 else w - 8; s.i = random.randrange(4); s.speed = random.choice([1, 1, 2])
    def body(s): return (FISH_R if s.dir == 1 else FISH_L)[s.i]
def main():
    w, h = shutil.get_terminal_size((80, 24)); h -= 1
    fish = [Fish(w, h) for _ in range(6)]; bubbles = []
    try:
        while True:
            grid = [[" "] * w for _ in range(h)]
            grid[h - 1] = list(("~^~" * w)[:w])
            for f in fish:
                f.x += f.dir * f.speed
                if f.x < -8 or f.x > w: f.__init__(w, h)
                for k, c in enumerate(f.body()):
                    if 0 <= f.x + k < w: grid[f.y][f.x + k] = c
                if random.random() < 0.05: bubbles.append([f.x, f.y - 1])
            for b in bubbles: b[1] -= 1
            bubbles = [b for b in bubbles if b[1] > 0]
            for x, y in bubbles:
                if 0 <= x < w: grid[y][x] = random.choice("oO.")
            os.system("cls" if os.name == "nt" else "clear")
            print("\n".join("".join(r) for r in grid)); time.sleep(0.12)
    except KeyboardInterrupt: print("\n再见，小鱼们 🐟")
if __name__ == "__main__": main()
