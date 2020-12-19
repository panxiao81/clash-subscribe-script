# Clash Subscribe Script

一个自用的 Clash 订阅更新脚本

## 使用方法

安装依赖

```shell
pip3 install ruamel.yaml requests
```

脚本会从标准输入读入 `URL`, 并将修改好的 YAML 文档送至标准输出。

```shell
echo "your_sub_url_here" | python3 main.py > config.yml
```

目前仅有写死的添加 `socks-port` 与 `redir-port` 的功能

理论上可以方便的对功能进行扩展，对字典与列表进行插入与赋值操作即可。

可以写进 `crontab` 来达到自动更新订阅的目的, 如：

```console
$ crontab -e -u clash

# 输入

0 4 * * * echo "your_sub_url_here" | python3 /path/to/main.py > /path/to/config.yml
```

进行每日 4 点更新订阅。