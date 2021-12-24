
---
title: '支持 tmux，类似 rz _ sz 的 trzsz 发布 0.1.4 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MIT-green.svg?style=flat'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 23:40:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MIT-green.svg?style=flat'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">tmux 不支持 rz / sz ，于是有一个兼容 tmux 的 trz / tsz ( </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">trzsz</a><span style="background-color:#ffffff; color:#333333"> )，可以与 iTerm2 一起用，还有一个不错的进度条。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">已发布 0.1.4 版本，支持静默模式，以及解决了 tmux 非控制模式下偶尔出错的问题。</p> 
<hr> 
<h1 style="margin-left:0; margin-right:0; text-align:start">trzsz</h1> 
<p style="color:#606c71; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftrzsz.github.io%2F" target="_blank">trzsz</a><span> </span>是一个简单的文件传输工具，和 lrzsz ( rz / sz ) 类似但支持 tmux，</p> 
<p style="color:#606c71; text-align:start">和 iTerm2 一起使用，并且有一个不错的进度条。</p> 
<p style="color:#606c71; text-align:start">GitHub:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">https://github.com/trzsz/trzsz</a></p> 
<p style="color:#606c71; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fchoosealicense.com%2Flicenses%2Fmit%2F" target="_blank"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green.svg?style=flat" style="margin-top:0px" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.python.org%2Fpypi%2Ftrzsz%2F" target="_blank"><img alt="PyPI trzsz" src="https://img.shields.io/pypi/v/trzsz?style=flat" style="margin-top:0px" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftrzsz.github.io%2Fcn%2F" target="_blank"><img alt="中文网站" src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E7%BD%91%E7%AB%99-blue?style=flat" style="margin-top:0px" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:start">为什么开发 trzsz ?</h2> 
<p style="color:#606c71; text-align:start">登录远程电脑时用 tmux 保持会话，但 tmux 不支持用 rz / sz 上传和下载文件，这就很不方便了。</p> 
<p style="color:#606c71; text-align:start">重新造一个 rz / sz 比修改 tmux 相对简单很多，并且可以加个进度条，体验上会好很多。</p> 
<h2 style="text-align:start">安装指南</h2> 
<h3 style="text-align:start">远程服务器安装<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Ftrzsz-svr" target="_blank">trzsz-svr</a></h3> 
<div style="text-align:start"> 
 <div> 
  <pre><code>sudo python3 -m pip install --upgrade trzsz-libs trzsz-svr
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>同样也支持 Python2: 
  <div> 
   <div> 
    <pre><code>sudo pip install --upgrade trzsz-libs trzsz-svr
</code></pre> 
   </div> 
  </div> </li> 
</ul> 
<h3 style="text-align:start">本地 macOS 安装<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Ftrzsz-iterm2" target="_blank">trzsz-iterm2</a></h3> 
<div style="text-align:start"> 
 <div> 
  <pre><code>sudo python3 -m pip install --upgrade trzsz-libs trzsz-iterm2
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>同样也支持 Python2: 
  <div> 
   <div> 
    <pre><code>sudo pip install --upgrade trzsz-libs trzsz-iterm2
</code></pre> 
   </div> 
  </div> </li> 
 <li>安装后执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code><span> </span>应该输出<span> </span><code class="language-plaintext">/usr/local/bin/trzsz-iterm2</code>，如果不是： 
  <ul> 
   <li>执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code><span> </span>没有输出，检查前面安装的输出是不是有错误。</li> 
   <li>执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code><span> </span>输出另一个路径，可以建一个软链接：<br> <code class="language-plaintext">sudo ln -sv $(which trzsz-iterm2) /usr/local/bin/trzsz-iterm2</code></li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fiterm2.com%2Findex.html" target="_blank">iTerm2</a><span> </span>配置触发器</h3> 
<p style="color:#606c71; text-align:start">打开<span> </span><code class="language-plaintext">Preferences -> Profiles -> Advanced -> Triggers -> Edit</code>，如下配置：</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#606c71; display:block; font-family:"Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:17.6px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:832px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Name</th> 
   <th>Value</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Regular Expression</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">:(:TRZSZ:TRANSFER:[SR]:\d+\.\d+\.\d+)</code></td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Action</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">Run Silent Coprocess</code></td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Parameters</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">/usr/local/bin/trzsz-iterm2 \1</code></td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Enabled</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">✅ 勾上</td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Use interpolated strings for parameters</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">❎ 别勾</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#606c71; text-align:start"><img alt="iTerm2触发器配置" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/config.png?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">本地 macOS 安装<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fncruces%2Fzenity" target="_blank">zenity</a></h3> 
<p style="color:#606c71; text-align:start">安装在<span> </span><code class="language-plaintext">/usr/local/bin/zenity</code><span> </span>就可以显示进度条，不安装也可以正常使用。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><code>brew install ncruces/tap/zenity
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>安装后执行<span> </span><code class="language-plaintext">which zenity</code><span> </span>应该输出<span> </span><code class="language-plaintext">/usr/local/bin/zenity</code>，如果不是： 
  <ul> 
   <li>执行<span> </span><code class="language-plaintext">which zenity</code><span> </span>没有输出，检查前面安装的输出是不是有错误。</li> 
   <li>执行<span> </span><code class="language-plaintext">which zenity</code><span> </span>输出另一个路径，可以建一个软链接：<br> <code class="language-plaintext">sudo ln -sv $(which zenity) /usr/local/bin/zenity</code></li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">使用指南</h2> 
<h4 style="text-align:start"><code class="language-plaintext">trz</code><span> </span>上传文件</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz</code><span> </span>命令可以不带任何参数，将上传文件到当前目录。也可以带一个目录参数，指定上传到哪个目录。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><code>trz /tmp/
</code></pre> 
 </div> 
</div> 
<h4 style="text-align:start"><code class="language-plaintext">tsz</code><span> </span>下载文件</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">tsz</code><span> </span>可以带一个或多个文件名（可使用相对路径或绝对路径，也可使用通配符），将下载指定的文件。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><code>tsz file1 file2 file3
</code></pre> 
 </div> 
</div> 
<h4 style="text-align:start"><code class="language-plaintext">-q</code><span> </span>静默模式</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -q</code><span> </span>或<span> </span><code class="language-plaintext">tsz -q</code><span> </span>( 加上<span> </span><code class="language-plaintext">-q</code><span> </span>选项 )，则在传输文件时不显示进度条。</p> 
<h2 style="text-align:start">屏幕截图</h2> 
<h4 style="text-align:start">上传文件示例</h4> 
<p style="color:#606c71; text-align:start"><img alt="上传文件示例" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/upload.gif?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start">下载文件示例</h4> 
<p style="color:#606c71; text-align:start"><img alt="下载文件示例" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/download.gif?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">写在最后</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftrzsz.github.io%2F" target="_blank">trzsz</a><span> </span>主要在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">GitHub</a><span> </span>上进行开发，会在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Ftrzsz%2F" target="_blank">PyPI</a><span> </span>上发布，可以直接用 pip 进行安装。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">虽然源代码不在 gitee，但是如果有问题，也可以在 gitee 直接提<span> </span><a href="https://gitee.com/trzsz/trzsz/issues">Issues</a><span> </span>。</p>
                                        </div>
                                      
</div>
            