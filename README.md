# Eco-Router 🚗

Eco-Router is a modular Python engine that computes optimal driving routes for any city using real-world road network data from OpenStreetMap.

The project is designed with production-style architecture and manually implements Dijkstra’s algorithm for shortest-path computation.

## Features

- Works for **any configurable city**
- Downloads road networks using **OSMnx**
- Converts road data into **NetworkX graphs**
- Extracts **real edge distances**
- Saves graph locally to avoid repeated downloads
- Implements **Dijkstra’s algorithm from scratch**

## Project Structure

eco_router/

route_engine/
- graph_loader.py → downloads and caches road networks  
- dijkstra.py → manual shortest-path algorithm  

config.py → city configuration  
main.py → execution entry point

## Tech Stack

- Python
- OSMnx
- NetworkX
- OpenStreetMap Data

## Goal

To build a scalable backend routing engine similar to those used in logistics, ride-hailing, and navigation systems.
