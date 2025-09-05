# ♟️ Project Chess

A full-featured chess game built in Python using Pygame, featuring a custom AI opponent powered by the Minimax algorithm. Designed for both casual play and technical exploration, this project blends strategic gameplay with clean GUI design and intelligent move logic.

![Chess Game Demo](https://github.com/RAHUL8489XX/Project-Chess/assets/demo.gif) <!-- Replace with your actual GIF URL -->

---

## 🚀 Features

- 🎨 **Graphical Interface** built with Pygame
- ♟️ **All major pieces**: Pawn, Rook, Knight, Bishop, Queen, King
- 🔄 **Turn-based play**: Human (White) vs AI (Black)
- 🧠 **AI opponent** using Minimax (depth 2)
- 🟩 **Move highlighting** for selected pieces
- ❌ **Piece capture** with visual removal
- 👑 **King movement** and basic check detection
- 📦 Modular codebase: `main.py`, `board.py`, `pieces.py`, `ai.py`

---

## 📽️ Gameplay Animation

> Add a short gameplay GIF showing piece movement, AI response, and captures.  
> You can record using OBS or ScreenToGif and upload to your GitHub repo’s assets.

---

## 💻 Requirements

| Component     | Version / Notes         |
|---------------|--------------------------|
| Python        | 3.8 or higher            |
| Pygame        | `pip install pygame`     |
| OS            | Windows, macOS, Linux    |
| RAM           | 2GB+ recommended         |

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/RAHUL8489XX/Project-Chess.git
cd Project-Chess

pip install pygame

```

---

## 🧠 AI Strategy

The AI opponent is powered by a custom implementation of the **Minimax algorithm**, which simulates future moves and evaluates board positions to choose the optimal path. Key features include:

- Recursive move simulation up to a configurable depth
- Piece-based scoring system (pawn = 1, queen = 9, king = 1000, etc.)
- Capture-aware decision-making
- Expandable to include alpha-beta pruning and positional heuristics

You can adjust the depth in `make_ai_move()` to control difficulty:

```python
_, best_move = minimax(self.board, depth=2, maximizing_player=False)

```

## 📄 License
This project is licensed under the MIT License. You’re free to use, modify, and distribute this code for personal or commercial projects — just keep the original credits intact.
## 👨‍💻 Author
Rahul Yogi 
🎓 BCA Student at Podar Group of Institutions 💻 Python Developer | Chess Enthusiast | AI Explorer 📍 Jaipur, India 🔗 LinkedIn • GitHub
