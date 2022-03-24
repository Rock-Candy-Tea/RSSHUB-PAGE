
---
title: 'Logstash 8.1.1 发布，日志管理与统计工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1030'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1030'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Logstash 是一个应用程序日志、事件的传输、处理、管理和搜索的平台，可用于对应用程序日志进行收集管理，提供 Web 接口用于查询和统计。</span></p> 
<p><span style="color:#333333">目前 Logstash 发布了 8.1.1 版本，带来如下变更：</span></p> 
<h3><span style="color:#333333">修复</span></h3> 
<ul> 
 <li><code>bin/logstash-plugin uninstall <plugin></code> 命令按预期运行，可成功卸载指定插件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F13823" target="_blank">#13823</a></li> 
 <li>Logstash CLI 工具现在可以在 Windows 上使用选定的 JDK。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F13839" target="_blank">#13839</a></li> 
 <li>Logstash 可以成功定位到 Windows JVM，即使路径中包含空格 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F13881" target="_blank">#13881</a></li> 
 <li>GeoIP 数据库查找现在将正常使用 http_proxy 环境变量定义的代理。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F13840" target="_blank">#13840</a></li> 
</ul> 
<h3>依赖项升级</h3> 
<ul> 
 <li>捆绑的 JDK 版本更新为11.0.14.1+1。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Flogstash%2Fpull%2F13869" target="_blank">#13869</a></li> 
</ul> 
<p style="margin-left:0px">除此之外，该版本还包含一些插件问题修复，详情可查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Flogstash%2F8.1%2Flogstash-8-1-1.html%23_plugins" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            