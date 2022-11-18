
# SSL configuration for web.conf [web_ssl]
## Values
All values must be set in the SSL object.
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|ssl_versions|sslVersions|list[string]|-|List of SSL versions accepted by server (splunkd)|
|cipher_suites|cipherSuite|list[string]|-|List of cipher suites accepted|
|ecdh_curves|ecdhCurves|list[string]|-|List of ecdh curves accepted|
|user_auth|enableCertBasedUserAuth|bool|-|Controls SSL user authentication|
|dh_file_path|dhFile|string|/etc/pki/tls/private/splunk-dh.pem|Path to DH param file|
|key_path|privKeyPath|string|/etc/pki/tls/private/splunk.key|Path to DH param file|
|cert_path|serverCert|string|/etc/pki/tls/certs/splunk.crt|Path to DH param file|
|key_password|sslPassword|string|-|Encryption key for private key|
|hsts_subdomains|includeSubDomains|bool|-|Include subdomains in HSTS security header|
