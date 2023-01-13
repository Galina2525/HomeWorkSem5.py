#Напишите программу, удаляющую из текста все слова, содержащие 'абв'
text = 'Какое абв чудное мгновабвенье мгновенье!'
text_ = text.split()
my_text = [word for word in text_ if 'абв' not in word]
print(*my_text)