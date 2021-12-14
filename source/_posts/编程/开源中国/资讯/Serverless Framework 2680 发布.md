
---
title: 'Serverless Framework 2.68.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7514'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7514'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#333333">Serverless 发布了<span> </span></span><span style="color:#24292f"><strong>2.69.0</strong></span><span style="color:#333333"> 版本，该框架使用 AWS Lambda、Azure Functions、Google CloudFunctions 等技术，可以构建 Serverless 架构的 Web、移动和 IoT 应用。 </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">此版本主要有以下改动：</span></p> 
<h3 style="text-align:start">特征</h3> 
<ul> 
 <li><strong>AWS </strong><strong style="color:#24292f"><span> </span>Deploy</strong><strong>：</strong>确保 S3 部署存储桶（deployment bucket）存在（如果可用）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10317" target="_blank">#10317</a>）</li> 
 <li><strong>AWS Kafka：</strong>添加对<code>mTLS</code>访问配置的支持( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10273" target="_blank">#10273</a> )</li> 
 <li><strong>Standalone：</strong> 
  <ul> 
   <li>支持在基于 M1 的 Mac 上安装 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10291" target="_blank">#10291</a> ) </li> 
   <li>使用 Node 16 作为二进制文件的基础 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10291" target="_blank">#10291</a> )</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">Bug 修复</h3> 
<ul> 
 <li><strong>AWS 部署：</strong> 
  <ul> 
   <li>允许在桶丢失的情况下移除堆栈（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10306" target="_blank">#10306</a>）</li> 
   <li>确保从 CloudFormation 模板中去除所有<code>null</code>属性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10304" target="_blank">#10304</a>）</li> 
   <li>识别<code>provider.disableRollback</code>处的所有布尔值( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10324" target="_blank">#10324</a> )</li> 
  </ul> </li> 
 <li><strong>变量：</strong>提供从<code>ssm</code>源头强制解密的选择退出选项（<span style="background-color:#ffffff; color:#24292f">opt-out</span>）( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10315" target="_blank">#10315</a> )</li> 
</ul> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>维护改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>将 <span style="background-color:#ffffff; color:#24292f">promise </span>返回函数配置为异步  ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F10309" target="_blank">#10309</a> )</li> 
 <li>在<code>bucket.js</code>中使用<code>async/await</code>语法 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fpull%2F10306" target="_blank">#10306</a> )</li> 
</ul>
                                        </div>
                                      
</div>
            