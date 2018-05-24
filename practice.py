import os, random, pygame, time

def sound_play(path):
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play()
	get_sleep(1)

def get_sleep(get_time):
	time.sleep(get_time)


directory = os.path.dirname(os.path.abspath(__file__))+"\sounds\\"
# print(directory)

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
	random_hiragana = random.choice(list(hiragana_dict_copy.items()))
	sound_play(random_hiragana[1])
	answer = input("Give your answer:  ")
	if answer is random_hiragana[0]:
		point = point + 1
		print("Your point in this session "+ point)
	else:
		continue




