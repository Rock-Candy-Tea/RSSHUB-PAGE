
---
title: '支持 tmux，类似 rz _ sz 的 trzsz 发布 0.3.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/trzsz/trzsz/raw/master/screen-shot/config.jpg?raw=true'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 00:42:00 GMT
thumbnail: 'https://gitee.com/trzsz/trzsz/raw/master/screen-shot/config.jpg?raw=true'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">tmux 不支持 rz / sz ，于是有一个兼容 tmux 的 trz / tsz ( </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz" target="_blank">trzsz</a><span style="background-color:#ffffff; color:#333333"> )，</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">可以与 iTerm2 一起用，还有一个不错的进度条。</span></p> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0">已发布 0.3.1 版本：<br> 1、支持 ctrl + c 优雅退出。<br> 2、支持 kill -SIGTERM 优雅终止。</p> 
</div> 
<hr> 
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
 <li>没有<span> </span><code class="language-plaintext">sudo</code><span> </span>权限也可以安装，但是要将安装路径 ( 可能是<span> </span><code class="language-plaintext">~/.local/bin</code><span> </span>) 添加到 PATH 环境变量中。</li> 
 <li>安装后执行<span> </span><code class="language-plaintext">trz -v</code><span> </span>或<span> </span><code class="language-plaintext">tsz -v</code>，如果输出 trzsz 的版本号就是安装成功了，否则检查前面安装的输出是不是有错误。</li> 
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
 <li>安装后执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code>，如果输出<span> </span><code class="language-plaintext">/usr/local/bin/trzsz-iterm2</code><span> </span>就是安装成功了，如果不是： 
  <ul> 
   <li>执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code><span> </span>没有输出，检查前面安装的输出是不是有错误。</li> 
   <li>执行<span> </span><code class="language-plaintext">which trzsz-iterm2</code><span> </span>输出另一个路径，可以建一个软链接：<br> <code class="language-plaintext">sudo ln -sv $(which trzsz-iterm2) /usr/local/bin/trzsz-iterm2</code></li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fiterm2.com%2Findex.html" target="_blank">iTerm2</a><span> </span>配置触发器</h3> 
<p style="color:#606c71; text-align:start">打开<span> </span><code class="language-plaintext">Preferences -> Profiles -> Advanced -> Triggers -> Edit</code>，如下配置：</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#606c71; display:block; font-family:"Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:17.6px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; orphans:2; overflow:auto; text-align:start; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:896px; word-break:keep-all; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>Name</th> 
   <th>Value</th> 
   <th>Note</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Regular Expression</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">:(:TRZSZ:TRANSFER:[SR]:\d+\.\d+\.\d+:\d+)</code></td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">前后无空格</td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Action</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">Run Silent Coprocess</code></td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Parameters</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px"><code class="language-plaintext">/usr/local/bin/trzsz-iterm2 \1</code></td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">前后无空格</td> 
  </tr> 
  <tr> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">Enabled</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">✅</td> 
   <td style="border-color:#e9ebec; border-style:solid; border-width:1px">选中</td> 
  </tr> 
 </tbody> 
</table> 
<ul> 
 <li> <p>不要选中最下面的<span> </span><code class="language-plaintext">Use interpolated strings for parameters</code>。</p> </li> 
 <li> <p>不同 Profile 的 Trigger 是互相独立的，也就是每个用到的 Profile 都要进行配置。</p> </li> 
 <li> <p>iTerm2 Trigger 的配置允许输入多行，但只显示一行，注意不要复制了一个换行符进去。</p> </li> 
</ul> 
<p style="color:#606c71; text-align:start"><img alt="iTerm2触发器配置" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/config.jpg?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">本地 macOS 安装<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fncruces%2Fzenity" target="_blank">zenity</a></h3> 
<p style="color:#606c71; text-align:start">安装在<span> </span><code class="language-plaintext">/usr/local/bin/zenity</code><span> </span>就可以显示进度条，不安装也可以正常使用。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><code>brew install ncruces/tap/zenity
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>如果<span> </span><code class="language-plaintext">Mac M1</code><span> </span>安装失败，可以试试用<span> </span><code class="language-plaintext">go</code><span> </span>进行编译安装： 
  <div> 
   <div> 
    <pre><code>brew install go
go install 'github.com/ncruces/zenity/cmd/zenity@latest'
sudo cp ~/go/bin/zenity /usr/local/bin/zenity
</code></pre> 
   </div> 
  </div> </li> 
 <li>安装后执行<span> </span><code class="language-plaintext">which zenity</code>，如果输出<span> </span><code class="language-plaintext">/usr/local/bin/zenity</code><span> </span>就是安装成功了，如果不是： 
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
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -q</code><span> </span>或<span> </span><code class="language-plaintext">tsz -q xxx</code><span> </span>( 加上<span> </span><code class="language-plaintext">-q</code><span> </span>选项 )，则在传输文件时不显示进度条。</p> 
<h4 style="text-align:start"><code class="language-plaintext">-y</code><span> </span>覆盖模式</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -y</code><span> </span>或<span> </span><code class="language-plaintext">tsz -y xxx</code><span> </span>( 加上<span> </span><code class="language-plaintext">-y</code><span> </span>选项 )，如果存在相同文件名的文件就直接覆盖。</p> 
<h4 style="text-align:start"><code class="language-plaintext">-b</code><span> </span>二进制模式</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -b</code><span> </span>或<span> </span><code class="language-plaintext">tsz -b xxx</code><span> </span>( 加上<span> </span><code class="language-plaintext">-b</code><span> </span>选项 )，二进制传输模式，对于压缩包、图片、影音等较快。</p> 
<h4 style="text-align:start"><code class="language-plaintext">-e</code><span> </span>转义控制字符</h4> 
<p style="color:#606c71; text-align:start">二进制传输模式时，控制字符可能会导致传输失败，<code class="language-plaintext">trz -eb</code><span> </span>或<span> </span><code class="language-plaintext">tsz -eb xxx</code><span> </span>( 加上<span> </span><code class="language-plaintext">-e</code><span> </span>选项 ) 转义所有已知的控制字符。</p> 
<h4 style="text-align:start"><code class="language-plaintext">-B</code><span> </span>缓冲区大小</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -B 10k</code><span> </span>或<span> </span><code class="language-plaintext">tsz -B 2M xxx</code><span> </span>等，设置缓存区大小 ( 默认 1M )。太小会导致传输速度慢，太大会导致进度条更新不及时。</p> 
<h4 style="text-align:start"><code class="language-plaintext">-t</code><span> </span>超时时间</h4> 
<p style="color:#606c71; text-align:start"><code class="language-plaintext">trz -t 10</code><span> </span>或<span> </span><code class="language-plaintext">tsz -t 30 xxx</code><span> </span>等，设置超时秒数 ( 默认 100 秒 )。在超时时间内，如果无法传完一个缓冲区大小的数据则会报错并退出。设置为 0 或负数，则永不超时。</p> 
<h4 style="text-align:start">异常处理方法</h4> 
<ul> 
 <li>如果<span> </span><code class="language-plaintext">tmux</code><span> </span>不是运行在远程服务器上，而是运行在本地 mac 上，或者运行在中间的跳板机上。 
  <ul> 
   <li>因为<span> </span><code class="language-plaintext">trzsz</code><span> </span>在远程服务器上找不到<span> </span><code class="language-plaintext">tmux</code><span> </span>进程，需要使用<span> </span><code class="language-plaintext">tmux -CC</code><span> </span>控制模式才可以。</li> 
   <li>关于<span> </span><code class="language-plaintext">tmux -CC</code><span> </span>控制模式的用法，请参考<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fc58cf33514bb" target="_blank">iTerm2 与 tmux -CC 集成</a>。</li> 
  </ul> </li> 
 <li>如果出现了错误，且<span> </span><code class="language-plaintext">trzsz</code><span> </span>挂住不能动了： 
  <ul> 
   <li>按组合键<span> </span><code class="language-plaintext">command + option + shift + r</code><span> </span>停止<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fiterm2.com%2Fdocumentation-coprocesses.html" target="_blank">iTerm2 Coprocesses</a>。</li> 
   <li>按组合键<span> </span><code class="language-plaintext">control + c</code><span> </span>停止服务器上的<span> </span><code class="language-plaintext">trz</code><span> </span>或<span> </span><code class="language-plaintext">tsz</code><span> </span>进程。</li> 
  </ul> </li> 
 <li>如果<span> </span><code class="language-plaintext">trz -b</code><span> </span>二进制上传失败，并且登录远程服务器时使用了<span> </span><code class="language-plaintext">telnet</code><span> </span>或<span> </span><code class="language-plaintext">docker exec</code>： 
  <ul> 
   <li>可以试试转义所有控制字符，例如<span> </span><code class="language-plaintext">trz -eb</code>。</li> 
  </ul> </li> 
 <li>如果<span> </span><code class="language-plaintext">trz -b</code><span> </span>二进制上传失败，并且远程服务器使用 Python3 ( 版本小于 3.7 )： 
  <ul> 
   <li>Python3 ( 版本小于 3.7 ) 支持 base64 模式，不使用<span> </span><code class="language-plaintext">-b</code><span> </span>选项即可，使用<span> </span><code class="language-plaintext">trz</code><span> </span>代替。</li> 
   <li>如果想用<span> </span><code class="language-plaintext">trz -b</code><span> </span>二进制上传，则需要升级 Python3 到 3.7 以上的版本，或者使用 Python2。</li> 
  </ul> </li> 
 <li>如果<span> </span><code class="language-plaintext">trz -b</code><span> </span>或<span> </span><code class="language-plaintext">tsz -b</code><span> </span>二进制传输失败，并且登录远程服务器时使用了<span> </span><code class="language-plaintext">expect</code>： 
  <ul> 
   <li>可以试试在<span> </span><code class="language-plaintext">expect</code><span> </span>脚本前设置环境变量<span> </span><code class="language-plaintext">export LC_CTYPE=C</code>，例如： 
    <div> 
     <div> 
      <pre><code>#!/bin/sh
export LC_CTYPE=C
expect -c '
  spawn ssh xxx
  expect "xxx: "
  send "xxx\n"
  interact
'
</code></pre> 
     </div> 
    </div> </li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">屏幕截图</h2> 
<h4 style="text-align:start">上传文件示例</h4> 
<p style="color:#606c71; text-align:start"><img alt="上传文件示例" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/upload.gif?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:start">下载文件示例</h4> 
<p style="color:#606c71; text-align:start"><img alt="下载文件示例" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/download.gif?raw=true" style="margin-top:0px" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            