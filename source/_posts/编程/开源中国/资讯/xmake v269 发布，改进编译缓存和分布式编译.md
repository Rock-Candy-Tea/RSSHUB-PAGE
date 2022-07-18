
---
title: 'xmake v2.6.9 发布，改进编译缓存和分布式编译'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1850'
author: 开源中国
comments: false
date: Mon, 18 Jul 2022 09:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1850'
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
<h3 style="text-align:start">新特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2474" target="_blank">#2474</a>: 添加 icx 和 dpcpp 工具链</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2523" target="_blank">#2523</a>: 改进对 LTO 的支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2527" target="_blank">#2527</a>: 添加 set_runargs 接口</li> 
</ul> 
<h3 style="text-align:start">改进</h3> 
<ul> 
 <li>改进 tools.cmake 支持 wasm 库构建</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2491" target="_blank">#2491</a>: 如果服务器不可访问，自动回退到本地编译和缓存</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2514" target="_blank">#2514</a>: 为工程生成器禁用 Unity Build</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2473" target="_blank">#2473</a>: 改进 apt::find_package，支持从 pc 文件中查找</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2512" target="_blank">#2512</a>: 改进远程服务支持超时配置</li> 
</ul> 
<h3 style="text-align:start">Bugs 修复</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2488" target="_blank">#2488</a>: 修复从 windows 到 linux 的远程编译路径问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2504" target="_blank">#2504</a>: 修复在 msys2 上远程编译失败问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2525" target="_blank">#2525</a>: 修复安装依赖包时候卡死问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxmake-io%2Fxmake%2Fissues%2F2557" target="_blank">#2557</a>: 修复 cmake.find_package 查找 links 错误</li> 
 <li>修复缓存导致的预处理文件路径冲突问题</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            