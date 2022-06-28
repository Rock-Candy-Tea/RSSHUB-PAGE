
---
title: 'cURL 7.84 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=866'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=866'
---

<div>   
<div class="content">
                                                                                            <p>cURL 是一个计算机软件项目，提供一个库（libcurl）和命令行工具（curl），用于使用各种网络协议传输数据。这个名字代表了 "Client URL"。</p> 
<p>cURL 7.84 正式发布，更新内容如下：</p> 
<h3>变化</h3> 
<ul> 
 <li> <p><code>-rate</code></p> <p>这个新的命令行选项 rate 限制了每个时间段的传输次数。</p> </li> 
 <li> <p><strong>弃用</strong> <code>-random-file</code> 和 <code>-egd-file</code></p> <p>这两个选项已经有很长一段时间没有人使用了，从现在开始，它们已经没有任何功能了，使用它们不会有任何效果。</p> </li> 
 <li> <p>curl_global_init() 是线程安全的</p> <p>即该函数在大多数平台上都是线程安全的。</p> </li> 
 <li> <p>curl_version_info: 增加了 <code>CURL_VERSION_THREADSAFE</code></p> <p>你可以检查全局 init 在你特定的 libcurl 构建中是否是线程安全的。</p> </li> 
 <li> <p>CURLINFO_CAPATH/CAINFO: 获取默认 CA 路径</p> <p>由于这些值的默认值通常是在构建时计算和设置的，应用程序可能会想要弄清楚它们默认设置为什么。</p> </li> 
 <li> <p>CURLOPT_SSH_HOSTKEYFUNCTION</p> <p>对于启用了 libssh2 的构建，你现在可以为主机密钥验证设置一个回调。</p> </li> 
 <li> <p>弃用 RANDOM_FILE 和 EGDSOCKET</p> <p>CURLOPT_RANDOM_FILE 和 CURLOPT_EGDSOCKET 选项不再有任何作用，它们已经很久没有被任何应用程序使用了。</p> </li> 
 <li> <p>unix sockets to socks proxy</p> <p>你现在可以告诉 (lib)curl 使用 unix 域套接字连接到 SOCKS 代理，而不是传统的 TCP。</p> </li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>改进了 cmake 对 libpsl 和 libidn2 的支持</li> 
 <li>使仓库符合 REUSE 标准</li> 
 <li>headers API 不再是试验性的了</li> 
 <li>支持 .netrc 中的引号字符串</li> 
 <li>对不区分大小写的字符串比较进行了优化</li> 
 <li>……</li> 
</ul> 
<h3>安全性：</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-32205.html" target="_blank">CVE-2022-32205</a>: Set-Cookie 拒绝服务</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-32206.html" target="_blank">CVE-2022-32206</a>: HTTP 压缩拒绝服务</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-32207.html" target="_blank">CVE-2022-32207:</a> 未保留的文件权限</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-32208.html" target="_blank">CVE-2022-32208:</a> FTP-KRB 错误信息验证</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdaniel.haxx.se%2Fblog%2F" target="_blank">https://daniel.haxx.se/blog/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            