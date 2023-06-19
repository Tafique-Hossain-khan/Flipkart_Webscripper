import pandas as pd
import requests 
from bs4 import BeautifulSoup
import numpy as np


def scrab(iteam):

    links=[]
    name=[]
    price=[]
    rating = []
    product_offer = []
    seller_name=[]
    seller_rating=[]
    final = pd.DataFrame()
    

    for j in range(1,10): # to iterate in multiple page
        url = f'https://www.flipkart.com/search?q={iteam}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={j}'
        html = requests.get(url).text 
        soup = BeautifulSoup(html,'html.parser')

        #for the grid page
        big_box_grid=[]
        grid_box = soup.find_all('div',class_='_13oc-S')
        for i in grid_box: #finding the big_box from the grid
            big_box_grid.append(i.div.div.a['href']) #this is similar to the bixbox for here we well get the link

        #getting the link from the boxes
        for k in big_box_grid:
            links.append('https://www.flipkart.com'+k)

        

    if len(big_box_grid) != 0:   

        for i in links:
            product_html = requests.get(i).text
            soup_html = BeautifulSoup(product_html,'html.parser')
            try:
                name.append(soup_html.find('span',class_='B_NuCI').text)
            except:
                name.append(np.nan)
            try:
               price.append(soup_html.find('div',class_='_30jeq3 _16Jk6d').text)
            except:
                price.append(np.nan)
            try:
                rating.append(soup_html.find('div',class_='_3LWZlK').text)
            except:
                rating.append(np.nan)
            try:
                product_offer.append(soup_html.find('div',class_='_3Ay6Sb _31Dcoz').text)
            except:
                product_offer.append(np.nan)
            try:
                seller_name.append(soup_html.find('div',class_='_1RLviY').text)
            except:
                seller_name.append(np.nan)
            try:
                seller_rating.append(soup_html.find('div',class_='_3LWZlK _1D-8OL').text)
            except:
                seller_rating.append(np.nan)
                
        df = pd.DataFrame({'product_name':name,'price':price,'rating':rating,'product_offer':product_offer,'seller_name':seller_name,'seller_rating':seller_rating})
        final = pd.concat([final,df],ignore_index=True)
        
        links.clear()
        name.clear()
        price.clear()
        rating.clear()
        product_offer.clear()
        seller_name.clear()
        seller_rating.clear()
        big_box_grid.clear()
        
        
        
    else:
        bigbox1 = soup.find_all('div',class_='_2kHMtA')
        for i in bigbox1:
            links.append('https://www.flipkart.com'+i.a['href'])

        for i in links:
            product_html = requests.get(i).text
            soup = BeautifulSoup(product_html,'html.parser')
            
            try:
                name.append(soup.find('span',class_='B_NuCI').text)
            except:
                name.append(np.nan)
            try:
                price.append(soup.find('div',class_='_30jeq3 _16Jk6d').text)
            except:
                price.append(np.nan)
            try:
                rating.append(soup.find('div',class_='_3LWZlK').text)
            except:
                rating.append(np.nan)
            try:
                product_offer.append(soup.find('div',class_='_3Ay6Sb _31Dcoz').text)
            except:
                product_offer.append(np.nan)
            try:
                seller_name.append(soup.find('div',class_='_1RLviY').text)
            except:
                seller_name.append(np.nan)
            try:
                seller_rating.append(soup.find('div',class_='_3LWZlK _1D-8OL').text)
            except:
                seller_rating.append(np.nan)
                
        df = pd.DataFrame({'product_name':name,'price':price,'rating':rating,'product_offer':product_offer,'seller_name':seller_name,'seller_rating':seller_rating})
        final = pd.concat([final,df],ignore_index=True)
        
        #scrab_data.append(df.to_dict())
        links.clear()
        name.clear()
        price.clear()
        rating.clear()
        product_offer.clear()
        seller_name.clear()
        seller_rating.clear()
                
   
      
    
    return final
       

