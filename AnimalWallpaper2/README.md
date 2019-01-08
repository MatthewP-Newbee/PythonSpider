第一次尝试只获取了缩略图，这次使用 `selenium` 获取高清原图，获取3页好了。  
先使用 `selenium` 的 `find_elements()` 函数使用 `XPATH` 方式获取到每个缩略图的节点，这里用 `requests` 也可以完成，但是为了练习使用了
`selenium`，使用 `click()` 函数打开图片，然后用获取新打开的选项卡，用 `switch_to.window()` 切换到图片网页。最后获取真的图片 `id` 和 `url`
使用 `requests` 下载图片。