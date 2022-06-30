
---
title: 'Magician 2.0.3 发布，支持监听多端口'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8842'
author: 开源中国
comments: false
date: Thu, 30 Jun 2022 14:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8842'
---

<div>   
<div class="content">
                                                                                            <p><strong><span style="color:#000000">Magician 大家可能比较陌生，在介绍本次更新前 先简单介绍一下吧：</span></strong></p> 
<p><span style="color:#000000">Magician是一套web开发的工具集，开发者可以自由选择自己想用的工具，可以选择只用一个小型的http服务包开发一个微型服务，也可以搭配MVC 来实现一个常规的web服务，也可以只选择JDBC框架 对数据库进行操作，也可以全部一起用，实现一个完整的web服务，同时我们也会提供各种小型组件库，来方便开发者。</span></p> 
<p><span style="color:#000000">目前已经发布了三个包，分别是Magician，Magician-Web，Magician-JDBC，他们分别对应，小型http服务器，MVC框架，数据库操作框架。</span></p> 
<p><strong><span style="color:#000000">本次更新的部分在于第一个包 - Magician (Magician既是这一套项目的名称，也是核心组件的名称)：</span></strong></p> 
<p>Magician是一个基于Netty的小型HTTP服务包，可以很方便的启动一个HTTP服务，支持WebSocket，采用注解来配置Handler。</p> 
<p>如果你想用netty开发一个http服务，但发现它很麻烦，那么Magician可能会帮到你。</p> 
<h3>本次更新的点</h3> 
<ol> 
 <li>支持自定义配置</li> 
 <li>支持监听多端口</li> 
 <li>同一个项目中，可以多地使用</li> 
</ol> 
<h3>自定义配置</h3> 
<p>以前，我们启动一个Magician服务，只能用默认的配置，现在有这么几个配置项支持自定义了</p> 
<pre><code class="language-java">MagicianConfig magicianConfig = new MagicianConfig();
magicianConfig.setNumberOfPorts(3); // 允许同时监听的端口数量，默认1个
magicianConfig.setBossThreads(1); // netty的boss线程数量 默认1个
magicianConfig.setWorkThreads(3); // netty的work线程数量 默认3个
magicianConfig.setNettyLogLevel(LogLevel.DEBUG); // netty的日志打印级别
magicianConfig.setMaxInitialLineLength(4096); // http解码器的构造参数1，默认4096 跟netty一样
magicianConfig.setMaxHeaderSize(8192); // http解码器的构造参数2，默认8192 跟netty一样
magicianConfig.setMaxChunkSize(8192); // http解码器的构造参数3，默认8192 跟netty一样</code></pre> 
<p>所有配置项都有默认值，所以在使用的时候 可以只选择自己需要更改的配置项进行设置，设置好了以后需要添加到HttpServer实例中</p> 
<pre><code class="language-java">Magician.createHttp()
        .scan("com.test")// 扫描范围（包名）
        .setConfig(magicianConfig) // 添加配置
        .bind(8080);</code></pre> 
<h3>监听多端口</h3> 
<p>很简单，只需要调用bind方法多次即可</p> 
<pre><code class="language-java">HttpServer httpServer = Magician.createHttp()
        .scan("com.test")// 扫描范围（包名）
        .setConfig(magicianConfig); // 添加配置

httpServer.bind(8080);
httpServer.bind(8081); 
httpServer.bind(8082); </code></pre> 
<h3>同项目中，多地使用</h3> 
<p>有时候可能会遇到这种需求，我们需要一个主服务对外提供接口，但是还需要一个次服务，实现内部通信，这个时候可能就需要启动两个服务了。 在本次升级的时候，为了实现监听多端口，bind已经变成异步的方法了，在调用bind以后，不会阻塞，而是可以继续往下执行，所以这个需求得到了完美的解决， 有两个实现方案。</p> 
<p><strong>1. 监听两个端口，把对外和对内分开</strong></p> 
<p><strong>2. 直接启动两个服务，把端口，配置，线程全都分开</strong></p> 
<p>第一种方法，不用多说，相信大家都知道怎么做了，咱们重点说说第二种方法，跟监听多端口差不多的思路，只不过变成了启动两个服务，比如：</p> 
<p><strong>启动一个对外服务</strong></p> 
<pre><code class="language-java">// 将8080端口做为对外的端口，并且scan只扫描对外的资源（接口，handler等）

HttpServer httpServer = Magician.createHttp()
        .scan("com.test")// 只扫描对外的资源
        .setConfig(magicianConfig); // 添加配置

httpServer.bind(8080);</code></pre> 
<p><strong>启动一个对内服务</strong></p> 
<pre><code class="language-java">// 将8081端口做为对内的端口，并且scan只扫描对内的资源（接口，handler等）

HttpServer httpServer = Magician.createHttp()
        .scan("com.test")// 只扫描对内的资源
        .setConfig(magicianConfig); // 添加配置

httpServer.bind(8081);</code></pre> 
<h3>想了解更多，可以访问官网</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmagician-io.com" target="_blank">https://magician-io.com</a></p>
                                        </div>
                                      
</div>
            