
---
title: '🚀Jarboot 服务管理诊断 v2.2.2 Docker 及示例更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 15:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#40485b">🔥 Jarboot <strong>Docker</strong>版本因JDK17目前存在部分兼容性问题，改用JDK12版本的镜像，使用旧版本的可以升级下镜像</span>。<span style="background-color:#ffffff; color:#40485b">另外最新版完整的Demo示例已更新到了百度网盘、</span>阿里云盘和技术交流QQ群中。</p> 
<p><span style="background-color:#ffffff; color:#40485b">Jarboot 是一个强大的Java进程管理、诊断的平台，可以在线管理、监控及诊断本地和远程的Java进程。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">最佳实践Demo：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot-with-spring-cloud-alibaba-example" target="_blank">https://github.com/majianzheng/jarboot-with-spring-cloud-alibaba-example</a></p> 
<p><img alt height="540" src="https://oscimg.oschina.net/oscnet/up-75f72cf92ef78e3a5ded35a7a4ca45ecc51.gif" width="980" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">觉得不错的可以Star⭐️支持</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub主页：<span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmajianzheng%2Fjarboot" target="_blank">https://github.com/majianzheng/jarboot</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee主页：<a href="https://gitee.com/majz0908/jarboot">https://gitee.com/majz0908/jarboot</a></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Docker Hub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fregistry.hub.docker.com%2Fr%2Fmazheng0908%2Fjarboot" target="_blank">https://registry.hub.docker.com/r/mazheng0908/jarboot</a></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-bash"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">sudo</span></span></span> <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">docker run -itd --name jarboot -p 9899:9899 mazheng0908/jarboot</span></span></span></code></pre> 
<p>完整Demo示例下载：</p> 
<p><span style="background-color:#ffffff; color:#40485b">示例包含了Spring Cloud的典型服务（业务服务、API网关）、Nacos、Sentinel、Seata等。 由于是完整的可运行环境，文件较大放在了网盘中，下载后解压即可用，</span><span style="background-color:#ffffff; color:#40485b">☀️</span><span style="background-color:#ffffff; color:#40485b">注意</span><strong style="color:#40485b">Windows</strong><span style="background-color:#ffffff; color:#40485b">环境下</span><strong style="color:#40485b">Seata</strong><span style="background-color:#ffffff; color:#40485b">的服务配置中需要修改</span><strong style="color:#40485b">boot.vmoptions</strong><span style="background-color:#ffffff; color:#40485b">中的classpath为</span><strong style="color:#40485b">-classpath ./conf;./lib/*。</strong></p> 
<ul> 
 <li>阿里云盘：<a href="https://gitee.com/link?target=https%3A%2F%2Fwww.aliyundrive.com%2Fs%2F3oAWkRZgDtr">https://www.aliyundrive.com/s/3oAWkRZgDtr</a></li> 
 <li>百度网盘:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1PvIIZP5LXjEJAM5uj4ye4w">https://pan.baidu.com/s/1PvIIZP5LXjEJAM5uj4ye4w</a><span> </span>提取码: 8yh5</li> 
</ul> 
<p> 关于v2.2.2版本更新内容：<a href="https://www.oschina.net/news/174617/jarboot-2-2-2-released">https://www.oschina.net/news/174617/jarboot-2-2-2-released</a></p>
                                        </div>
                                      
</div>
            