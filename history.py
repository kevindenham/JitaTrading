# Change the following settings to suit your needs:
 
EVEROOT = r"C:/Program Files (x86)/CCP/EVE"
OUTPATH = r"C:/DUMP"

import time
import os
from reverence import blue

def evetime2date(evetime):
        s = (evetime - 116444736000000000) / 10000000 
        return time.strftime("%Y-%m-%d", time.gmtime(s))

eve = blue.EVE(EVEROOT)
cfg = eve.getconfigmgr()
cachemgr = eve.getcachemgr()
cmc = cachemgr.LoadCacheFolder("CachedMethodCalls")

for key, obj in cmc.iteritems():
        if key[1]=="GetOldPriceHistory":
                item = cfg.invtypes.Get(key[3])
                region = cfg.evelocations.Get(key[2])
                print "Processing " + item.name + " [" + region.locationName +"]... \n"
                xmlfile = open(os.path.join(OUTPATH, item.name+"-history-"+region.locationName+".xml"), 'w')
                xmlfile.write ("<data>")
                for history_item in obj['lret']:
                        line = "<entry>\n<lowPrice>%(lowPrice)i</lowPrice>\n<highPrice>%(highPrice)i</highPrice>\n<avgPrice>%(avgPrice)i</avgPrice>\n<volume>%(volume)i</volume>\n<orders>%(orders)i</orders>\n</entry>\n" % \
                                                              { 'lowPrice': history_item['lowPrice']/1, \
                                                                'highPrice': history_item['highPrice']/1, \
                                                                'avgPrice': history_item['avgPrice']/1, \
                                                                'volume': history_item['volume'], \
                                                                'orders': history_item['orders']}
                        xmlfile.write(line+"\n")
                xmlfile.write ("</data>")
                xmlfile.close()
		
