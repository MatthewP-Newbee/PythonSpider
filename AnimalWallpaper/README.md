[wallhaven](https://alpha.wallhaven.cc/)是我常逛的壁纸网站，试着爬一下里面包含标签为 `animal` 的图片，爬10页并且存在本地。  
手动在网页点击标签 `animal` 分析一下请求。   
```bash
Request URL: https://alpha.wallhaven.cc/search?q=id:82
Request Method: GET
Status Code: 200 
Remote Address: 104.24.4.58:443
Referrer Policy: no-referrer-when-downgrade
```
我们标签 `animal` 就是搜索的 `q=id:82`  
这个网页往下拉，能自动出现下一页内容且不刷新，因此是用 `Ajax` 的，我们多下拉几页，观察规律。能够发现其他内容都不变，只有 `page` 改变，控制页数。
```bash
q: id:82
page: 2
```
根据这点我们配合 `urlencode` 就能获取到每一页的 `url` 再用 `requests.get()` 获取内容。使用 `lxml.etree` 解析我们的内容，这个网页很简单，
我们很容易就找到 `li` 下的 `figure` 的子节点 `img` 代表着图片，里面的 `data-src` 属性是图片 `url` ，获得图片 `url` 爬下来存在文件就好了。