
---
title: 'Erlang_OTP 25.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8107'
author: 开源中国
comments: false
date: Fri, 23 Sep 2022 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8107'
---

<div>   
<div class="content">
                                                                                            <p>Erlang/OTP 25.1 是 OTP 25 的第一个维护补丁包，主要包含错误修复以及许多小改进。</p> 
<blockquote> 
 <p>Erlang 是一种通用的并发函数式程序设计语言。Erlang 也可以指 Erlang/OTP 的通称，开源电信平台 (OTP) 是 Erlang 的常用执行环境及一系列标准组件。</p> 
</blockquote> 
<p>主要变化</p> 
<p><strong>Crypto</strong></p> 
<ul> 
 <li> <p>Crypto 现在被认为可以与 OpenSSL 3.0 cryptolib 一起用于生产环境。ENGINE 和 FIPS 尚未完全发挥作用。</p> </li> 
 <li> <p>改变引擎加载/卸载函数的行为</p> </li> 
</ul> 
<p><strong>ssl</strong></p> 
<ul> 
 <li>已发现并修复了一个漏洞，编号为 CVE-2022-37026，用于绕过客户端认证。目前已通过 23.3.4.15, 24.3.4.2 和 25.0.2 补丁在受支持的 track 上发布修正。该漏洞也可能存在于较旧的 OTP 版本中们建议受影响的用户在各自的 track 上升级到这些版本之一或更高版本，OTP 25.1 将是一个更好的选择。受影响的是那些直接或通过其他应用程序间接使用该应用程序运行<code>ssl/tls/dtls</code>服务器的用户。例如通过 <code>inets</code>( <code>httpd</code>),<code>cowboy</code>）等。注意该漏洞只影响请求客户端认证的服务器，即设置选项<code>&#123;verify, verify_peer&#125;</code>。</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Fnews%2F158" target="_blank">发布公告</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.erlang.org%2Fdownloads" target="_blank">下载地址</a></p>
                                        </div>
                                      
</div>
            