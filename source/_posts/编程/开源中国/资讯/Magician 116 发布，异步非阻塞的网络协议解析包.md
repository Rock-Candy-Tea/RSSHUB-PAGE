
---
title: 'Magician 1.1.6 发布，异步非阻塞的网络协议解析包'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7996'
author: 开源中国
comments: false
date: Sun, 02 May 2021 01:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7996'
---

<div>   
<div class="content">
                                                                                            <p>Magician 1.1.6 已经发布，此版本更新内容包括：</p> 
<ol> 
 <li>彻底改写NIO实现部分，引入EventRunner机制</li> 
 <li>重新回归Selector，以事件来驱动，有效避免了 在报文不完整时 空转+阻塞的问题</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/yuyenews/Magician/releases/1.1.6">https://gitee.com/yuyenews/Magician/releases/1.1.6</a></p> 
<h2>项目简介</h2> 
<p>Magician 是一个异步非阻塞的网络协议解析包，支持Http, WebSocket, UDP等协议</p> 
<h2>运行环境</h2> 
<p>JDK11+</p> 
<h2>导入依赖</h2> 
<pre><dependency>
    <groupId>com.github.yuyenews</groupId>
    <artifactId>Magician</artifactId>
    <version>最新版</version>
</dependency>

<!-- 这个是日志包，支持任意可以跟slf4j桥接的包 -->
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-jdk14</artifactId>
    <version>1.7.12</version>
</dependency>
</pre>
                                        </div>
                                      
</div>
            