
---
title: 'Serverless Framework 3.22.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1762'
author: 开源中国
comments: false
date: Thu, 18 Aug 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1762'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Serverless 架构开发框架 Serverless Framework 发布了 3.22.0 版本，该框架使用 AWS Lambda、Azure Functions、Google CloudFunctions 等技术，可以构建 Serverless 架构的 Web、移动和 IoT 应用。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">此版本更新内容包括：</span></p> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Features</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>AWS Cognito：</strong>添加对 Custom Sender Triggers 的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11201" target="_blank">#11201</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2F22802efde1d1721404b4e0d704f7806938183522" target="_blank">22802ef</a> ) </li> 
</ul> 
<h4><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
<ul> 
 <li><strong>AWS HTTP API：</strong>修复 API 网关超时问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11223" target="_blank">#11223</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2F16b0cd60c9914d871eaa3639562ec580c855af43" target="_blank">16b0cd6</a> )</li> 
 <li><strong>Variables：</strong>修复对同一变量的 parallel resolution 的处理 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11299" target="_blank">#11299</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2F1f9a07f989fc0b56885edf8a271a0bd63cf8911f" target="_blank">1f9a07f</a> )</li> 
</ul> 
<h4><strong>Maintenance Improvements</strong></h4> 
<ul> 
 <li>删除剩余的内部<code>self:</code><span style="background-color:#ffffff; color:#24292f"><span> </span>handling</span> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11279" target="_blank">#11279</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2F544717e703c093340b73dcbf94dc40555cda5251" target="_blank">544717e</a> )</li> 
 <li><strong><code>lodash</code>replacement：</strong> 
  <ul> 
   <li>替换<code>_.flatMap</code>为<code>Array.prototype.flatMap</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11272" target="_blank">#11272</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2F4f7e12939ced5b269d53624e5643bd5a9173ed7b" target="_blank">4f7e129</a> )</li> 
   <li>替换<code>_.flatten</code>为<code>Array.prototype.flat</code>( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11271" target="_blank">#</a> 11271) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2Fb36cdf2db6ee25f7defe6f2c02dd40e1d5cb65c4" target="_blank">b36cdf2</a> )</li> 
  </ul> </li> 
 <li>忽略 Compose triage 中的<code>doctor</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fissues%2F11283" target="_blank">#11283</a> ) ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Fcommit%2Fef2dcb6df7cf5dd4b82a74613d02f22f04b7147a" target="_blank">ef2dcb6</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fserverless%2Fserverless%2Freleases%2Ftag%2Fv3.22.0" target="_blank">https://github.com/serverless/serverless/releases/tag/v3.22.0</a></p>
                                        </div>
                                      
</div>
            