
---
title: 'Pidgin 2.14.9 发布，跨平台即时聊天工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1709'
author: 开源中国
comments: false
date: Mon, 02 May 2022 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1709'
---

<div>   
<div class="content">
                                                                                            <p>Pidgin 原名 Gaim，是一款采用 <a href="http://www.oschina.net/p/gtk">GTK</a> <span style="color:#000000">开发的跨平台即时聊天客户端软件，支持包括 Aim、ICQ （基于 Oscar 协议）、MSN Messenger、Yahoo、IRC、Jabber、Gadu-Gadu、SILC、Groupwise Messenger 和 Zephyr 等即时通信软件。你可以同时用不同的账号在多个即时通信网络中登录。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Pidgin 2.14.9 现已发布，这是<span style="background-color:#ffffff">一个错误修复版本，包含许多随机错误修复。需要注意的是，Windows 安装程序中的字典下载以及 Windows 上的 IRC 文件传输终于得到修复。还有一个较小的安全修复程序，该修复程序是通过删除对 _xmppconnect DNS TXT 记录的支持而修复的，该记录很长时间以来一直被认为是不安全的。</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">完整变更日志如下：</span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Security：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>移除<code>_xmppconnect</code>支持。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1357" target="_blank">Review 1357</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpidgin.im%2Fabout%2Fsecurity%2Fadvisories%2Fcve-2022-26491%2F" target="_blank">CVE-2022-26491</a>) </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>libpurple：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复键入超时的 GLib CRITICAL 消息。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1123" target="_blank">Review 1123</a>)</li> 
 <li>修复了 Purple_str_to_time 的单元测试会失败的问题。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.gentoo.org%2F819774" target="_blank">GENTOO-819774</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1238" target="_blank">Review 1238</a>)</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Pidgin：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复 pidgin_conversations_set_tab_colors 中的内存泄漏。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1244" target="_blank">Review 1244</a>)</li> 
 <li>修复了大部分输入框无限调整大小的问题。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-16753" target="_blank">PIDGIN-16753</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-16999" target="_blank">PIDGIN-16999</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17287" target="_blank">PIDGIN-17287</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17413" target="_blank">PIDGIN-17413</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17430" target="_blank">PIDGIN-17430</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17568" target="_blank">PIDGIN-17568</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17602" target="_blank">PIDGIN-17602</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1342" target="_blank">Review 1342</a>)</li> 
 <li>添加 transient-buddy back，用于显示一些上下文菜单和其他内容。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17523" target="_blank">PIDGIN-17523</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1381" target="_blank">Review 1381</a>) </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start">Windows<span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复 Windows 安装程序中字典的下载问题。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-14618" target="_blank">PIDGIN-14618</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-15648" target="_blank">PIDGIN-15648</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-15540" target="_blank">PIDGIN-15540</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-14612" target="_blank">PIDGIN-14612</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-14893" target="_blank">PIDGIN-14893</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1303" target="_blank">Review 1303</a>) </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Translations：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修正德语翻译中的一个错字。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17575" target="_blank">PIDGIN-17575</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1242" target="_blank">Review 1242</a>) </li> 
 <li>将所有翻译与 Transifex 同步。</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>IRC：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复 Windows 上的 IRC 文件传输。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17175" target="_blank">PIDGIN-17175</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1382" target="_blank">Review 1382</a>) </li> 
 <li>修复 IRC 上 99% 的文件传输失败问题。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-15893" target="_blank">PIDGIN-15893</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1385" target="_blank">Review 1385</a>) </li> 
 <li>将 IRC 中的 realname 和 ident name 默认为帐户的用户名（昵称）。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-17610" target="_blank">PIDGIN-17610</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1386" target="_blank">Review 1386</a>) </li> 
 <li>向 IRC 帐户添加高级帐户选项，以明确设置 SASL 登录名。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-15451" target="_blank">PIDGIN-15451</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1388" target="_blank">Review 1388</a>)</li> 
 <li>添加了一个速率限制器，应该可以防止过度泛滥。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1391" target="_blank">Review 1391</a>) </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>SIMPLE：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复了 SIMPLE 中 Cseq numbers 的问题。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-9675" target="_blank">PIDGIN-9675</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1379" target="_blank">Review 1379</a>) </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span style="color:#323232"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>XMPP：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复 XMPP attention messages 被发送到不正确的 JID。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fissues.imfreedom.org%2Fissue%2FPIDGIN-14714" target="_blank">PIDGIN-14714</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Freviews.imfreedom.org%2Fr%2F1387" target="_blank">Review 1387</a>) </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpidgin.im%2Fposts%2F2022-04-2.14.9-released%2F" target="_blank">https://pidgin.im/posts/2022-04-2.14.9-released/</a></p>
                                        </div>
                                      
</div>
            