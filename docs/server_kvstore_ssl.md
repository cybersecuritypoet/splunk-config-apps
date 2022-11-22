# SSL configuration for [kvstore] in server.conf
## Values
All values must be set in the __SSL__ object.
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|verify_server_cert|sslVerifyServerCert|bool|true|Controls verification of SSL certificate|
|verify_server_name|sslVerifyServerName|bool|true|Controls verification of the hostname in SSL certificate|
|kvstore_crl_path|sslCRLPath|string|-|CRL file path|
|kvstore_bundle_path|serverCert|string|/etc/tls/certs/splunk.pem|Path to certificate/private key bundle for kvstore __WITH__ password|
|key_password|sslPassword|string|-|Encryption key for private key. __Required__ if kvstore_bundle_path is set.|