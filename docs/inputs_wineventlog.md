# Windows Event Log input definitions (inputs.conf) [inputs_monitor_file]

# App config

| Name                           |     Type     | Required | Default |               Desc                |
|--------------------------------|--------------|----------|---------|-----------------------------------|
| inputs                         | array[input] | false    | -       | All inputs should be defined here |

## Input object

| Name                      | SplunkName            | Type           | Required | Default  | Desc                                           |
|---------------------------|-----------------------|----------------|----------|----------|------------------------------------------------|
| name                      | name                  | string         | true     | -        | The Event Log that is to be read by this input |
| disabled                  | disabled              | bool           |          | false    |                                                |
| index                     | index                 | string         |          | -        |                                                |
| start_from                | start_from            | string         |          | "oldest" |                                                |
| current_only              | current_only          | bool           |          | false    |                                                |
| use_old_api               | use_old_eventlog_api  | bool           |          | false    |                                                |
| render_xml                | renderXml             | true           |          | true     |                                                |
| use_threads               | use_threads           | int            |          |          |                                                |
| thread_wait_time_msec     | thread_wait_time_msec | int            |          |          |                                                |
| batch_size                | batch_size            | int            |          |          |                                                |
| checkpoint_interval       | checkpointInterval    | int            |          |          |                                                |
| evt_exclude_fields        | exclude_fields        | array[string]  |          |          |                                                |
| evt_sid_cache_disabled    | sid_cache_disabled    | bool           |          |          |                                                |
| evt_sid_cache_exp         | sid_cache_exp         | int            |          |          |                                                |
| evt_sid_cache_exp_neg     | sid_cache_exp_neg     | int            |          |          |                                                |
| evt_sid_cache_max_entries | sid_cache_max_entries | int            |          |          |                                                |
| suppress                  |                       | suppress       |          |          |                                                |
| resolve_ad_obj            |                       | resolve_ad_obj |          |          |                                                |
| filtering                 |                       | filtering      |          |          |                                                |

### resolve_ad_obj object
| Name                     | SplunkName               | Type          | Required | Desc |
|--------------------------|--------------------------|---------------|----------|------|
| skip_GUIDs               | evt_skip_GUID_resolution | array[string] |          |      |
| dc_name                  | evt_dc_name              | string        |          |      |
| dns_name                 | evt_dns_name             | string        |          |      |
| evt_resolve_ad_ds        | ad_ds                    | string        |          |      |
| evt_ad_cache_disabled    | cache_disabled           | false         |          |      |
| evt_ad_cache_exp         | cache_exp                | int           |          |      |
| evt_ad_cache_exp_neg     | cache_exp_neg            | int           |          |      |
| evt_ad_cache_max_entries | cache_max_entries        | int           |          |      |

### suppress object
| Name       | SplunkName          | Type | Required | Desc |
|------------|---------------------|------|----------|------|
| checkpoint | suppress_checkpoint | bool |          |      |
| sourcename | suppress_sourcename | bool |          |      |
| keywords   | suppress_keywords   | bool |          |      |
| type       | suppress_type       | bool |          |      |
| task       | suppress_task       | bool |          |      |
| opcode     | suppress_opcode     | bool |          |      |
| text       | suppress_text       | bool |          |      |

### filtering object
| Name       | SplunkName   | Type          | Required | Desc                          |
|------------|--------------|---------------|----------|-------------------------------|
| whitelist  | whitelist    | filter        |          |                               |
| blacklist  | blacklist    | filter        |          |                               |
| whitelists | whitelist1-9 | array[filter] |          | Numbered (!) Array of filters |
| blacklists | blacklist1-9 | array[filter] |          | Numbered (!) Array of filters |

#### filter object
| Name  | Type       | Required | Desc                           |
|-------|------------|----------|--------------------------------|
| regex | string     | false*   | Regex to use as a filter       |
| IDs   | array[int] | false*   | List of Event IDs to filter by |

* one of regex or IDs is required per filter object

## Examples
```yml
inputs:
  - name: "Application"
    index: "os_sharepoint"
    disabled: false
    start_from: "oldest"
    current_only: false
    checkpointInternval: 5
    rederXML: true

  - name: "Security"
    index: "os_sharepoint"
    checkpointInternval: 5
    resolve_ad_obj:
    filtering:
      blacklists:
        1:
          regex: 'EventCode="4662" Message="Object Type:(?!\s*groupPolicyContainer)"'
        2:
          regex: 'EventCode="566" Message="Object Type:(?!\s*groupPolicyContainer)"'
	
  - name: "System"
    index: "os_sharepoint"
    checkpointInternval: 5
```