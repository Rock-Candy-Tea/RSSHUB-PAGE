
---
title: 'zlt-mp v4.4.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 09:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img alt src="https://oscimg.oschina.net/oscnet/up-45ebd22a4d43320cb3454a5f672087370c7.png" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left">功能介绍</h1> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a40df48eb5e79bff3622171ee91f4269395.png" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:left">更新内容</h2> 
<h3 style="text-align:left">特性/增强</h3> 
<ul> 
 <li>新增工程zlt-oss-spring-boot-starter</li> 
 <li>新增工程zlt-zookeeper-spring-boot-starter</li> 
 <li>新增Zookeeper分布式锁</li> 
 <li>优化日志埋点工具类</li> 
 <li>升级zlt-register/nacos到2.0.0</li> 
</ul> 
<h2 style="text-align:left"> </h2> 
<h2 style="text-align:left">内容说明</h2> 
<h3>一、新增工程oss-starter</h3> 
<p>既支持各种 <strong>「S3」</strong> 协议的对象存储如 <code>阿里云OSS</code>、<code>七牛云OSS</code>、<code>MinIO</code> 等，同时也支持阿里的 <code>FastDFS</code>。</p> 
<p>配置S3：</p> 
<pre><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">file-server:</span>
    <span style="color:#d19a66">type:</span> <span style="color:#98c379">s3</span>
    <span style="color:#d19a66">s3:</span>
      <span style="color:#d19a66">access-key:</span> <span style="color:#98c379">$&#123;zlt.s3.access-key&#125;</span>
      <span style="color:#d19a66">accessKeySecret:</span> <span style="color:#98c379">$&#123;zlt.s3.accessKeySecret&#125;</span>
      <span style="color:#d19a66">endpoint:</span> <span style="color:#98c379">$&#123;zlt.s3.endpoint&#125;</span>
      <span style="color:#d19a66">bucketName:</span> <span style="color:#98c379">$&#123;zlt.s3.bucketName&#125;</span>
</code></pre> 
<p>使用S3</p> 
<pre><code><span style="color:#61aeee">@Resource</span>
<span style="color:#c678dd">private</span> S3Template s3Template;

s3Template.upload(...);
</code></pre> 
<p> </p> 
<p>配置FastDFS：</p> 
<pre><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">file-server:</span>
    <span style="color:#d19a66">type:</span> <span style="color:#98c379">fastdfs</span>
    <span style="color:#d19a66">fdfs:</span>
      <span style="color:#d19a66">web-url:</span> <span style="color:#98c379">$&#123;zlt.fdfs.web-url&#125;</span>
      
<span style="color:#d19a66">fdfs:</span>
  <span style="color:#d19a66">trackerList:</span> <span style="color:#98c379">$&#123;zlt.fdfs.trackerList&#125;</span>
</code></pre> 
<p>使用FastDFS</p> 
<pre><code><span style="color:#61aeee">@Resource</span>
<span style="color:#c678dd">private</span> FdfsTemplate fdfsTemplate;

fdfsTemplate.upload(...);
</code></pre> 
<p> </p> 
<h3>二、新增工程zookeeper-starter</h3> 
<p>集成 <code>curator</code> 客户端</p> 
<p>配置：</p> 
<pre><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">zookeeper:</span>
    <span style="color:#d19a66">connectString:</span> <span style="color:#d19a66">127.0</span><span style="color:#d19a66">.0</span><span style="color:#d19a66">.1</span><span style="color:#98c379">:2181</span>
</code></pre> 
<p> </p> 
<h3>三、新增zookeeper分布式锁</h3> 
<p>依赖：</p> 
<pre><code><<span style="color:#e06c75">dependency</span>>
    <<span style="color:#e06c75">groupId</span>>com.zlt</<span style="color:#e06c75">groupId</span>>
    <<span style="color:#e06c75">artifactId</span>>zlt-zookeeper-spring-boot-starter</<span style="color:#e06c75">artifactId</span>>
</<span style="color:#e06c75">dependency</span>>
</code></pre> 
<p>配置：</p> 
<pre><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">lock:</span>
    <span style="color:#d19a66">lockerType:</span> <span style="color:#98c379">ZK</span>
</code></pre> 
<p>手动加锁：</p> 
<pre><code><em>//lock</em>
<span style="color:#c678dd">try</span> (
        ZLock lock = locker.lock(<span style="color:#98c379">"test"</span>);
        ) &#123;
    <em>//......业务逻辑</em>
&#125;

<em>//tryLock</em>
<span style="color:#c678dd">try</span> (
        ZLock lock = locker.tryLock(<span style="color:#98c379">"test"</span>, <span style="color:#d19a66">10</span>, TimeUnit.SECONDS);
        ) &#123;
    <span style="color:#c678dd">if</span> (lock != <span style="color:#c678dd">null</span>) &#123;
        <em>//......业务逻辑</em>
    &#125;
&#125;
</code></pre> 
<p>注解加锁：</p> 
<pre><code><em>/**
 * 等同于 locker.lock("test")
 */</em>
<span style="color:#61aeee">@Lock</span>(key = <span style="color:#98c379">"test"</span>)
<span style="color:#c678dd">public</span> <span style="color:#c678dd">void</span> <span style="color:#61aeee">test</span>() &#123;&#125;

<em>/**
 * 等同于 locker.tryLock("test", 10, TimeUnit.SECONDS)
 */</em>
<span style="color:#61aeee">@Lock</span>(key = <span style="color:#98c379">"test"</span>, waitTime = <span style="color:#d19a66">10</span>)
<span style="color:#c678dd">public</span> <span style="color:#c678dd">void</span> <span style="color:#61aeee">test2</span>() &#123;&#125;
</code></pre> 
<p> </p> 
<h3>四、优化日志埋点工具类</h3> 
<p>埋点工具类 <code>PointUtil</code> 新增 <strong>「builder」</strong> 模式，如下代码所示：</p> 
<pre><code>Map properties = <span style="color:#c678dd">new</span> HashMap(<span style="color:#d19a66">2</span>);
properties.put(<span style="color:#98c379">"key1"</span>, <span style="color:#98c379">"value1"</span>);
properties.put(<span style="color:#98c379">"key2"</span>, <span style="color:#98c379">"value2"</span>);

PointUtil.builder()
        .id(<span style="color:#d19a66">1</span>)
        .type(<span style="color:#98c379">"test"</span>)
        .properties(properties)
        .build();
</code></pre> 
<blockquote> 
 <p>输出日志：2021-04-03 23:18:19.112|user-center|1|test|key1=value1&key2=value2</p> 
</blockquote> 
<p> </p> 
<h3>五、升级zlt-register到2.0.0</h3> 
<p><code>zlt-register/nacos</code> 替换为官方最新的 <code>2.0.0</code> 版本</p> 
<blockquote> 
 <p>内容与官网一致，只是方便大家直接使用</p> 
</blockquote> 
<p> </p> 
<h2 style="text-align:left"><strong>项目地址</strong></h2> 
<p style="text-align:left">Gitee地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="text-align:left">Github地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="text-align:left">项目文档</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="text-align:left">项目更新日志</h2> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/936235</a></p>
                                        </div>
                                      
</div>
            