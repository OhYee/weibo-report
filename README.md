# 微博反黑小助手

具体干什么用的，咱也不知道，咱也不敢问。我就是被拉过来写代码的。

## 步骤

1. 将用户信息写入到`user.txt`中，将要举报的链接写入到`url.txt`中。格式为一行一组数据，账号和密码使用空格隔开
2. 由于国外代理会导致页面强制跳转，因此只会使用中国大陆以及香港地区代理
3. 开始执行任务后，会模拟登录微博(使用[xchaoinfo/fuck-login](https://github.com/xchaoinfo/fuck-login)相关部分代码)
4. 登陆时可能会需要输入验证码，会在目录下输出图片文件(`cha.jpg`)，识别输入即可
5. 登录成功后执行相应的举报任务

## 致谢

- [jhao104/proxy_pool](https://github.com/jhao104/proxy_pool)
- [xchaoinfo/fuck-login](https://github.com/xchaoinfo/fuck-login)