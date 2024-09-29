import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests #install requests too
def q03():
    BASE_URL = 'https://fakestoreapi.in/api/products'
    response = requests.get(BASE_URL)  # No need to concatenate "/api/products" again
    if response.status_code == 200:
        data = response.json()
    df = json_normalize(data)
    df2 = json_normalize(df.products[0])
    #print(df2[['brand']])

    brand_list = []
    for x in df2.index:
        brand_list.append(df2.at[x, 'brand'])
    # Remove the duplication
    brand_list2 = list(dict.fromkeys(brand_list))
    #print(len(brand_list2))

    num_product_brand = []
    for x in brand_list2:
        df_state2 = df2[df2['brand'] == x]
        num_product = len(df_state2)
        print("Product in " + x + " is " + str(num_product) + ".")
        num_product_brand.append(num_product)

    # output, pie plot
    # make data
    x = [1, 2, 3, 4]
    colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(x)))

    # plot
    fig, ax = plt.subplots()
    ax.pie(num_product_brand, labels=brand_list2, colors=colors, radius=3, center=(4, 4), labeldistance=1.1,
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\A6510582\\" + 'q03.png'
    plt.savefig(path)
