# TheBrickWall

Python solution for the The Brick Wall problem.

## Problem

A wall is made using Red and Green bricks of different lengths.

- Red bricks cannot be broken.
- Green bricks can be broken.
- The goal is to connect the source and destination pipes by breaking the minimum number of Green bricks.

## Approach

The wall is converted into a grid by expanding the compressed brick notation.

A pathfinding algorithm is then used to find the minimum number of Green bricks that need to be broken while avoiding Red bricks.

## Language

Python 3
