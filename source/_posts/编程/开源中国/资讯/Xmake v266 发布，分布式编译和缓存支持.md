
---
title: 'Xmake v2.6.6 发布，分布式编译和缓存支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=978'
author: 开源中国
comments: false
date: Thu, 26 May 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=978'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">Xmake</a><span> </span>是一个基于 Lua 的轻量级跨平台构建工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它非常的轻量，没有任何依赖，因为它内置了 Lua 运行时。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">它使用 xmake.lua 维护项目构建，相比 makefile/CMakeLists.txt，配置语法更加简洁直观，对新手非常友好，短时间内就能快速入门，能够让用户把更多的精力集中在实际的项目开发上。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们能够使用它像 Make/Ninja 那样可以直接编译项目，也可以像 CMake/Meson 那样生成工程文件，另外它还有内置的包管理系统来帮助用户解决 C/C++ 依赖库的集成使用问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前，Xmake 主要用于 C/C++ 项目的构建，但是同时也支持其他 native 语言的构建，可以实现跟 C/C++ 进行混合编译，同时编译速度也是非常的快，可以跟 Ninja 持平。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake = Build backend + Project Generator + Package Manager + [Remote|Distributed] Build + Cache
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">尽管不是很准确，但我们还是可以把 Xmake 按下面的方式来理解：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>Xmake ~= Make/Ninja + CMake/Meson + Vcpkg/Conan + distcc + ccache/sccache
</code></pre> 
</div> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake" target="_blank">项目源码</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2F" target="_blank">官方文档</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fxmake.io%2F%23%2Fzh-cn%2Fabout%2Fcourse" target="_blank">入门课程</a></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">新特性介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这个版本，我们增加了大量的重量级新特性：</p> 
<ul> 
 <li>分布式编译支持</li> 
 <li>内置本地编译缓存</li> 
 <li>远程编译缓存支持</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">通过这些特性，我们可以更加快速地编译大型 C/C++ 项目。另外，它们完全是跨平台的，不仅支持 gcc/clang 也支持 msvc，而且除了编译器无任何第三方依赖，使用也非常方便。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">因此，使用了 Xmake，就等于同时使用了<span> </span><code>distcc/ccache/sccache</code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相比这些第三方的工具，Xmake 完全支持 Windows 和 msvc，在消除了平台差异性的同事，也省去了独立进程调用，以及额外的守护进程带来的开销。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">除了这些特性之外，新版本 Xmake 还新增 Keil/c51 项目的编译支持，以及对 nvidia-hpc-sdk 工具链中的 nvc/nvc++/nvfortran 编译器的支持。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">远程编译支持用户认证</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">上个版本我们已经初步支持了远程编译，但是没有提供用户认证支持，这会带来一些安全性问题，因此这个版本，我们新增了用户认证支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">目前，Xmake 主要提供以下几种认证机制，另外，它对分布式编译和远程缓存也同样生效。</p> 
<ol> 
 <li>Token 认证</li> 
 <li>密码认证</li> 
 <li>可信主机验证</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:start">Token 认证</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这也是我们默认推荐的方式，更加安全，配置和连接也更加方便，每次连接也不用输入密码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们在执行<span> </span><code>xmake service</code><span> </span>命令时候，默认就会生成一个服务端和客户端的配置文件，并且自动生成一个默认的 token，因此本地直连是不需要任何配置的。</p> 
<p>服务端认证配置</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">服务端可以配置多个 token 用于对不同用户主机进行授权连接，当然也可以共用一个 token。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    remote_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9691"</span>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/remote_build"</span>
    <strong style="color:black">&#125;</strong>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"e438d816c95958667747c318f1532c0f"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p>客户端认证配置</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">客户端只需要添加服务器上的 token 到对应的客户端配置中即可。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/client.conf
<strong style="color:black">&#123;</strong>
    remote_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        connect <strong style="color:black">=</strong> <span style="color:#ff00ff">"127.0.0.1:9691"</span>,
        token <strong style="color:black">=</strong> <span style="color:#ff00ff">"e438d816c95958667747c318f1532c0f"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p>手动生成新 token</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以执行下面的命令，手动生成一个新的 token，自己添加到服务器配置中。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --gen-token
New token a7b9fc2d3bfca1472aabc38bb5f5d612 is generated!
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">密码认证</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也提供密码认证的授权模式，相比 token 认证，它需要用户每次连接的时候，输入密码，验证通过后，才能连接上。</p> 
<p>服务端认证配置</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">密码认证，我们不需要手动配置 token，只需要执行下面的命令，添加用户就行了，添加过程中，会提示用户输入密码。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --add-user<strong style="color:black">=</strong>ruki
Please input user ruki password:
123456
Add user ruki ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，xmake 就会通过用户名，密码生成一个新的 token 添加到服务器配置的 token 列表中去。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    remote_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9691"</span>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/remote_build"</span>
    <strong style="color:black">&#125;</strong>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"e438d816c95958667747c318f1532c0f"</span>,
        <span style="color:#ff00ff">"7889e25402413e93fd37395a636bf942"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">当然，我们也可以删除指定的用户和密码。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">$xmake</span> service --rm-user<strong style="color:black">=</strong>ruki
Please input user ruki password:
123456
Remove user ruki ok!
</code></pre> 
</div> 
<p>客户端认证配置</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">对于客户端，我们不再需要设置服务器的 token 了，只需要在连接配置中，追加需要连接的用户名即可开启密码认证，格式：<code>user@address:port</code></p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/client.conf
<strong style="color:black">&#123;</strong>
    remote_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        connect <strong style="color:black">=</strong> <span style="color:#ff00ff">"root@127.0.0.1:9691"</span>
  <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">!> 如果去掉用户名，也没配置 token，那就是匿名模式，如果服务器也没配置 token，就是完全禁用认证，直接连接。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">可信主机验证</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，为了更进一步提高安全性，我们还提供了服务端可信主机验证，如果在服务器配置的 known_hosts 列表中，配置了可以连接的客户端主机 ip 地址， 那么只有这些主机可以成功连接上这台服务器，其他主机对它的连接都会被提示为不可信而拒绝连接，即使 token 和密码认证都没问题也不行。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/logs.txt"</span>,
    server <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
            <span style="color:#ff00ff">"4b928c7563a0cba10ff4c3f5ca0c8e24"</span>
        <strong style="color:black">&#125;</strong>,
        known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <span style="color:#ff00ff">"127.0.0.1"</span>, <span style="color:#ff00ff">"xx.xx.xx.xx"</span><strong style="color:black">&#125;</strong>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">连接远程的服务器</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">接下来，我们只需要进入需要远程编译的工程根目录，执行<span> </span><code>xmake service --connect</code><span> </span>命令，进行连接。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果是 token 认证模式，那么不需要的额外的密码输入，直接连接。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> create test
</span><u>$ </u><span style="color:black">cd</span><span> test
</span><u>$ </u><span style="color:black">xmake</span><span> service --connect
</span><remote_build_client>: connect 192.168.56.110:9091 ..
<remote_build_client>: connected!
<remote_build_client>: sync files in 192.168.56.110:9091 ..
Scanning files ..
Comparing 3 files ..
    [+]: src/main.cpp
    [+]: .gitignore
    [+]: xmake.lua
3 files has been changed!
Archiving files ..
Uploading files with 1372 bytes ..
<remote_build_client>: sync files ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果是密码认证，那么会提示用户输入密码，才能继续连接。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --connect
Please input user root password:
000000
<remote_build_client>: connect 127.0.0.1:9691 ..
<remote_build_client>: connected!
<remote_build_client>: sync files <span style="color:blue">in </span>127.0.0.1:9691 ..
Scanning files ..
Comparing 3 files ..
    <strong style="color:black">[</strong>+]: xmake.lua
    <strong style="color:black">[</strong>+]: .gitignore
    <strong style="color:black">[</strong>+]: src/main.cpp
3 files has been changed!
Archiving files ..
Uploading files with 1591 bytes ..
<remote_build_client>: sync files ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果密码不对，就会提示错误。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --connect
Please input user root password:
123
<remote_build_client>: connect 127.0.0.1:9691 ..
<remote_build_client>: connect 127.0.0.1:9691 failed, user and password are incorrect!
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">分布式编译支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">Xmake 提供了内置的分布式编译服务，通常它可以跟 本地编译缓存，远程编译缓存 相互配合，实现最优的编译的加速。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，它是完全跨平台支持，我们不仅支持 gcc/clang，也能够很好地支持 Windows 和 msvc。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">对于交叉编译，只要交叉工具链支持，我们不要求服务器的系统环境，即使混用 linux, macOS 和 Windows 的服务器资源，也可以很好的实现分布式编译。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">开启服务</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以指定<span> </span><code>--distcc</code><span> </span>参数来开启分布式编译服务，当然如果不指定这个参数，xmake 会默认开启所有服务端配置的服务。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --distcc
</span><distcc_build_server>: listening 0.0.0.0:9093 ..
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以开启服务的同时，回显详细日志信息。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --distcc -vD
</span><distcc_build_server>: listening 0.0.0.0:9093 ..
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">以 Daemon 模式开启服务</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --distcc --start
</span><u>$ </u><span style="color:black">xmake</span><span> service --distcc --restart
</span><u>$ </u><span style="color:black">xmake</span><span> service --distcc --stop
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置服务端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们首先，运行<span> </span><code>xmake service</code><span> </span>命令，它会自动生成一个默认的<span> </span><code>server.conf</code><span> </span>配置文件，存储到<span> </span><code>~/.xmake/service/server.conf</code>。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service
generating the config file to /Users/ruki/.xmake/service/server.conf ..
an token<strong style="color:black">(</strong>590234653af52e91b9e438ed860f1a2b<strong style="color:black">)</strong> is generated, we can use this token to connect service.
generating the config file to /Users/ruki/.xmake/service/client.conf ..
<distcc_build_server>: listening 0.0.0.0:9693 ..
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，我们编辑它，修复服务器的监听端口（可选）。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    distcc_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9693"</span>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/distcc_build"</span>
    <strong style="color:black">&#125;</strong>,
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置客户端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">客户端配置文件在<span> </span><code>~/.xmake/service/client.conf</code>，我们可以在里面配置客户端需要连接的服务器地址。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以在 hosts 列表里面配置多个服务器地址，以及对应的 token。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">!> 分布式编译，推荐使用 token 认证模式，因为密码模式，每台服务器连接时候都要输入一次密码，很繁琐。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>$cat ~/.xmake/service/client.conf
&#123;
    distcc_build = &#123;
        hosts = &#123;
            &#123;
                connect = "127.0.0.1:9693",
                token = "590234653af52e91b9e438ed860f1a2b"
            &#125;
        &#125;
    &#125;
&#125;
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">连接服务器</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">配置完认证和服务器地址后，就可以输入下面的命令，将当前工程连接到配置的服务器上了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们需要在连接时候，输入<span> </span><code>--distcc</code>，指定仅仅连接分布式服务。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span><span style="color:black">cd </span>projectdir
<span style="color:#8f5902">$ </span>xmake service --connect --distcc
<client>: connect 127.0.0.1:9693 ..
<client>: 127.0.0.1:9693 connected!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以同时连接多个服务，比如分布式编译和远程编译缓存服务。</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code class="language-hash">$ xmake service --connect --distcc --ccache
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">!> 如果不带任何参数，默认连接的是远程编译服务。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">分布式编译项目</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">连接上服务器后，我们就可以像正常本地编译那样，进行分布式编译了，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake
...
<strong style="color:black">[</strong> 93%]: ccache compiling.release src/demo/network/unix_echo_client.c         ----> <span style="color:black">local </span>job
<strong style="color:black">[</strong> 93%]: ccache compiling.release src/demo/network/ipv6.c
<strong style="color:black">[</strong> 93%]: ccache compiling.release src/demo/network/ping.c
<strong style="color:black">[</strong> 93%]: distcc compiling.release src/demo/network/unix_echo_server.c.         ----> distcc job
<strong style="color:black">[</strong> 93%]: distcc compiling.release src/demo/network/http.c
<strong style="color:black">[</strong> 93%]: distcc compiling.release src/demo/network/unixaddr.c
<strong style="color:black">[</strong> 93%]: distcc compiling.release src/demo/network/ipv4.c
<strong style="color:black">[</strong> 94%]: distcc compiling.release src/demo/network/ipaddr.c
<strong style="color:black">[</strong> 94%]: distcc compiling.release src/demo/math/fixed.c
<strong style="color:black">[</strong> 94%]: distcc compiling.release src/demo/libm/float.c
<strong style="color:black">[</strong> 95%]: ccache compiling.release src/demo/libm/double.c
<strong style="color:black">[</strong> 95%]: ccache compiling.release src/demo/other/test.cpp
<strong style="color:black">[</strong> 98%]: archiving.release libtbox.a
<strong style="color:black">[</strong> 99%]: linking.release demo
<strong style="color:black">[</strong>100%]: build ok!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">其中，带有 distcc 字样的是远程编译任务，其他的都是本地编译任务，默认 xmake 还开启了本地编译缓存，对分布式编译结果进行缓存，避免频繁请求服务器。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，我们也可以开启远程编译缓存，跟其他人共享编译缓存，进一步加速多人协同开发的编译。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">断开连接</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --disconnect --distcc
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">指定并行编译任务数</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们先简单介绍下，目前根据主机 cpu core 数量默认计算的并行任务数：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:blue">local</span> <span style="color:#000000">default_njob</span> <strong style="color:black">=</strong> <span style="color:black">math.ceil</span><strong style="color:#000000">(</strong><span style="color:#000000">ncpu</span> <strong style="color:black">*</strong> <strong style="color:#800080">3</strong> <strong style="color:black">/</strong> <strong style="color:#800080">2</strong><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">因此，如果不开启分布式编译，默认的最大并行编译任务数就是这个 default_njob。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果开启分布式编译后，默认的并行编译任务数就是：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:blue">local</span> <span style="color:#000000">maxjobs</span> <strong style="color:black">=</strong> <span style="color:#000000">default_njob</span> <strong style="color:black">+</strong> <span style="color:#000000">server_count</span> <strong style="color:black">*</strong> <span style="color:#000000">server_default_njob</span>
</code></pre> 
</div> 
<p>修改本地并行任务数</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们只需要通过<span> </span><code>-jN</code><span> </span>就能指定本地并行任务数，但是它不会影响服务端的并行任务数。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake -jN
</code></pre> 
</div> 
<p>修改服务端并行任务数</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果要修改服务端的并行任务数，需要修改客户端的配置文件。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:black">$cat</span> ~/.xmake/service/client.conf
<strong style="color:black">&#123;</strong>
    distcc_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
            <strong style="color:black">&#123;</strong>
                connect <strong style="color:black">=</strong> <span style="color:#ff00ff">"127.0.0.1:9693"</span>,
                token <strong style="color:black">=</strong> <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>,
                njob <strong style="color:black">=</strong> 8   <------- modify here
            <strong style="color:black">&#125;</strong>,
            <strong style="color:black">&#123;</strong>
                connect <strong style="color:black">=</strong> <span style="color:#ff00ff">"192.168.01:9693"</span>,
                token <strong style="color:black">=</strong> <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>,
                njob <strong style="color:black">=</strong> 4
            <strong style="color:black">&#125;</strong>
        <strong style="color:black">&#125;</strong>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">可以对每个服务器主机，添加<span> </span><code>njob = N</code><span> </span>参数配置，指定这台服务器可以提供的并行任务数。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">分布式编译 Android 项目</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">xmake 提供的分布式编译服务是完全跨平台的，并且支持 Windows, Linux, macOS, Android, iOS 甚至交叉编译。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果要进行 Android 项目编译，只需要在服务端配置中，增加<span> </span><code>toolchains</code><span> </span>工具链配置，提供 NDK 的跟路径即可。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    distcc_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9693"</span>,
        toolchains <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
            ndk <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
                ndk <strong style="color:black">=</strong> <span style="color:#ff00ff">"~/files/android-ndk-r21e"</span>   <------------ here
            <strong style="color:black">&#125;</strong>
        <strong style="color:black">&#125;</strong>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/distcc_build"</span>
    <strong style="color:black">&#125;</strong>,
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，我们就可以像正常本地编译那样，分布式编译 Android 项目，甚至可以配置多台 Windows, macOS, Linux 等不同的服务器主机，做为分布式编译服务的资源，来编译它。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">只需要下载对应平台的 NDK 就行了。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f -p android --ndk<strong style="color:black">=</strong>~/files/xxxx
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">分布式编译 iOS 项目</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">编译 iOS 项目更加简单，因为 Xmake 通常能自动检测到 Xcode，所以只需要像正常本地一样，切一下平台到 ios 即可。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f -p iphoneos
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">分布式交叉编译配置</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果要分布式交叉编译，我们需要在服务端配置工具链 sdk 路径，例如：</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    distcc_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9693"</span>,
        toolchains <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
            cross <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
                sdkdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"~/files/arm-linux-xxx"</span>   <------------ here
            <strong style="color:black">&#125;</strong>
        <strong style="color:black">&#125;</strong>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/distcc_build"</span>
    <strong style="color:black">&#125;</strong>,
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">其中，toolchains 下，每一项对应一个工具链，这里配置为<span> </span><code>cross = &#123;&#125;</code><span> </span>交叉工具链，对应<span> </span><code>toolchain("cross")</code>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">工具链里面我们可以配置<span> </span><code>sdkdir</code>,<span> </span><code>bindir</code>,<span> </span><code>cross</code><span> </span>等等，对应<span> </span><code>toolchain("cross")</code><span> </span>里面的<span> </span><code>set_sdkdir</code>,<span> </span><code>set_bindir</code><span> </span>和<span> </span><code>set_cross</code><span> </span>等接口配置。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">如果交叉工具链比较规范，我们通常只需要配置<span> </span><code>sdkdir</code>，xmake 就能自动检测到。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而客户端编译也只需要指定 sdk 目录。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f -p cross --sdk<strong style="color:black">=</strong>/xxx/arm-linux-xxx
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">清理服务器缓存</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">每个项目在服务端的编译，都会产生一些缓存文件，他们都是按工程粒度分别存储的，我们可以通过下面的命令，对当前工程清理每个服务器对应的缓存。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --clean --distcc
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">一些内部优化</h4> 
<ol> 
 <li>缓存服务器端编译结果，避免重复编译</li> 
 <li>本地缓存，远程缓存优化，避免不必要的服务端通信</li> 
 <li>服务器负载均衡调度，合理分配服务器资源</li> 
 <li>预处理后小文件直接本地编译，通常会更快</li> 
 <li>大文件实时压缩传输，基于 lz4 快速压缩</li> 
 <li>内部状态维护，相比 distcc 等独立工具，避免了频繁的独立进程加载耗时，也避免了与守护进程额外的通信</li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:start">本地编译缓存支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">默认，Xmake 就会开启本地缓存，2.6.5 之前的版本默认使用外置的 ccache，而 2.6.6 之后版本，Xmake 提供了内置的跨平台本地缓存方案。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">相比 ccache 等第三方独立进程，xmake 内部状态维护，更加便于优化，也避免了频繁的独立进程加载耗时，也避免了与守护进程额外的通信。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，内置的缓存能够更好的支持跨平台，Windows 上 msvc 也能够很好的支持，而 ccache 仅仅支持 gcc/clang。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">当然，我们也可以通过下面的命令禁用缓存。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f --ccache<strong style="color:black">=</strong>n
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">注：不管是否使用内置本地缓存，配置名都是<span> </span><code>--ccache=</code>，意思是 c/c++ 构建缓存，而不仅仅是指 ccache 工具的名字。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们如果想继续使用外置的其他缓存工具，我们也是可以通过下面的方式来配置。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake f --ccache<strong style="color:black">=</strong>n --cxx<strong style="color:black">=</strong><span style="color:#ff00ff">"ccache gcc"</span> --cc<strong style="color:black">=</strong><span style="color:#ff00ff">"ccache gcc"</span>
<span style="color:#8f5902">$ </span>xmake
</code></pre> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:start">远程编译缓存支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">除了本地缓存，我们也提供了远程缓存服务，类似 mozilla 的 sscache，如果只是个人开发，平常不会用到它。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">但是，如果是公司内部多人协同开发一个大型项目，仅仅靠分布式编译和本地缓存，是不够的。我们还需要对编译的对象文件缓存到独立的服务器上进行共享。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">这样，其他人即使首次编译，也不需要每次都去分布式编译它，直接从远程拉取缓存来加速编译。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">另外，Xmake 提供的远程缓存服务，也是全平台支持的，不仅支持 gcc/clang 还支持 msvc。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">开启服务</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以指定<span> </span><code>--ccache</code><span> </span>参数来开启远程编译缓存服务，当然如果不指定这个参数，xmake 会默认开启所有服务端配置的服务。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --ccache
</span><remote_cache_server>: listening 0.0.0.0:9092 ..
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以开启服务的同时，回显详细日志信息。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --ccache -vD
</span><remote_cache_server>: listening 0.0.0.0:9092 ..
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">以 Daemon 模式开启服务</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><u>$ </u><span style="color:black">xmake</span><span> service --ccache --start
</span><u>$ </u><span style="color:black">xmake</span><span> service --ccache --restart
</span><u>$ </u><span style="color:black">xmake</span><span> service --ccache --stop
</span></code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置服务端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们首先，运行<span> </span><code>xmake service</code><span> </span>命令，它会自动生成一个默认的<span> </span><code>server.conf</code><span> </span>配置文件，存储到<span> </span><code>~/.xmake/service/server.conf</code>。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service
generating the config file to /Users/ruki/.xmake/service/server.conf ..
an token<strong style="color:black">(</strong>590234653af52e91b9e438ed860f1a2b<strong style="color:black">)</strong> is generated, we can use this token to connect service.
generating the config file to /Users/ruki/.xmake/service/client.conf ..
<remote_cache_server>: listening 0.0.0.0:9692 ..
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">然后，我们编辑它，修复服务器的监听端口（可选）。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>cat ~/.xmake/service/server.conf
<strong style="color:black">&#123;</strong>
    distcc_build <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        listen <strong style="color:black">=</strong> <span style="color:#ff00ff">"0.0.0.0:9692"</span>,
        workdir <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/remote_cache"</span>
    <strong style="color:black">&#125;</strong>,
    known_hosts <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong> <strong style="color:black">&#125;</strong>,
    logfile <strong style="color:black">=</strong> <span style="color:#ff00ff">"/Users/ruki/.xmake/service/server/logs.txt"</span>,
    tokens <strong style="color:black">=</strong> <strong style="color:black">&#123;</strong>
        <span style="color:#ff00ff">"590234653af52e91b9e438ed860f1a2b"</span>
    <strong style="color:black">&#125;</strong>
<strong style="color:black">&#125;</strong>
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">配置客户端</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">客户端配置文件在<span> </span><code>~/.xmake/service/client.conf</code>，我们可以在里面配置客户端需要连接的服务器地址。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们可以在 hosts 列表里面配置多个服务器地址，以及对应的 token。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code>$cat ~/.xmake/service/client.conf
&#123;
    remote_cache = &#123;
            connect = "127.0.0.1:9692,
            token = "590234653af52e91b9e438ed860f1a2b"
        &#125;
    &#125;
&#125;
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">连接服务器</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">配置完认证和服务器地址后，就可以输入下面的命令，将当前工程连接到配置的服务器上了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们需要在连接时候，输入<span> </span><code>--ccache</code>，指定仅仅连接远程编译缓存服务。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span><span style="color:black">cd </span>projectdir
<span style="color:#8f5902">$ </span>xmake service --connect --ccache
<client>: connect 127.0.0.1:9692 ..
<client>: 127.0.0.1:9692 connected!
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以同时连接多个服务，比如分布式编译和远程编译缓存服务。</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code class="language-hash">$ xmake service --connect --distcc --ccache
</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">!> 如果不带任何参数，默认连接的是远程编译服务。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">断开连接</h4> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --disconnect --ccache
</code></pre> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:start">清理服务器缓存</h4> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们也可以通过下面的命令，清理当前工程对应的远程服务器上的缓存。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#8f5902">$ </span>xmake service --clean --ccache
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">而如果我们执行<span> </span><code>xmake clean --all</code>，在连接了远程服务的状态下，也会去自动清理所有的缓存。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">一些内部优化</h4> 
<ol> 
 <li>拉取远程缓存的快照，通过 bloom filter + lz4 回传本地后，用于快速判断缓存是否存在，避免频繁的查询服务端缓存信息</li> 
 <li>配合本地缓存，可以避免频繁地请求远程服务器，拉取缓存。</li> 
 <li>内部状态维护，相比 sscache 等独立工具，避免了频繁的独立进程加载耗时，也避免了与守护进程额外的通信</li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Keil/C51 工程支持</h3> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">我们只需要绑定到 c51 工具链，Xmake 就能自动检测到系统安装的 Keil/C51 SDK 工具链环境，然后使用它进行编译。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><code><span style="color:#000000">target</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"hello"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_rules</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c51.binary"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">set_toolchains</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"c51"</span><strong style="color:#000000">)</strong>
    <span style="color:#000000">add_files</span><strong style="color:#000000">(</strong><span style="color:#ff00ff">"src/main.c"</span><strong style="color:#000000">)</strong>
</code></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">当然，如果不通过<span> </span><code>set_toolchains("c51")</code><span> </span>设置工具链，我们也可以通过<span> </span><code>xmake f --toolchain=c51</code><span> </span>手动切换到 c51 工具链上去。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2327" target="_blank">#2327</a>: 支持 nvidia-hpc-sdk 工具链中的 nvc/nvc++/nvfortran 编译器</li> 
 <li>添加 path 实例接口</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2334" target="_blank">#2334</a>: 添加 lz4 压缩模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fpull%2F2349" target="_blank">#2349</a>: 添加 keil/c51 工程支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F274" target="_blank">#274</a>: 跨平台分布式编译支持</li> 
 <li>使用内置的本地缓存替代 ccache</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">改进</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2309" target="_blank">#2309</a>: 远程编译支持用户授权验证</li> 
 <li>改进远程编译，增加对 lz4 压缩支持</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">Bugs 修复</h3> 
<ul> 
 <li>修复选择包版本时候 lua 栈不平衡导致的崩溃问题</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            