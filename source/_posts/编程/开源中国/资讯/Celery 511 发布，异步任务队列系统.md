
---
title: 'Celery 5.1.1 发布，异步任务队列系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8642'
author: 开源中国
comments: false
date: Tue, 22 Jun 2021 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8642'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Celery 5.1.1 现已发布。Celery 是一个简单，灵活且可靠的分布式系统，可以处理大量消息，同时为操作提供维护该系统所需的工具。这是一个任务队列，着重于实时处理，同时还支持任务调度。Celery 是用 Python 编写的，但协议可以用任何语言实现。 </p> 
<p>新版本具体更新内容如下：</p> 
<ul> 
 <li>修复命令行选项解析中的<code>--pool=threads</code>支持。(#6787)</li> 
 <li>修复<code>LoggingProxy.write()</code>返回类型。(#6791)</li> 
 <li>Couchdb key 现在总是被强制转换为字符串。(#6781)</li> 
</ul> 
<p>grp 不再无条件导入（#6804）。这修复了 5.1.0 中在非 unix 系统中运行 Celery 时的一个回归。</p> 
<ul> 
 <li>确保 regen 实用程序类在协调时被标记为完成。(#6789)</li> 
 <li>保留替换任务的 call/errbacks。(#6770)</li> 
 <li>使用 single-lookahead 的方式进行再生消耗。(#6799)</li> 
 <li>已撤销的任务不再错误地标记为重试。(#6812, #6816)</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcelery%2Fcelery%2Fblob%2Fmaster%2FChangelog.rst" target="_blank">https://github.com/celery/celery/blob/master/Changelog.rst</a></p> 
<p><strong>下载：</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcelery%2Fcelery%2Farchive%2Frefs%2Ftags%2Fv5.1.1.zip" target="_blank">Source code(zip)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcelery%2Fcelery%2Farchive%2Frefs%2Ftags%2Fv5.1.1.tar.gz" target="_blank">Source code(tar.gz)</a></li> 
</ul>
                                        </div>
                                      
</div>
            