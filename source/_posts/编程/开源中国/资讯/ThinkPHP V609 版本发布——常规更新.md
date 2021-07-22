
---
title: 'ThinkPHP V6.0.9 版本发布——常规更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=531'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 14:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=531'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p><code>V6.0.9</code>版本为常规更新，主要添加了事件监听的通配符支持，并修正了框架的一处可能的序列化漏洞，同时对模型做了一些改进和优化。</p> 
</blockquote> 
<h2 style="text-align:start">主要更新</h2> 
<ul> 
 <li>更新<code>league/flysystem</code>版本</li> 
 <li>事件监听支持通配符</li> 
 <li>支持时间字段的统一配置</li> 
 <li>改进<code>Request</code>类<code>all</code>方法</li> 
</ul> 
<blockquote> 
 <p>由于<code>league/flysystem</code>低版本存在漏洞，官方进行了安全升级，该升级使得框架的PHP版本依赖也提升到<code>7.2+</code>。</p> 
</blockquote> 
<p style="text-align:start"><code>ThinkORM</code>主要更新如下：</p> 
<ul> 
 <li>强化虚拟模型支持</li> 
 <li>改进模型事件和数据库事件</li> 
 <li>改进动态获取器处理</li> 
 <li>优化分页查询</li> 
 <li>改进聚合查询</li> 
 <li>关联增加<code>withoutField</code>方法</li> 
 <li>软删除<code>destroy</code>方法优化</li> 
</ul> 
<h2 style="text-align:start">安装和更新</h2> 
<p style="text-align:start"><code>V6</code>版本开始仅支持<code>Composer</code>安装及更新，支持上个版本的无缝更新，直接使用</p> 
<pre style="text-align:start"><code>composer update
</code></pre> 
<p style="text-align:start">更新到最新版本即可。</p> 
<blockquote> 
 <p>如果你的PHP版本是<code>7.1.*</code>，可以仅仅更新<code>topthink/think-orm</code>库而无需更新框架。</p> 
</blockquote> 
<p style="text-align:start">如果需要全新安装，使用：</p> 
<pre style="text-align:start"><code>composer create<span style="background-color:rgba(255, 255, 255, 0.5)">-</span>project topthink<span style="background-color:rgba(255, 255, 255, 0.5)">/</span>think tp
</code></pre> 
<h2 style="text-align:start">官方文档</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fmanual%2Fthinkphp6_0%2Fcontent" target="_blank">官方<code>6.0</code>完全开发手册</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fthinkphp%2Fthinkphp6-quickstart" target="_blank"><code>6.0</code>入门必读教程</a></li> 
</ul> 
<h2 style="text-align:start">官方服务</h2> 
<h3 style="text-align:start">官方服务市场——生态服务交易及交付平台</h3> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2F" target="_blank"><code>ThinkPHP</code>应用服务市场</a>是官方作为战略服务倾力打造的生态服务交易及交付平台，为<code>ThinkPHP</code>开发者和爱好者严选官方及第三方产品和服务，并提供交易保障。</p> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-api" target="_blank"><code>ThinkAPI</code></a>——官方统一API接口服务</h3> 
<p style="text-align:start"><code>ThinkAPI</code>统一<code>API</code>接口服务是由官方联合合作伙伴封装的一套接口调用服务及<code>SDK</code>，旨在帮助<code>ThinkPHP</code>开发者<strong>更方便和更低成本</strong>调用官方及第三方的提供的各类<code>API</code>接口及服务，从而更好的构建开发者生态。目前已经接入包括实名认证、人工智能、电子商务、新闻资讯和生活服务在内的常用API接口。</p> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-ssl%2F" target="_blank"><code>ThinkSSL</code></a>——官方自营SSL证书服务</h3> 
<p style="text-align:start"><code>ThinkSSL</code>服务是<code>ThinkPHP</code>官方联合合作伙伴推出的自营<code>SSL/TLS</code>证书服务，精选了多个优质证书品牌和证书类型，为个人和企业提供极具性价比的证书服务，支持DV（域名型）和OV（企业型），同时也提供免费证书服务（包括通配符证书）。</p>
                                        </div>
                                      
</div>
            