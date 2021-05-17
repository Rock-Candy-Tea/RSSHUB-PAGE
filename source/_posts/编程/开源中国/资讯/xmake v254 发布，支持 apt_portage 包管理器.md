
---
title: 'xmake v2.5.4 发布，支持 apt_portage 包管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5523'
author: 开源中国
comments: false
date: Mon, 17 May 2021 13:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5523'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">xmake</a> 是一个基于 Lua 的轻量级跨平台构建工具，使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="text-align:start">在 2.5.4 版本中，我们新增了对 Apt、Portage 这两个包管理器的支持，在 Ubuntu/Gentoo 上我们也可以使用 <code>add_requires</code> 可以快速集成它们提供的包。</p> 
<p style="text-align:start">并且我们也改进支持了 Vcpkg 包管理器的支持，新增对 arm/arm64 架构包的安装支持。</p> 
<p style="text-align:start">另外，我们还增强了 <code>xrepo env shell</code> 环境，可以通过在 <code>xmake.lua</code> 中配置一系列 <code>add_requires</code> 包配置，加载带有特定包配置的 shell 环境。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="text-align:start">新特性介绍</h2> 
<h3 style="text-align:start">新的包管理器支持</h3> 
<h4 style="text-align:start">添加 ubuntu/apt 的依赖包</h4> 
<p style="text-align:start">现在我们支持使用 apt 集成依赖包，也会自动查找 ubuntu 系统上已经安装的包。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"apt::zlib1g-dev"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">alias</span> <strong>=</strong> <span style="color:#ff00ff">"zlib"</span><strong>&#125;)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"zlib"</span><strong>)</strong>
</code></pre> 
</div> 
<h4 style="text-align:start">添加 gentoo/portage 的依赖包</h4> 
<p style="text-align:start">我们也支持了使用 Portage 集成依赖包，并且也会自动查找 Gentoo 系统上已经安装的包。</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"portage::libhandy"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">alias</span> <strong>=</strong> <span style="color:#ff00ff">"libhandy"</span><strong>&#125;)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"libhandy"</span><strong>)</strong>
</code></pre> 
</div> 
<h4 style="text-align:start">从 Vcpkg 集成 arm/arm64 架构包</h4> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"vcpkg::zlib"</span><strong>,</strong> <strong>&#123;</strong><span style="color:#000000">alias</span> <strong>=</strong> <span style="color:#ff00ff">"zlib"</span><strong>&#125;)</strong>

<span style="color:#000000">target</span><strong>(</strong><span style="color:#ff00ff">"test"</span><strong>)</strong>
    <span style="color:#000000">set_kind</span><strong>(</strong><span style="color:#ff00ff">"binary"</span><strong>)</strong>
    <span style="color:#000000">add_files</span><strong>(</strong><span style="color:#ff00ff">"src/*.c"</span><strong>)</strong>
    <span style="color:#000000">add_packages</span><strong>(</strong><span style="color:#ff00ff">"zlib"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">配置方式还是跟之前的相同，只需要切换到 arm/arm64 架构编译就可以自动从 Vcpkg 拉取 arm/arm64 的包。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xmake</span> f -a arm64
<u>$ </u><span style="color:black">xmake</span>
</code></pre> 
</div> 
<h4 style="text-align:start">支持导入导出安装包</h4> 
<p style="text-align:start">通常，我们使用 xrepo 命令或者 xmake 去安装完包后，如果相同的项目迁移到其他机器编译，那就要重新下载安装包。</p> 
<p style="text-align:start">为了提高开发效率，现在 xrepo 可以快速导出已经安装后的包，包括对应的库文件，头文件等等。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> export -o /tmp/output zlib
</code></pre> 
</div> 
<p style="text-align:start">然后我们也可以在其他机器上导入之前导出的安装包，实现包的迁移。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> import -i /xxx/packagedir zlib
</code></pre> 
</div> 
<p style="text-align:start">导入后，对应项目编译会直接使用它们，不再额外重新安装包。</p> 
<h4 style="text-align:start">特定包 shell 环境支持</h4> 
<p style="text-align:start">xrepo 有个 <code>xrepo env</code> 命令，可以指定加载特定包的环境，然后运行特定程序，例如加载 luajit 包的安装环境，然后运行 luajit：</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> env luajit
</code></pre> 
</div> 
<p style="text-align:start">或者绑定特定 luajit 版本包环境，加载 bash 后，就可以直接运行对应的 lujit。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> env -b "luajit 5.1" bash
> luajit --version
</code></pre> 
</div> 
<p style="text-align:start">但是，这样有个问题，如果我们安装的包很多，不同的包配置和版本都还不同，如果我们想加载一个 bash，并且同时带有多个包的环境。</p> 
<p style="text-align:start">那么，之前的方式就无法支持了，因此，新版本中，我们对其进一步改进，是的可以通过在当前目录下，添加 xmake.lua 文件，定制化一些包配置，然后进入特定的包 shell 环境。</p> 
<p style="text-align:start">xmake.lua</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"zlib 1.2.11"</span><strong>)</strong>
<span style="color:#000000">add_requires</span><strong>(</strong><span style="color:#ff00ff">"python 3.x"</span><strong>,</strong> <span style="color:#ff00ff">"luajit"</span><strong>)</strong>
</code></pre> 
</div> 
<p style="text-align:start">比如上面这样，我们通过在 xmake.lua 中配置了三个包，想在 shell 中同时使用它们，那么只需要在当前目录下运行下面的命令就行了。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> env shell
> python --version
> luajit --version
</code></pre> 
</div> 
<p style="text-align:start">需要注意的是，这里我们使用了 <code>xrepo env shell</code> 而不是 <code>xrepo env bash</code>，是因为 bash 只能在特定平台使用，而 <code>xrepo env shell</code> 属于内置命令。</p> 
<p style="text-align:start">它可以自动检测当前用的终端环境，加载对应的 bash, sh, zsh 以及 windows 下的 cmd 或者 powershell 环境，这一切都是自动的。</p> 
<p style="text-align:start">另外，我们还加了一些辅助特性，比如 prompt 提示，<code>xrepo env quit</code> 环境退出命令，历史输入命令切换等等。</p> 
<h4 style="text-align:start">设置镜像加速包下载</h4> 
<p style="text-align:start">为了改进国内网络环境下载包慢的问题，xmake 是支持代理设置的，还可以支持 pac.lua 代理配置策略。</p> 
<p style="text-align:start">而新版本中，我们对 pac.lua 配置进行了改进，进一步支持配置镜像代理规则，比如对所有 github.com 域名的访问切到 hub.fastgit.org 域名，实现加速下载包。</p> 
<p style="text-align:start">pac.lua 配置：</p> 
<div style="text-align:start"> 
 <pre><code><span style="color:blue">function</span> <span style="color:black">mirror</span><strong>(</strong><span style="color:#000000">url</span><strong>)</strong>
     <span style="color:blue">return</span> <span style="color:#000000">url</span><strong>:</strong><span style="color:#000000">gsub</span><strong>(</strong><span style="color:#ff00ff">"github.com"</span><strong>,</strong> <span style="color:#ff00ff">"hub.fastgit.org"</span><strong>)</strong>
<span style="color:blue">end</span>
</code></pre> 
</div> 
<p style="text-align:start">然后我们设置次 pac.lua 文件，默认路径在 <code>~/.xmake/pac.lua</code>。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xmake</span> g --proxy_pac=/tmp/pac.lua
</code></pre> 
</div> 
<p style="text-align:start">然后，我们安装包的时候，如果遇到 github.com 域名下的包源，下载时候会自动切到 fastgit 镜像加速下载。</p> 
<div style="text-align:start"> 
 <pre><code><u>$ </u><span style="color:black">xrepo</span> install libpng
> curl https://hub.fastgit.org/glennrp/libpng/archive/v1.6.37.zip -o v1.6.37.zip
</code></pre> 
</div> 
<h4 style="text-align:start">自定义切换包存储目录</h4> 
<p style="text-align:start">之前我们只能通过 <code>xmake g --pkg_installdir=/tmp/xx</code> 来配置修改默认的包安装目录。</p> 
<p style="text-align:start">现在，我们也可以通过 <code>XMAKE_PKG_INSTALLDIR</code> 环境变量也修改它，默认路径在：<code>~/.xmake/packages</code>。</p> 
<p style="text-align:start">另外，我们还额外添加了 <code>XMAKE_PKG_CACHEDIR</code> 环境变量来修改包的缓存目录，默认路径在：<code>~/.xmake/cache/packages</code>。</p> 
<h2 style="text-align:start">更新内容</h2> 
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1323" target="_blank">#1323</a>: 支持从 apt 查找安装包，<code>add_requires("apt::zlib1g-dev")</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1337" target="_blank">#1337</a>: 添加环境变量去改进包安装和缓存目录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1338" target="_blank">#1338</a>: 支持导入导出已安装的包</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1087" target="_blank">#1087</a>: 添加 <code>xrepo env shell</code> 并且支持从 <code>add_requires/xmake.lua</code> 加载包环境</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1313" target="_blank">#1313</a>: 为 <code>add_requires/add_deps</code> 添加私有包支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1358" target="_blank">#1358</a>: 支持设置镜像 url 站点加速包下载</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1369" target="_blank">#1369</a>: 为 vcpkg 增加 arm/arm64 包集成支持，感谢 @fallending</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F1405" target="_blank">#1405</a>: 添加 portage 包管理器支持，感谢 @Phate6660</li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li>改进 <code>find_package</code> 并且添加 <code>package:find_package</code> 接口在包定义中方便查找包</li> 
 <li>移除废弃的 <code>set_config_h</code> 和 <code>set_config_h_prefix</code> 接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1343" target="_blank">#1343</a>: 改进搜索本地包文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1347" target="_blank">#1347</a>: 针对 binary 包改进 vs_runtime 配置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1353" target="_blank">#1353</a>: 改进 del_files() 去加速匹配文件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1349" target="_blank">#1349</a>: 改进 xrepo env shell 支持，更好的支持 powershell</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1380" target="_blank">#1380</a>: 修复 <code>add_packages()</code> 失败问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1381" target="_blank">#1381</a>: 修复添加本地 git 包源问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F1391" target="_blank">#1391</a>: 修复 cuda/nvcc 工具链</li> 
</ul>
                                        </div>
                                      
</div>
            