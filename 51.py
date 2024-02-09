def same_by(characteristik, objects):
    return len(set(map(characteristik, objects))) < 2
 
    


values = [2, 20, 101, 6] 
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("diferent")