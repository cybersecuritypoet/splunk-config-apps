# Distributed search configuration for distsearch.conf
All settings will be placed in [distributedSearch] stanza. Configures a list of search peers in __servers__ field.
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|peers|-|array[peer]|-|List of peer objects as defined below|

## Peer
|Name|Splunk Name|Type|Default|Desc|
|---|---|---|---|---|
|fqdn|-|string|-|Peer FQDN|
|port|-|ushort|8089|Peer port|

All peers are rendered in a list of URIs based on following template:
```
https://{{peer.fqdn}}:{{peer.port}}
```