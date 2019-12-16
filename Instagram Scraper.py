#creating the final dataframe and collecting the amount of followers and posts each user has
from igramscraper.instagram import Instagram
import pandas as pd
import numpy as np
instagram = Instagram()

#A website showing most followed Instagram users.
#https://www.trackalytics.com/the-most-followed-instagram-profiles/page/5/

#reading in the file containing all the usernames
df_names = pd.read_csv('Instagram Usernames.csv')

#creating new excel sheet and transfering all usernames over
df = pd.DataFrame(columns = ['Usernames', 'Followers', 'Posts', 'Gender', 'Link to photo', 'Photo likes', 'Photo comments',
                             'Framing', 'Background', 'Headwear', 'Hair style', 'Hair color', 'Eye color',
                             'Facial piercings', 'Earrings', 'Smile', 'Teeth', 'Facial hair', 'Glasses', 'Eye shadow color',
                             'Lipstick color', 'Makeup', 'Clothes', 'Cleavage', 'Necklace', 'Tattoos'])

df['Usernames'] = df_names['Usernames']

#removing the @ in front of usernames
df['Usernames'] = df['Usernames'].str[1:]

#loop
for i in range(len(df)):
    
    #prints the account username it has completed
    print(account.username)
    
    #Locating the username on instagram
    account = instagram.get_account(df['Usernames'][i])

    #getting the number of followers the user has and adding them to the data frame
    df['Followers'][i] = account.followed_by_count
    
    #getting the number of posts the user has and adding them to the data frame
    df['Posts'][i] = account.media_count
    
#saves dataframe to computer
df.to_csv(r'C:\')#insert file directory
