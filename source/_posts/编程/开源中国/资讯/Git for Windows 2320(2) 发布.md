
---
title: 'Git for Windows 2.32.0(2) 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7222'
author: 开源中国
comments: false
date: Thu, 08 Jul 2021 06:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7222'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Git for Windows 2.32.0(2) 现已发布，主要更新内容如下：</p> 
<p><strong>New Features</strong></p> 
<ul> 
 <li>Windows 终端配置文件现在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F356" target="_blank">由 GUID 标识</a>，以实现更强大的自定义。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.gnupg.org%2Fpipermail%2Fgnupg-announce%2F2021q2%2F000460.html" target="_blank">GNU Privacy Guard v2.2.28</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fgit-credential-manager-core%2Freleases%2Ftag%2Fv2.0.475" target="_blank">Git Credential Manager Core v2.0.475.64295</a>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3292" target="_blank">可以启用</a>对需要客户端证书的远程 HTTPS 存储库的访问。现在这是必要的，因为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcurl%2Fcurl%2Fcommit%2F54e747501626b81149b1b44949119d365db82004" target="_blank">默认情况下 cURL 不再发送客户端证书</a>。</li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复了在某些情况下，内置文件系统观察程序可能会挂起的问题。</li> 
 <li>修复了无法从安装到网络共享中的便携式 Git 中访问远程 HTTPS 存储库的问题。</li> 
 <li>修复了当在 pager 中滚动时（例如在<code>git log</code>的输出中），lines 会被错误地复制。</li> 
 <li>修复了<code>git subtree</code>命令在之前的版本中被完全破坏的问题。</li> 
 <li>修复了一个远程操作出现挂起的错误（但正在等待用户对隐藏控制台的反馈）。</li> 
 <li>修复了一个错误，即实验性内置文件系统观察程序在处理路径为 non-ASCII 字符的 worktrees 时出现了问题。</li> 
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
   <td>Git-2.32.0.2-64-bit.exe</td> 
   <td>266fb20b60d53acd1bceb5d02877614c510a9dfd39bed3434342b2187c7a0fc6</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0.2-32-bit.exe</td> 
   <td>9cd78f6d86e33f1db963fc544a25e50e6ca32bf01cf77eec0d9146feb29ba98d</td> 
  </tr> 
  <tr> 
   <td>PortableGit-2.32.0.2-64-bit.7z.exe</td> 
   <td>c5efec6e470dabfb97696dce5f15c50a1173c14a8ae55d5a4cb144dd4c9cb68a</td> 
  </tr> 
  <tr> 
   <td>PortableGit-2.32.0.2-32-bit.7z.exe</td> 
   <td>c186d5260025203fb862343bc16ae94722f2d23fb160f083b89b0a50f54b1424</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0.2-64-bit.zip</td> 
   <td>40e0e8a8a4ccc3399d323b2edfab34fc4ebac7350471525d679d9839b689f4a6</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0.2-32-bit.zip</td> 
   <td>f253b0d3dca2ab09ba616b1da6aea3dffe9a66befccd8933b61271400d15c447</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0.2-busybox-64-bit.zip</td> 
   <td>a439abf1a0f00e1c031a94e427255dbd303556ece5231d1cf6d5c8ff7d43b461</td> 
  </tr> 
  <tr> 
   <td>MinGit-2.32.0.2-busybox-32-bit.zip</td> 
   <td>964a2dcf648499d4d125c3cc4511243b993cb3b32c01163704c22f7a6e6d4055</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0.2-64-bit.tar.bz2</td> 
   <td>4fde219d84943dd31e56b4641184d5fa6c9274f1faedcf87970bc1bb70bd3b72</td> 
  </tr> 
  <tr> 
   <td>Git-2.32.0.2-32-bit.tar.bz2</td> 
   <td>c82082423e0f9e9f120c3ee6f935a1da6b2259158cfe427003f13d5f16cb06c2</td> 
  </tr> 
 </tbody> 
</table> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.32.0.windows.2" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.32.0.windows.2</a></p>
                                        </div>
                                      
</div>
            