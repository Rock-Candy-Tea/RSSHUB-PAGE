
---
title: '计算机图形学编程语言 Taichi（太极）发布 1.0.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2020/0609/174153_rbDe_4252687.gif'
author: 开源中国
comments: false
date: Thu, 14 Apr 2022 07:39:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2020/0609/174153_rbDe_4252687.gif'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">专为高性能计算机图形学设计的编程语言 Taichi（太极）已经发布 1.0.0 版本，这是一个里程碑版本，同时带来大量新特性，另外需要注意的是：许可证从 MIT 改成了 Apache 2.0 。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/space/2020/0609/174153_rbDe_4252687.gif" referrerpolicy="no-referrer"></p> 
<h2>许可证变更</h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Taichi 的许可证在公开投票后从 MIT 更改为 Apache-2.0 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Fdiscussions%2F4772" target="_blank">#4607</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python 3.10 支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本在所有受支持的操作系统（Windows、macOS 和 Linux）上支持 Python 3.10。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Manylinux2014 兼容</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 v1.0.0 之前，Taichi 仅适用于支持 glibc 2.27+（例如 Ubuntu 18.04+）的 Linux 发行版。从 v1.0.0 开始，除了普通的 Taichi 轮子，Taichi 还提供了 manylinux2014 兼容的轮子，可以在大多数现代 Linux 发行版上运行，包括 CentOS 7。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2>新功能</h2> 
<h3><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>非 Python 部署解决方案</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>通过与 OPPO 美国研究中心合作，Taichi 提供了 Taichi AOT，这是一种用于在非 Python 环境（例如移动设备）中部署内核的解决方案。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>编译的 Taichi 内核可以从 Python 进程中保存，然后由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Fdownload%2Fv1.0.0%2Flibtaichi_export_core.so" target="_blank">提供的 C++ 运行时库</a>加载和运行。通过一组 API， Python/Taichi 代码可以轻松部署在任何 C++ 环境中。点此</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi-aot-demo" target="_blank">查看<code>taichi-aot-demo</code>repo</a>。</p> 
<p style="text-align:start"><img alt height="1117" src="https://oscimg.oschina.net/oscnet/up-48c4a9eedb9bdf92f7ecd050a264cf8b49f.gif" width="500" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#24292f">注意，目前 Taichi 仅支持 C++ 运行时库中的 Vulkan 后端。</span></p> 
<h3>real <span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>函数（实验）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>所有 Taichi 函数在编译期间都内联到 Taichi 内核中。但是，如果太极函数调用过多，内核就会变得冗长并且需要更长的编译时间。如果 Taichi 函数涉及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.taichi-lang.org%2Flang%2Farticles%2Fmeta%23compile-time-recursion-of-tifunc" target="_blank">编译时递归</a>，这一点尤其明显。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start">这个版本引入了“real function”，一种新型的 Taichi 函数，它可以独立编译而不是内联到内核中。这是一项实验性功能，目前仅支持标量参数和标量返回值。</p> 
<h2><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>文字的类型注释</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<p><span style="background-color:#ffffff; color:#24292f">从 v1.0.0 开始，可以为文字编写类型注释：</span></p> 
<pre><code>@ti.kernel
def foo():
    a = ti.u32(2891336453)  # similar to 2891336453u in C</code></pre> 
<h3><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code>math</code>模块</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本添加了一个<code>math</code>模块来支持 GLSL 标准矢量操作，并使其更容易将 GLSL 着色器代码移植到 Taichi。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h2>CLI 命令 <code>ti gallery </code></h2> 
<p>此版本引入了 CLI 命令 ti gallery，允许在弹出窗口中选择和运行 Taichi 示例。比如：</p> 
<pre><code>ti gallery</code></pre> 
<p><em>弹出一个窗口：</em></p> 
<p><img height="376" src="https://oscimg.oschina.net/oscnet/up-edec801b83224406bc935a80167c2d8a133.png" width="600" referrerpolicy="no-referrer"></p> 
<p>单击可运行弹出窗口中的任何示例，控制台会同时打印相应的源代码。</p> 
<h2><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<h3><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>增强矩阵类型</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从 v1.0.0 开始，Taichi 接受矩阵或向量类型作为参数和返回值，可以使用<code>ti.types.matrix</code>或<code>ti.types.vector</code>作为类型注释。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Taichi 还支持基本的只读矩阵切片，使用<code>mat[:,:]</code>语法快速检索矩阵的特定部分。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code>assert</code>语句中的 f 字符串支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本支持在<code>assert</code>语句中包含 f 字符串作为错误消息，可以在 f 字符串中包含标量变量。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"> </p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多详细内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftaichi-dev%2Ftaichi%2Freleases%2Ftag%2Fv1.0.0" target="_blank">发行公告</a>中查看。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p>
                                        </div>
                                      
</div>
            