# Indexer __SSL_ replication port configuration for server.conf
## Values
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|replication_ports_ssl|-|array[port]|-|List of port objects as defined below|
|SSL|-|-|SSL|SSL configuration definition - for all ports|

### Port
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|port|-|ushort|-|Network port|
|SSL|-|-|SSL|SSL configuration definition - per port|

### SSL
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|bundle_path|serverCert|string|/etc/tls/certs/splunk.pem|Path to certificate/private key bundle|
|key_password|sslPassword|string|-|Encryption key for private key|
|require_client_cert|requireClientCert|bool|true|Controls client certificate authentication|
|cipher_suites|cipherSuite|list[string]|-|List of cipher suites accepted|
|ssl_versions|sslVersions|list[string]|-|List of SSL versions|
|ecdh_curves|ecdhCurves|list[string]|-|List of ecdh curves accepted|
|dh_file_path|dhFile|string|/etc/pki/tls/private/splunk-dh.pem|Path to DH param file|
|compression|useSslCompression|bool|-|Controls SSL compression|
|renegotiation|allowSslRenegotiation|bool|-|Controls SSL renegotiation|

### Examples
```
{
	
	"SSL" :
	{
		"require_client_cert" : true,
		"bundle_path" : "/etc/pki/tls/private/splunk.pem",
		"dh_file_path" : "/etc/pki/tls/private/splunk-dh.pem",
		"cipher_suites" :
		[
			"ECDHE-RSA-AES256-GCM-SHA384",
			"ECDHE-ECDSA-AES256-GCM-SHA384"
		],
		"ecdh_curves" : ["secp521r1","secp384r1"],
		"ssl_versions" : ["tls1.2"],
		"compression": true,
		"renegotiation" : true
	},
	"replication_ports_ssl" :
	[
		{
			"port" : 1234,
			"disabled" : false,
			"ipv6_listen" : false,
			"SSL" :
			{
				
			}
		},
		{
			"port" : 1235,
			"disabled" : false,
			"ipv6_listen" : false,
			"SSL" :
			{
				"require_client_cert" : false
			}
		}
	]
}
```
### References
[Splunk: server.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Serverconf)