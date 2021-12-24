
---
title: 'PHP-Casbin v3.20.0 发布，性能大幅提升'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3537'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 11:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3537'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp-casbin%2Fphp-casbin" target="_blank">PHP-Casbin</a><span style="background-color:#ffffff; color:#333333"> v3.20.0 发布了，</span><span style="background-color:#ffffff; color:#333333">PHP-Casbin</span><span style="background-color:#ffffff; color:#333333"> 是一个用 PHP 语言打造的轻量级开源访问控制框架，支持 ACL、RBAC、ABAC 多种模型。它采用了元模型的设计思想，支持多种经典的访问控制方案，如基于角色的访问控制 RBAC、基于属性的访问控制 ABAC 等。</span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新内容：</h4> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp-casbin%2Fphp-casbin%2Freleases" target="_blank">https://github.com/php-casbin/php-casbin/releases</a></h4> 
<h4 style="margin-left:0; margin-right:0; text-align:left">Casbin 开源项目介绍</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#24292e">Casbin 是一个强大的、高效的开源访问控制框架。涉及到 Go、Java、Node.js、Javascript (React)、Python、PHP、.NET、Delphi、Rust 等多种语言。Casbin 由北京大学罗杨博士创立于 2017 年，核心维护团队有数十人。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本次更新，在 PHP 8.0 下性能有数倍提升：</p> 
<pre><code>Intel(R) Core(TM) i5-6500 CPU @ 3.20GHz, 3.20 GHz, 4 Core(s), 8 Logical Processor(s)</code></pre> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:0px; box-sizing:border-box; color:#24292e; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; font-size:16px; font-stretch:inherit; font-style:normal; font-variant-caps:normal; font-variant-east-asian:inherit; font-variant-ligatures:normal; font-variant-numeric:inherit; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 16px; orphans:2; overflow:auto; padding:0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; vertical-align:baseline; white-space:normal; widows:2; width:784.034px; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th style="background-color:inherit; vertical-align:baseline">Test case</th> 
   <th style="background-color:inherit; vertical-align:baseline">Rule size</th> 
   <th style="background-color:inherit; vertical-align:baseline">Time overhead (ms/op)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">5 rules (2 users, 1 role)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.050881</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC (small)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">1100 rules (1000 users, 100 roles)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.336172</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC (medium)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">11000 rules (10000 users, 1000 roles)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">2.911541</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC (large)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">110000 rules (100000 users, 10000 roles)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">34.153414</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC with resource roles</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">6 rules (2 users, 2 roles)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.061189</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RBAC with domains/tenants</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">6 rules (2 users, 1 role, 2 domains)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.069991</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">ABAC</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0 rule (0 user)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.035182</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">RESTful</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">5 rules (3 users)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.060467</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">Deny-override</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">6 rules (2 users, 1 role)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.070071</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">Priority</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">9 rules (2 users, 2 roles)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px; vertical-align:baseline">0.055194</td> 
  </tr> 
 </tbody> 
</table> 
<h4 style="margin-left:0; margin-right:0; text-align:left">PHP-Casbin 项目： </h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fphp-casbin%2Fphp-casbin" target="_blank">https://github.com/php-casbin/php-casbin</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云：<a href="https://gitee.com/casbin/php-casbin">https://gitee.com/casbin/php-casbin</a></p>
                                        </div>
                                      
</div>
            