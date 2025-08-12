# Martian Robots Challenge

This is my take on the Martian Robots coding challenge.

The idea is simple: there’s a grid (the “planet”) and a bunch of robots starting at different spots, each with a set of movement commands. The program moves each robot one step at a time.  
If a robot walks off the edge, it’s marked as LOST and the spot it fell from gets a “scent” so the next robot knows not to make the same mistake.

---

## Running the tests

The whole thing is tested using Python’s built-in `unittest`.  
The tests send input directly into the program, so you don’t need any extra files.

Run all tests with:

```bash
python -m unittest test_martian_robots.py
