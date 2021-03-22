
---
title: 【漏洞预警】XStream _ 1.4.16 多个反序列化漏洞
categories: 
    - 编程
    - 阿里云 - 公告
author: 阿里云 - 公告
comments: false
date: Mon, 15 Mar 2021 07:23:24 GMT
thumbnail: ''
---

<div>   
<p>2021年3月13日，阿里云应急响应中心监测到 XStream 官方发布安全公告，披露多个反序列化漏洞。</p><p><br></p><p><strong>漏洞描述</strong></p><p>XStream是一个常用的Java对象和XML相互转换的工具。近日XStream官方发布安全更新，修复了多个XStream 反序列化漏洞。攻击者通过构造恶意的XML文档，可绕过XStream的黑名单，触发反序列化，从而造成如CVE-2021-21345 反序列化代码执行漏洞等。<strong>实际漏洞利用依赖于具体代码实现以及相关接口请求，无法批量远程利用，实际危害相对较低。阿里云应急响应中心提醒 XStream 用户尽快采取安全措施阻止漏洞攻击。</strong></p><p><br><strong>漏洞评级</strong></p><p>CVE-2021-21344 XStream 反序列化代码执行漏洞 高危</p><p>CVE-2021-21345 XStream 反序列化代码执行漏洞 高危</p><p>CVE-2021-21346 XStream 反序列化代码执行漏洞 高危</p><p>CVE-2021-21347 XStream 反序列化代码执行漏洞 高危</p><p>CVE-2021-21350 XStream 反序列化代码执行漏洞 高危</p><p>CVE-2021-21351 XStream 反序列化代码执行漏洞 高危</p><p></p><p><br></p><p><strong>影响版本</strong></p><p>XStream < 1.4.16</p><p><br></p><p><strong>安全版本</strong></p><p>XStream 1.4.16</p><p><br></p><p><strong>安全建议</strong></p><p>针对使用到XStream组件的web服务升级至最新版本：<a href="http://x-stream.github.io/changes.html" target="_blank" class>http://x-stream.github.io/changes.html</a></p><p><br></p><p><strong>相关链接</strong></p><p><a href="https://x-stream.github.io/security.html#workaround" target="_blank" class>https://x-stream.github.io/security.html#workaround</a></p><p><br><br></p><p style="text-align:start;line-height:24px"><strong>阿里云</strong><a style="font-size:14px;font-weight:400;letter-spacing:normal;text-align:start;white-space:normal;color:rgb(0, 183, 211);background-color:transparent;margin:0px;margin-bottom:0px;margin-top:0px;margin-left:0px;margin-right:0px;padding:0px;padding-bottom:0px;padding-top:0px;padding-left:0px;padding-right:0px" href="https://yundunnext.console.aliyun.com/?p=sasnext#/vulManage/cn-hangzhou" target="_blank" class><strong>云安全中心</strong></a><strong>应用漏洞模块已支持对该漏洞一键检测</strong></p><p></p><p><br></p><p></p><p>我们会关注后续进展，请随时关注官方公告。</p><p>如有任何问题，可随时通过工单或服务电话95187联系反馈。</p><p></p><p style="text-align:right">阿里云应急响应中心</p><p style="text-align:right">2021.3.15</p>  
</div>
            