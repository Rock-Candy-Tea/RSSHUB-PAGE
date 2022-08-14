
---
title: 'Git for Windows 2.37.2(2) 发布，将放弃支持 Windows 7_8'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4901'
author: 开源中国
comments: false
date: Sat, 13 Aug 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4901'
---

<div>   
<div class="content">
                                                                                            <p>Git for Windows 2.37.2(2) 现已发布，<span style="color:#333333">主要更新内容如下：</span></p> 
<p><strong>(Upcoming) breaking changes</strong></p> 
<p>将包含的 Bash 更新到了 5.1 版本（之前是 4.4），用户需检查自己的 shell 脚本是否有潜在的兼容性问题。</p> 
<p>此外，<span style="background-color:#ffffff; color:#24292f">Git for Windows 放弃了对 Windows Vista 的支持。</span>大约在 2023 年初，Git for Windows 将放弃对 Windows 7 和 Windows 8 的支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.37.2%2FDocumentation%2FRelNotes%2F2.37.2.txt" target="_blank">Git v2.37.2</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjonas%2Ftig%2Freleases%2Ftag%2Ftig-2.5.6" target="_blank">tig v2.5.6</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftiswww.case.edu%2Fphp%2Fchet%2Fbash%2FNEWS" target="_blank">Bash v5.1 patchlevel<span> </span>016</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsearch.cpan.org%2Fdist%2Fperl-5.36.0%2Fpod%2Fperldelta.pod" target="_blank">Perl v5.36.0</a>。</li> 
 <li>Git 的可执行文件<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F429" target="_blank">现在</a>被标记为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3942" target="_blank">Terminal Server-aware</a>，这意味着：使用远程桌面服务运行 Git 会稍微快一些。</li> 
 <li><code>git svn</code>现在基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsvn.apache.org%2Frepos%2Fasf%2Fsubversion%2Ftags%2F1.14.2%2FCHANGES" target="_blank">subversion v1.14.2</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.gnupg.org%2Fpipermail%2Fgnutls-help%2F2022-July%2F004746.html" target="_blank">GNU TLS v3.7.7</a>。</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>Git for Windows 现在没有<code>zmore</code>和<code>bzmore</code>工具（这些工具已经坏了，只是无意中包括在内）。</li> 
 <li>git mergetool 的 vimdiff 模式中的一个回归已修复。</li> 
 <li>对于某些网络驱动器，与缓存相关的某些属性会混淆 Git for Windows。这已被修复。</li> 
</ul> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#24292f; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji"; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:0px !important; margin-top:0px; max-width:100%; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:max-content; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <th>Filename</th> 
   <th>SHA-256</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.2.2-64-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">6f91f1bb28b222f30c13f905a5e9b0ad491e67c28a37a238000def19f86e0a2f</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.2.2-32-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">672569b7041024b1fdb5c29cc9a775658be78f7d3afea025973e07954f5070fa</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.37.2.2-64-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">20d9b7e8e8b8b4f27d16420597772e19e7cb1f396b355473867942ed86d0d931</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.37.2.2-32-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">36e24698b3cf5270d8276c80a1f7c14ff5d140ee2ac37e8e28a935d0a0ab3418</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.2.2-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">12b7c2c8cb9db03fd8c81e618aab196a366d919b2dc0dcd5a062738a07960a05</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.2.2-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">d3bf1f155872cc431f3ebe898906d6b52988802ff7c3597d9bc16d0937f81209</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.2.2-busybox-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">0a299ae5621ef69424d80b27b7a3b177f7299b124139d20afadfed9226648c47</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.2.2-busybox-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">69cdd838c924eb4c989652191d77bd9a7ef069e4e059eced69cfeb1e92bfe343</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.2.2-64-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">96b564cfbd99e355e340e1ba5350674fa7c0a04b5390ccca078a1a37637eba6b</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.2.2-32-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">153defc4bed02814a772d473ae74a380e68a2377331ee8ad51ac6d21ed35cbbe</td> 
  </tr> 
 </tbody> 
</table> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.37.2.windows.2" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.37.2.windows.2</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            