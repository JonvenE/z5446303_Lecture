
dates = [
  '2020-01-02', 
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600, 
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]


bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]




prc_ser = pd.Series(data=prices, index=dates)
# print(prc_ser)

bday_ser = pd.Series(data=bday, index=dates)
# print(bday_ser)


df = pd.DataFrame({'Close': prc_ser, 'bday': bday_ser})
# print(df)
# print(df.columns)
# print('The type of this column is', type(df.columns))


# col0 = df['Close']
# print(col0)

# col1 = df['bday']
# print(col1)


# print(col0.index)
# print(type(col0.index))

# print(df.index)
# print(type(df.index))



# df.columns = ['A', 'B']
# df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(df)


# df.columns = ['Close', 'Bday']
# df.index = [
#  '2020-01-02',
#  '2020-01-03',
#  '2020-01-06',
#  '2020-01-07',
#  '2020-01-08',
#  '2020-01-09',
#  '2020-01-10',
#  '2020-01-13',
#  '2020-01-14',
#  '2020-01-15',
# ]
# print(df)



new_ser = pd.Series(data=[1, 3, 2], index=['a', 'c', 'b'])
# print(new_ser)

#print(new_ser.is_monotonic_increasing) 


# sorted_ser = new_ser.sort_index()
# print(sorted_ser)
# print(new_ser)


#x = sorted_ser['a':'b']
#print(x) 
# Out:
# a    1
# b    2
# dtype: int64


#x = sorted_ser['b':'z'] 
#print(x) 
# Out:
# b    2
# c    3
# dtype: int64


ser_sort_inplace = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])


ser_sort_inplace.sort_index(inplace=True)
print(ser_sort_inplace)