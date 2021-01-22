import pygeoip
gip=pygeoip.GeoIP("GeoLiteCity.dat")
res=gip.record_by_addr('')  #ip address goes here
for key,value in res.items():
    print('%s : %s' %(key,value))
