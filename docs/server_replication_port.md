# Indexer replication port configuration for server.conf
## Values
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|replication_ports|-|array[port]|-|List of plaintext replication ports|
|replication_ports_ssl|-|array[port]|-|List of SSL replication ports|

## Port
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|port|-|ushort|-|Network port|
|disabled|disabled|bool|false|Port status|
|ipv6_listen|listenOnIPv6|bool|-|Port listen on IPv6|
|accept_from|acceptFrom|string|-|Splunk network ACL definition for the port|

### Examples
```
{
	"replication_ports" :
	[
		{
			"port" : 1234,
			"disabled" : true,
			"ipv6_listen" : false,
		},
		{
			"port" : 1235,
			"disabled" : false,
			"ipv6_listen" : false,
		}
	]
}
```
### References
[Splunk: server.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Serverconf)
