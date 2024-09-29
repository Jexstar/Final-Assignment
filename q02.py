import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def q02():
    #question unclear again, is question asking sum of master card transaction amount?
    #or just count again? I used count for this question

    path = "C:\\Users\\ADMIN\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\transactions.csv"
    df = pd.read_csv(path)

    # filtering only us
    df2 = df[df['shippingCountry'].notnull()]  # taking out nulls from shippingCountry column
    df3 = df2.query('shippingCountry == "US"')  # taking only US
    # from US states, if there is null, write N/A
    df3['shippingState'] = df3['shippingState'].fillna('N/A')
    # change states to capital
    df3['shippingState'] = df3['shippingState'].str.upper()
    df4 = df3.query("cardType == 'MC'")

    state_list = [] #make empty list
    for x in df4.index:
        state_list.append(df4.at[x, 'shippingState'])
    # Remove the duplication
    state_list2 = list(dict.fromkeys(state_list))

    num_transactions_state = []
    for x in state_list2:
        df_state3 = df3[df3['shippingState'] == x]
        num_transactions = len(df_state3)  # getting number of transactions
        print(num_transactions)
        print("Master Card Transactions in " + x + " is " + str(num_transactions) + ".")
        num_transactions_state.append(num_transactions)

    plt.figure(figsize=(6.4, 50.4))
    plt.barh(state_list2, num_transactions_state)
    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\A6510582\\" + 'q02.png'
    plt.savefig(path)