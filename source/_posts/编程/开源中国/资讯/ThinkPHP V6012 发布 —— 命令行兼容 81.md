
---
title: 'ThinkPHP V6.0.12 发布 —— 命令行兼容 8.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.kancloud.cn/63/b4/63b41afa13627e3ee8991fe0758d0dba_900x383.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 15:54:00 GMT
thumbnail: 'https://img.kancloud.cn/63/b4/63b41afa13627e3ee8991fe0758d0dba_900x383.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><img alt src="https://img.kancloud.cn/63/b4/63b41afa13627e3ee8991fe0758d0dba_900x383.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <h3 style="margin-left:0; margin-right:0"><code>V6.0.12</code>版本完善了命令行的<code>PHP8.1</code>的兼容支持，并增加了路由的闭包检测机制，以及<code>ThinkORM</code>的一些改进。</h3> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start">主要更新</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进缓存驱动<code>unserialize</code>方法参数类型限制</li> 
 <li>优化代码使IDE友好</li> 
 <li>修正命令行对<code>PHP8.1</code>的兼容性</li> 
 <li>路由增加闭包检测有效性</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><code>ThinkORM</code>主要更新包括：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>完善sqlite驱动</li> 
 <li>修正Fetch类</li> 
 <li>改进多对多关联</li> 
 <li>添加数据写入对对象值的判断处理</li> 
 <li>改进一对一关联写入</li> 
 <li>一对一关联查询绑定属性调整</li> 
 <li>改进远程一对多关联查询</li> 
 <li>优化模型数据处理</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">安装和更新</h2> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><code>V6</code>版本开始仅支持<code>Composer</code>安装及更新，支持上个版本的无缝更新，直接使用</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>composer update
</code></pre> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">更新到最新版本即可。</p> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">如果需要全新安装，使用：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>composer create<span style="background-color:rgba(255, 255, 255, 0.5)">-</span>project topthink<span style="background-color:rgba(255, 255, 255, 0.5)">/</span>think tp
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:start">官方文档</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fmanual%2Fthinkphp6_0%2Fcontent" target="_blank">官方<code>6.0</code>完全开发手册</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fthinkphp%2Fthinkphp6-quickstart" target="_blank"><code>6.0</code>入门必读教程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">官方服务</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><img alt height="45" src="https://img.kancloud.cn/ca/f7/caf7e270eab6a67416094cf542fd87f0_500x500.png" referrerpolicy="no-referrer"></h3> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong>官方服务市场——生态服务交易及交付平台</strong></h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2F" target="_blank"><code>ThinkPHP</code>应用服务市场</a>是官方作为战略服务倾力打造的生态服务交易及交付平台，为<code>ThinkPHP</code>开发者和爱好者严选官方及第三方产品和服务，并提供交易保障。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-api" target="_blank"><code>ThinkAPI</code></a>——官方统一API接口服务</strong><span> </span>（<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2Fproduct%2F210" target="_blank">API会员限时秒杀￥480/年</a></strong>）</h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><code>ThinkAPI</code>统一<code>API</code>接口服务是由官方联合合作伙伴封装的一套接口调用服务及<code>SDK</code>，旨在帮助<code>ThinkPHP</code>开发者<strong>更方便和更低成本</strong>调用官方及第三方的提供的各类<code>API</code>接口及服务，从而更好的构建开发者生态。目前已经接入包括实名认证、人工智能、电子商务、新闻资讯和生活服务在内的常用API接口。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-ssl%2F" target="_blank"><code>ThinkSSL</code></a>——官方自营SSL证书服务</strong><span> </span>（<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2Fcertificates%2Fnew" target="_blank">通配符DV证书限时秒杀￥200/年</a></strong>）</h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><code>ThinkSSL</code>服务是<code>ThinkPHP</code>官方联合合作伙伴推出的自营<code>SSL/TLS</code>证书服务，精选了多个优质证书品牌和证书类型，为个人和企业提供极具性价比的证书服务，支持DV（域名型）和OV（企业型），同时也提供免费证书服务（包括通配符证书）。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2F" target="_blank">看云文档写作和托管服务</a></strong></h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start">看云<code>KanCloud</code>的愿景是做国内最专业的产品文档/书籍/用户手册的在线写作、数字出版和托管平台，致力于提供最佳的在线文档创作和阅读体验，企业版可用于构建企业的文档中心和内部知识库。</p>
                                        </div>
                                      
</div>
            