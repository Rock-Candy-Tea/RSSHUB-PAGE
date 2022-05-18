
---
title: '😊 学 .NET5_.NET6 从 Furion 开始，v3.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b9e0a54d669fe549c08f2a8e4c2b8d79803.png'
author: 开源中国
comments: false
date: Wed, 18 May 2022 15:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b9e0a54d669fe549c08f2a8e4c2b8d79803.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>序言</h2> 
<p><span style="color:#3498db"><strong>截至 2022年05月18日，Furion 发布了 272个版本，提交了 4147次代码更改，贡献者 192人，处理了 1274个工单，Nuget 安装量 245万。</strong></span></p> 
<p><a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-b9e0a54d669fe549c08f2a8e4c2b8d79803.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>本期亮点</h2> 
<ul> 
 <li>改进远程请求文件上传</li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-c20f2699985fe37eb57ba6474eaff4898c0.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-dfe6cf6ff832047c27e935cacfebb62df45.png" width="1920" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>改进文件上传下载</li> 
</ul> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-196ac303a111376eade71c8d94b5d7bc5e3.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>版本日志</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 远程请求文件上传自动识别<span> </span><code>Content-Type</code><span> </span>和<span> </span><code>Mime</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">I57ZMN</a></li> 
    <li>[新增] 远程请求方法支持设置<span> </span><code>Content-Type</code><span> </span>和<span> </span><code>Encoding</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">I57ZMN</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li>[更新]<span> </span><code>.NET</code><span> </span>所有依赖包至<span> </span><code>v6.0.5</code><span> </span>版本</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 自定义全局异常<span> </span><code>Exception</code><span> </span>后导致获取错误行号，文件空异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I53EGM">#I53EGM</a></li> 
    <li>[修复] 配置数据库上下文传递空委托导致空引用异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I519AW">#I519AW</a></li> 
    <li>[修复] 字符串模板模板<span> </span><code>Render</code><span> </span>拓展方法返回<span> </span><code>void</code><span> </span>问题，应该返回<span> </span><code>string</code></li> 
    <li>[修复] 远程请求文件上传出现空情况问题（原因是缺失<span> </span><code>Content-Type</code><span> </span>）<a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">I57ZMN</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[优化] 视图引擎反射性能</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[更新] 二级虚拟目录部署文档，远程请求文档，文件上传文档，安全授权文档</li> 
    <li>[新增] 将<span> </span><code>byte[]</code><span> </span>转<span> </span><code>url</code><span> </span>文档</li> 
   </ul> </li> 
 </ul> 
</blockquote>
                                        </div>
                                      
</div>
            