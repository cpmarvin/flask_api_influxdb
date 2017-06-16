import datetime
import pandas as pd
from influxdb import InfluxDBClient

def get_graph(hostname,interface):
	
	INFLUXDB_HOST = '172.16.1.26 '
	INFLUXDB_NAME = 'telegraf'

	timestamp = datetime.datetime.utcnow().isoformat()

	client = InfluxDBClient(INFLUXDB_HOST,'8086','','',INFLUXDB_NAME)
	
	queryurl = "SELECT non_negative_derivative(max(bytes_sent), 1s) *8 from interface_counters where hostname = '%s' and interface_name = '%s' AND time > now()- 24h and time <now()- 5m  GROUP BY time(5m)" %(hostname,interface) 
	print queryurl
	result = client.query(queryurl)
	points = list(result.get_points(measurement='interface_counters'))
	df = pd.DataFrame(points)
	df.columns = ['bps', 'time']
	#pd.set_option('display.float_format', lambda x: '%.3f' % x)
	df1=df.reindex(columns=["time","bps"]).to_csv(index=False)
	return df1

