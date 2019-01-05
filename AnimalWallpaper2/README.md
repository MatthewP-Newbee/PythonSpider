第一次尝试只获取了缩略图，这次使用 `selenium` 获取高清原图，获取3页好了。  
先使用 `selenium` 的 `find_elements()` 函数使用 `XPATH` 方式获取到每个缩略图的节点，这里用 `requests` 也可以完成，但是为了练习使用了
`selenium`，然后找到 `href` 属性就是我们平时点击缩略图跳转到大图的链接了，后面的步骤用 `requests` 完成，因为用 `selenium` 的 `click()` 
函数虽然能跳转网页，但是无法追踪到新打开的网页。