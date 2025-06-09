# Snake Game

A modern, responsive Snake Game built with Python (Flask) and HTML5 Canvas. Control the snake to eat food and grow longer while avoiding collisions with the walls and yourself.

![Snake Game Screenshot](https://via.placeholder.com/400x400/0f3460/4cc9f0?text=Snake+Game)

## Features

- 🎨 Modern and responsive UI with smooth animations
- 🕹️ Intuitive controls (arrow keys or WASD)
- 📱 Touch controls for mobile devices
- 📊 Score tracking
- 🔄 Game over detection with restart option
- 🌈 Stylish gradient background and visual effects

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

- Use the **arrow keys** or **WASD** to control the snake's direction
- On mobile devices, **swipe** in the direction you want to move
- Eat the food (colored square) to grow longer and increase your score
- Avoid hitting the walls or yourself
- Try to achieve the highest score possible!

## Project Structure

```
snake-game/
├── app.py            # Flask backend with game logic
├── requirements.txt   # Python dependencies
└── templates/
    └── index.html    # Frontend (HTML, CSS, JavaScript)
```

## Dependencies

- Flask 2.0.3 - Web framework
- Werkzeug 2.0.3 - WSGI utility library
- python-dotenv 0.19.0 - Environment variable management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with ❤️ using Flask and vanilla JavaScript
- Inspired by the classic Snake game
- Special thanks to all contributors!
