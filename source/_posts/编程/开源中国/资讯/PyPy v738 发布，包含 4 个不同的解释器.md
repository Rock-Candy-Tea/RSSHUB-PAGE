
---
title: 'PyPy v7.3.8 发布，包含 4 个不同的解释器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0222/153409_POFy_2720166.png'
author: 开源中国
comments: false
date: Wed, 23 Feb 2022 07:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0222/153409_POFy_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>PyPy v7.3.8 已正式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pypy.org%2Fposts%2F2022%2F02%2Fpypy-v738-release.html" target="_blank">发布</a>，更新内容主要是提升速度和修复错误，API 保持不变，所有 API 均与其他 7.3 版本兼容。</p> 
<p>新版本包含 4 个不同的解释器：</p> 
<ul> 
 <li>PyPy2.7：支持 Python 2.7 语法和特性，包括 CPython 2.7.18+ 的 stdlib</li> 
 <li>PyPy3.7：支持 Python 3.7 语法和特性，包括 CPython 3.7.12+ 的 stdlib，这将是 PyPy3.7 的最后一个版本</li> 
 <li>PyPy3.8：支持 Python 3.8 语法和特性，包括 CPython 3.8.12 的 stdlib，这是第三个版本，并取消了"beta"标签</li> 
 <li>PyPy3.9：支持 Python 3.9 语法和特性，包括 CPython 3.9.10 的 stdlib。由于此版本是第一次发布，所以目前还处于"beta"阶段</li> 
</ul> 
<p>据介绍，这 4 个解释器均基于相同的代码库构建，新版本的更新亮点：</p> 
<ul> 
 <li>PyPy3.9 使用 RPython 版本的 PEG 解析器，并对词法和解析器进行了全面的清理</li> 
 <li>修复当 JITting 处于空列表推导 (list comprehensions) 时出现的回归错误</li> 
 <li>调整打包后更改文件布局 (file layout) 出现的部分问题，确保 PyPy3.8 的 on-disk 布局与 CPython 更加兼容。此特性要求<code><span>setuptools>=58.1.0</span></code></li> 
 <li>RPython 现已支持在目标可执行文件的名字中使用<code>.</code>，因此 PyPy3.9 会生成一个<code><span>pypy3.9-c</span></code><span>和</span><code><span>libpypy3.9-c.so</span></code>。通过将共享对象的名字改为特定的版本（此前为<span> </span><code><span>libpypy3-c.so</span></code>）将支持与其他版本并存。</li> 
 <li>构建 PyPy3.9+ 时支持接收像 CPython 这样的<code><span>--platlibdir</span></code>参数</li> 
 <li>改进 ssl 对 CFFI 缓冲区的使用，提升<code>recv</code><span>和</span><code>recvinto</code>速度</li> 
 <li>将打包好的 OpenSSL 更新为 1.1.1m</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.pypy.org%2Fen%2Flatest%2Frelease-v7.3.8.html%23changelog" target="_blank">详情查看 Changelog</a>。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypy.org%2Fdownload.html" target="_blank">https://pypy.org/download.html</a></p> 
<p>PyPy 是一个 Python 解释器，可作为 CPython 2.7、3.7、3.8 和 3.9 的直接替代品。由于其集成的跟踪 JIT 编译器，PyPy 速度很快。</p> 
<p><img height="746" src="https://static.oschina.net/uploads/space/2022/0222/153409_POFy_2720166.png" width="1401" referrerpolicy="no-referrer"></p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0222/153459_67nD_2720166.png" referrerpolicy="no-referrer"></p> 
<p>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspeed.pypy.org%2F" target="_blank">PyPy 和 CPython 3.7.4 的性能对比</a>）</p>
                                        </div>
                                      
</div>
            