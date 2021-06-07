
---
title: 'Redkale 2.4.0 发布，Java 分布式微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-254910cc0f802310b992352c1ef18ce0cd9.png'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 20:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-254910cc0f802310b992352c1ef18ce0cd9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">Redkale 2.4.0 发布。</p> 
<p style="text-align:left">Redkale， 一个Java分布式微服务框架，1.4M的jar可以代替传统几十M的第三方。包含TCP/UDP、HTTP、RPC、依赖注入、序列化与反序列化、数据库操作、WebSocket等功能。  一方面模块高度整合，极大的简化业务开发代码，一方面暴露大量底层，方便二次框架开发。  </p> 
<p style="text-align:left">Java并不臃肿， 臃肿的是你自己的设计思维！</p> 
<p style="text-align:left">本次版本更新内容：</p> 
<p style="text-align:start">1、【新增】增加SearchSource模块功能<br> 2、【新增】增加HttpMessageLocalClient本地虚拟mq类<br> 3、【新增】DataSource增加带ChannelContext参数的方法<br> 4、【优化】【不兼容】 移除CacheSource中的泛型定义以及相关方法<br> 5、【优化】调整EntityCache部分内部实现<br> 6、【优化】注释掉部分标记为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdeprecated" target="_blank">@deprecated</a>的方法<br> 7、【优化】【不兼容】去掉HttpRender的泛型<br> 8、【优化】RestMapping.name 以 xxx/ 结尾的会变成 xxx/*<br> 9、【优化】HttpScope、Utility、AsyncConnection等类优化和增加了部分方法<br> 10、【修复】修复mqConfs[0]配置的bug<br> 11、修复2.3.0改造成nio后导致HttpRequest上传不了文件的bug<br> 12、修复HttpRender没有执行init方法的BUG<br> 13、修复HttpResponse.finishFile的bug</p> 
<p style="text-align:start"><span style="color:#333333">本次更新最大亮点是增加了SearchSource， 提供了Elasticsearch版的DataSource实现。</span></p> 
<p style="text-align:left">最新TFB的压测报告)中, redkale依旧性能强劲， 同时验证了redkale的json性能也是java中最好的。</p> 
<p style="text-align:left">地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3Ddeb1f040-aac4-4a54-b91c-02de27e5a35b%26hw%3Dph%26test%3Djson%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=deb1f040-aac4-4a54-b91c-02de27e5a35b&hw=ph&test=json&a=2</a></p> 
<p style="text-align:left"><img src="https://oscimg.oschina.net/oscnet/up-254910cc0f802310b992352c1ef18ce0cd9.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">（-j17 表示使用JDK 17 预览版）</p>
                                        </div>
                                      
</div>
            