
---
title: 'Git for Windows 2.33.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5857'
author: 开源中国
comments: false
date: Sat, 16 Oct 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5857'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Git for Windows 2.33.1 现已发布，主要更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.33.1%2FDocumentation%2FRelNotes%2F2.33.1.txt" target="_blank">Git v2.33.1</a></li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fnews%2Fopenssl-1.1.1-notes.html" target="_blank">OpenSSL v1.1.1l</a></li> 
 <li>包含的<code>git svn</code>现在在内部使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsvn.apache.org%2Frepos%2Fasf%2Fsubversion%2Ftags%2F1.14.1%2FCHANGES" target="_blank">subversion v1.14.1</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FGit-Credential-Manager-for-Windows" target="_blank">Git Credential Manager for Windows</a>（已被 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faka.ms%2Fgcmcore" target="_blank">Git Credential Manager Core</a> 取代，现已弃用很长时间，不再能成功地与 GitHub 进行认证）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F377" target="_blank">不再包含在 Git for Windows 中</a></li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.haxx.se%2Fchanges.html%237_79_1" target="_blank">cURL v7.79.1</a></li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssh.com%2Ftxt%2Frelease-8.8" target="_blank">OpenSSH v8.8p1</a></li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-lfs%2Fgit-lfs%2Freleases%2Ftag%2Fv3.0.1" target="_blank">Git LFS v3.0.1</a></li> 
 <li>内置文件系统观察器（“FSMonitor”）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3447" target="_blank">已更新到最新版本</a></li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2Fgit-credential-manager-core%2Freleases%2Ftag%2Fv2.0.567" target="_blank">Git Credential Manager Core v2.0.567.18224</a></li> 
</ul> 
<p><strong>Bug 修复</strong></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292f">Wordpad </span>可以再次被<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F378" target="_blank">配置为 Git 的首选编辑器</a></li> 
 <li>在 git pull 过程中，Git 的垃圾收集未能删除过时的文件，这个错误已经被修复</li> 
 <li><code>git svn</code>命令<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3392" target="_blank">在 Git for Windows v2.33.0(2)</a> 中被破坏，现已修复</li> 
 <li>通过 SSH 克隆时的密码提示<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F381" target="_blank">再次起作用</a></li> 
 <li>MSYS2 运行时<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fmsys2-runtime%2Fpull%2F33" target="_blank">不再 complains Windows/ARM64 上的 FAST_CWD</a></li> 
 <li>当 VS Code 配置为编辑器时，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3452" target="_blank">它不再需要关闭窗口，只需关闭 tab</a></li> 
 <li>32 位版本的 Git for Windows 包含了过时的<code>ca-certificates</code>和<code>less</code>版本，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2FMSYS2-packages%2Fpull%2F49" target="_blank">现已得到纠正</a></li> 
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
   <td style="border-style:solid; border-width:1px">Git-2.33.1-64-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">b1b69fcf56d50199536f7e6fc79b75ab16734d4d9a4b85c8e931596f02dd0688</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.33.1-32-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">bc2ca8f6ffcc6914ed04cfb13b2d0b6b994bd2437283cb3b43188b969bd5ef8b</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.33.1-64-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">723c879eb447583b893aa3234eae8caaa77d9d3ecf90883271fba98e8b2d99ac</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.33.1-32-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">fad2f32a3ca6e39cfbf7258c485a5601b0bfb620f44c582c1ba22784dd3faad3</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.33.1-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">8c28cde02668bfa3b117a49fe85728c1c8244d21701d5ab675668fc4677c4c7f</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.33.1-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">f340a3433c2c782ff8724707b87769d15519030d1a0e1c1314255f98eaa4f42f</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.33.1-busybox-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">96e2e9c8561eb20a3982fe292d4795bd4c09705f93cc03cf45a2f6b880fba181</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.33.1-busybox-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">3cd68aa4691202f2a182f8e0bf5a8eda2b795fbc6074de3e3c55548efdf28d15</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.33.1-64-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">1a002a49bc25e51b4571d35d5470a373fa7e0d2c7a6de81573c2d485063f066d</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.33.1-32-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">712a23a9c153402a75b88ec8ca5f51f4a75be6af3ef6ef965d9ed508d3a9a205</td> 
  </tr> 
 </tbody> 
</table> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.33.1.windows.1" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.33.1.windows.1</a> </p>
                                        </div>
                                      
</div>
            