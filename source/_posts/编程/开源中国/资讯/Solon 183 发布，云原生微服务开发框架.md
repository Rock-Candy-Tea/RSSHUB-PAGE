
---
title: 'Solon 1.8.3 发布，云原生微服务开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7b0e77f536aa245971fa50ea2809f89c4ba.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 16:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7b0e77f536aa245971fa50ea2809f89c4ba.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目</h3> 
<ul> 
 <li>启动快 5 ～ 10 倍</li> 
 <li>qps 高 2～ 3 倍</li> 
 <li>运行时内存节省 1/3 ~ 1/2</li> 
 <li>打包可以缩小到 1/2 ~ 1/10（比如，90Mb 的变成了 9Mb）</li> 
 <li>基于 app.name 进行注册发现 与 k8s svc 相互对应</li> 
 <li>支持 Service Mesh 架构部署方案</li> 
</ul> 
<h3 style="text-align:start">关于 Solon</h3> 
<p style="color:#24292e; text-align:start">Solon 是一个更现代感的应用开发框架，轻量、开放生态型的。支持 Web、Data、Job、Remoting、Cloud 等任何开发场景。</p> 
<ul> 
 <li>强调，<strong>克制 + 简洁 + 开放 + 生态的原则</strong></li> 
 <li>力求，<strong>更小、更少、更快、更自由的体验</strong></li> 
</ul> 
<p style="color:#24292e; text-align:start">目前有近<strong>130</strong>个生态插件，含盖了日常开发的各种需求：</p> 
<p style="color:#24292e; text-align:start"><img height="591" src="https://oscimg.oschina.net/oscnet/up-7b0e77f536aa245971fa50ea2809f89c4ba.png" width="717" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">本次主要更新内容</h3> 
<ul> 
 <li>添加 solon.extend.config 属性配置支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-bash">java -Dsolon.extend.config=./app.yml -jar demoapp.jar
</code></pre> 
<ul> 
 <li>添加 ContextPathFilter 类，摸拟 contextPath 效果</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span style="color:#a626a4">public</span> <span style="color:#a626a4">class</span> <span style="color:#c18401">App</span>&#123;
    <span style="color:#a626a4">public</span> <span style="color:#a626a4">static</span> <span style="color:#a626a4">void</span> <span style="color:#4078f2">main</span><span>(String[] args)</span>&#123;
        Solon.start(App.class, args);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>修复 @Inject("$&#123;list&#125;") List<span> </span>list ，数据不对的问题</li> 
 <li>插件 solon.boot.jdkhttp，添加 ssl 支持（尝试替代 jlhttp ；框架性能高 50%）</li> 
 <li>插件 sqltoy-solon-plugin 升级为 sqltoy 5.2.0</li> 
 <li>插件 weed3-solon-plugin 升级 weed3 3.4.26</li> 
 <li>插件 beetlsql-solon-plugin 升级 beetlsql 3.14.4-RELEASE</li> 
 <li>插件 solon-api, solon-web 默认改用 jdkhttp</li> 
 <li>添加 server.host 和 server.?.host 支持</li> 
 <li>添加 StaticMappings::remove 接口</li> 
 <li>添加 EventBus::unsubscribe 接口</li> 
 <li>snack3 升为 3.2.29</li> 
 <li>fastjson 升为 1.2.83</li> 
 <li>hutool 升为：5.8.1</li> 
 <li>jetty 升为：9.4.46.v20220331</li> 
 <li>undertow 升为：2.2.17.Final</li> 
 <li>jackson 升为：2.13.3</li> 
 <li>gson 升为：2.9.0</li> 
</ul> 
<h3 style="text-align:start">进一步了解 Solon</h3> 
<ul> 
 <li><a href="https://my.oschina.net/noear/blog/4980834">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/4863844">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://my.oschina.net/noear/blog/5039169">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<h3 style="text-align:start">项目地址</h3> 
<ul> 
 <li>gitee：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsolon" target="_blank">https://github.com/noear/solon</a></li> 
 <li>website:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsolon.noear.org%2F" target="_blank">https://solon.noear.org</a></li> 
</ul>
                                        </div>
                                      
</div>
            