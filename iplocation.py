import pygeoip
gip=pygeoip.GeoIP("GeoLiteCity.dat")
res=gip.record_by_addr('27.34.16.159')
for key,value in res.items():
    print('%s : %s' %(key,value))
