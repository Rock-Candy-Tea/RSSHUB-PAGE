
---
title: 'ThinkPHP V6.0.10LTS 发布，兼容 PHP8.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.kancloud.cn/8f/c6/8fc66bd06132f419eefec871d60637eb_900x383.png'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 14:17:00 GMT
thumbnail: 'https://img.kancloud.cn/8f/c6/8fc66bd06132f419eefec871d60637eb_900x383.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><img alt src="https://img.kancloud.cn/8f/c6/8fc66bd06132f419eefec871d60637eb_900x383.png" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <h3 style="margin-left:0; margin-right:0"><code>V6.0.10</code>版本主要添加了<code>PHP8.1</code>的兼容支持，以及<code>ThinkORM</code>的一些改进，并宣布成为<code>ThinkPHP</code>历史上第二个<code>LTS</code>版本，借此辞旧迎新之际，ThinkPHP祝大家新年快乐。</h3> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><code>6.0LTS</code>版本核心不再做功能更新，仅作优化及BUG修复，BUG修复时间和安全更新均延长至2024年10月24日。</h3> 
<h2 style="margin-left:0; margin-right:0; text-align:start">主要更新</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>兼容<code>PHP8.1</code></li> 
 <li>改进<code>cookie</code>跨域删除</li> 
 <li>改进多语言自动加载</li> 
 <li>改进<code>url</code>生成</li> 
 <li><code>Filesystem</code>增加<code>url</code>方法 获取文件访问地址</li> 
 <li>文件上传错误支持多语言</li> 
 <li>修正<span> </span><code>make:controller</code><span> </span>指令错误</li> 
 <li>发送<code>cookie</code>前先检查请求头是否已发送</li> 
 <li>改进多文件上传的文件<code>hashName</code>冲突问题</li> 
 <li>调整<code>thinkPath</code>路径赋值为真实绝对路径 以避免特殊环境潜在隐患</li> 
 <li>支持 psr7 response</li> 
 <li>控制器中间件支持动态参数</li> 
 <li>改进<code>env</code>文件解析</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><code>ThinkORM</code>主要更新：</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修正<code>column</code>方法</li> 
 <li>Db和模型增加<code>filter</code>数据处理机制</li> 
 <li>调整<code>json</code>处理</li> 
 <li>修正<code>sqlite</code>驱动lock</li> 
 <li>获取数据库字段类型不区分大小写</li> 
 <li>修正多对多关联中间表数据</li> 
 <li>修正多对多模型</li> 
 <li>改进db类<code>hidden</code>/<code>visible</code>/<code>append</code><span> </span>方法处理机制</li> 
 <li>改进关联的软删除查询</li> 
 <li>完善获取sql时的字符转义</li> 
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
<h3 style="margin-left:0; margin-right:0; text-align:start">官方服务市场——生态服务交易及交付平台</h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2F" target="_blank"><code>ThinkPHP</code>应用服务市场</a>是官方作为战略服务倾力打造的生态服务交易及交付平台，为<code>ThinkPHP</code>开发者和爱好者严选官方及第三方产品和服务，并提供交易保障。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-api" target="_blank"><code>ThinkAPI</code></a>——官方统一API接口服务</strong><span> </span>（<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2Fproduct%2F210" target="_blank">API会员限时秒杀￥480/年</a></strong>）</h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><code>ThinkAPI</code>统一<code>API</code>接口服务是由官方联合合作伙伴封装的一套接口调用服务及<code>SDK</code>，旨在帮助<code>ThinkPHP</code>开发者<strong>更方便和更低成本</strong>调用官方及第三方的提供的各类<code>API</code>接口及服务，从而更好的构建开发者生态。目前已经接入包括实名认证、人工智能、电子商务、新闻资讯和生活服务在内的常用API接口。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.topthink.com%2Fthink-ssl%2F" target="_blank"><code>ThinkSSL</code></a>——官方自营SSL证书服务</strong><span> </span>（<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarket.topthink.com%2Fcertificates%2Fnew" target="_blank">通配符DV证书限时秒杀￥200/年</a></strong>）</h3> 
<p style="color:#525252; margin-left:0; margin-right:0; text-align:start"><code>ThinkSSL</code>服务是<code>ThinkPHP</code>官方联合合作伙伴推出的自营<code>SSL/TLS</code>证书服务，精选了多个优质证书品牌和证书类型，为个人和企业提供极具性价比的证书服务，支持DV（域名型）和OV（企业型），同时也提供免费证书服务（包括通配符证书）。</p>
                                        </div>
                                      
</div>
            