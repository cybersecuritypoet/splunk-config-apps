# SSL configuration for web.conf [web_ssl]
## Values
All values must be set in the __SSL__ object.
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|ssl_versions|sslVersions|list[string]|-|List of SSL versions accepted by server (splunkd)|
|cipher_suites|cipherSuite|list[string]|-|List of cipher suites accepted|
|ecdh_curves|ecdhCurves|list[string]|-|List of ecdh curves accepted|
|dh_file_path|dhFile|string|/etc/pki/tls/private/splunk-dh.pem|Path to DH param file|
|key_path|privKeyPath|string|/etc/pki/tls/private/splunk.key|Path to DH param file|
|cert_path|serverCert|string|/etc/pki/tls/certs/splunk.crt|Path to DH param file|
|web_require_cert|requireClientCert|bool|-|Controls whether authentication with SSL certificate is required|
|key_password|sslPassword|string|-|Encryption key for private key|
|hsts_subdomains|includeSubDomains|bool|-|Include subdomains in HSTS security header|
|handshake_timeout|sslServerHandshakeTimeout|int|60||

### Examples
```json
{
	"SSL" :
	{
		"key_path" : "/etc/pki/tls/private/splunk.key",
		"cert_path" : "/etc/pki/tls/certs/splunk.crt",
		"dh_file_path" : "/etc/pki/tls/private/splunk-dh.pem",
		"key_password" : null,
		"cipher_suites" :
		[
			"ECDHE-RSA-AES256-GCM-SHA384",
			"ECDHE-ECDSA-AES256-GCM-SHA384"
		],
		"ecdh_curves" : ["secp521r1","secp384r1"],
		"ssl_versions" : ["tls1.2"],
		"hsts_subdomains" : true,
		"web_require_cert" : false,
		"handshake_timeout" : 30
	}
}
```
### References
[Splunk: server.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Webconf)
