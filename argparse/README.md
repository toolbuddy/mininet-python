# argparse 的使用

利用 python 提供的模組來達到 getopt 的功能！使用起來比起以往來的方便！

用起來跟 `node.js` 當中的 `commander` 套件相似！

# Usage

* 引入函式庫
```python
import argparse
```

* 建立 parser
    * `description`: 提供程式簡易的敘述
```python
parser=argparser.ArgumentParser(
    description='Something description about this program')
```

* 加入我們要 parse 的 argument 項目
    * name of flags: 前面用單引號包住的內容，同時也是程式被呼叫時，用 flags 來指定要存入什麼樣的變數中，或是做出什麼對應的操作
    * `metavar`: A name for the argument in usage messages.
        * 從下面 Usage 1 可以看到，這個範例中可以讓使用者輸入多個 integer 做使用；而每個輸入的數字都會被存放在由 metavar 指定的名稱的 N 當中
    * `nargs`: The number of command-line arguments that should be consumed.
        * 這邊可以指定這項 argument 可以支援幾個 variables 
        * Usage 1 中的 `+` 即表示 "多個"
        * 而 `*` 提供的功能與 `+` 類似，不過 `*` 表示的是可有可無，而 `+` 則表示數入的 argument 數量至少大於等於 1，否則會回傳錯誤訊息給使用者！
        * 也可以透過給予常數來限定我要的數目！
        * [更多詳細內容](https://docs.python.org/3/library/argparse.html#nargs)
    * `action`: The basic type of action to be taken when this argument is encountered at the command line.
        * 拿到輸入參數後做的動作
        * 這邊使用的是 `store_const`，內容以 *const* 型態做儲存
        * [更多詳細內容](https://docs.python.org/3/library/argparse.html#action)
    * `const`: A constant value required by some action and nargs selections.
        * 若 action 指定 `store_const`、`append_const`, 就必須要加上 `const` 這個項目
        * 這邊指定這些儲存的 const value 的處理動作；
        * 使用的是 `sum`，表示當 `--sum` 這個 flags 被使用時，則會把這些 const value list 做一個加總的動作
        * 若沒有指定，則會進到 `default` 指定的 `max`，取 const value list 中的最大值
    * `dest`: The name of the attribute to be added to the object returned by parse_args().
        * 這邊跟之後 parser 呼叫 `parse_args()` 後回傳的物件有關
        * `dest` 後面加的名稱即是回傳物件擁有的 function name!
        * 其功能由 `action` 所指定
    * `help`: 寫入這項 argument 相關的資訊內容，讓程式可以透過 `-h`, `--help` 來印出漂亮的幫助訊息
```python
# Usage 1
parser.add_argument('integers',metavar='N',type=int,nargs='+',help='an integer for the accumulator')
# Usage 2
parser.add_argument('-s','--sum',dest='sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
```

## Reference

* [Official site - argparse](https://docs.python.org/3/library/argparse.html)