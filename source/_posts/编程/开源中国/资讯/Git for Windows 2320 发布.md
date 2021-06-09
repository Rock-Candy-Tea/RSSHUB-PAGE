
---
title: 'Git for Windows 2.32.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2339'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 06:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2339'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Git for Windows 2.32.0 已发布，主要更新内容如下：</p> 
<p><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.32.0%2FDocumentation%2FRelNotes%2F2.32.0.txt" target="_blank">Git v2.32.0</a>。</li> 
 <li>安装程序现在提供安装一个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F339" target="_blank">Windows 终端配置文件</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.haxx.se%2Fchanges.html%237_77_0" target="_blank">cURL v7.77.0</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpcre.org%2Fnews.txt" target="_blank">PCRE2 v10.37</a>。</li> 
 <li>实验性的内置<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fdiscussions%2F3251" target="_blank">文件系统监视器</a>现在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F351" target="_blank">在安装程序中作为实验性选项提供</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fgit-credential-manager-core%2Freleases%2Ftag%2Fv2.0.474" target="_blank">Git Credential Manager Core v2.0.474.41365</a>。</li> 
 <li>Sublime Text 4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F355" target="_blank">现在可以被安装程序检测到</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjonas%2Ftig%2Freleases%2Ftag%2Ftig-2.5.4" target="_blank">tig v2.5.4</a>。</li> 
</ul> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li>当在安装程序中测试一个自定义编辑器时，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3155" target="_blank">现在以 non-elevated 模式生成它，</a>修复了例如 Atom 在实例已经运行时的问题。</li> 
 <li>Git for Windows 的 Portable Git 版所使用的 meta credential-helper <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3196" target="_blank">有时会崩溃</a>，已修复。</li> 
 <li>自动更新程序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F347" target="_blank">不再建议从 -rc0 版本降级</a>。</li> 
</ul> 
<table cellspacing="0"> 
 <tbody> 
  <tr> 
   <th>Filename</th> 
   <th>SHA-256</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td>Git-2.32.0-64-bit.exe</td> 
   <td>eed601ef835c3dac08d2e27f6f38b5db7998747c753c87a45b326fbd6c710309</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0-32-bit.exe</td> 
   <td>5239b465b893ea595f6a73fde20691bcfc9c65661fa1b74441d9ce7b98848ade</td> 
  </tr> 
  <tr> 
   <td>PortableGit-2.32.0-64-bit.7z.exe</td> 
   <td>cc561200eb89fdb19c75f901aea2740ffa57a627a31c1a6ef86a8d37e3186275</td> 
  </tr> 
  <tr> 
   <td>PortableGit-2.32.0-32-bit.7z.exe</td> 
   <td>29495a17a58ee5fb0345a18d25bf410bd2d1ead86896ba9d2eecf0b690d78f0a</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0-64-bit.zip</td> 
   <td>e55a73125ea2fd6d1d71470e089a97cf19e6f1c4aaf7c25958d1a9105112a6de</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0-32-bit.zip</td> 
   <td>6463c624236cbd2c9772be12ff88c5137f83a3fd550a1dbe9bcb307d0923d8e9</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0-busybox-64-bit.zip</td> 
   <td>51b90b7a857d6407b5f10c2d657a4bcc71f461438bb23958576893c2b41b9780</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0-busybox-32-bit.zip</td> 
   <td>937330daccc3be48da4ee7b30381f9a00271d5c1ee2c56f9d70005c5c68a1144</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0-64-bit.tar.bz2</td> 
   <td>5ddd62781c33535a8bfab894b5861e47d1024416f9196eff2d9047853c636728</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0-32-bit.tar.bz2</td> 
   <td>699ded239282b56f7d120e1e2a0aab3652e63c4586400b21a618d1b31189c9bb</td> 
  </tr> 
 </tbody> 
</table> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.32.0.windows.1" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.32.0.windows.1</a></p>
                                        </div>
                                      
</div>
            