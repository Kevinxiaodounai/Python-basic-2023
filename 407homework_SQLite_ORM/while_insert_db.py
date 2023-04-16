from router_config_hash_monitor import RouterConfig, session
from router_config_insert_db import get_show_run
import time

ip = '127.0.0.1'
username = 'cisco'
password = 'cisco123'

while True:
    router_config, config_hash = get_show_run(ip, username, password)
    print(f'本次采集的HASH：{config_hash}')
    # 插入数据到数据库
    new_config = RouterConfig(router_config=router_config, config_hash=config_hash, router_ip=ip)
    session.add(new_config)
    session.commit()
    # 获取最近两次的配置
    last_two_config = session.query(RouterConfig).order_by(RouterConfig.id.desc()).limit(2).all()
    if len(last_two_config) < 2:
        time.sleep(5)
        continue
    # 最近一次
    last_1 = last_two_config[0]
    # 上一次
    last_2 = last_two_config[1]

    if last_1.config_hash != last_2.config_hash:
        print('=' * 10 + '配置发生变化' + '=' * 10)
        title_1 = '\tTHE MOST RECENT HASH'
        title_2 = '\tTHE LAST HASH'
        print(f'{title_1:<25}:{last_1.config_hash}')
        print(f'{title_2:<25}:{last_2.config_hash}')

    time.sleep(5)
