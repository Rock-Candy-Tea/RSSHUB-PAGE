
---
title: 'jsoup 1.15.3 发布，Java HTML 解析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4570'
author: 开源中国
comments: false
date: Thu, 25 Aug 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4570'
---

<div>   
<div class="content">
                                                                                            <p>jsoup 1.15.3 现已发布，<span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>包括针对潜在 XSS 攻击的安全修复，以及其他改进，包括更具描述性的验证错误消息。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>jsoup 是一个用于处理 real-world HTML 的 Java 库。它使用最好的 HTML5 DOM 方法和 CSS 选择器提供了一个非常方便的 API 用于提取和操作数据。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p><span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>下载地址：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fdownload" target="_blank">https://jsoup.org/download</a></p> 
<p>具体更新内容包括：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong><span><span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>安全</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复了如果<code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fapidocs%2Forg%2Fjsoup%2Fsafety%2FSafelist.html%23preserveRelativeLinks%28boolean%29" target="_blank">SafeList.preserveRelativeLinks</a></code>启用，jsoup cleaner 可能会错误地清理精心制作的 XSS attempts 的问题。有关更多详细信息，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjhy%2Fjsoup%2Fsecurity%2Fadvisories%2FGHSA-gp7f-rwcx-9369" target="_blank">安全公告</a>。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong><span><span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>如果在原始解析中启用了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fapidocs%2Forg%2Fjsoup%2Fparser%2FParser.html%23setTrackPosition%28boolean%29" target="_blank">源跟踪</a>，Cleaner 将保留已清理元素的源位置。</li> 
 <li>从<code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fapidocs%2Forg%2Fjsoup%2Fhelper%2FValidate.html" target="_blank">Validate</a></code>输出的错误消息更具描述性。Exceptions 现在是<code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fapidocs%2Forg%2Fjsoup%2Fhelper%2FValidationException.html" target="_blank">ValidationExceptions</a></code>（扩展了<code>IllegalArgumentException</code>）。堆栈跟踪不包括 Validate 类，以便更简单地看到异常的来源。常见的验证错误（包括格式错误的 URL 和空选择器结果）都有更明确的错误信息。</li> 
 <li>构建改进：在 jar 清单中添加了实现版本和相关字段。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjhy%2Fjsoup%2Fissues%2F1809" target="_blank">#1809</a></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong><span><span><span style="color:#192943"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fapidocs%2Forg%2Fjsoup%2Fhelper%2FDataUtil.html" target="_blank">DataUtil</a></code>将从 InputStream 中错误地读取小于请求大小的读数。例如，当从分块的服务器响应中解析时，这会导致不正确的结果。#1807</li> 
</ul> 
<p>详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjsoup.org%2Fnews%2Frelease-1.15.3" target="_blank">查看官方公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            