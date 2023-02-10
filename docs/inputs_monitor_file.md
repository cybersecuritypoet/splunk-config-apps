# File input definition (inputs.conf) [inputs_monitor_file]

# App config

| Name                           |     Type     | Required | Default |               Desc                |
|--------------------------------|--------------|----------|---------|-----------------------------------|
| inputs                         | array[input] | false    | -       | All inputs should be defined here |


## Input object

| Name                           | SplunkName                     | Type   | Required | Default | Desc |
|--------------------------------|--------------------------------|--------|----------|---------|------|
| disabled                       | disabled                       | bool   |          | false   |      |
| path                           | path                           | string | true     | -       |      |
| index                          | index                          | string | true     | -       |      |
| sourcetype                     | sourcetype                     | string | true     | -       |      |
| host_regex                     | host_regex                     | string |          | -       |      |
| host_segment                   | host_segment                   | string |          | -       |      |
| whitelist                      | whitelist                      | string |          | -       |      |
| blacklist                      | blacklist                      | string |          | -       |      |
| crc_salt                       | crcSalt                        | string |          | -       |      |
| init_crc_len                   | initCrcLength                  | int    |          | -       |      |
| ignore_older_than              | ignoreOlderThan                | string |          | -       |      |
| follow_tail                    | followTail                     | bool   |          | -       |      |
| always_open                    | alwaysOpenFile                 | bool   |          | -       |      |
| time_before_close              | time_before_close              | string |          | -       |      |
| multiline_event_extra_waittime | multiline_event_extra_waittime | bool   |          | -       |      |
| recursive                      | recursive                      | bool   |          | -       |      |
| follow_symlink                 | followSymlink                  | string |          | -       |      |
| host                           | host                           | string |          | -       |      |
| source                         | source                         | string |          | -       |      |

### Examples
```json
{
	"inputs":
	[
		{
			"path" : "/var/log/messages",
			"index" : "linux",
			"sourcetype" : "linux:messages"
		}
	]
}
```

```yaml
inputs:
  - path: "E:\\LOGS\\IIS"
    index: "default_iis"
    sourcetype: "ms:iis:splunk"
    ignore_older_than: 1d
    disabled: false
    recursive: true
```

### References
[Splunk: inputs.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf)