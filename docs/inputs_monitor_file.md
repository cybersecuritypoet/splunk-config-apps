# File input definition (inputs.conf) [inputs_monitor_file]
## Values

All values must be set in the global object.

| Name                           | SplunkName                     | Type   | Required | Default | Desc |
|--------------------------------|--------------------------------|--------|----------|---------|------|
| path                           | path                           | string | true     | -       |      |
| index                          | index                          | string | true     | -       |      |
| sourcetype                     | sourcetype                     | string | true     | -       |      |
| host_regex                     | host_regex                     | string |          | -       |      |
| host_segment                   | host_segment                   | string |          | -       |      |
| whitelist                      | whitelist                      | string |          | -       |      |
| blacklist                      | blacklist                      | string |          | -       |      |
| crc_salt                       | crcSalt                        | string |          | -       |      |
| init_crc_len                   | initCrcLength                  | int    |          | -       |      |
| ignore_older_than              | ignoreOlderThan                | int    |          | -       |      |
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
	"path" : "/var/log/messages",
	"index" : "linux",
	"sourcetype" : "linux:messages"
}
```

### References
[Splunk: inputs.conf](https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf)