
---
title: 'Nim 1.6.2 版本已发布，修复若干 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2510'
author: 开源中国
comments: false
date: Sun, 19 Dec 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2510'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Nim 1.6.2 版本已发布，这是针对 Nim 1.6 的第一个补丁版本，两个月努力的结果包含 41 次提交，修复了超过 15 个报告的问题，比 1.6.0 带来了一些总体改进，建议所有用户升级并使用 1.6.2 版。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Bug 修复</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">修复了“在 Linux 内核版本 < 3.17 上，Nim 的编译在编译 std/sysrand 时失败”问题。</span><span style="color:#111111">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19052" target="_blank">#19052</a><span style="color:#111111">)</span></li> 
 <li>修复了“如果<span> </span><code>--gc:arc</code><span> </span>或<span> </span><code>--gc:orc</code><span> </span>给定，当 proc 返回带有<code>lent</code>或<code>var</code>类型的全局变量时，编译器以 IndexDefect 终止”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18971" target="_blank">#18971</a>）</li> 
 <li>修复了“使用 C++ 后端初始化 RootObj 对象的错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F18410" target="_blank">#18410</a>）</li> 
 <li>修复了“<span style="color:#111111">arc/orc 下损害</span>的堆栈跟踪”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19078" target="_blank">#19078</a>）</li> 
 <li>修复了“尽管无法证明不存在捕获的引用，但仍能愉快地编译”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19013" target="_blank">#19013</a>）</li> 
 <li>修复了“PragmaExpr 错误地添加到枚举类型”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19011" target="_blank">#19011</a>）</li> 
 <li>修复了“RVO 不适用于具有大数组的对象”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F14470" target="_blank">#14470</a>）</li> 
 <li>修复了“定义泛型 int 类型时，后端 gcc 编译错误”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19051" target="_blank">#19051</a>）</li> 
 <li>修复了“当长度为 0 或之前出现过块参数时， 1.6.0 中的可变参数会被破坏。” （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19015" target="_blank">#19015</a>）</li> 
 <li>修复了“VM 用别名替换声明的类型”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19198" target="_blank">#19198</a>）</li> 
 <li>修复了“回归：无效果的内部模板会被声明为副作用”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19159" target="_blank">#19159</a>）</li> 
 <li>修复了“闭包迭代器循环中的变量未正确分配”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19193" target="_blank">#19193</a>）</li> 
 <li>修复了“未导出的转换器通过导入传播并影响代码”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19213" target="_blank">#19213</a>）</li> 
 <li>修复了“ [arc]<span> </span><span style="color:#2e3033">包含跟踪引用的 PTR 对象的操作段错误</span>”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F19205" target="_blank">#19205</a>）</li> 
 <li>修复了“与 .lib 文件的静态链接不起作用”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fissues%2F15955" target="_blank">#15955</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">此版本还包括了如下改进：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>允许将静态变量转换为 openArray (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19047" target="_blank">PR #19047</a><span> </span>)</li> 
 <li>不要中断字段初始化消息字符串的插值（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19085" target="_blank">PR #19085</a>）</li> 
 <li>修复了一个效果推断错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19100" target="_blank">PR #19100</a>）</li> 
 <li>修复 rst2tex/doc2tex 中的 nimindexterm (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19106" target="_blank">PR #</a><span> </span>19106 )</li> 
 <li>从 Windows + GCC 配置中删除启用的 tlsEmulation (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19119" target="_blank">PR #19119</a><span> </span>)</li> 
 <li>修复了 –gc:orc 下内置的 newSeq 的 .raises 推理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19158" target="_blank">PR #19158</a>）</li> 
 <li>修复未声明<span> </span><code>SYS_getrandom</code><span> </span>的 emscripten (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19144" target="_blank">PR #19144</a><span> </span>)</li> 
 <li>在 Windows 上正确合并文件的大小字段 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19141" target="_blank">PR #19141</a><span> </span>)</li> 
 <li>修复 VM 中的 marshal 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19161" target="_blank">PR #19161</a>）</li> 
 <li>允许<span> </span><code>HSlice</code><span> </span>以不同类型的常量为界（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19219" target="_blank">PR #19219</a>）</li> 
 <li>修复了一个可能发生的 “javascript:” 协议漏洞（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19134" target="_blank">PR #19134</a>）</li> 
 <li>让 Nim 支持带有锁文件支持的 Nimble 0.14 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19236" target="_blank">PR #19236</a><span> </span>)</li> 
 <li>nimRawSetjmp：支持 Windows（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19197" target="_blank">PR #19197</a>）</li> 
 <li>不要在 uri.hostname 中读取 \0 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19148" target="_blank">PR #19148</a><span> </span>) </li> 
 <li>json：限制递归深度（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnim-lang%2FNim%2Fpull%2F19252" target="_blank">PR #19252</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnim-lang.org%2Fblog%2F2021%2F12%2F17%2Fversion-162-released.html" target="_blank">https://nim-lang.org/blog/2021/12/17/version-162-released.html</a></p>
                                        </div>
                                      
</div>
            