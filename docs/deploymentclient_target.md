
# Configuration for deploymentclient.conf [deploymentclient_target]
## Settings - deployment-client
All settings in this section will be placed in [deployment-client] stanza
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|client_name|clientName|string|-|A name that the deployment server can filter on|
|verify_cert|sslVerifyServerCert|bool|true|Controls verification of SSL certificate; Only set if this setting is not set by SSL config|
|verify_name|sslVerifyServerName|bool|true|Controls verification of the hostname in SSL certificate; Only set if this setting is not set by SSL config|
|verify_SAN|-|bool|-|Enables verification of target.fqdn as SAN|
|verify_CN|-|bool|-|Enables verification of target.fqdn as Common Name|
|phone_home_interval|phoneHomeIntervalInSecs|int|-|How frequently, in seconds, this deployment client should check for new content|
|app_events_interval|appEventsResyncIntervalInSecs|int|-|This sets the interval at which the client reports back its app state to the server|
|connect_timeout|connect_timeout|uint|-|The amount of time, in seconds, that a deployment client can take to connect to a deployment server before the server connection times out|
|send_timeout|send_timeout|uint|-|The amount of time, in seconds, that a deployment client can take to send or write data to a deployment server before the server connection times out|
|recv_timeout|recv_timeout|uint|-|he amount of time, in seconds, that a deployment client can take to receive or read data from a deployment server before the server connection times out|
|ssl||SSL|-|SSL configuration|
|target||target|-|Target definition|

### Object: SSL

* All values must be set in the __SSL__ object.

|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|verify_server_cert|sslVerifyServerCert|bool|true|Controls verification of SSL certificate|
|verify_server_name|sslVerifyServerName|bool|true|Controls verification of the hostname in SSL certificate|
|ssl_versions|sslVersions|list[string]|-|List of SSL versions accepted by server (splunkd)|
|cipher_suites|cipherSuite|list[string]|-|List of cipher suites accepted|
|ecdh_curves|ecdhCurves|list[string]|-|List of ecdh curves accepted|
|trust_chain_path|caCertFile|string|/etc/tls/cert/splunk-trust-chain.pem|Path to CA certificates bundle|


### Object: target

* All values must be set in the __target__ object.
* All settings in this section will be placed in [target-broker:deploymetServer] stanza

|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|fqdn|targetUri|string+int|-|Configures the target deployment server using HTTPS - sets FQDN|
|port|targetUri|string+int|-|Configures the target deployment server using HTTPS - sets port|
|connect_timeout|connect_timeout|uint|-|The amount of time, in seconds, that a deployment client can take to connect to a deployment server before the server connection times out|
|send_timeout|send_timeout|uint|-|The amount of time, in seconds, that a deployment client can take to send or write data to a deployment server before the server connection times out|
|recv_timeout|recv_timeout|uint|-|he amount of time, in seconds, that a deployment client can take to receive or read data from a deployment server before the server connection times out|

## Examples

```json
{
	"template" : "deploymentclient_target",
	"SSL" : {},
	"verify_SAN" : true,
	"target" : { "fqdn" : "deployment-server.example.com", "port" : 8089 },
	"phone_home_interval" : 30,
	"app_events_interval" : 300
}
```