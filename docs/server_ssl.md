# SSL configuration for server.conf [server_ssl]
## Values
All values must be set in the SSL object.
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|verify_server_cert|sslVerifyServerCert|bool|true|Controls verification of SSL certificate|
|verify_server_name|sslVerifyServerName|bool|true|Controls verification of the hostname in SSL certificate|
|cli_verify_cert_name|cliVerifyServerName|bool|-|Controls verification of the name in SSL certificate for CLI client|
|verify_CRL|certificateStatusValidationMethod|bool|-|Controls CLR validation|
|require_client_cert|requireClientCert|bool|true|Controls client certificate authentication|
|ssl_versions|sslVersions|list[string]|-|List of SSL versions accepted by server (splunkd)|
|cipher_suites|cipherSuite|list[string]|-|List of cipher suites accepted|
|ecdh_curves|ecdhCurves|list[string]|-|List of ecdh curves accepted|
|client_ssl_versions|sslVersionsForClient|list[string]|-|List of SSL versions used by client (splunkd)|
|bundle_path|serverCert|string|/etc/tls/certs/splunk.pem|Path to certificate/private key bundle|
|trust_chain_path|sslRootCAPath|string|/etc/tls/cert/splunk-trust-chain.pem|Path to CA certificates bundle|
|dh_file_path|dhFile|string|/etc/pki/tls/private/splunk-dh.pem|Path to DH param file|
|key_password|sslPassword|string|-|Encryption key for private key|
|compression|allowSslCompression|bool|-|Controls SSL compression|
|renegotiation|allowSslRenegotiation|bool|-|Controls SSL renegotiation|
|hsts|sendStrictTransportSecurityHeader|bool|-|Send HSTS security header in HTTP responses|
|client_compression|useClientSSLCompression|bool|-|Controls SSL compression for client|
|splunkd_client_compression|useSplunkdClientSSLCompression|bool|-|Controls SSL compression for splunkd|
|client_session_cache|useSslClientSessionCache|bool|-|Controls SSL session cache|
|client_session_path|sslClientSessionPath|bool|-|Path to SSL session cache storage|
|session_timeout|sslServerSessionTimeout|bool|-|SSL session timeout|
|handshake_timeout|sslServerHandshakeTimeout|bool|-|SSL handshake timeout|