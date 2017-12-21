# mininet CLI

使用 mininet 提供的 CLI API，在我們建置完 mininet 內網路配置後，可以直接呼叫 mininet API 開啟 CLI 介面開始操作

## simple-cli

* 簡單範例，建置網路配置，並開啟 CLI 

### xterm <host>

* 使用前，需確認是否安裝 xterm 的相依性
```bash
sudo apt install xterm
```

* 在 mininet 裡頭，可以透過呼叫 xterm + host 裝置（h1,h2...）來開啟該裝置的 process
* 值得一提的是，這些 host 的網路介面（`hx-ethx`）在一般 process 裏面 `ifconfig` 下是看不到的，與本機 host 的 namespace 不同
    * 而 switch 的網路介面（`sx-ethx`）則是與本機 host 相同，透過 `veth` 與不同 namespace 的 host 做連接

* 使用：
    * 等程式進入 mininet 的 CLI 時，即可輸入指令： `xterm <host>`，會額外開啟一個 xterm 視窗做為該 host 的 console
    * 雖然網路介面不同，但這些 process 運行的環境還是跟本機一樣的（都在運行 mininet CLI 程式同個 workspace）