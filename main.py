import tkinter as tk
import ccxt

def get_binance_bitcoin_price():
    binance = ccxt.binance()

    # try and except blocks to catch errors and prevent the program from stopping abruptly
    try:
        ticker = binance.fetch_ticker('BTC/USD')
        last_price = ticker['last']
        return last_price

    except ccxt.NetworkError as e:
        print(f"Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def on_button_click():

    btc_price = get_binance_bitcoin_price()

    label.config(text=f"The most recent price of bitcoin is: {btc_price}")

# Create the main window
app = tk.Tk()
app.title("Simple Tkinter App")
app.geometry("400x400")

# Create a label
label = tk.Label(app, text="Welcome to Tkinter App")
label.pack(pady=10)

# Create a button
button = tk.Button(app, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
app.mainloop()
