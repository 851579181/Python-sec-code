#Python_Benchmark

本来是用于测试针对Python代码的静态扫描器效果的benchmark,基于`flask`应用创建，整理了一下发现也可以当做在CTF中的Python题的一点点整理，用于过WAF，目前RCE样本整理的相对来说是比较全面的（当然肯定有缺，后期慢慢补）

手工或者黑盒测试执行执行`python manager.py`即可

目前含括的漏洞类型包括：
- SSRF
- Sql injection
- RCE
- 任意文件下载

##ps：
- 因为靶场中的样例有些是基于python2，有些是基于python3，所以如果用于黑盒扫描器测试或者手工测试会出现问题
- 白盒扫描的过程中可能会出现污点无法追踪下去的情况，因为相对来说本应用使用了蓝图路由略微有那么一丢丢的复杂
- 友情链接同团队大佬项目：[@joyhou](https://github.com/JoyChou93)老师的[java-sec-code](https://github.com/JoyChou93/java-sec-code), 和[Anemone](https://github.com/Anemone95/)的[node-sec-code](https://github.com/Anemone95/NodeSecCode)
- 有意共事的师傅整活儿 Email：yangjie.syc@alibaba-inc.com 摸摸哒