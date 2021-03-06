# Simple Topo

* A simplest example of using mininet API in python.

## Get Started

* Install Mininet (Under `ubuntu 16.04.3 LTS`)
```
sudo apt install mininet
```

* Install ovs controller 
```
sudo apt install openvswitch-testcontroller

sudo ln /usr/bin/ovs-testcontroller /usr/bin/controller
```

* Install dependencies 
```
pip install -r requirements.txt
```

## Run 

```
sudo python main.py
```

## Explain & Learn

### Simple Topology
* 先看到程式碼內`繼承 Topo`的 SingleSwitchTopo
    * Topo - [source code]
    * 可以看到在 `__init__` 的 constructor 最後呼叫了 build function
    * 而在這邊繼承後則修改 build function (override!)
    * 再範例裏面則是在 build function 內加入 switch 並且實作 n 個 host 與這個 switch 連接
        * `self.addSwitch`: 產生 switch 進 topology 中，回傳 switch name
        * `self.addHost`: 產生 host device，回傳 host name
        * `self.addLink`: 產生 switch & host device 間的`雙向`連線，也會回傳一個 link key；
* Mininet()
    * 產生一個可操作的網路環境
    * 運行 `.start()` 來執行開始網路
    * `pingAll()` 測試每個 nodes 之間的連線是否通暢
    * `stop()` 停止 mininet

這樣就可以產生你所建立的網路狀態!

* setLogLevel
    * `setLogLevel( 'info' | 'debug' | 'output' )`: set Mininet's default output level; 'info' is recommended as it provides useful information.

### Setting Performance Parameter

* 在這個範例中，展示 mininet 的 API，除了剛剛做出創建 host, switch, link 等等操作之外，還可以控制幾項：
    * link 的多項參數調整
    * host 的使用資源
* 還可以使用 iperf 的操作，讓兩個 host 做 iperf 測試 TCP bandwidth 

## Reference

* Introduction of mininet - [Creating topologies](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#creating-topologies)

* Introduction of mininet - [Setting performance parameters](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#setting-performance-parameters)



## Other

* Store current dependencies
```
pip freeze > requirements.txt
```