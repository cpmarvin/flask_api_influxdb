import datetime
import pandas as pd
from influxdb import InfluxDBClient

def get_util(hostname,interface,start):
	
	INFLUXDB_HOST = '172.16.1.26'
	INFLUXDB_NAME = 'telegraf'
	int(start)
	timestamp = datetime.datetime.utcnow().isoformat()

	client = InfluxDBClient(INFLUXDB_HOST,'8086','','',INFLUXDB_NAME)
	
	queryurl = "SELECT non_negative_derivative(last(ifHCOutOctets), 1s) *8 from interface_statistics where hostname = '%s' and ifName = '%s' AND time >= now()- %sh5m and time <=now()- %sh GROUP BY time(5m)" %(hostname,interface,start,start) 
	print queryurl
	result = client.query(queryurl)
	points = list(result.get_points(measurement='interface_statistics'))
	df = pd.DataFrame(points)
	df.columns = ['bps', 'time']
	df1=df.to_dict(orient='records')
	#df1=df.to_dict(orient='records',double_precision=0)
	return str(int(round(df1[0]['bps'])))
	#return "red"

