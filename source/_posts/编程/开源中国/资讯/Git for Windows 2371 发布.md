
---
title: 'Git for Windows 2.37.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4373'
author: 开源中国
comments: false
date: Thu, 14 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4373'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Git for Windows 2.37.1 现已发布<span style="color:#333333">，主要更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>New Features</strong></p> 
<ul> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fblob%2Fv2.37.1%2FDocumentation%2FRelNotes%2F2.37.1.txt" target="_blank">Git v2.37.1</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openssl.org%2Fnews%2Fopenssl-1.1.1-notes.html" target="_blank">OpenSSL v1.1.1q</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FGitCredentialManager%2Fgit-credential-manager%2Freleases%2Ftag%2Fv2.0.785" target="_blank">Git Credential Manager Core v2.0.785</a>。</li> 
 <li>随附 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjonas%2Ftig%2Freleases%2Ftag%2Ftig-2.5.5" target="_blank">tig v2.5.5</a>。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>在 Windows Terminal 中运行时，在 Git for Windows 的 Bash 中粘贴大量文本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fissues%2F3936" target="_blank">通常会导致文本乱码</a>，该问题已得到修复。</li> 
 <li>Perl 模块 perl-Clone 链接到了一个不存在的 DLL，为了解决这个问题已重建了这个模块。</li> 
 <li>Git for Windows 的安装程序不再能被诱导在 elevated mode 下运行不受信任的<code>git.exe</code> ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Fsecurity%2Fadvisories%2FGHSA-gjrj-fxvp-hjj2" target="_blank">CVE-2022-31012</a> )。</li> 
 <li>在当前用户拥有的全局可写目录中运行 Git 时（think<code>C:\Windows\Temp</code>，当在<code>SYSTEM</code>帐户下运行时），对<code>.git</code>目录可疑所有权的检查现在可以正确检测到这种情况 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit%2Fgit%2Fsecurity%2Fadvisories%2FGHSA-j342-m5hw-rr3v" target="_blank">CVE-2022-29187</a> )。</li> 
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
   <td style="border-style:solid; border-width:1px">Git-2.37.1-64-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">1966761ad2c9e4cbd38f9e583b1125949b011a5a250a99d65e9bb21958e6ef8b</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.1-32-bit.exe</td> 
   <td style="border-style:solid; border-width:1px">714069fe4291c4ca7a51f7e7e81b0c94038590294f3b9e0981456a664c92966b</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.37.1-64-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">b0bc403bb03326b835e239b3bf7c0af277f43eba5421132dc8531204c78b6b25</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">PortableGit-2.37.1-32-bit.7z.exe</td> 
   <td style="border-style:solid; border-width:1px">1a32f1de26d52ef866f27db395d8ab6bd9dc4c53bfc0161937b20f8749b4d96b</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.1-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">edacf2d5c39555c25a396e0b9d27182ab5587259dc2e824b4490996b373f9300</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.1-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">b336137fb286552c5c2616af50c54e9aca7d16a24ec1b00189a6c221a81af14c</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.1-busybox-64-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">1fb7db2cb181ef962e06b1b99c4b254b3ace6f6dce73740bd498d3948189ca42</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">MinGit-2.37.1-busybox-32-bit.zip</td> 
   <td style="border-style:solid; border-width:1px">7470ec55d4ac0ddc3738614dbfe6642770a001b0bae9d3c944e22e25019bf16d</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.1-64-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">b1c87e136947102ce32f75ef880ebee79b547f8ef33bb1b5010c3455ac83a655</td> 
  </tr> 
  <tr> 
   <td style="border-style:solid; border-width:1px">Git-2.37.1-32-bit.tar.bz2</td> 
   <td style="border-style:solid; border-width:1px">b0fef8f618e5e5cdad200571211fb6b42be595ef55bf8b648b8211c8bd5e02ea</td> 
  </tr> 
 </tbody> 
</table> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgit-for-windows%2Fgit%2Freleases%2Ftag%2Fv2.37.1.windows.1" target="_blank">https://github.com/git-for-windows/git/releases/tag/v2.37.1.windows.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            