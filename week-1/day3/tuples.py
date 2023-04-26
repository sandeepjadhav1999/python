names=('abc','wer','poi')
print(names)
print('--',type(names),'--')

names=tuple(['abc','wer','poi'])
print(names)
print('--',type(names),'--')

print(names.index('poi'))
print(names.count('abc'))
