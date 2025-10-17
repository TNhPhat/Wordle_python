import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.dont_write_bytecode = True
from engine.game_engine import game_engine

def main():
    engine = game_engine()
    engine.run()

if __name__ == "__main__":
    main()