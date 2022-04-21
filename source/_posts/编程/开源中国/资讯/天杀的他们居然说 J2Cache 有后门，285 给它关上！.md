
---
title: '天杀的他们居然说 J2Cache 有后门，2.8.5 给它关上！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0421/091638_9PIi_12.jpg'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 09:22:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0421/091638_9PIi_12.jpg'
---

<div>   
<div class="content">
                                                                                            <p>昨天有个朋友的公司要用 J2Cache ，然后用公司的一些工具对这个项目检测，居然发现 J2Cache 暗藏后门！！！</p> 
<p>而且还截图给我看，如下图：</p> 
<p><img height="1536" src="https://static.oschina.net/uploads/space/2022/0421/091638_9PIi_12.jpg" width="2048" referrerpolicy="no-referrer"></p> 
<p>我的天啊，jansi.dll   我第一眼看到的这个名字以为是 ： 监视.dll</p> 
<p>原来是 J2Cache 使用的一个三方依赖 jline 包里包含了这个“后门”。不过大家也不用担心，因为 J2Cache 用 jline 只是一个测试小工具，用来对两级缓存进行测试的，实际作为缓存使用的时候并不会用到。</p> 
<p>没有必要依赖这个项目，紧急发布了一个更新版本 2.8.5 ，去掉了 jline 这个依赖！</p> 
<p>版本信息：</p> 
<pre><code class="language-xml"><dependency>
  <groupId>net.oschina.j2cache</groupId>
  <artifactId>j2cache-core</artifactId>
  <version>2.8.5-release</version>
</dependency></code></pre> 
<p>建议更新。</p> 
<hr> 
<p>是我无知了，这不是后门：</p> 
<p>已经证实这不是一个后门，而是 jline 依赖了另外一个开源项目 <a href="https://www.oschina.net/p/jansi">jansi</a></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><span style="color:#db2828">Jansi</span><span> </span>是一个 Java 类库，它能够让你在控制台输出色彩缤纷的文字。</p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">示例代码：</p> 
<pre style="text-align:start">AnsiConsole.systemInstall();
AnsiConsole.out.println("Hello World");</pre> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><img alt="before" src="http://static.oschina.net/uploads/img/201408/27070824_hf46.png" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><img alt="after" src="http://static.oschina.net/uploads/img/201408/27070824_qSSN.png" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            