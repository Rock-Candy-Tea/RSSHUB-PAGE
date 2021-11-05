
---
title: '无服务器框架 Serverless 发布 2.65.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6190'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 08:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6190'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Serverless </span><span style="background-color:#ffffff; color:#40485b"> </span><span style="background-color:#ffffff; color:#333333">发布了 2.65.0 版本，该框架使用 AWS Lambda、Azure Functions、Google CloudFunctions 等技术，可以构建 Serverless 架构的 Web、移动和 IoT 应用。 </span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>特性</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>AWS Lambda：</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>为<span> </span><code>functions[].reservedConcurrency</code><span> </span>添加 CF 内在函数支持。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10129" target="_blank">#10129</a><span> </span>)</li> 
   <li>允许使用<span> </span><code>lambdaHashingVersion: 20200924</code><span> </span>设置来维持当前默认的 Lambda 哈希版本模式。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10173" target="_blank">#10173</a><span> </span>) </li> 
  </ul> </li> 
 <li><strong>AWS EventBridge：</strong><span style="color:#24292f">仍然可以对 EventBridge 资源使用基于自定义资源的部署方法。</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10133" target="_blank">#10133</a>）</li> 
 <li><strong>AWS Local Invocation：</strong>支持 Python 十进制序列化。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10178" target="_blank">＃10178</a>）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>AWS Deploy：</strong>修复对部署存储桶扩展的处理。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10137" target="_blank">#10137</a><span> </span>)</li> 
 <li><strong>AWS HTTP API：</strong>将最大超时时间识别为 30 秒，而不是 29 秒。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10119" target="_blank">#10119</a>）</li> 
 <li><strong>命令行界面：</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>修复<span> </span><code>help</code><span> </span>命令的使用信息 。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10175" target="_blank">#10175</a><span> </span>)</li> 
   <li>修复未集成命令的帮助解析 。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10128" target="_blank">#10128</a><span> </span>)</li> 
  </ul> </li> 
 <li>在验证错误时，自动识别可访问的配置部分。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10134" target="_blank">#10134</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>性能改进</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>CLI：</strong>集成 CLI 分流到包中（没有<code>@serverless/components</code>和<code>@serverless/cli</code>模块，除非使用它们的 CLI）<span style="color:#000000">(<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10131" target="_blank">#10131</a><span style="color:#000000">) 。</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>维护改进</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>命令行界面：</strong> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>改进日志的文件大小输出。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10169" target="_blank">#10169</a><span> </span>) </li> 
   <li>改进主要进度的消息。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10183" target="_blank">#10183</a><span> </span>)</li> 
  </ul> </li> 
 <li><strong>遥测：</strong>添加<span> </span><code>projectId</code><span> </span>到有效载荷。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10180" target="_blank">#10180</a><span> </span>)</li> 
 <li><strong>AWS EventBridge：</strong>修复错误消息的拼写错误。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10165" target="_blank">#10165</a><span> </span>) </li> 
 <li>分离内部和插件输出部分。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10184" target="_blank">#10184</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>模板</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在<span> </span><code>aws-nodejs-typescript</code><span> </span>中单独打包 lambda 。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10106" target="_blank">#10106</a><span> </span>) </li> 
 <li>升级<span> </span><code>azure-nodejs-typescript</code><span> </span>。(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10163" target="_blank">#10163</a><span> </span>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Freleases%2Ftag%2Fv2.65.0" target="_blank">https://github.com/serverless/serverless/releases/tag/v2.65.0</a></p>
                                        </div>
                                      
</div>
            