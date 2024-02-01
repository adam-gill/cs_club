import tkinter as tk # library that allows us to build a little app
from tkinter import PhotoImage # add image
import ccxt # API to fetch btc price from crypto.com
import locale # to format currency to USD

# something I added to format number into currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

crypto_tickers = {
    'btc' : 'BTC/USD',
    'eth' : 'ETH/USD',
    'sol' : 'SOL/USD'
}

def get_crypto_price(ticker):
    cryptocom = ccxt.cryptocom()

    # try and except blocks to catch errors and prevent the program from stopping abruptly
    try:
        ticker = cryptocom.fetch_ticker(ticker)
        last_price = ticker['last']
        return locale.currency(last_price, grouping=True)

    except ccxt.NetworkError as e:
        print(f"Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_price():
    btc_price = get_crypto_price(crypto_tickers.get('btc', 'none'))
    eth_price = get_crypto_price(crypto_tickers.get('eth', 'none'))
    sol_price = get_crypto_price(crypto_tickers.get('sol', 'none'))

    bitcoinLabel.config(text=f"Bitcoin Price: {btc_price}")
    ethereumLabel.config(text=f"Ethereum Price: {eth_price}")
    solanaLabel.config(text=f"Solana Price: {sol_price}")

    app.after(2000, update_price)

# Create the main window
app = tk.Tk()
app.title("Get Crypto Prices")
app.geometry("800x600")

title_font = ('JetBrains Mono', 32)
gen_font = ('JetBrains Mono', 18)

# Create a label
label = tk.Label(app, text="Live Crypto Prices:", font=title_font)
bitcoinLabel = tk.Label(app, text=f"Bitcoin Price: fetching...", font=gen_font)
ethereumLabel = tk.Label(app, text=f"Ethereum Price: fetching...", font=gen_font)
solanaLabel = tk.Label(app, text=f"Solana Price: fetching...", font=gen_font)
btc_img = PhotoImage(file='btc.png')
img = tk.Label(app, image=btc_img)

label.pack(pady=10)
bitcoinLabel.pack(pady=10)
ethereumLabel.pack(pady=10)
solanaLabel.pack(pady=10)
img.pack(pady=10)


update_price()

# git test

# Start the main event loop
app.mainloop()
