
---
title: '兼容 tmux，类似 rz _ sz 的 trzsz 发布 1.0 正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MIT-green.svg?style=flat'
author: 开源中国
comments: false
date: Sat, 26 Mar 2022 15:27:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MIT-green.svg?style=flat'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">兼容 tmux，类似 rz / sz 的 trzsz ( trz / tsz ) 发布 1.0 正式版。</p> 
<ol> 
 <li>支持更多终端</li> 
 <li>支持文本进度条</li> 
 <li>支持默认保存路径</li> 
</ol> 
<hr> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trzsz</code><span> </span>( trz / tsz ) 是一个简单的文件传输工具，和 lrzsz ( rz / sz ) 类似，并且支持 tmux。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">GitHub:<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz">https://github.com/trzsz/trzsz</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fchoosealicense.com%2Flicenses%2Fmit%2F"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-green.svg?style=flat" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fpypi.python.org%2Fpypi%2Ftrzsz%2F"><img alt="PyPI trzsz" src="https://img.shields.io/pypi/v/trzsz?style=flat" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Ftrzsz.github.io%2Fcn%2F"><img alt="中文网站" src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-%E7%BD%91%E7%AB%99-blue?style=flat" referrerpolicy="no-referrer"></a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">为什么?</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">考虑<span> </span><code>laptop -> hostA -> hostB -> docker -> tmux</code><span> </span>这种场景，使用<span> </span><code>scp</code><span> </span>或<span> </span><code>sftp</code><span> </span>是不方便的。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在这种场景下，使用<span> </span><code>lrzsz</code><span> </span>( rz / sz ) 是很方便的，但是很可惜它与<span> </span><code>tmux</code><span> </span>不兼容。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>tmux</code><span> </span>不愿意支持 rz / sz (<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftmux%2Ftmux%2Fissues%2F906">906</a>,<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftmux%2Ftmux%2Fissues%2F1439">1439</a><span> </span>)，而重新造一个工具比修改<span> </span><code>tmux</code><span> </span>简单很多。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装指南</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">在远程服务器上安装</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">用 Python3 安装</p> 
  <div> 
   <div> 
    <pre><span>sudo python3 -m pip install --upgrade trzsz</span></pre> 
    <div style="text-align:center">
      
    </div> 
   </div> 
  </div> </li> 
 <li> <p style="margin-left:0; margin-right:0">用 Python2 安装</p> 
  <div> 
   <div> 
    <pre><span>sudo python2 -m pip install --upgrade trzsz</span></pre> 
    <div style="text-align:center">
      
    </div> 
   </div> 
  </div> </li> 
 <li> <p style="margin-left:0; margin-right:0">用 Homebrew 安装</p> 
  <div> 
   <div> 
    <pre><span>brew update</span>
<span>brew install trzsz</span></pre> 
    <div style="text-align:center">
      
    </div> 
   </div> 
  </div> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">  没有<span> </span><code>sudo</code><span> </span>权限也可以安装，只要将安装路径 ( 可能是<span> </span><code>~/.local/bin</code><span> </span>) 添加到<span> </span><code>PATH</code><span> </span>环境变量中即可。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">支持的终端</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/link?target=https%3A%2F%2Fiterm2.com%2F">iTerm2</a><span> </span>-- 参考<span> </span><a href="https://gitee.com/trzsz/trzsz/blob/master/iterm2.md">Trzsz-iTerm2 安装文档</a>。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/link?target=https%3A%2F%2Ftabby.sh%2F">tabby</a><span> </span>-- 安装<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftabby-trzsz">tabby-trzsz</a><span> </span>插件即可。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/link?target=https%3A%2F%2Felecterm.github.io%2Felecterm%2F">electerm</a><span> </span>-- 升级到<span> </span><code>1.19.0</code><span> </span>以上的版本即可。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftrzsz%2Ftrzsz.js">trzsz.js</a><span> </span>-- 让运行在浏览器中的 webshell 和用 electron 开发的终端支持<span> </span><code>trzsz</code>。</p> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">  <em>如果你的终端也支持<span> </span><code>trzsz</code>，请告诉我，我很乐意将它加到此列表中。</em></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">使用指南</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>trz</code><span> </span>上传文件</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz</code><span> </span>命令可以不带任何参数，将上传文件到当前目录。也可以带一个目录参数，指定上传到哪个目录。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>trz /tmp/</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>tsz</code><span> </span>下载文件</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>tsz</code><span> </span>可以带一个或多个文件名（可使用相对路径或绝对路径，也可使用通配符），将下载指定的文件。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>tsz file1 file2 file3</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-q</code><span> </span>静默模式</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz -q</code><span> </span>或<span> </span><code>tsz -q xxx</code><span> </span>( 加上<span> </span><code>-q</code><span> </span>选项 )，则在传输文件时不显示进度条。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-y</code><span> </span>覆盖模式</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz -y</code><span> </span>或<span> </span><code>tsz -y xxx</code><span> </span>( 加上<span> </span><code>-y</code><span> </span>选项 )，如果存在相同文件名的文件就直接覆盖。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-b</code><span> </span>二进制模式</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz -b</code><span> </span>或<span> </span><code>tsz -b xxx</code><span> </span>( 加上<span> </span><code>-b</code><span> </span>选项 )，二进制传输模式，对于压缩包、图片、影音等较快。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-e</code><span> </span>转义控制字符</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">二进制模式时，控制字符可能会导致失败，<code>trz -eb</code><span> </span>或<span> </span><code>tsz -eb xxx</code><span> </span>( 加上<span> </span><code>-e</code><span> </span>选项 ) 转义所有已知的控制字符。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-B</code><span> </span>缓冲区大小</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz -B 10k</code><span> </span>或<span> </span><code>tsz -B 2M xxx</code><span> </span>等，设置缓存区大小 ( 默认 1M )。太小可能会导致传输速度慢，太大可能会导致进度条更新不及时。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><code>-t</code><span> </span>超时时间</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>trz -t 10</code><span> </span>或<span> </span><code>tsz -t 30 xxx</code><span> </span>等，设置超时秒数 ( 默认 100 秒 )。在超时时间内，如果无法传完一个缓冲区大小的数据则会报错并退出。设置为 0 或负数，则永不超时。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">异常处理方法</h4> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">如果<span> </span><code>tmux</code><span> </span>不是运行在远程服务器上，而是运行在本地电脑上，或者运行在中间的跳板机上。</p> 
  <ul> 
   <li>因为<span> </span><code>trzsz</code><span> </span>在远程服务器上找不到<span> </span><code>tmux</code><span> </span>进程，所以只支持<span> </span><code>tmux -CC</code><span> </span>控制模式。</li> 
   <li>关于<span> </span><code>tmux -CC</code><span> </span>控制模式的用法，请参考<span> </span><a href="https://gitee.com/trzsz/trzsz/blob/master/tmuxcc.md">iTerm2 与 tmux -CC 集成</a>。</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果出现了错误，且<span> </span><code>trzsz</code><span> </span>挂住不能动了：</p> 
  <ul> 
   <li>按组合键<span> </span><code>control + c</code><span> </span>可以停止服务器上的<span> </span><code>trz</code><span> </span>或<span> </span><code>tsz</code><span> </span>进程。</li> 
   <li>对于 iTerm2 用户，按组合键<span> </span><code>command + option + shift + r</code><span> </span>可以停止<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fiterm2.com%2Fdocumentation-coprocesses.html">iTerm2 Coprocesses</a>。</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果<span> </span><code>trz -b</code><span> </span>二进制上传失败，并且登录远程服务器时使用了<span> </span><code>telnet</code><span> </span>或<span> </span><code>docker exec</code>：</p> 
  <ul> 
   <li>可以试试转义所有控制字符，例如<span> </span><code>trz -eb</code>。</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果<span> </span><code>trz -b</code><span> </span>二进制上传失败，并且远程服务器使用 Python3 ( 版本小于 3.7 )：</p> 
  <ul> 
   <li>Python3 ( 版本小于 3.7 ) 支持 base64 模式，不使用<span> </span><code>-b</code><span> </span>选项即可，使用<span> </span><code>trz</code><span> </span>代替。</li> 
   <li>如果想用<span> </span><code>trz -b</code><span> </span>二进制上传，则需要升级 Python3 到 3.7 以上的版本，或者使用 Python2。</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">如果<span> </span><code>trz -b</code><span> </span>或<span> </span><code>tsz -b</code><span> </span>二进制传输失败，并且登录远程服务器时使用了<span> </span><code>expect</code>：</p> 
  <ul> 
   <li>可以试试在<span> </span><code>expect</code><span> </span>脚本前设置环境变量<span> </span><code>export LC_CTYPE=C</code>，例如： 
    <div> 
     <div> 
      <pre><span>#!/bin/sh</span>
<span>export LC_CTYPE=C</span>
<span>expect -c '</span>
<span>  spawn ssh xxx</span>
<span>  expect "xxx: "</span>
<span>  send "xxx\n"</span>
<span>  interact</span>
<span>'</span></pre> 
      <div style="text-align:center">
        
      </div> 
     </div> 
    </div> </li> 
  </ul> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">屏幕截图</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">trzsz 在 iTerm2 中 text 进度条示例</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="using trzsz in iTerm2 with text progress bar" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/iterm2_text.gif" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">trzsz 在 iTerm2 中 zenity 进度条示例</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="using trzsz in iTerm2 with zenity progress bar" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/iterm2_zenity.gif" referrerpolicy="no-referrer"></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">trzsz 在 tabby 中 tabby-trzsz 插件示例</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="using trzsz in tabby with tabby-trzsz plugin" src="https://gitee.com/trzsz/trzsz/raw/master/screen-shot/tabby_trzsz.gif" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            