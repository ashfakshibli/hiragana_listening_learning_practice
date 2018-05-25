import os, random, pygame, time

def sound_play(path):
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play()
	get_sleep(1)

def get_sleep(get_time):
	time.sleep(get_time)

def get_selection():
	input_digit = ''
	while input_digit is not int:
		try:
			input_digit = int(input("1. Next Character \n2. Reset \n3. Exit\n"))
			break
		except:
			print("Invalid Input. Select Again.")
	return input_digit
		
	



directory = os.path.dirname(os.path.abspath(__file__))+"\sounds\\"
print("Initializing...")

hiragana_dict = {}

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	filename_without_ext = os.path.splitext(filename)[0]
	if filename.endswith(".mp3"): 
		hiragana_dict[filename_without_ext] = directory+filename
	else:
		continue


hiragana_dict_copy = hiragana_dict
point = 0
while True:
	if not hiragana_dict_copy:
		print("Congratulations! You have mastered all Hiragana Characters. Ending Session")
		break
	print("Listen...")
	random_hiragana = random.choice(list(hiragana_dict_copy.items()))
	random_hiragana_ch = random_hiragana[0]
	random_hiragana_path = random_hiragana[1]
	sound_play(random_hiragana_path)
	answer = input("Give your answer:  ")	
	if answer == random_hiragana_ch:
		point = point + 1
		print("Right, Your point "+ str(point))
		del hiragana_dict_copy[random_hiragana_ch]
	else:
		print("Wrong, Correct answer is \""+random_hiragana_ch+"\"\nYour point "+ str(point))

	selection = get_selection()

	if selection == 1:
		continue
	elif selection == 2:
		print("Resetting...")
		hiragana_dict_copy = hiragana_dict
		point = 0
	else:
		print("Your total point in this session "+ str(point)+"\nSee you soon...")
		break




