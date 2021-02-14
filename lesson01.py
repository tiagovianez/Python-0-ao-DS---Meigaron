# carregue o conjunto de dados chamado kc_house.csv do HD para a memoria

#funcao - head.csv()

#biblioteca - pandas

import pandas as pd

data = pd.read_csv ( 'datasets/kc_house_data.csv' )

#1. mostre todas as linhas do conjunto de dados
print( data.head )

#2. mostre os atributos da casa
#print ( data.columns )

#3. mostre qual a casa mais cara
#print ( data [['id', 'price']].sort_values ( 'price', ascending=False) )

#4. mostre a casa com o maior numero de quartos
#print( data [['id', 'bedrooms']].sort_values( 'bedrooms', ascending=False))

#5. mostre a soma do total de quartos do conjunto de dados
#print (data ['bedrooms'].sum())

#7 quantas casas possuem apenas 2 banheiros
#print(data[data['bathrooms']==2].shape)

#8 qual o preco medio de todas as casas do conjunto de dados?
#print(data['price'].mean())

#9 preço medio de casas com 2 banheiros
#print(data.loc[data['bathrooms']==2, 'price'].mean())

#10 qual o preco minimo entre as casas com 3 quartos
#print(data.loc[data['bedrooms']==3, 'price'].min())

#11 quantas casas possuem mais de 300m2 na sala de estar
#data['m2_living']=data['sqft_living']*0,092 print(data['m2_living']>300].shape))

#12 quantas casas tem mais de 2 andares
#print(data[data['floors']>2].shape)

#13 quantas casas tem vista para o mar
#print(data[data['waterfront']==1].shape)

#14 das casas com vista para o mar, quantas tem 3 quartos?
#print(data[(data['waterfront']==1)&(data['bedrooms']==3)].shape)

#15 das salas com mais de 300m2 de sala de estar, quantas tem mais de 2 banheiros?
#print(data[(data['m2_living']>300)&(data['bathrooms']>2)].shape)










