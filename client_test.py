import unittest
from client import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint(self):
        quote = [
          {
            'top_ask':{'price':121.2, 'size':36},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':120.48, 'size':109},
            'id':'0.109974697771','stock':'ABC'
          }, 
            'top_ask':{'price':121.68, 'size':4},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':117.87, 'size':81},
            'id':'0.109974697771','stock':'DEF'
        ]
        # add the assertion for the test case
        for quate in quotes:
            self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))
        
def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):

  quote = [
          {
            'top_ask':{'price':119.2, 'size':36},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':120.48, 'size':109},
            'id':'0.109974697771','stock':'ABC'
          }, 
            'top_ask':{'price':121.68, 'size':4},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':117.87, 'size':81},
            'id':'0.109974697771','stock':'DEF'
        ]
# add the assertion for the test case
  for quate in quotes:
    self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))

def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
  
    quote = [
            {
              'top_ask':{'price':121.2, 'size':36},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':120.48, 'size':109},
              'id':'0.109974697771','stock':'ABC'
            }, 
              'top_ask':{'price':117.68, 'size':4},'timestamp':'2019-02-11 22:06:30.572453','top_bid':{'price':117.87, 'size':81},
              'id':'0.109974697771','stock':'DEF'
          ]
    # add the assertion for the test case
    for quate in quotes:
        self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+ quote['top_ask']['price'])/2))


if __name__ == '__main__':
    unittest.main()