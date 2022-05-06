
---
title: 'Nim 1.6.6 版本已发布，修复大量 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1831'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1831'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Nim 1.6.6 版本已发布，这是针对 Nim 1.6 的第三个补丁版本，两个月努力的结果包含 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fcompare%2Fv1.6.4...v1.6.6" target="_blank">55 次提交</a> 。下面介绍一些较为重要的修复项：</p> 
<ul> 
 <li>修复了“std.streams 无法在 Windows 和 –cpu:amd64 上使用 TCC 编译器编译”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F16326" target="_blank">#16326</a>）</li> 
 <li>修复“编译器版本 1.6.0 不适用于 Windows XP”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19038" target="_blank">#19038</a>）</li> 
 <li>修复了“<code>os.putEnv</code>在 Windows 上的 cpp 后端无法编译”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19292" target="_blank">#19292</a>）</li> 
 <li>修复“JS 目标定义 gcc”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19059" target="_blank">#19059</a>）</li> 
 <li>修复了“当 CC = tcc 时 <em>JavaScript </em>输出中的<em> </em><code>static int __tcc_cas(</code> 函数”（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19330" target="_blank">#19330</a>）</li> 
 <li>修复了“i386 的 CPU 检测”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19577" target="_blank">#19577</a>）</li> 
 <li>修复了“不刷新标准输出<code>MSYS</code>”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19584" target="_blank">#19584</a>）</li> 
 <li>修复了“Nim-1.6 错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19569" target="_blank">#19569</a>）</li> 
 <li>修复了“在闭包迭代器的 try-catch 块中使用控制流语句时， Nim 编译器崩溃”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19575" target="_blank">#19575</a>）</li> 
 <li>修复“&#123;.byref,exportc.&#125; 类型不输出到 –header 文件”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19445" target="_blank">#19445</a>）</li> 
 <li>修复了“<code>nim check</code> 为 nimscript 报告不正确的错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19440" target="_blank">#19440</a>）</li> 
 <li>修复了“是否有正确的方法来检查 .nims 文件的语法？” （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F3858" target="_blank">#3858</a>）</li> 
 <li>修复了“拨号忽略缓冲参数”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19650" target="_blank">#19650</a>）</li> 
 <li>修复“<code>nim dump</code>等信息获取命令在 nims 文件中执行顶层 <code>exec</code> 语句”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F8219" target="_blank">#8219</a>）</li> 
 <li>修复了“在闭包迭代器中使用嵌套循环的错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18474" target="_blank">#18474</a>）</li> 
 <li>修复了“导入/排除在开发中不起作用”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18986" target="_blank">#18986</a>）</li> 
 <li>修复了“无法检查 stderr 是否为静态”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19680" target="_blank">#19680</a>）</li> 
 <li>修复了“使用 arc 时在写入时，从字符串段错误创建的 StringStream”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19707" target="_blank">#19707</a>）</li> 
 <li>修复了“次要 NimNode 注释 repr() 回归 1.0.10 到 1.2.9”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F16307" target="_blank">#16307</a>）</li> 
 <li>修复了“方法调度很慢”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18612" target="_blank">#18612</a>）</li> 
 <li>修复了“构造函数错误可能是虚假的无元组类型”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18409" target="_blank">#18409</a>）</li> 
 <li>修复了“传递给概念函数参数的匿名元组错误”。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19730" target="_blank">#19730</a> )</li> 
</ul> 
<p>完整的更新列表可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fcompare%2Fv1.6.4...v1.6.6" target="_blank">此处</a>获得。</p>
                                        </div>
                                      
</div>
            