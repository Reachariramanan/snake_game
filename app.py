from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)

# Game state
game_state = {
    'snake': [[200, 200], [190, 200], [180, 200]],  # Start from center
    'food': [100, 100],
    'direction': 'RIGHT',
    'score': 0,
    'game_over': False
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game_state')
def get_game_state():
    return jsonify(game_state)

@app.route('/update_direction', methods=['POST'])
def update_direction():
    data = request.json
    current_direction = game_state['direction']
    new_direction = data['direction']
    
    # Prevent 180-degree turns
    if (current_direction == 'UP' and new_direction != 'DOWN' or
        current_direction == 'DOWN' and new_direction != 'UP' or
        current_direction == 'LEFT' and new_direction != 'RIGHT' or
        current_direction == 'RIGHT' and new_direction != 'LEFT'):
        game_state['direction'] = new_direction
    
    return jsonify({'status': 'success'})

def move_snake():
    if game_state['game_over']:
        return
        
    head = game_state['snake'][0].copy()
    
    # Move head based on direction
    if game_state['direction'] == 'UP':
        head[1] -= 20
    elif game_state['direction'] == 'DOWN':
        head[1] += 20
    elif game_state['direction'] == 'LEFT':
        head[0] -= 20
    elif game_state['direction'] == 'RIGHT':
        head[0] += 20
    
    # Check for collisions with walls or self
    if (head[0] < 0 or head[0] >= 400 or 
        head[1] < 0 or head[1] >= 400 or
        head in game_state['snake']):
        game_state['game_over'] = True
        return
    
    # Move snake
    game_state['snake'].insert(0, head)
    
    # Check if food is eaten
    if (abs(head[0] - game_state['food'][0]) < 10 and 
        abs(head[1] - game_state['food'][1]) < 10):
        game_state['score'] += 10
        place_food()
    else:
        # Remove tail if no food is eaten
        game_state['snake'].pop()

def place_food():
    while True:
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        if [x, y] not in game_state['snake']:
            game_state['food'] = [x, y]
            break

@app.route('/update')
def update():
    move_snake()
    return jsonify(game_state)

@app.route('/reset')
def reset():
    game_state['snake'] = [[200, 200], [190, 200], [180, 200]]  # Reset to center
    game_state['direction'] = 'RIGHT'
    game_state['score'] = 0
    game_state['game_over'] = False
    place_food()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    place_food()
    app.run(debug=True)
