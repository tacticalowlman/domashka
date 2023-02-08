from random import choice, random


def rps(human_hand, computer_hand):
	global counter_computer, counter_human
	if human_hand == computer_hand:
		print('Ничья!')
	elif human_hand == 'r' and computer_hand == 'p':
		print('Вы проиграли!')
		counter_computer += 1
	elif human_hand == 'r' and computer_hand == 's':
		print('Вы победили!')
		counter_human += 1
	elif human_hand == 'p' and computer_hand == 'r':
		print('Вы победили!')
		counter_human += 1
	elif human_hand == 'p' and computer_hand == 's':
		print('Вы проиграли!')
		counter_computer += 1
	elif human_hand == 's' and computer_hand == 'r':
		print('Вы проиграли!')
		counter_computer += 1
	elif human_hand == 's' and computer_hand == 'p':
		print('Вы победили!')
		counter_human += 1


counter_human = 0
counter_computer = 0

while True:
	print(f'Текущий счет: компьютер - {counter_computer} человек - {counter_human}')
	human_hand = input('Введите свой знак p / r / s: ')
	computer_hand = choice(['p', 'r', 's'])
	print(f'Ваш знак - {human_hand} знак компьютера - {computer_hand}')
	rps(human_hand, computer_hand)
	if counter_human == 3 or counter_computer == 3:
		if counter_human == 3:
			print(f'Победил человек! Со счетом {counter_human} - {counter_computer}')
		if counter_computer == 3:
			print(f'Победил компьютер! Со счетом {counter_human} - {counter_computer}')
		if input('Продолжить игру? да/нет: ') == 'да':
			counter_human = 0
			counter_computer = 0
		else:
			break