
---
title: 'Chrome 95 发布，完全移除 FTP 支持、限制 cookie 大小'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8625'
author: 开源中国
comments: false
date: Thu, 21 Oct 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8625'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">上个月 Google 推出了 Chrome 94，在 Chrome 94 中加入了具有争议的空闲检测 API。如今时隔四周时间，Chrome 95 也如期到来，随着 Chrome 95 的推出，之前已被弃用的 FTP 支持在该版本中被完全移除，除此以外 Chrome 95 中值得关注的更新内容还包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Chrome 将强制限制 cookie 的名称+值的大小，最大为 4096 字节，每个属性的长度最多设置为 1024 字节。超过这些长度的 cookies 将被直接拒绝。此前，Chrome 浏览器曾对整个 Set-Cookie 行设置了 4096 字节的限制。该变化将使其与 Mozilla Firefox 保持一致，并提高互操作性。</li> 
 <li>减少用户代理字符串在 HTTP 请求中暴露的信息量，以减少网站可能出现的浏览器指纹识别。</li> 
 <li>为 WebAssembly 添加异常处理支持，异常处理允许代码在抛出异常时中断控制流。</li> 
 <li>在 WebAuthn 的帮助下，安全支付确认（Secure payment confirmation）增强了网络上的支付认证体验。该功能为 WebAuthn 增加了一个新的 "支付" 扩展，允许依赖方（如银行）创建一个 PublicKeyCredential，作为在线结账的一部分，任何商家都可以通过支付请求 API 使用 "安全支付确认"支付方法进行查询。</li> 
 <li>一个新的 EyeDropper API，使开发人员能够在构建自定义颜色选择器时使用浏览器提供的滴管。</li> 
 <li>URLPattern 作为一个新的 API，提供操作系统支持，将 URL 与提供的模式相匹配。</li> 
 <li>弃用对以数字结尾的非 IPv4 主机名的 URL 的支持。</li> 
 <li>Google 自 Chrome 88 开始弃用 FTP 的支持，现在 FTP 的支持已被完全移除。</li> 
 <li>……</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">下一个稳定版本 —— Chrome 96 预计将于 11 月 16 日发布。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchromestatus.com%2Froadmap" target="_blank">https://chromestatus.com/roadmap</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            