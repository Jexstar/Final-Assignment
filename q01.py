import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def q01():
   #question unclear, is it total amount of transactions(count)
   # or total transaction amount(sum)? I've done the former.

    path = "C:\\Users\\ADMIN\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\transactions.csv"
    df = pd.read_csv(path)
    df2 = df[df['transactionCurrencyCode'].notnull()]  # filter null value
    df2['transactionCurrencyCode'] = df2['transactionCurrencyCode'].str.upper()

    currency_list = []  # make empty list
    for x in df2.index:
        currency_list.append(df2.at[x, 'transactionCurrencyCode'])
    # Remove the duplication
    currency_list2 = list(dict.fromkeys(currency_list))

    num_transactions_currency = []
    for x in currency_list2:
        df_currency3 = df2[df2['transactionCurrencyCode'] == x]
        num_transactions = len(df_currency3) #getting number of transactions
        #print(num_transactions)
        print("Transactions for " + x + " is " + str(num_transactions) + ".")
        num_transactions_currency.append(num_transactions)

    plt.figure(figsize=(16.4, 6.4))
    plt.xticks(rotation=90, ha='right') #rotating x ticks for more readability
    plt.bar(currency_list2, num_transactions_currency)
    #plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\A6510582\\" + 'q01.png'
    plt.savefig(path)
