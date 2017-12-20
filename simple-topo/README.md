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

## Reference

* Introduction of mininet - [Creating topologies](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#creating-topologies)

## Other

* Store current dependencies
```
pip freeze > requirements.txt
```