
---
title: 'Magician 1.1.10 发布，http 支持 keep-alive 保活'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-8da5e994ffc1a4ffb6bb2133b451cfe6097.png'
author: 开源中国
comments: false
date: Sun, 09 May 2021 21:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-8da5e994ffc1a4ffb6bb2133b451cfe6097.png'
---

<div>   
<div class="content">
                                                                                            <p>本次更新主要是对http解码器 加入了 keep-alive保活机制，让一个tcp连接可以被同一个http客户端复用，从而减少建立tcp连接的开销，在一定程度上提高了吞吐量。</p> 
<h2>如何使用</h2> 
<p>发起http请求的时候 加上这个请求头【connection:keep-alive】，一旦加了这个 服务端将会保持tcp连接，响应之后不再关闭。现在浏览器一般都是默认有的。</p> 
<p>如果不想用这个机制，那么务必要传这个请求头【connection:close】 或者干脆不传connection请求头。</p> 
<h2>如何回收连接</h2> 
<p>目前是第一版，还不是特别完美，回收连接主要靠两个点</p> 
<ol> 
 <li>系统的tcp keepalive，这个是系统带的功能 如果tcp连接闲置过久 就会被回收</li> 
 <li>客户端主动断开，如果客户端断开了连接，那么服务端会收到一个read事件，读取数据的时候会返回-1，后端对这个-1做了判断，一旦发现返回-1就会关闭tcp连接</li> 
</ol> 
<h2>这个机制带来的吞吐量如何</h2> 
<p><strong>在本机用wrk做了一轮测试，结果如下图所示</strong></p> 
<p><img height="507" src="https://oscimg.oschina.net/oscnet/up-8da5e994ffc1a4ffb6bb2133b451cfe6097.png" width="800" referrerpolicy="no-referrer"></p> 
<p><strong>测试脚本如下</strong></p> 
<p><img height="507" src="https://oscimg.oschina.net/oscnet/up-0b65a67bcb48996dd4908eae93c730a252d.png" width="800" referrerpolicy="no-referrer"></p> 
<p><strong>本机配置如下</strong></p> 
<p><img height="453" src="https://oscimg.oschina.net/oscnet/up-8cd9a15b906168962b112b768fe8e44fe49.png" width="800" referrerpolicy="no-referrer"></p> 
<h2>想了解更多可以访问官网</h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmagician-io.com%2F" target="_blank">http://magician-io.com</a></p>
                                        </div>
                                      
</div>
            