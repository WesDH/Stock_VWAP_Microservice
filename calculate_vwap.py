# TODO This is a work in progress
"""
  Calculates MONTHLY volume-weighted average price (VWAP)
  The VWAP can be calculated for different timeframes,
  such as intraday, daily, weekly, or monthly, depending on the needs of the trader
  """

# variables needed by csv:
# high, low, close, volume for past 30 days

# variables calculated here:
# typical_price, price_x_volume,
# summation_of_typical_price_x_volume,
# summation_of_volume,
#


""" Below is calulated for each trading  day """
# typical_price = (high + low + close) / 3
# price_x_volume = typical_price * volume

""" Summations for 30 days """
# Summation of: price_x_volume for past 30 days
# Summation of: volume for past 30 days

""" Calculate 30 day VWAP """
#vwap = summation_of_typical_price_x_volume / summation_of_volume