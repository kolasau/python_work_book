print("------------ЗАГАДКА------------")
start = "Напиши 'старт' и нажми Enter: "
x1 = "\n\t\tКрасные двери в пещере ****"
x2 = "Белые звери сидят у ******"
x3x4 = "\t\tИ мясо и хлеб – всю добычу мою\n\t\tЯ с радостью белым зверям *****"
full = "\nА ТЕПЕРЬ ОТГАДАЙ ЗАГАДКУ:\n\n\t\tКрасные двери в пещере моей\n\t\tБелые звери сидят у дверей." \
	   "\n\t\tИ мясо и хлеб – всю добычу мою\n\t\t" \
	   "Я с радостью белым зверям отдаю"
full2 = "\n\t\tКрасные двери в пещере моей\n\t\tБелые звери сидят у дверей." \
	   "\n\t\tИ мясо и хлеб – всю добычу мою\n\t\t" \
	   "Я с радостью белым зверям отдаю"
x5 = "Ответ состоит из двух слов '****' и '****'\n"
x6 = ""
answer = "губы и зубы"

while True:
	message = input(start)

	if message == 'старт':
		print("\nУгадывай слово вместо звёздочек(*****), чтобы прочитать загадку полностью")
		break
	else:
		print('---------------------------------------------------------------------------')

while True:
	print(x1)
	message1 = input("\t\t\t\t\t\t\tОТВЕТ: ")
	if message1 == 'моей':
		print('---------------------------------------------------------------------------')
		print(f"\n\t\tКрасные двери в пещере моей,\n\t\t{x2}")
		break
	else:
		print('---------------------------------------------------------------------------')
		print("\nИз всех глупостей, что можно было написать, эта — шедевр...")

while True:
	message2 = input("\t\t\t\t\t\t\tОТВЕТ: ")

	if message2 == 'дверей':
		print('---------------------------------------------------------------------------')
		print(f"\n\t\tКрасные двери в пещере моей,\n\t\tБелые звери сидят у дверей.\n{x3x4}")
		break
	else:
		print('---------------------------------------------------------------------------')
		print("\nРодиться глупым не стыдно; стыдно только умирать глупцом.")
		print(f"\n\t\tКрасные двери в пещере моей\n\t\t{x2}")

while True:
	message3 = input("\t\t\t\t\t\t\tОТВЕТ: ")

	if message3 == 'отдаю':
		print('---------------------------------------------------------------------------')
		print(full)
		break
	else:
		print('---------------------------------------------------------------------------')
		print("\n... глупость уже не выглядит глупо, когда ее без стыда,\nна виду у всех совершает неглупый человек.")
		print(f"\n\t\tКрасные двери в пещере моей,\n\t\tБелые звери сидят у дверей.\n{x3x4}")

while True:
	message4 = input("\t\t\t\t\t\t\tОТВЕТ: ")

	if message4.lower() == 'губы и зубы' or message4.lower() == 'зубы и губы':
		print('---------------------------------------------------------------------------')
		print(f"\n\t\t\t\tУРАААА!!!\n\t\tДа, правильный ответ: {answer.title()}\n"
			  f"\n\t\tОсновное правило для сохранения здоровой прекрасной улыбки"
			  f"\n\t\tв течение всей жизни - это соблюдение правил гигиены полости рта!")
		break
	else:
		print('---------------------------------------------------------------------------')
		print("\nСтоит мне подумать, что ещё тупее ты быть не можешь,"
			  "\nкак ты делаешь такое... что возвращает тебе твоё доброе имя!")
		print(f"\n{x5}")
		print(full2)