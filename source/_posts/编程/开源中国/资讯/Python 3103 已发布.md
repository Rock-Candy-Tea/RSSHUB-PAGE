
---
title: 'Python 3.10.3 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9811'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9811'
---

<div>   
<div class="content">
                                                                                            <p>Python 3.10.3 已发布，该版本带来一些修复和改进，更新内容如下：</p> 
<h3 style="margin-left:0px">核心</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46940" target="_blank">bpo-46940</a>：避免覆盖 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.10.3%2Flibrary%2Fexceptions.html%23AttributeError" target="_blank"><code>AttributeError</code></a> 嵌套属性访问调用的元数据信息。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46794" target="_blank">bpo-46794</a>：将 libexpat 版本提升到 2.4.6</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46762" target="_blank">bpo-46762</a>：修复调试版本中的断言失败</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46732" target="_blank">bpo-46732</a>：更正<code>__bool__()</code>方法的文档字符串。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46707" target="_blank">bpo-46707</a>：当产生一些涉及大量括号的语法错误时，避免潜在的指数回溯</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue40479" target="_blank">bpo-40479</a> <code>va_end()</code> ：添加对in 的缺失调用<code>Modules/_hashopenssl.c</code>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46615" target="_blank">bpo-46615</a>：在内部迭代集合<code>setobject.c</code> 时，从集合中获取对结果项的强引用。</li> 
</ul> 
<h3>Windows</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue44549" target="_blank">bpo-44549</a>：在 Windows 版本中将 bzip2 更新到 1.0.8 以缓解 CVE-2016-3189 和 CVE-2019-12900</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46948" target="_blank">bpo-46948</a>：通过确保 Windows 安装程序中的添加到 PATH 选项在修复时使用正确的路径来防止 CVE-2022-26488。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46638" target="_blank">bpo-46638</a>：确保始终禁用注册表虚拟化。对于 3.10 和更早版本，它保持启用（某些注册表写入受到保护），而对于 3.11 和更高版本，它被禁用（注册表修改影响所有应用程序）。</li> 
</ul> 
<h3 style="margin-left:0px">macOS</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45925" target="_blank">bpo-45925</a>：将 macOS 安装程序更新到 SQLite 3.37.2</li> 
</ul> 
<h3 style="margin-left:0px">IDLE</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46630" target="_blank">bpo-46630</a>：使 Windows 上的查询对话框以输入框中的光标开始。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45296" target="_blank">bpo-45296</a>：澄清在 IDLE 中关闭、退出和退出。在“文件”菜单中，“关闭”和“退出”现在是“关闭窗口”（当前窗口），“退出”现在是“退出空闲”（通过关闭所有窗口）。在 Shell 中，“quit()”和“exit()”表示“关闭 Shell”。如果没有其他窗口，这也会退出 IDLE。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45447" target="_blank">bpo-45447</a>：对 <code>pyi</code> 文件应用 IDLE 语法突出显示。</li> 
</ul> 
<h3 style="margin-left:0px">C API</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue46433" target="_blank">bpo-46433</a>：内部函数 _PyType_GetModuleByDef 现在可以正确处理涉及静态类型的继承模式。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue14916" target="_blank">bpo-14916</a>：修复了标记器阻止从提供的 FD 解析中  <code>PyRun_InteractiveOne</code>  的错误。</li> 
</ul> 
<p> </p> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.10.3%2Fwhatsnew%2Fchangelog.html%23python-3-10-3-final" target="_blank">https://docs.python.org/release/3.10.3/whatsnew/changelog.html#python-3-10-3-final</a></p>
                                        </div>
                                      
</div>
            