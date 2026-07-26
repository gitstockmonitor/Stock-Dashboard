import yfinance as yf
import datetime
import pytz
import os

TICKERS = {
    "Nifty 50": "^NSEI",
    "Nifty Next 50": "JUNIORBEES.NS",
    "Midcap 150": "MID150BEES.NS",
    "MidSmall400MomQual100": "MIDSMALL.NS",
    "Gold (India)": "GOLDBEES.NS",
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "SPMO": "SPMO",
    "QCOM": "QCOM"
}

def main():
    tz_india = pytz.timezone('Asia/Kolkata')
    tz_us = pytz.timezone('America/New_York')
    
    now_india = datetime.datetime.now(tz_india)
    now_us = datetime.datetime.now(tz_us)

    india_open = now_india.weekday() < 5 and (9 <= now_india.hour <= 15)
    us_open = now_us.weekday() < 5 and (9 <= now_us.hour <= 16)

    alerts = []

    for name, symbol in TICKERS.items():
        is_indian_asset = symbol.endswith('.NS') or symbol == '^NSEI'
        if is_indian_asset and not india_open:
            continue
        elif not is_indian_asset and not us_open:
            continue

        try:
            data = yf.Ticker(symbol).history(period="2d")
            if len(data) < 2:
                continue
                
            yesterday_close = data['Close'].iloc[0]
            current_price = data['Close'].iloc[-1]
            diff_pct = ((current_price - yesterday_close) / yesterday_close) * 100

            if abs(diff_pct) >= 2.5:
                direction = "🔴 DOWN" if diff_pct < 0 else "🟢 UP"
                alerts.append(f"{direction} **{name}**: {abs(diff_pct):.2f}% \n(Current: {current_price:.2f} | Yest: {yesterday_close:.2f})")
                
        except Exception as e:
            print(f"Error fetching {name}: {e}")

    if alerts:
        final_message = "The following assets have moved by 2.5% or more today:\n\n" + "\n\n".join(alerts)
        # Create a markdown file with the alert text
        with open("alert.md", "w") as f:
            f.write(final_message)
        print("Alert file generated for GitHub Issues!")
    else:
        print("No assets crossed the 2.5% threshold.")

if __name__ == "__main__":
    main()