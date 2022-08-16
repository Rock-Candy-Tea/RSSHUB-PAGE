
---
title: 'Firebird 4.0.2 发布，C++ 开发的关系数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0816/071452_hG6U_5430600.png'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 07:16:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0816/071452_hG6U_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>Firebird 4.0.2<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffirebirdsql.org%2Fen%2Fnews%2Ffirebird-4-0-2-sub-release-is-available%2F" target="_blank"> 已发布</a>。</p> 
<p style="margin-left:0">Firebird 是一个跨平台的关系数据库，可运行在 Windows、Linux 和多种 Unix 操作系统上，提供了大部分 SQL-99 标准的功能。它既能作为多用户环境下的数据库服务器运行，也提供嵌入式数据库的实现。</p> 
<p style="margin-left:0">Firebird 源于 Borland 公司的 InterBase 6.0，是一个完全非商业化的产品，源代码经过大规模重写，使用 C++ 开发。</p> 
<p style="margin-left:0"><br> <img alt height="452" src="https://static.oschina.net/uploads/space/2022/0816/071452_hG6U_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fpull%2F6983" target="_blank">#6983</a><span style="color:rgba(0,0,0,0.8)"> — 新增内置函数 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffirebirdsql.org%2Ffile%2Fdocumentation%2Frelease_notes%2Fhtml%2Fen%2F4_0%2Frlsnotes40.html%23rnfb40-dml-new-blob-append" target="_blank">BLOB_APPEND</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7208" target="_blank">#7208</a><span style="color:rgba(0,0,0,0.8)"> — Trace: </span>为 DDL 语句提供性能统计</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7194" target="_blank">#7194</a><span style="color:rgba(0,0,0,0.8)"> — </span>使用 firebird.pas 可以避免 Pascal 程序中的 fbclient 依赖</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7168" target="_blank">#7168</a><span style="color:rgba(0,0,0,0.8)"> — </span>在恢复期间忽略丢失的 UDR 库</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7161" target="_blank">#7161</a><span style="color:rgba(0,0,0,0.8)"> — 将 </span>zlib<span style="color:rgba(0,0,0,0.8)"> 升级到 1.2.12</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7093" target="_blank">#7093</a><span style="color:rgba(0,0,0,0.8)"> — </span>当最后一个 key 字符是 collated contractions 的一部分时，提升字符串的索引查找速度</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7092" target="_blank">#7092</a><span style="color:rgba(0,0,0,0.8)"> — 优化</span><code>CURRENT_TIME</code><span style="color:rgba(0,0,0,0.8)">性能</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7042" target="_blank">#7042</a><span style="color:rgba(0,0,0,0.8)"> — </span>在强制附件 (<span style="color:rgba(0,0,0,0.8)">forced attachment</span>) 关闭期间，不执行<code>ON DISCONNECT</code><span style="color:rgba(0,0,0,0.8)">触发器</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7041" target="_blank">#7041</a><span style="color:rgba(0,0,0,0.8)"> — 提供支持 Apple M1 架构的 Firebird 移植</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F7038" target="_blank">#7038</a><span style="color:rgba(0,0,0,0.8)"> — </span>优化不敏感排序的<code>STARTING WITH</code><span style="color:rgba(0,0,0,0.8)">的性能</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFirebirdSQL%2Ffirebird%2Fissues%2F6730" target="_blank">#6730</a><span style="color:rgba(0,0,0,0.8)"> — Trace: </span>提供查看<code>STATEMENT RESTART</code><span style="color:rgba(0,0,0,0.8)">事件的能力</span></li> 
</ul> 
<p style="margin-left:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ffirebirdsql.org%2Ffile%2Fdocumentation%2Frelease_notes%2Fhtml%2Fen%2F4_0%2Frlsnotes40.html" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            