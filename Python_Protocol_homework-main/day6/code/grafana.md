### SI vs IEC
```
SI(International System of Units，国际单位制)制定的标准，采用十进制换算。例如：
1 MB = 106 bytes = 1 000 000 bytes = 1000 kilobyte
1024 MB = 1 gigabyte (GB)

IEC（International Electrotechnical Commission，国际电工委员会）于1998年制定的标准，采用二进制换算。例如：
1 MiB = 220 bytes = 1 048 576 bytes = 1024 kibibytes
1024 MiB = 1 gibibyte (GiB)
```

### Grafana配置化
```
# 出向Query
SELECT non_negative_derivative(mean("out_bytes"), 1s) * 8  FROM "interface_monitor" WHERE $timeFilter GROUP BY time($__interval), device_ip, interface_name

# 入向Query
SELECT non_negative_derivative(mean("in_bytes"), 1s) * 8  FROM "interface_monitor" WHERE $timeFilter GROUP BY time($__interval), device_ip, interface_name

# Alias By
[[tag_device_ip]]--[[tag_interface_name]]
```