driving = input('請問你有沒有開過車？')
if driving != '有' or driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit #這裡回答錯可以讓程式強制終止／離開
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('請配合警方調查')
elif driving == '沒有':
	if age >= 18:
		print('你可以學開車')
	else:
		print('你很乖誒')
