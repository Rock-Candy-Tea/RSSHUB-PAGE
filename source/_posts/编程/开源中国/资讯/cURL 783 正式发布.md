
---
title: 'cURL 7.83 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9303'
author: 开源中国
comments: false
date: Fri, 29 Apr 2022 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9303'
---

<div>   
<div class="content">
                                                                                            <p>cURL 是一个计算机软件项目，提供一个库（libcurl）和命令行工具（curl），用于使用各种网络协议传输数据。这个名字代表了 "Client URL"。</p> 
<p>cURL 7.83 正式发布，更新内容如下：</p> 
<h3>安全修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-22576.html" target="_blank">CVE-2022-22576</a>：当使用 OAUTH2 承载令牌时，curl 可能重复使用错误的连接。</li> 
 <li>CVE-2022-27774：当 curl 跟随重定向到另一个协议或另一个端口号时，它可能会继续在新的连接上发送凭证，从而将合理的信息泄露给错误的一方。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-27775.html" target="_blank">CVE-2022-27775</a>：当要求使用 zone id 连接到 IPv6 地址时，curl 可能会重复使用错误的连接，因为在从池中挑选连接时没有正确检查 zone id。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.se%2Fdocs%2FCVE-2022-27776.html" target="_blank">CVE-2022-27776</a>：curl 的系统避免在重定向后向其他主机发送自定义的 auth 和 cookie，但没有考虑到端口号或协议，可能会将合理的信息泄露给错误的一方。</li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li> <p>实验性函数</p> 
  <ul> 
   <li>引入了两个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdaniel.haxx.se%2Fblog%2F2022%2F03%2F22%2Fa-headers-api-for-libcurl%2F" target="_blank">新函数</a> curl_easy_header() 和 curl_easy_nextheader()。 它们允许应用程序获取特定 HTTP headers 的内容或在传输完成后迭代所有这些 headers。 应用程序之前已经能够访问 headers，但这些功能带来了新的易用性和灵活性。</li> 
  </ul> </li> 
 <li> <p>命令行工具也被扩展为使用这些功能，以便轻松将 header 输出到 <code>[--write-out](<https://everything.curl.dev/usingcurl/verbose/writeout>)</code>选项。</p> </li> 
 <li> <p><code>-no-clobber</code></p> <p>使用此选项，你可以要求 curl 不覆盖本地文件，即使你已在 curl 命令行中将其指定为输出文件名。</p> </li> 
 <li> <p><code>-remove-on-error</code></p> <p>新的命令行选项中的第二个：告诉 curl 在检测到并返回一个错误时，删除可能已经下载的部分文件。</p> </li> 
 <li> <p>msh3</p> <p>这是第三个支持的 HTTP/3 后端</p> </li> 
 <li> <p>其他 Bug 修复</p> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdaniel.haxx.se%2Fblog%2F2022%2F04%2F27%2Fcurl-7-83-0-headers-bonanza%2F" target="_blank">https://daniel.haxx.se/blog/2022/04/27/curl-7-83-0-headers-bonanza/</a></p>
                                        </div>
                                      
</div>
            