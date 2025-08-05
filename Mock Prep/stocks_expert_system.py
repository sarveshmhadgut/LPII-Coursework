def evaluate_stock_trend(
    stock_price, price_trend, volume_change, rsi, macd_signal, news_sentiment
):

    print("\nSTOCK EVALUATION REPORT\n")

    if rsi < 30:
        print("RSI: Stock is oversold. Consider buying.")
    elif rsi > 70:
        print("RSI: Stock is overbought. Consider selling.")
    else:
        print("RSI: Stock is in a neutral range.")

    if macd_signal == "bullish":
        print("MACD: Bullish signal. Favorable for buying.")
    elif macd_signal == "bearish":
        print("MACD: Bearish signal. Favorable for selling.")
    else:
        print("MACD: Neutral. Caution advised.")

    if price_trend == "up":
        print("Price Trend: Upward movement detected. Good potential for gains.")
    elif price_trend == "down":
        print("Price Trend: Downward movement detected. Potential losses.")
    else:
        print("Price Trend: No significant change.")

    if volume_change == "increase":
        print("Volume Change: Increased volume detected. Confirming trend.")
    elif volume_change == "decrease":
        print("Volume Change: Decreased volume. Trend weakening.")
    else:
        print("Volume Change: Stable volume.")

    if news_sentiment == "positive":
        print("News Sentiment: Positive news. Buy signal.")
    elif news_sentiment == "negative":
        print("News Sentiment: Negative news. Sell signal.")
    else:
        print("News Sentiment: Neutral news. Hold.")

    if rsi < 30 and macd_signal == "bullish" and news_sentiment == "positive":
        return "Buy"
    elif rsi > 70 and macd_signal == "bearish" or news_sentiment == "negative":
        return "Sell"
    else:
        return "Hold"


def main():
    print()
    decision = evaluate_stock_trend(150.00, "up", "increase", 28, "bullish", "positive")
    print(f"Decision: {decision}\n")

    decision = evaluate_stock_trend(
        320.00, "down", "decrease", 75, "bearish", "negative"
    )
    print(f"Decision: {decision}\n")

    decision = evaluate_stock_trend(
        85.50, "neutral", "neutral", 50, "neutral", "neutral"
    )
    print(f"Decision: {decision}\n")
    # stock_price = float(input("Enter current stock price (in USD): "))
    # price_trend = input("Enter price trend (up/down/neutral): ").lower()
    # volume_change = input("Enter volume change (increase/decrease/neutral): ").lower()
    # rsi = float(input("Enter Relative Strength Index (RSI): "))
    # macd_signal = input("Enter MACD signal (bullish/bearish/neutral): ").lower()
    # news_sentiment = input("Enter news sentiment (positive/negative/neutral): ").lower()

    # decision = evaluate_stock_trend(
    #     stock_price, price_trend, volume_change, rsi, macd_signal, news_sentiment
    # )


if __name__ == "__main__":
    main()
