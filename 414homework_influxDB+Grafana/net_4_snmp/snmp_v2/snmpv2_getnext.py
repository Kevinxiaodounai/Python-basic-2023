#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于亁颐堂NetDevOps课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主VIP, 让我们聊点高级的
# https://vip.qytang.com/


from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpv2_getnext(ip, community, oid, port=161):
    cmd_gen = cmdgen.CommandGenerator()

    error_indication, error_status, error_index, var_bind_table = cmd_gen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if error_indication:
        print(error_indication)
    elif error_status:
        print(error_status)

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for var_bind_table_row in var_bind_table:
        for item in var_bind_table_row:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 显示接口信息
    print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161))
    for x, y in snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161):
        print(x, y)
    # 接口速率
    print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161))

    # 进接口字节数
    print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161))

    # 出接口字节数
    print(snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161))

    # ---------------------------------------------------------------------------------
    if_name_raw = snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.2", port=161)
    if_name_list = [i[1] for i in if_name_raw]

    if_speed_raw = snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.5", port=161)
    if_speed_list = [i[1] for i in if_speed_raw]

    if_in_raw = snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.10", port=161)
    if_in_list = [i[1] for i in if_in_raw]

    if_out_raw = snmpv2_getnext("10.1.1.253", "tcpipro", "1.3.6.1.2.1.2.2.1.16", port=161)
    if_out_list = [i[1] for i in if_out_raw]

    final_list = []
    for name, speed, in_bytes, out_bytes in zip(if_name_list, if_speed_list, if_in_list, if_out_list):
        final_list.append({'name': name, 'speed': speed, 'in_bytes': in_bytes, 'out_bytes': out_bytes})
    from pprint import pprint
    pprint(final_list, indent=4)

