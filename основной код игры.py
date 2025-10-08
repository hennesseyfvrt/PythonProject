# Основная программа игры
# Импортируем все функции из нашего модуля
from game_functions import *

def main():
    # Начинаем новую игру
    start_new_game()
    
    # Главный игровой цикл
    while True:
        # Очищаем экран
        print("\n" * 50)
        
        # Рисуем виселицу
        draw_hangman()
        print()
        
        # Показываем слово
        print("Слово:", get_hidden_word())
        print("Ошибки:", get_mistakes(), "/", get_max_mistakes())
        print("Использованные буквы:", get_used_letters())
        print()
        
        # Проверяем статус игры
        status = get_game_status()
        
        if status == "win":
            print("Поздравляем! Вы выиграли!")
            print("Загаданное слово:", current_word)
            break
        elif status == "lose":
            print("Игра окончена! Вы проиграли!")
            print("Загаданное слово было:", current_word)
            break
        
        # Получаем букву от игрока
        guess = input("Введите букву: ").strip()
        
        # Проверяем ввод
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву!")
            continue
        
        # Делаем ход
        result = make_guess(guess)
        
        # Обрабатываем результат
        if result == "already_used":
            print("Вы уже использовали эту букву!")
        elif result == "correct":
            print("Верно! Буква есть в слове!")
        elif result == "wrong":
            print("Неверно! Такой буквы нет в слове!")
        
        # Пауза перед следующим ходом
        input("Нажмите Enter для продолжения...")

# Запускаем игру
if __name__ == "__main__":
    main()