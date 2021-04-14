
---
title: 'Easy_Trans 1.0.3 发布，添加 Mybatis Plus 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aeefd95d0b9f8a43be32d8f43dad8cbdc6a.JPEG'
author: 开源中国
comments: false
date: Wed, 14 Apr 2021 17:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aeefd95d0b9f8a43be32d8f43dad8cbdc6a.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <ol> 
 <li><strong>Easy_Trans 1.0.3 更新说明</strong></li> 
</ol> 
<p><strong>    </strong>A 添加了Mybatis Plus的扩展，让MP项目用起来更简单</p> 
<p>    B 添加了@TransMethodResult 注解，加到方法上会自动对返回结果进行翻译</p> 
<p style="text-align:left"><strong>2、Easy Trans简介</strong></p> 
<p style="text-align:left"><strong>  </strong>  easy trans是一个springboot的字典/外键 翻译组件，可以不用表关联查询 根据字典码 外键翻译  字典描述 和title/name 等信息，使用效果和方法如下图：</p> 
<p><img alt height="700" src="https://oscimg.oschina.net/oscnet/up-aeefd95d0b9f8a43be32d8f43dad8cbdc6a.JPEG" width="1000" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>3、Easy Trans集成</strong></p> 
<p style="text-align:left">EasyTrans支持 进程缓存翻译，redis缓存翻译，动态查表三种方式，集成步骤如下：</p> 
<p style="text-align:left">1 、先把maven 引用加上</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span>
    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span>
    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy-trans-spring-boot-starter<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span>
    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.0.3<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span>
<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></pre> 
 </div> 
 <p>2 、如果是Mybatis Plus 项目另外需要加下面的扩展 </p> 
 <pre><code class="language-xml"><dependency>
   <groupId>com.fhs-opensource</groupId>
   <artifactId>easy_trans_mybatis_plus_extend</artifactId>
   <version>1.0.3</version>
</dependency></code></pre> 
 <p> </p> 
</div> 
<p style="text-align:left">3、如果使用Redis 换存翻译请添加redis的引用(如果之前加过了请不要重复添加)</p> 
<div style="text-align:left"> 
 <div> 
  <pre>        <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span>
            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>org.springframework.boot<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span>
            <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>spring-boot-starter-data-redis<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span>
        <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></pre> 
 </div> 
</div> 
<p style="text-align:left">4、在yaml中添加如下配置</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span style="color:#008080"><span style="color:#6f42c1">easy-trans</span></span><span style="color:#6f42c1">:</span>
   <span style="color:#008080"><span style="color:#6f42c1">autotrans</span></span><span style="color:#6f42c1">:</span>
       <span style="color:#888888"><span style="color:#6a737d">#您的service/mapper 所在的包 支持通配符比如com.*.**.service.**，他的默认值是com.*.*.service.impl</span></span>
       <span style="color:#008080"><span style="color:#6f42c1">package</span></span><span style="color:#6f42c1">:</span> <span style="color:#dd2200"><span style="color:#032f62">com.fhs.test.service.**;</span></span> <span style="color:#dd2200"><span style="color:#032f62">com.fhs.test.mapper.**;</span></span>
<span style="background-color:#ffadad; color:#a61717"></span>   <span style="color:#888888"><span style="color:#6a737d">#启用redis缓存</span></span>
   <span style="color:#008080"><span style="color:#6f42c1">is-enable-redis</span></span><span style="color:#6f42c1">:</span> <span style="color:#008080"><span style="color:#005cc5">true</span></span>
  
<span style="color:#008080"><span style="color:#6f42c1">spring</span></span><span style="color:#6f42c1">:</span>
  <span style="color:#008080"><span style="color:#6f42c1">redis</span></span><span style="color:#6f42c1">:</span>
    <span style="color:#008080"><span style="color:#6f42c1">host</span></span><span style="color:#6f42c1">:</span> <span style="color:#dd2200">192.168.0.213</span>
    <span style="color:#008080"><span style="color:#6f42c1">port</span></span><span style="color:#6f42c1">:</span> <strong>6379</strong>
    <span style="color:#008080"><span style="color:#6f42c1">password</span></span><span style="color:#6f42c1">:</span> <strong>123456</strong>
    <span style="color:#008080"><span style="color:#6f42c1">database</span></span><span style="color:#6f42c1">:</span> <strong>0</strong>
    <span style="color:#008080"><span style="color:#6f42c1">timeout</span></span><span style="color:#6f42c1">:</span> <strong>6000</strong></pre> 
 </div> 
</div> 
<p style="text-align:left">4、如果不使用redis，请在启动类加禁用掉redis的自动配置类</p> 
<div style="text-align:left"> 
 <div> 
  <pre>@<span style="color:#d73a49">SpringBootApplication</span>(<span style="color:#d73a49">exclude</span> = &#123; <strong><span style="color:#d73a49">RedisAutoConfiguration</span></strong><span style="color:#6f42c1">.</span><span style="color:#008080"><span style="color:#6f42c1">class</span></span> &#125;)</pre> 
 </div> 
 <p style="text-align:left"><strong>4. 传送门</strong></p> 
 <p style="text-align:left">源码和其他高级特性使用教程 <a href="https://gitee.com/fhs-opensource/easy_trans">https://gitee.com/fhs-opensource/easy_trans</a></p> 
 <p style="text-align:left">集成demo:<a href="https://gitee.com/fhs-opensource/easy_trans_springboot_demo">https://gitee.com/fhs-opensource/easy_trans_springboot_demo</a></p> 
</div>
                                        </div>
                                      
</div>
            