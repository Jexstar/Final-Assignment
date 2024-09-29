import pandas as pd
import matplotlib.pyplot as plt

def q04():
    path = "C:\\Users\\ADMIN\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\transactions.csv"
    df = pd.read_csv(path)
    df2 = df[df['transactionAmountUSD'].notnull()]
    df3 = df2.query("transactionAmountUSD < 1000")

    plt.figure(figsize=(10.4, 6.4))
    plt.ylim(0, 35000)
    plt.hist(df3[['transactionAmountUSD']], edgecolor='white', linewidth=1.5)
    # plt.show()
    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\A6510582\\" + 'q04.png'
    plt.savefig(path)
