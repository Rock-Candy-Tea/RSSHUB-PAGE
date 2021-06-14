
---
title: 'Electron应用申请管理员权限'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f99ecf15c5b421197904dbf6fcd72a1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 06:58:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f99ecf15c5b421197904dbf6fcd72a1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p><code>Electron</code>是一款使用 <code>JavaScript</code>, <code>HTML</code> 和 <code>CSS</code> 等 <code>Web</code> 技术创建原生程序的框架,它内部集成了<code>Chromium</code> 和 <code>Node.js</code>.</p>
<p>前端工程师通过<code>Electron</code>相关技术,可以开发基于<code>Windows</code>、<code>Linux</code>以及<code>Mac</code>系统的客户端应用,这些能力拓展了前端所能触摸的边界,释放了更大的想象空间.</p>
<p>如果客户端应用仅仅局限于页面内容的展现和操作,通过<code>web</code>相关技术就可以实现.但由于<code>Electron</code>集成了<code>Node.js</code>,这便使开发的应用具备调用操作系统级别服务的能力.</p>
<p><code>Electron</code>调用某些操作系统的服务时,往往会受到系统权限的限制.比如在<code>Linux</code>系统下开发的程序,调用<code>shell</code>脚本命令时就需要在执行命令前面加上<code>sudo</code>,运行后再输入管理员密码,密码验证通过后脚本才能如期执行.</p>
<p><code>win10</code>操作系统以及<code>mac</code>系统对权限同样有着严格的把控.本文接下来将研究一下<code>Electron</code>应用如何在程序运行期间申请提权以及背后的实现原理.</p>
<h1 data-id="heading-1">实践</h1>
<p><code>Electron</code>应用运行期间想申请更高的执行权限,通过引用<code>githup</code>上的一个<code>js</code>库<code>sudo-prompt</code>就能轻松实现.</p>
<p><code>sudo-prompt</code>没有外部的依赖以及原生模块的绑定,是一段完全使用<code>nodejs</code>编写的脚本.</p>
<p><code>sudo-prompt</code>将<code>windows</code>、<code>Linux</code>以及<code>Mac</code>系统不同平台下对权限申请方式做了处理和封装,使<code>Electron</code>应用能支持多平台下的提权操作.接下来将演示一下<code>sudo-prompt</code>的使用方式,详情可点击访问 <a href="https://github.com/jorangreef/sudo-prompt" target="_blank" rel="nofollow noopener noreferrer">仓库地址</a>.</p>
<ul>
<li>
<p>项目根目录下执行 <code>npm install sudo-prompt --save</code> 安装依赖.</p>
</li>
<li>
<p>调用方式如下代码(当前最新版本<code>9.2.1</code>,如果版本不同请访问仓库地址查阅).</p>
</li>
</ul>
<p>创建一个对象<code>options</code>,属性名<code>name</code>(应用名称)可以自定义.但<code>name</code>只能为字母、数字和空格,最多不能超过<code>70</code>个字符.</p>
<p>最后使用 <code>sudo.exec('命令',...)</code> 执行命令.<code>sudo.exec</code>一执行就会弹出申请权限的窗口,用户输完密码进入回调函数,<code>stdout</code>为执行命令后的输出结果.</p>
<pre><code class="copyable">const sudo = require('sudo-prompt');
const options = &#123;
  name: 'Electron'
&#125;;
sudo.exec('echo hello', options,
  function(error, stdout, stderr) &#123;
    if (error) throw error;
    console.log('stdout: ' + stdout);
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Linux</code>图形界面的执行效果图如下:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f99ecf15c5b421197904dbf6fcd72a1~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">原理分析</h1>
<p><code>sudo-prompt</code>在不同平台下对权限做了不同的处理,接下来以<code>Linux</code>和<code>Windows</code>为例,探索一下它背后的实现原理.</p>
<h2 data-id="heading-3">Linux</h2>
<p>当前<code>Linux</code>系统有四大图形桌面环境,分别是<code>KDE</code>、<code>Gnome</code>、<code>Xfce</code>、<code>LXDE</code>.其中<code>KDE</code>和<code>Gnome</code>都包含了一系列标准的桌面工具和很多功能强大的应用软件,使用体验逐渐逼近<code>Windows</code>.<code>Xfce</code>和<code>LXDE</code>属于轻量级桌面环境.</p>
<p>这些桌面环境安装好后,一般默认会内置一些提升程序权限的指令,比如<code>KDE</code>图形界面默认内置<code>/usr/bin/kdesudo</code>,该路径下的<code>kdesudo</code>指令运行起来就能提示输入管理员密码,允许授权用户以其他身份执行程序.</p>
<p>同样其他桌面环境也如此,利用这些内置的指令程序就能顺利申请管理员权限运行.</p>
<p>具体做法可以先定义两个路径 <code>const paths = ['/usr/bin/kdesudo', '/usr/bin/pkexec']</code>,先在系统中去寻找这两个程序,看系统中包含哪一个就调用谁.</p>
<p>如果找到了<code>pkexec</code>,拼接字符串格式如下:</p>
<pre><code class="copyable"> '"/usr/bin/pkexec" --disable-internal-agent "/bin/bash" -c "echo SUDOPROMPT; echo hello"'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是<code>kdesudo</code>,,拼接字符串格式如下:</p>
<pre><code class="copyable"> '"/usr/bin/pkexec" --comment "Electron wants to make changes.Enter your password to allow this." -d -- /bin/bash -c "echo SUDOPROMPT; echo hello"'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串拼接好后,我们就可以利用<code>Node.js</code>的子进程<code>Process.child.exec</code>来执行上面的字符串命令.</p>
<p>如果执行后发现报错,错误信息为<code>No polkit authentication agent foun</code>. 那可能是因为<code>Linux</code>系统内<code>polkit</code>相关的服务没有安装或没启动起来.比如安装的轻量级桌面<code>xfce4</code>(<code>Ubuntu</code>系统)可能会缺少这个模块,可以采用以下两步来解决.</p>
<ul>
<li>安装<code>polkit</code> <code>sudo apt-get install policykit-1-gnome</code></li>
<li>启动服务 <code>/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &</code></li>
</ul>
<p>如果一切顺利,命令执行完后界面就会弹出输入密码框,只有当密码验证正确后才会执行上面拼接字符串的最后面的指令<code>echo hello</code>,这就是我们自定义希望获取系统权限后要执行的指令.</p>
<h2 data-id="heading-4">Windows</h2>
<p><code>Windows</code>系统下使用传统的<code>CMD</code>窗口去申请管理员的权限十分繁琐,但所幸有<code>PowerShell</code>的存在让一切都变的非常简单.</p>
<p><code>Windows PowerShell</code>是一种和<code>CMD</code>类似的命令行外壳程序,它可以使命令行用户和脚本编写者利用<code>.NET Framework</code>的强大功能完成想要的操作.从<code>Windows 7</code>开始系统就已经内置了<code>PowerShell</code>.</p>
<p>有了<code>PowerShell</code>的加持,我们可以先把想要系统去执行的命令封装成一个<code>command.bat</code>文件(代码如下).</p>
<pre><code class="copyable">@echo off
chcp 65001>nul
cd /d '/Users/kay/Desktop/demo/project'
echo hello
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>@echo off</code>关闭回显,不显示正在执行的批处理命令及执行的结果等.</li>
<li><code>chcp 65001</code>将命令行窗口活动代码页设置为<code>utf-8</code>格式</li>
<li><code>cd</code>切换到项目目录下</li>
<li><code>echo hello</code>是最终希望系统执行的命令</li>
</ul>
<p>以上字符可通过字符串的拼接的方式组合而成,再通过<code>Node.js</code>的<code>fs.writeFile</code>将字符串写入到<code>command.bat</code>文件中储存起来.</p>
<p>脚本文件准备好后,接下来拼接命令字符串如下:</p>
<pre><code class="copyable">powershell.exe Start-Process -FilePath '/Users/kay/Desktop/demo/project/command.bat' -WindowStyle hidden -Verb runAs
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>powershell</code>通过添加参数<code>-Verb runAs</code>就能为应用程序提权,从而执行<code>command.bat</code>里面的脚本代码.</p>
<p>字符串拼接好后,<code>Node.js</code>的子进程<code>Process.child.exec</code>执行字符串命令从而达到最终的目的.</p>
<h1 data-id="heading-5">总结</h1>
<p>综上所述,不管是<code>Windows</code>还是<code>Linux</code>系统,它们都会内置一些提权的程序.只要找到这些程序的调用方式以及相关参数的含义,就能顺利为<code>Electron</code>应用申请到管理员权限从而完目标操作.</p></div>  
</div>
            