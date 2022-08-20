# splunk-config-apps
Applications for configuring Splunk


|Name                             |Description                                                        |
|---------------------------------|-------------------------------------------------------------------|
|indexes                          | Indexes and volumes configuration                                 |
|inputs_internal_fwd              | Inputs for internal Splunk forwarding                             |
|outputs_internal_fwd             | Outputs for internal Splunk forwarding                            |
|server_deployer_push_threads_auto| Deployer configuration - push bundle on all threads (auto)        |
|server_ssl                       | SSL configuration for splunkd                                     |
|server_ssl_client_san            | Configuration of allowed SSL clients                              |
|server_ssl_disable               | Disable SSL in splunkd                                            |
|server_ssl_enable                | Enable SSL in splunkd                                             |
|splunk_httpinput                 | HTTP Event Collector configuration                                |
|splunk_httpinput_inputs          | HTTP Event Collector inputs                                       |
|web_disable                      | Disable web UI                                                    |
|web_enable                       | Enable web UI                                                     |
|web_ssl                          | SSL configuration for web UI                                      |
|web_ssl_disable                  | Disable web UI SSL                                                |
|web_ssl_enable                   | Enable web UI SSL                                                 |


## How to use

Example usage (in repository root):
```
python3 utils/scripts/compile-apps.py utils/conf-examples/example_1.json ~/splunk-config-apps-out/ apps/
```

## JSON config
### Structure
```
{
	"globals" :{},
	"groups" : [{}]
}
```
#### Globals
```
"globals":
{
	"SSL" : {},
	"apps" : [{}]
}
```
#### Groups

```
"groups" :
[
	{
		"template" : "",
		"name" : "",
		"path" : "",
		"prefix" : "",
		"postfix" : "",
		"apps" : [{}]
	}
]
```

|name               |type  |default|desc|
|-------------------|------|-------|----|
|name               |string|       |Sets group name|
|path               |string|       |Specifies destination folder name|
|prefix		        |string|       |Destination folder name prefix for apps|
|postfix            |string|       |Destination folder name postfix for apps|
|apps               |array |       |Application configurations|

#### SSL

Schema: utils/json-schama/ssl-schema.json
```
"SSL" :
{
	"verify_server_cert" : true,
	"verify_server_name" : true,
	"key_path" : "/etc/pki/tls/private/splunk.key",
	"cert_path" : "/etc/pki/tls/certs/splunk.cert",
	"bundle_path" : "/etc/pki/tls/private/splunk.pem",
	"trust_chain_path" : "/etc/pki/tls/certs/splunk-trust-chain.pem",
	"dh_file_path" : "/etc/pki/tls/private/splunk-dh.pem",
	"crl_path" : "/etc/pki/tls/crl/splunk-crl.pem",
	"cipher_suites" :
	[
		"ECDHE-RSA-AES256-GCM-SHA384",
		"ECDHE-ECDSA-AES256-GCM-SHA384",
		"TLS_AES_256_GCM_SHA384"
	],
	"ecdh_curves" : ["secp521r1","secp384r1"],
	"ssl_versions" : ["tls1.2","tls1.3"],
	"client_ssl_versions" : ["tls1.2","tls1.3"],
	"client_compression": true,
	"splunkd_client_compression": true,
	"ssl_compression": true,
	"verify_crl" : true
}
```

|name               |type  |default|desc|
|-------------------|------|-------|----|
|verify_server_cert |bool  |true                                     |Configurest server cert verification|
|verify_server_name |bool  |true                                     |Configures server name verification|
|key_path		    |string|/etc/pki/tls/private/splunk.key          |Private key for Splunk|
|cert_path          |string|/etc/pki/tls/certs/splunk.cert           |Public certificate for Splunk|
|bundle_path        |string|/etc/pki/tls/private/splunk.pem          |Private key + public certificate bundle for Splunk|
|trust_chain_path   |string|/etc/pki/tls/certs/splunk-trust-chain.pem|Trust chain for Splunk (CA)|
|dh_file_path       |string|/etc/pki/tls/private/splunk-dh.pem       |DH param file for Splunk |
|crl_path           |string|/etc/pki/tls/crl/splunk-crl.pem          |CRL file for Splunk |
|cipher_suites      |array |ECDHE-RSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES256-GCM-SHA384|OpenSSL cipher suites|
|ecdh_curves        |array |secp521r1, secp384r1                     |OpenSSL ecdh curves specification|
|ssl_versions       |array |tls1.2, tls1.3                           |OpenSSL TLS versions|
|client_ssl_versions|array |tls1.2","tls1.3                          |OpenSSL TLS versions for client|
|client_compression |bool  |true                                     |SSL Client compression|
|splunkd_client_compression|bool|true                                |SSL Client compression for splunkd|
|ssl_compression    |bool  |true                                     |SSL compression|
|verify_crl         |bool  |true                                     |PKI CRL verification. Must have crl_path set and CRL uploaded|

#### APPS

Schemas: utils/json-schama/app-`<app-name`>-schema.json
|name               |type  |default|desc|
|-------------------|------|-------|----|
|template           |string|       |Specifies application template from apps folder|
|name               |string|       |Sets application name|
|prefix		        |string|       |Destination folder name prefix. Inherited from globals|
|postfix            |string|       |Destination folder name postfix. Inherited from globals|
|SSL                |SSL   |       |SSL configuration, inherited from global if SSL object is present in app|
|...                |      |       |Application configuration, see JSON schemas (or app source) for possible options|