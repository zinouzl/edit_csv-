import pandas as pd

train_df = pd.read_csv('/home/zinou/Desktop/Tensor/train1.csv')
dev_df = pd.read_csv('/home/zinou/Desktop/Tensor/dev1.csv')
test_df = pd.read_csv('/home/zinou/Desktop/Tensor/test1.csv')

listext = train_df['wav_filename']
#print(len(listext))
k=[]
print('manupilation of training data')
for i in listext:
	i=i.replace('C:\\android\\audio\\Main','/home/zinou/Desktop').replace('\\','/')
	k+=[i]

train_df['wav_filename'] = k	
train_df.to_csv('/home/zinou/Desktop/Tensor/train.csv',index=False)
print('end of manupiliting trainig data')
print('....')
print('starting dev data')
listext = dev_df['wav_filename']
k=[]
for i in listext:
	i=i.replace('C:\\android\\audio\\Main','/home/zinou/Desktop').replace('\\','/')
	k+=[i]
dev_df['wav_filename']=k
dev_df.to_csv('/home/zinou/Desktop/Tensor/dev.csv',index=False)	
print('end manupilating dev data')
print('.....')
print('starting manupilation of testing data')
listext = test_df['wav_filename']
k=[]
for i in listext:
	i=i.replace('C:\\android\\audio\\Main','/home/zinou/Desktop').replace('\\','/')	
	k+=[i]
test_df['wav_filename'] = k
test_df.to_csv('/home/zinou/Desktop/Tensor/test.csv',index=False)
print('end manupilation of test data ')
print('end of script bye!')
