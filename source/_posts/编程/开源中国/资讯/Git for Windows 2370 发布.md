
---
title: 'Git for Windows 2.37.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8941'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8941'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0"><span style="color:#333333">Git for Windows 2.37.0 现已发布，主要更新内容如下：</span></p> 
<p style="margin-left:0"><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.37.0%2FDocumentation%2FRelNotes%2F2.37.0.txt" target="_blank">Git v2.37.0</a>。</li> 
 <li><span style="color:#333333">许多反恶意软件产品似乎在我们的 MSYS2 运行时存在问题，导致运行时出现问题，例如 </span><code>git subtree</code><span style="color:#333333">。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fmsys2-runtime%2Fpull%2F37" target="_blank">添加了一种变通方法</a>，希望能在大多数情况下有所帮助。</li> 
 <li><span style="color:#333333">随附基于 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcygwin.com%2Fpipermail%2Fcygwin-announce%2F2022-May%2F010565.html" target="_blank">Cygwin 3.3.5</a> 的 MSYS2 运行时（<span style="color:#333333">Git for Windows flavor</span>）。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2FPCRE2Project%2Fpcre2%2Fpcre2-10.40%2FChangeLog" target="_blank">PCRE2 v10.40</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-lfs%2Fgit-lfs%2Freleases%2Ftag%2Fv3.2.0" target="_blank">Git LFS v3.2.0</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.gnupg.org%2Fpipermail%2Fgnutls-help%2F2022-May%2F004744.html" target="_blank">GNU TLS v3.7.6</a>。</li> 
 <li><span style="color:#333333">SSH 的 CBC 密码在 2017 年重新启用以更好地支持 Azure Repos</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F421">，</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fbuild-extra%2Fpull%2F421" target="_blank">但现在默认情况下再次被禁用，</a>因为 Azure Repos 不再需要它们。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fnews%2Fopenssl-1.1.1-notes.html" target="_blank">OpenSSL v1.1.1p</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FGitCredentialManager%2Fgit-credential-manager%2Freleases%2Ftag%2Fv2.0.779" target="_blank">Git Credential Manager Core v2.0.779</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcurl.haxx.se%2Fchanges.html%237_84_0" target="_blank">cURL v7.84.0</a>。</li> 
</ul> 
<p><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li><span style="color:#24292f">git status 中 Git for Windows-only --show-ignored-directory 选项在很久以前就被废弃了，现在终于被移除。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3875" target="_blank">修复</a>了在 Wine 中运行 Git for Windows 时的崩溃问题。</li> 
 <li>修复了 FSCache 和 parallel checkout 之间的交互<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3909" target="_blank">错误</a>。</li> 
 <li>在某些网络文件系统上克隆到网络共享失败，已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3646" target="_blank">修复</a>。</li> 
 <li>当 Git 由于文件系统（例如 FAT32）无法记录所有权而指示不安全目录时，Git <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fpull%2F3887" target="_blank">现在会提供更好的提示</a>。</li> 
</ul> 
<p><span style="color:#333333">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.37.0.windows.1" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.37.0.windows.1</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            