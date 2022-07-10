
---
title: 'Debian 11.4 发布，修复大量 Bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5466'
author: 开源中国
comments: false
date: Sun, 10 Jul 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5466'
---

<div>   
<div class="content">
                                                                                            <p>Debian 11（代号 <em>Bullseye</em>）的第四次更新已发布，Debian 11.4 版本主要增加了对安全问题的修正，以及对大量严重 Bug 的一些调整。</p> 
<p><span style="color:#222222">该发布并不构成 Debian 11 的新版本，只是更新了一些软件包，</span>可以使用最新的 Debian 镜像将软件包升级到当前版本。</p> 
<h2>Bugfixes<strong> </strong></h2> 
<table style="width:700px"> 
 <tbody> 
  <tr> 
   <td><strong>包</strong></td> 
   <td><strong>更新理由</strong></td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Aapache2" target="_blank">apache2</a></td> 
   <td>新的上游稳定版本；修复 HTTP 请求走私问题 [CVE-2022-26377]、越界读取问题 [CVE-2022-28330 CVE-2022-28614 CVE-2022-28615]、拒绝服务问题 [CVE-2022-29404 CVE- 2022-30522]</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Abash" target="_blank"><u>bash</u></a></td> 
   <td>修复 1 字节缓冲区溢出读取，导致命令替换中损坏的多字节字符</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Acomposer" target="_blank"><u>composer</u></a></td> 
   <td>修复代码注入问题 [CVE-2022-24828]；更新 GitHub 令牌模式</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Afreetype" target="_blank"><u>freetype</u></a></td> 
   <td>修复缓冲区溢出问题 [CVE-2022-27404]；修复崩溃 [CVE-2022-27405 CVE-2022-27406]</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Agnutls28" target="_blank"><u>gnutls28</u></a></td> 
   <td>修复 SSSE3 SHA384 计算错误；修复空指针引用问题 [CVE-2021-4209]</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Agrunt" target="_blank"><u>grunt</u></a></td> 
   <td><span style="color:#222222">修复路径遍历问题 [CVE-2022-0436]</span></td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Alinux" target="_blank"><u>linux</u></a></td> 
   <td>新的上游稳定版本；将 ABI 增加到 16</td> 
  </tr> 
  <tr> 
   <td><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpackages.debian.org%2Fsrc%3Alxc" target="_blank"><u>LXC</u></a></td> 
   <td> 更新默认 GPG 密钥服务器，修复使用下载模板创建容器</td> 
  </tr> 
 </tbody> 
</table> 
<p>更多细项可在 Debian 11.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2FNews%2F2022%2F20220709" target="_blank">released 公告</a>中查看。</p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>完整的镜像列表可在以下位置获得：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span><span><span style="color:#222222"><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.debian.org%2Fmirror%2Flist" target="_blank">https://www.debian.org/mirror/list</a> 。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            