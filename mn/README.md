# 運行 mn 搭配 python 檔案使用

## 測試指令

`mn` 指令運行後，可以透過傳遞 parameter 方式，來載入開啟我們需要的網路環境

* 透過指令 `--custom` 後，可以傳入的參數：
    * 這方式能夠加入我們自己定義的方法，並再開啟的 CLI 中來做使用

option | dict name | key: value
--- | --- | ---
`--topo` | `topos` | 'short name': `Topo` constructor
`--switch` | `switches` | 'short name': `Switch` constructor
`--host` | `hosts` | 'short name': `Host` constructor
`--controller` | `controllers` | 'short name': `Controller` constructor
`--link` | `links` | 'short name': `Link` constructor
`--test` | `test` | 'short name': test function to call with mininet object

* 示例：
    * 假設有一個 python: `mytopo.py` 腳本
    ```python
    class MyTopo( Topo ):
    def build( self, ...):
    def myTest( net ):
    ...
    topos = { 'mytopo': MyTopo }
    tests = { 'mytest': myTest }
    ```
    * 我們則可以透過 `--topo` 來做指定：
    ```bash
    sudo mn --custom mytopo.py --topo mytopo,3
    ```
    * 或是指定多個檔案：
    ```bash
    sudo mn --custom mytopo.py,mytest.py --topo mytopo,3 --test mytest
    ```
* 還可以加入自訂義的指令在開啟 Mininet CLI 後使用
    * 於 python: `mycmd.py` 內寫指令
    * 如果要再 CLI 加入 user-defined 指令，則需要加上 prefix `do_`
    ```python
    def mycmd( self, line ):
        "mycmd is an example command to extend the Mininet CLI"
        net = self.mn
        output( 'mycmd invoked for', net, 'with line', line, '\n'  )
    CLI.do_mycmd = mycmd
    ```
    * 載入指令後於 mininet 中使用：
    ```bash
    sudo mn --custom mycmd.py -v output
    mininet> help mycmd
    mycmd is an example command to extend the Mininet CLI
    mininet> mycmd foo
    mycmd invoked for <mininet.net.Mininet object at 0x7fd7235fb9d0> with line foo
    ```
## Try

* command
```
sudo mn --custom cmd.py -v output
```

* display
```
~/tests/mininet-python/mn(master*) » sudo mn --custom cmd.py -v output 
mininet> help mycmd
mycmd is an example command to extend the Mininet CLI
mininet> mycmd foo
mycmd invoked for <mininet.net.Mininet object at 0x7f0c68919150> with line foo
```