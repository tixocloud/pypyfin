class Formula:
    def graham_number(eps, bvs):
        """
            Values a company based on the company's earnings per share
            and book value per share.

            See: http://en.wikipedia.org/wiki/Graham_number
        """
        return math.sqrt(22.5 * eps * bvs)

    def earnings_per_share(net_income, shares):
        """
            shares is shares outstanding
        """
        return net_income/shares

    def bookvalue_per_share(equity, shares):
        """
            shares is shares outstanding
        """
        return equity/shares

    def bookvalue(assets, liabilities):
        return assets - liabilities

    def daily_return(yesterday_open=0,today_close=0):
        return (today_close - yesterday_open)/yesterday_open
