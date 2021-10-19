
---
title: '无服务器框架 Serverless 发布 2.63.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4161'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4161'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Serverless<span> </span></span><span style="color:#40485b"><span> </span></span><span style="color:#333333">发布了 2.63.0 版本，该框架使用 AWS Lambda、Azure Functions、Google CloudFunctions 等技术，可以构建 Serverless 架构的 Web、移动和 IoT 应用。 </span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">重点更新</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>AWS Deploy：引入关于<span> </span><code>deploy -f<span> </span></code>别名的提示</li> 
 <li>AWS Lambda：允许无 VPC 函数覆盖供应商 VPC</li> 
 <li>AWS S3：<span style="color:#2e3033">允许 s3 事件的 ExpirationInDays 属性使用 Cf If 语句</span></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033"><strong>CLI：</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">引入重复定义插件时的弃用提示</span></li> 
 <li><span style="color:#24292f">S3 Accelerate 中</span><span style="color:#2e3033">用户引入桶，使用“弃用”警告来代替报错</span></li> 
 <li><span style="color:#2e3033">加入<span> </span></span><span style="color:#24292f">versioning 配置文件来</span>支持 S3 桶的版本控制</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">维护和改进</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>CLI：新日志（试验版）</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将<span> </span><code>logInfo</code><span style="color:#24292f"><span> </span>加入最新日志</span></li> 
 <li><span style="color:#24292f">将</span><code>logWarning</code><span style="color:#24292f"><span> </span>加入最新日志</span></li> 
 <li>用最新日志覆盖图形构建</li> 
 <li>改进最新日志中对服务产出的处理</li> 
 <li>引入资源限制的最新警告</li> 
 <li>更新最新日志的微小调整</li> 
 <li>删除<span> </span><code>info<span> </span></code>命令中的空行</li> 
 <li>使用 更新日志来调整  <code>process.stdout 的用法 </code></li> 
 <li>用最新的提示语句来代替之前的报错</li> 
 <li>更新最新日志的链接样式</li> 
 <li>修正<span> </span><code>lib/classes/Variables.js</code><span style="color:#24292f"><span> </span>中的错别字</span></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">模板：</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在<code>aws-nodejs-typescript</code><span style="color:#24292f"><span> </span>的<span> </span></span><code>gitignore</code><span style="color:#24292f"><span> </span>中加入</span><code>esbuild</code></p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Freleases%2Ftag%2Fv2.63.0" target="_blank">https://github.com/serverless/serverless/releases/tag/v2.63.0</a></p>
                                        </div>
                                      
</div>
            