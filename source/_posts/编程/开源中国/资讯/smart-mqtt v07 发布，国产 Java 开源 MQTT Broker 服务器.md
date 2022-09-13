
---
title: 'smart-mqtt v0.7 发布，国产 Java 开源 MQTT Broker 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6430'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 09:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6430'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:start">一、关于 smart-mqtt</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">smart-mqtt 是用 java 语言开发的 MQTT Broker 服务，也是 smartboot 组织下首款真正意义上面向物联网的解决方案。旨在帮助企业以较低的成本快速搭建稳定、可靠的物联网服务，助力万物互联互通。</p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:start">二、快速启动</h1> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">2.1 Jar 包启动</h2> 
<pre><code class="language-bash">java -jar smart-mqtt-broker-community-0.7.jar</code></pre> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">2.2 docker 启动</h2> 
<pre><code class="language-bash">docker run -d --name smart-mqtt -p 1883:1883 smartboot/smart-mqtt:latest</code></pre> 
<h1 style="margin-left:0; margin-right:0; text-align:start">三、更新内容 🎉</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:start">3.1 Features 🌈</h2> 
<ol> 
 <li>新增 docker-compose.yml ，极致体验的 MQTT Broker。</li> 
 <li>优化日志级别。</li> 
 <li>Broker接受消息后不对Qos进行持久化。</li> 
 <li>ping响应消息采用单例模式。</li> 
 <li>支持系统环境变量配置broker运行参数，现开放 BROKER_PORT、BROKER_THREADNUM两项配置。</li> 
 <li>将插件的启动先于 Broker TCP服务启动之前完成。</li> 
 <li>启动 TCP 服务时若发生异常释放相关资源。</li> 
 <li>启用内存池，提升运行性能。</li> 
 <li>消息read缓冲区暂时下降至 4KB，下个迭代换成配置化。</li> 
 <li>启用运行指标监控插件。</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">3.2 Bugfix 🛠</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">暂无</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">3.3 文档 📘</h2> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fsmartboot%2Fsmart-mqtt%2Fquickstart" target="_blank">快速上手</a>》</p>
                                        </div>
                                      
</div>
            