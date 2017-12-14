Monitor License Usage inside OFG
======================================
This tool can help artists monitor all software licenses usage when they are working in house.

To enable this app, additional lines needed to be add to environment config `project.yml`
```
tk-multi-licensemonitor:
  license_server_info: []
  location:
    path: https://github.com/qpskcn1/tk-multi-licensemonitor.git
    version: v1.0.0
    type: git
```

To add license into this monitor, plase add dict to `license_server_info`
For example
```
tk-multi-licensemonitor:
  license_server_info:
    - {Application: "Nuke",
       LicenseManager: "RLM",
       Port: "4101",
       Server: "192.168.10.250",
       ISV: "foundry"}
    - {Application: "Toom Boom",
       LicenseManager: "FLEXLM",
       Port: "27000",
       Server: "ofgsr-mpio1.local",
       ISV: ""}
    - {Application: "Arnold",
       LicenseManager: "FLEXLM",
       Port: "27001",
       Server: "ofgsr-mpio1.local",
       ISV: ""}
    - {Application: "Deadline",
       LicenseManager: "FLEXLM",
       Port: "27008",
       Server: "ofgsr-mpio1.local",
       ISV: ""}
  location:
    path: https://github.com/qpskcn1/tk-multi-licensemonitor.git
    version: v1.0.0
    type: git
```
Note that `LicenseManager` can only be `RLM` or `FLEXLM`
