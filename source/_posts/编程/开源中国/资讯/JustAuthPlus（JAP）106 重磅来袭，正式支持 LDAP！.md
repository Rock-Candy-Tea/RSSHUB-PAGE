
---
title: 'JustAuthPlus（JAP）1.0.6 重磅来袭，正式支持 LDAP！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cdn.jsdelivr.net/gh/filess/img13@main/2021/09/28/1632813514533-24918b16-533d-433d-8bef-ec4569a70baf.png'
author: 开源中国
comments: false
date: Wed, 03 Nov 2021 10:21:00 GMT
thumbnail: 'https://cdn.jsdelivr.net/gh/filess/img13@main/2021/09/28/1632813514533-24918b16-533d-433d-8bef-ec4569a70baf.png'
---

<div>   
<div class="content">
                                                                                            <h1>JustAuthPlus（JAP）1.0.6重磅来袭，支持 LDAP！</h1> 
<p><img alt src="https://cdn.jsdelivr.net/gh/filess/img13@main/2021/09/28/1632813514533-24918b16-533d-433d-8bef-ec4569a70baf.png" referrerpolicy="no-referrer"></p> 
<h2>上一版本功能预告(<span style="background-color:#ffffff; color:rgba(0, 0, 0, 0.87)">2021-09-28</span>)</h2> 
<p>预计在下一里程碑版中，将会推出 <code>jap-ldap</code> 组件，支持 ldap 的登录认证功能。在做这个功能时，我调研过不少开源的关于 ldap 项目，很少有项目能对 ldap 的密码加密方法做适配，大部分都是验证的 md5、sha 这两种常用加密算法，在<code>jap-ldap</code> 中将会对 ldap 支持的标准加密算法做全量适配。</p> 
<p><img alt src="https://cdn.jsdelivr.net/gh/filess/img8@main/2021/09/28/1632813949898-a587bf30-f6c3-4eae-829a-44403c35b9a0.png" referrerpolicy="no-referrer"></p> 
<h2>当前版本更新的内容</h2> 
<h3>新特性</h3> 
<ul> 
 <li>正式支持 LDAP 中用户的登录认证，<code>jap-ldap</code> 支持使用 LDAP 中的用户进行身份认证。适配 LDAP 中的标准密码加密类型，如：clear, k5key, md5, smd5, sha, ssha, sha512, sha256, ext_des, md5crypt, sha256crypt, sha512crypt 和 crypt。更多使用说明请参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjustauth.plus%2Fquickstart%2Fjap-ldap%2F" target="_blank">使用jap-ldap</a></li> 
 <li>支持自定义 <code>JapUserStore</code>。（Gitee Issue <a href="https://gitee.com/fujieid/jap/issues/I4BHBJ">#I4BHBJ</a>）</li> 
</ul> 
<h3>优化修复</h3> 
<ul> 
 <li>重构发布快照流水线。 (Github PR <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffujieid%2Fjap%2Fpull%2F15" target="_blank">#15</a>)</li> 
 <li>修改 <code>JapUserService</code> 接口中的 <code>createAndGetHttpApiUser</code>方法名使其更符合语义。 (Github PR <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffujieid%2Fjap%2Fpull%2F13" target="_blank">#13</a>)</li> 
 <li>[jap-ids] 将 <code>AccessToken</code> 中的 <code>LocalDateTime</code> 改为 Date</li> 
 <li>合并 Github PR <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffujieid%2Fjap%2Fpull%2F16" target="_blank">#16</a></li> 
 <li>解决 Gitee Issue <a href="https://gitee.com/fujieid/jap/issues/I4FGZ1">#I4FGZ1</a></li> 
 <li>更新了一些错误的文案</li> 
</ul> 
<h3>依赖升级</h3> 
<ul> 
 <li>升级 <code>hutool</code> 的版本为 5.7.14</li> 
 <li>升级 <code>JustAuth</code> 的版本为 1.16.5</li> 
</ul>
                                        </div>
                                      
</div>
            