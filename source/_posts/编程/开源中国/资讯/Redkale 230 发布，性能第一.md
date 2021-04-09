
---
title: 'Redkale 2.3.0 发布，性能第一'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-094a6326c0ce85a079d281849786f561cfd.png'
author: 开源中国
comments: false
date: Fri, 09 Apr 2021 01:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-094a6326c0ce85a079d281849786f561cfd.png'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Redkale 2.3.0 发布。Redkale， 一个Java分布式微服务框架，1.3M的jar可以代替传统几十M的第三方。包含TCP/UDP、HTTP、RPC、依赖注入、序列化与反序列化、数据库操作、WebSocket等功能。  一方面模块高度整合，极大的简化业务开发代码，一方面暴露大量底层，方便二次框架开发。  </p> 
<p style="text-align:left">Java并不臃肿， 臃肿的是你自己的设计思维！</p> 
<p style="text-align:left">本次版本更新内容：</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#24292e">1、【新增】增加网络层client包</span><br> <span style="background-color:#ffffff; color:#24292e">2、【新增】增加CacheClusterAgent功能</span><br> <span style="background-color:#ffffff; color:#24292e">3、【新增】增加ConvertSmallString、JsonCharsWriter、JsonFinalArrayEncoder</span><br> <span style="background-color:#ffffff; color:#24292e">4、【优化】net层实现由aio(nio.2)改成nio实现，性能大幅提高</span><br> <span style="background-color:#ffffff; color:#24292e">5、【优化】Application 增加 reloadConfig 方法</span><br> <span style="background-color:#ffffff; color:#24292e">6、【优化】WebSocket兼容connection:upgrade 小写的upgrade</span><br> <span style="background-color:#ffffff; color:#24292e">7、【优化】</span>@Local<span style="background-color:#ffffff; color:#24292e"> </span>@Autoload<span style="background-color:#ffffff; color:#24292e">(false) Service 能自动加载</span><br> <span style="background-color:#ffffff; color:#24292e">8、【优化】优化cluster、mq包</span><br> <span style="background-color:#ffffff; color:#24292e">9、【修复】修复HttpSimpleRequest的path编码bug</span></p> 
<p style="text-align:left">本次更新最大亮点是net层由aio改成nio， 性能得到大幅提升。</p> 
<p style="text-align:left">最新TFB的压测报告)中, redkale暂居第一。</p> 
<p style="text-align:left">地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D6ba8043b-bfc2-47c1-8450-1eb0520ef3ba%26hw%3Dph%26test%3Dplaintext%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=6ba8043b-bfc2-47c1-8450-1eb0520ef3ba&hw=ph&test=plaintext&a=2</a></p> 
<p style="text-align:left"><img height="902" src="https://oscimg.oschina.net/oscnet/up-094a6326c0ce85a079d281849786f561cfd.png" width="1274" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">        （后缀 -pgc 表示开启了 -XX:+UseParallelGC  -zgc 表示开启了 -XX:+UseZGC）</p> 
<p style="text-align:left">   redkale一直采用的是aio，aio使用起来非常简单， 后面发现JDK自带的aio性能并不理想， 所以这一版将aio切换成nio，得利于redkale早期良好的设计，在net层定义了AsyncConnection，屏蔽了aio和nio的差异，因此aio改nio并没有涉及很多改动。 改完后在TFB做了测试，效果还是比较理想的。</p> 
<p style="text-align:left">   redkale压测结果不仅排前列， 而且redkale的测试代码也是TFB前50名中唯一一个按真实项目中使用的方式来写的：</p> 
<p style="text-align:left"><img height="621" src="https://oscimg.oschina.net/oscnet/up-368281b6637c53b704f314a9e04f91957d4.png" width="818" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">而其他几乎所有java项目是按最底层的Handler或Servlet来写的， 例如：</p> 
<p style="text-align:left"><img height="435" src="https://oscimg.oschina.net/oscnet/up-2bc0ba9ab3eb8c614dd5e2b3c1c3651f75e.png" width="772" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">  redkale不仅net层性能强劲，  在json方面在java中也是数一数二的。</p> 
<p style="text-align:left"><img height="1455" src="https://oscimg.oschina.net/oscnet/up-02248fb7fa9ebeec2ff3732085e2442998d.png" width="1279" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">     上图是最近两次TFB的json项压测结果， 一次redkale排java中第二， 另一次排java中第一。 </p> 
<p style="text-align:left">   由第三方压测数据来看， redkale是个高性能的类似J2EE的全功能框架。 使用redkale开发一般系统， 几乎不需要引用其他第三方。</p> 
<p style="text-align:left">Redkale官网： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredkale.org%2F" target="_blank">https://redkale.org</a></p>
                                        </div>
                                      
</div>
            