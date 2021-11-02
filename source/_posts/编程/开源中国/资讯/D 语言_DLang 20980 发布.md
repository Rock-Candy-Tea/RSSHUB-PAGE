
---
title: 'D 语言_DLang 2.098.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7240'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7240'
---

<div>   
<div class="content">
                                                                                            <p>D 语言(DLang) 2.098.0 版本已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fblog%2F2021%2F10%2F29%2Fdlang-news-september-october-2021-d-2-098-0-openbsd-saoc-dconf-online-swag%2F" target="_blank">发布</a>，公告显示，DLang 2.098.0 现在以 DMD 2.098.0（D 编译器）和 LDC 1.28.0（基于 LLVM 的 D 编译器）的形式提供。此外，D 语言已经支持 OpenBSD。</p> 
<p>此版本包含 17 项目主要变更，同时修复了 160 个 issue。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">编译器变更</h2> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23AliasAssign" target="_blank">添加别名赋值 (Alias Assignment) 功能</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23ImportC" target="_blank">通过 ImportC 编译器从 D 语言访问</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23ImportC" target="_blank">C 语言的声明</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23ambiguous-lambda" target="_blank">使用 syntax<span> </span><strong>(args) => &#123;&#125;</strong><span> 会触发</span>一条 deprecation 消息</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23dtoh-improvements" target="_blank">对生成 C++ 头文件的改进</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23dtorfileds" target="_blank">默认启用 -preview=dtorfields</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23fix10445" target="_blank">为向量类型添加</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23fix10445" target="_blank">.min, .max 等属性</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23mutable-cases" target="_blank">使用可变变量作为 switch case 会触发错误</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23range-error" target="_blank">越界的数组访问现在会提供更友好的错误消息</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23remove_alloc" target="_blank">从 D 语言中删除</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23remove_alloc" target="_blank">类分配器 (Class allocators)</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23static_this_immutable_initialization" target="_blank">初始化来自 static this 的不可变全局数据现在会触发一个错误</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23target" target="_blank">添加<span> </span><strong>-target=<triple></strong><span> 用于操作系统、C 和 C++ 运行时交叉编译</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23union_initialization" target="_blank">默认初始化<span> </span><strong>union</strong><span> 不是第一个成员的字段现在会触发错误</span></a></li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">运行时变更</h2> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23UniqueTypeInfoNames" target="_blank">聚合体的 TypeInfo 名称完全符合要求，因此目前是唯一的</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23forkgc" target="_blank">针对 Posix 系统的</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23forkgc" target="_blank">并发 GC</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23improve_posix_imports" target="_blank">改进 POSIX imports</a></li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">库变更</h2> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23add_isValidCharacter" target="_blank">在<span> </span>std.utf</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23add_isValidCharacter" target="_blank">中新增函数<span> </span>isValidCharacter</a></li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Dub 变更</h2> 
<ol> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html%23add_env" target="_blank">在 dub 设置文件和 dub.json/dub.sdl 中增加了对环境变量的支持，可使用编译和运行（或测试）选项</a></li> 
</ol> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdlang.org%2Fchangelog%2F2.098.0.html" target="_blank">详情查看 Changelog</a>。</p>
                                        </div>
                                      
</div>
            