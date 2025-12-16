# FEMM Object-Oriented Wrapper (Python)

A lightweight object-oriented wrapper around **FEMM** designed to simplify finite element magnetic modeling by replacing sequential, procedural commands with a clean Python class-based interface.

---

## Overview

This project provides an object-oriented abstraction layer for FEMM using Python. It was originally developed to support the research paper:

Verdirame, J. M., Seaberg, C., Kwon Y., Nayfeh, K. S., Trumper, D. L., and Nayfeh, S. A., “A Survey of Passive Magnetic Springs,” American Society for Precision Engineering 40th Annual Meeting, San Diego, California, 2025.

The motivation behind this wrapper is to improve upon existing FEMM scripting approaches (such as octaveFEMM), which rely on primitive, sequential command execution and lack an object-oriented structure. By introducing classes such as models and magnetic bodies, this wrapper enables clearer, more maintainable, and more reusable FEMM simulations.

---

## Features

- Object-oriented interface for FEMM simulations
- Thin wrapper over existing FEMM functionality
- Designed for finite element magnet modeling
- Simplifies complex FEMM command sequences into intuitive method calls

> **Note:** This project is intentionally minimal. Its primary feature is the object-oriented wrapper itself.

---

## Tech Stack

- **Language:** Python  
- **Library:** `pyfemm`  
- **External Dependency:** FEMM (must be installed separately)

---

## Installation

Install the required Python dependency using pip:

```bash
pip install pyfemm
