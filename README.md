# Isometric-Terrain-Generator

A 2D isometric terrain generator, inspired by Minecraft's approach to world generation built using Python.

---

## About

This project gets terrain heights using the perlin library, then renders the result as an isometric grid. For every point in the grid, a Perlin noise value determines the height of the terrain at that point, and isometric projection math converts those grid/height coordinates into the correct 2D screen-space position for each tile giving the classic angled, layered look of isometric games.

## Stack

* Python
* Pygame
* Perlin
