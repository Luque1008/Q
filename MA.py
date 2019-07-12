import pandas as pd


class MA_family ():
    def __init__(self, close_price, num_days: int ):
        self.close_price = pd.Series(close_price)
        self.num_days = num_days

    def MA(self):
        MA_seires = pd.Series(range(self.num_days))
        for k in range(self.num_days):
            MA_seires.iloc[k] = sum(self.close_price.iloc[:k+1])/(k + 1)
        return MA_seires

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
        else :
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
    print(MA_family(close_price, num_days ).DMA(turnover_rate))