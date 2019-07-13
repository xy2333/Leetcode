import numpy as np
outputs = np.array([[556,160,780,661,1],[785,174,994,563,2],[339,151,547,552,3],[557,161,781,662,1]])
last = np.array([])
# last = np.array([[556,160,780,661,0]])
distance = []
for i in range(outputs.shape[0]):
	if last.shape[0] == 0:

		last = np.array([np.insert(outputs[i],5,[0,0])],dtype = 'float')
		distance.append(0)
	else:
		if outputs[i][4] not in last[:,4]:
			last = np.vstack([last,np.array([np.insert(outputs[i],5,[0,0])])])
			distance.append(0)
		else:
			index = np.where(last[:,4] == outputs[i][4])[0][0]
			center1 = np.array([(outputs[i][2]+outputs[i][0])/2,(outputs[i][1]+outputs[i][3])/2])
			center2 = np.array([(last[index][2]+last[index][0])/2,(last[index][1]+last[index][3])/2])
			print(center1-center2)
			move = np.sqrt(np.sum((center1-center2)*(center1-center2)))
			print(move)
			last[index][:4] = outputs[i][:4]
			last[index][5] += move
			distance.append(last[index][5])

print(last)
print(distance)
# a = np.where(last[:,4] == outputs[0][4])
# print(a[0][0])
# print('***************************')
# temp = last[last[:,4] == outputs[1:][4]]
# print(temp)