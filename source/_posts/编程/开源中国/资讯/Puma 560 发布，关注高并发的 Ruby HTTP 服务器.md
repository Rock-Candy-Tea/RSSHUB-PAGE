
---
title: 'Puma 5.6.0 发布，关注高并发的 Ruby HTTP 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-813aa50dda7222be618da333381e16ed232.jpg'
author: 开源中国
comments: false
date: Thu, 27 Jan 2022 07:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-813aa50dda7222be618da333381e16ed232.jpg'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Puma 是一个简单、快速、线程化并且关注高并发的 HTTP 1.1 服务器，适用于开发和生产中的 Ruby/Rack 应用。</span></p> 
<p>Puma 5.6.0 发布了，该版本带来如下变更：</p> 
<p><strong>特性</strong></p> 
<ul> 
 <li>支持在 <code>ssl_bind</code> 中集成本地主机 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2764" target="_blank">#2764</a>],[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2708" target="_blank">#2708</a>])</li> 
 <li>允许使用 ssl_bind DSL 设置 backlog 参数 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2780" target="_blank">#2780</a>])</li> 
 <li>删除 StateFile 中的 yaml (psych)需求 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2784" target="_blank">#2784</a>])</li> 
 <li>添加 worker_check_interval 配置选项（[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2759" target="_blank">#2759</a> ]）</li> 
 <li>始终向客户端发送低级错误响应（[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2731" target="_blank">#2731</a> ],[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2341" target="_blank">#2341</a> ]）</li> 
 <li>使用 ssl_bind DSL 支持 cert_pem 和 key_pem ([ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2728" target="_blank">#2728</a> ])</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>线程名保持在15个字符以下，防止在某些操作系统上出现中断 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2733" target="_blank">#2733</a>])</li> 
 <li>修复两个“老式定义”的编译警告 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2807" target="_blank">#2807</a>], [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fissues%2F2806" target="_blank">#2806</a>])</li> 
 <li>正确使用选项值来记录环境 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2799" target="_blank">#2799</a>])</li> 
 <li>修复 Ruby master 的警告(将启用 3.2.0 版本) ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2785" target="_blank">#2785</a>])</li> 
 <li>extconf.rb - 用旧的 Windows 版本修复 openssl ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2757" target="_blank">#2757</a>])</li> 
 <li>server.rb - 新增对 <code>@notify.close</code> 的救援处理(<code>Errno::EBADF</code>) ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2745" target="_blank">#2745</a>])</li> 
</ul> 
<p><strong>重构</strong></p> 
<ul> 
 <li>server.rb - 使用 [:remote_address] 重构代码 ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2742" target="_blank">#2742</a>])</li> 
 <li>[jruby] 一些避免复制字节的重构  ([<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Fpull%2F2730" target="_blank">#2730</a>])</li> 
</ul> 
<p> </p> 
<p>此外，Puma 的维护者之一 @nateberkopec 的女儿刚诞生，小名叫 Birdie，因此 Puma 5.6.0 版本也叫 “Birdie 版本”。</p> 
<p><img alt height="500" src="https://oscimg.oschina.net/oscnet/up-813aa50dda7222be618da333381e16ed232.jpg" width="375" referrerpolicy="no-referrer"></p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpuma%2Fpuma%2Freleases%2Ftag%2Fv5.6.0" target="_blank">https://github.com/puma/puma/releases/tag/v5.6.0</a></p>
                                        </div>
                                      
</div>
            