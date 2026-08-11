# 🐍💧🔫 Snake Water Gun Game

A feature-packed terminal implementation of the classic **Snake, Water, Gun** game built in Python. This project compares standard conditional decision structures against an optimized 2D matrix lookup mechanism.

---

## 🚀 Key Features & Architectural Highlights

### 1. Dual Implementation Approaches
* **Conditional Logic (`normal_version.py`):** Uses standard `if-elif-else` control flow to evaluate game rules and determine winners.
* **Matrix Lookup Optimization (`efficent_version.py`):** Utilizes **Label Encoding** (mapping categorical inputs `['s', 'w', 'g']` to numerical indices `[0, 1, 2]`) and a **2D Matrix/Lookup Table** to retrieve game results in $O(1)$ constant time without branching conditional statements.

### 2. Custom Game Mechanics (Designed & Feature-Engineered)
* **Custom Series Formats:** Choose between **Best of 1**, **Best of 3**, or **Best of 5** series modes. The game dynamically calculates majority wins needed to lock in a series victory.
* **Robust Input Validation:** Continuous validation loops for start prompts, format selections, and player inputs to gracefully handle invalid/nonsense inputs.
* **Live Scoreboard Tracking:** Tracks scores dynamically across rounds until a series winner is determined.
* **Replay Option:** After a series ends, players can immediately restart without re-running the program.
* **Modular Functions:** Core logic (round play, input handling, format selection) is encapsulated into reusable functions for cleaner structure and easier maintenance.

---

## 🎮 Rules of the Game

| Choice 1 | Choice 2 | Outcome |
| :--- | :--- | :--- |
| **Snake** 🐍 | **Water** 💧 | Snake drinks Water $\rightarrow$ **Snake Wins** |
| **Water** 💧 | **Gun** 🔫 | Water rusts/drowns Gun $\rightarrow$ **Water Wins** |
| **Gun** 🔫 | **Snake** 🐍 | Gun shoots Snake $\rightarrow$ **Gun Wins** |
| **Same Choice** | **Same Choice** | Match Draw $\rightarrow$ **Tie** |

---
