import pandas as pd
import numpy as np

class MA_family ():
    def __init__(self, close_price, num_days: int ):
        self.close_price = pd.Series(close_price)
        self.num_days = num_days

    def MA(self):
        MA_seires = pd.Series(range(self.num_days))
        for k in range(self.num_days):
            MA_seires.iloc[k] = sum(self.close_price.iloc[:k+1])/(k + 1)
        return MA_seires

    def EMA(self):
        import pandas as pd
        assert num_days == self.close_series.shape[0]
        EMA_series = pd.Series(range(self.num_days))
        k = -1
        for close_price in self.close_series:
            if k == -1:
                EMA = close_price
                EMA_series.iloc[k + 1] = EMA
                k += 1
            else:
                EMA = (2 * close_price + (self.num_days - 1) * EMA_series.iloc[k]) / (self.num_days + 1)
                EMA_series.iloc[k + 1] = EMA
                k += 1

        return EMA_series


    def SMA(self, weight):
        '''

        :param weight: 增加每一天的权重
        :return: 返回一个SMA的seires
        '''
        if weight < self.num_days:
            SMA_seires = pd.Series(range(self.num_days))
            for k in range(self.num_days):
                if k == 0:
                    SMA_seires.iloc[k] = self.close_price.iloc[k]
                else:
                    SMA_seires.iloc[k] = (weight*self.close_price.iloc[k] +
                                          (self.num_days-weight)*SMA_seires.iloc[k-1])/self.num_days
            return SMA_seires
        else:
            raise ValueError("weight must lower than Num_days")

    def DMA(self, turnover_rate):

        '''
        :param turnover_rate: 增加每天的换手率来代替权重
        :return: 返回一个DMA的seires
        '''

        turnover_rate = pd.Series(turnover_rate)
        if sum(turnover_rate > 1) == 0 :
            DMA_seires = pd.Series(range(self.num_days))
            for k in range(self.num_days):
                if k == 0:
                    DMA_seires.iloc[k] = self.close_price.iloc[k]
                else:
                    DMA_seires.iloc[k] = (turnover_rate.iloc[k]*self.close_price.iloc[k] +
                                          (1-turnover_rate.iloc[k])*DMA_seires.iloc[k-1])
            return DMA_seires
        else :
            raise ValueError("All turnover_rate must lower than 1")

    def TMA(self, weight_1, weight_2):
        if weight_1 <1 & weight_2 < 1:
            TMA_seires = pd.Series(range(self.num_days))
            for k in range(self.num_days):
                if k == 0:
                    TMA_seires.iloc[k] = self.close_price.iloc[k] * weight_2
                else:
                    TMA_seires.iloc[k] = weight_1 * TMA_seires.iloc[k-1] + weight_2 * self.close_price.iloc[k]
            return TMA_seires
        else :
            raise ValueError("All weights must lower than 1")

    def WMA(self):
        WMA_seires = pd.Series(range(self.num_days))
        WMA_list = []
        for k in range(self.num_days):
            WMA_list.append(self.close_price.iloc[k] * (k+1))
            WMA_seires.iloc[k] = np.cumsum(WMA_list[:k+1])[-1]/np.cumsum(range(k+2))[-1]
        return WMA_seires


if __name__ == '__main__':
    close_price = [35.12,
                   31.61,
                   34.10,
                   31.12,
                   32.16]
    turnover_rate = [0.830,
                     0.386,
                     0.282,
                     0.257,
                     0.157]
    num_days = 5
    print(MA_family(close_price, num_days ).WMA())