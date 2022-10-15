class SetUA:
    def safari(self):
        return('User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50')
    def ie(self, Version):
        if Version == int(6):
            return('User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')
        elif Version == int(7):
            return('User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')
        elif Version == int(8):
            return('User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)')
        elif Version == int(9):
            return('User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        elif Version == int(10):
            return('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)')
        elif Version == int(11):
            return('Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')
        else:
            return(1)
    def chrome(self):
        return('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36')
    def vf360(self):
        return('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36 QIHU 360EE')
    def qq(self):
        return('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; QQBrowser/8.0.1374.400)')
    def baidu(self):
        return('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 BIDUBrowser/6.x Safari/537.36')
    def v360(self):
        return('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')