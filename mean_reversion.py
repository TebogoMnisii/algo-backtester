import backtrader as bt

class MeanReversion(bt.Strategy):
    params = (('period', 20), ('devfactor', 1.5))

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period)
        self.std = bt.indicators.StandardDeviation(self.data.close, period=self.params.period)

    def next(self):
        upper = self.sma[0] + self.params.devfactor * self.std[0]
        lower = self.sma[0] - self.params.devfactor * self.std[0]

        if self.position.size == 0:
            if self.data.close[0] < lower:
                self.buy()
            elif self.data.close[0] > upper:
                self.sell()
        else:
            if self.position.size > 0 and self.data.close[0] > self.sma[0]:
                self.close()
            elif self.position.size < 0 and self.data.close[0] < self.sma[0]:
                self.close()
