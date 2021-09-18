
---
title: 'cURL 7.79.0 发布，安全的本地 COOKIES'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7d42947e8d488f5e57a32b35c2ceabdeef4.png'
author: 开源中国
comments: false
date: Sat, 18 Sep 2021 07:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7d42947e8d488f5e57a32b35c2ceabdeef4.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>cURL 7.79.0 现已发布，具体更新内容如下：</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-7d42947e8d488f5e57a32b35c2ceabdeef4.png" referrerpolicy="no-referrer"></p> 
 <p><strong>Security</strong></p> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2021-22945.html" target="_blank">CVE-2021-22945</a> 是 MQTT 代码中的一个 double-fre 缺陷。如果你用它来发送 MQTT，则需要给你的旧 curl 打上补丁或升级到这个版本。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2021-22946.html" target="_blank">CVE-2021-22946</a> 是几个协议（IMAP、POP3 和 FTP）的响应处理中的一个错误，它绕过了强制的 TLS 检查.因此，即使是明确告知需要 TLS 的传输也会意外地以 clear text 方式悄悄进行。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2021-22947.html" target="_blank">CVE-2021-22947</a> 允许 mitm 攻击者在 TLS 升级前将数据注入 FTP、IMAP、POP3 或 SMTP 的协议流中，从而使 curl 接受该数据并在升级到 TLS 后使用它。不受信任的数据就会溜进去，并被当作受信任的数据处理。</li> 
</ul> 
<p><strong>Changes</strong></p> 
<ul> 
 <li>bearssl TLS 后台的现在也支持 CURLOPT_CAINFO_BLOB 选项，这样 CA 证书就可以很容易地由应用程序在内存中提供。</li> 
 <li>curl 中的 cookie 引擎现在认为 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost" target="_blank">http://localhost</a> 是安全的，因此被标记为"secure"的 cookie 将通过它发送--即使不使用 HTTPS。这样做是因为 curl 从不久前开始确保 localhost 始终是 truly local。</li> 
 <li>Secure Transport TLS backend 用户现在可以使用 CURLINFO_CERTINFO 来提取关于服务器证书链的信息。</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>使用 ares_getaddrinfo()：当你构建 c-ares 名称解析器后端时，curl 现在会使用这个函数来获得对 IPv4+IPv6 的改进处理。这也使得对 c-ares 的要求提高到 1.16.0。</li> 
 <li>hyper works better：1xx responses、Transfer-Encoding 和更多的问题都得到了修复。对 hyper 构建禁用的测试数量比以前更少了，但在它脱离实验性之前，仍有很多工作要做。</li> 
 <li>cmake 构建：避免在 macOS 上使用 poll()。</li> 
 <li>configure：也检查 OpenSSL pkg-config 文件中的 lib64。这有助于 configure 找到 OpenSSL v3 installs。</li> 
 <li>curl.1：为每个选项提供示例。现在的文档必须为 curl 提供的每个命令行选项提供至少一个命令行实例。</li> 
 <li>HTTP 1.1：不允许超过 3 位的响应代码。</li> 
 <li>HTTP 1.1：如果使用任何 transfer-encoding，忽略 content-length。</li> 
 <li>http_proxy：发送请求时只等待可写的套接字。</li> 
 <li>支持 mbedTLS 3.0.0。</li> 
 <li>禁止 strerror。</li> 
 <li>邮件列表从 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcool.haxx.se" target="_blank">cool.haxx.se</a> 迁移到 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flists.haxx.se" target="_blank">lists.haxx.se</a>。</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdaniel.haxx.se%2Fblog%2F2021%2F09%2F15%2Fcurl-7-79-0-secure-local-cookies%2F" target="_blank">https://daniel.haxx.se/blog/2021/09/15/curl-7-79-0-secure-local-cookies/</a> </p>
                                        </div>
                                      
</div>
            