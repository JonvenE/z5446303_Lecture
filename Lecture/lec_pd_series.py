


import pandas as pd


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


ser = pd.Series(data=prices, index=dates)

# print(dates.index('2020-01-02'))
# prc0 = prices[dates.index('2020-01-02')]
# print(prc0)


# prc1  = ser['2020-01-02']
# print(prc1)

# prcs  = ser['2020-01-06':'2020-01-10']
# print(prcs)



# ary  = ser.array
# print(ary)


# print(type(ser.array))


# the_index = ser.index
# print(the_index)


# print('The type of `the_index` is', type(the_index))


# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')


#ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000] 


# Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')


#print(ser) 

x  = '?'
#print(x) 


#print(ser[-4]) 


#print(prices[-4])