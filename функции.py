import random

# Глобальные переменные
current_word = ""
hidden_word = []
used_letters = []
mistakes = 0
max_mistakes = 6

def start_new_game():
    """Начинает новую игру"""
    global current_word, hidden_word, used_letters, mistakes
    
    # Читаем слова из файла
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    
    # Выбираем случайное слово
    current_word = random.choice(words).upper()
    
    # Создаем скрытое слово (буквы заменены на _)
    hidden_word = ['_' for _ in current_word]
    
    # Очищаем использованные буквы и ошибки
    used_letters = []
    mistakes = 0

def make_guess(letter):
    """Проверяет букву и обновляет игру"""
    global mistakes
    
    letter = letter.upper()
    
    # Если буква уже использовалась
    if letter in used_letters:
        return "already_used"
    
    # Добавляем букву в использованные
    used_letters.append(letter)
    
    # Если буква есть в слове
    if letter in current_word:
        # Показываем все такие буквы в слове
        for i, char in enumerate(current_word):
            if char == letter:
                hidden_word[i] = letter
        return "correct"
    else:
        # Увеличиваем счетчик ошибок
        mistakes += 1
        return "wrong"

def is_game_won():
    """Проверяет, выиграл ли игрок"""
    return '_' not in hidden_word

def is_game_lost():
    """Проверяет, проиграл ли игрок"""
    return mistakes >= max_mistakes

def get_hidden_word():
    """Возвращает текущее состояние слова"""
    return ' '.join(hidden_word)

def get_used_letters():
    """Возвращает использованные буквы"""
    return ', '.join(used_letters)

def get_mistakes():
    """Возвращает количество ошибок"""
    return mistakes

def get_max_mistakes():
    """Возвращает максимальное количество ошибок"""
    return max_mistakes

def draw_hangman():
    """Рисует виселицу в зависимости от количества ошибок"""
    hangman_parts = [
        "  _____",
        "  |   |",
        "  |   O",
        "  |  /|\\",
        "  |  / \\",
        "__|__"
    ]
    
    # Показываем только те части, которые соответствуют ошибкам
    for i in range(min(mistakes, len(hangman_parts))):
        print(hangman_parts[i])
    
    # Дополняем пустыми строками для красивого отображения
    for i in range(mistakes, len(hangman_parts)):
        print()

def get_game_status():
    """Возвращает статус игры"""
    if is_game_won():
        return "win"
    elif is_game_lost():
        return "lose"
    else:
        return "playing"