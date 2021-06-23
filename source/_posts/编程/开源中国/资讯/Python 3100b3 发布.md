
---
title: 'Python 3.10.0b3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3760'
author: 开源中国
comments: false
date: Wed, 23 Jun 2021 06:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3760'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Python 3.10 仍在开发中，3.10.0b3 是计划中的四个测试版中的第三个。测试版的目的是让更多的社区有机会测试新的特性和修复错误，并让他们的项目准备好支持新的版本特性。目前不建议在生产环境中使用该版本。</p> 
<p><strong>核心和内置程序：</strong></p> 
<ul> 
 <li>bpo-44409: 修正初始化标记器时产生的标记器错误的位置信息；</li> 
 <li>bpo-44396: 修正标记器在引发未闭合字符串的语法错误时可能出现的崩溃；</li> 
 <li>bpo-44349: 修正在语法错误中显示带编码文件的文本时的一个边缘情况；</li> 
 <li>bpo-44335: 修正语法错误中识别错误字符时的回归问题；</li> 
 <li>bpo-44304: 修正 sqlite3 模块在垃圾回收器清除 sqlite.Statement 对象时发生的崩溃；</li> 
 <li>bpo-44305: 改进没有 <code>except</code> 或 <code>finally</code> 块的 <code>try</code> 块的错误信息；</li> 
 <li>bpo-43833: 如果数字字头后面紧跟着一个关键字：and, else, for, if, in, is, or，则发出弃用警告。如果紧随其后的是其他关键字或标识符，则引发语法错误，并提供更多信息；</li> 
 <li>bpo-11105: 当通过 <code>compile()</code> 编译带有递归引用的 <code>ast.AST</code> 对象时，解释器不会再崩溃，而是引发 <code>RecursionError</code> ；</li> 
</ul> 
<p><strong>库：</strong></p> 
<ul> 
 <li>bpo-44389: 修复了 ssl.OP_NO_TLSv1_3 的废弃问题；</li> 
 <li>bpo-44362: 改进 ssl 模块的弃用信息、错误报告和弃用文档；</li> 
 <li>bpo-44342: [Enum]将pickling从by-value改为by-name。</li> 
 <li>bpo-44356: [Enum] 允许多个数据类型混合；</li> 
 <li>bpo-44351: 恢复 distutils.sysconfig 中的 parse_makefile() ，因为它的行为与 sysconfig 中的类似实现不同。</li> 
 <li>bpo-44242: 移除 Enum 创建中缺失的标志检查，并移至 verify 装饰器中；</li> 
 <li>bpo-44246: 在 importlib.metadata.entry_points 中，去重分布不再需要为 PathDistribution 对象加载完整的元数据，从而使入口点的加载性能提高了 10 倍；</li> 
 <li>bpo-43853: 改进 sqlite3 错误处理；</li> 
 <li>bpo-37022: pdb现在用p和pp命令显示来自repr()的异常。</li> 
</ul> 
<p><strong>文档：</strong></p> 
<ul> 
 <li>bpo-44392: 在 C API 文档中增加了一个关于类型提示中使用的类型的新章节，记录了 Py_GenericAlias 和 Py_GenericAliasType；</li> 
 <li>bpo-38291: 在文档中把 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftyping.io%2F" target="_blank">typing.io</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftyping.re%2F" target="_blank">typing.re</a> 标记为自 Python 3.8 起已废弃；</li> 
 <li>bpo-44322: 记录 SyntaxError args 有一个细节元组，并且在 f-string 字段替换表达式中，细节会被调整为错误。</li> 
</ul> 
<p><strong>IDLE：</strong></p> 
<ul> 
 <li>bpo-40128: 在不使用 tcl/tk 8.6.11 时，主要修复了 macOS 上的完成度；</li> 
 <li>bpo-33962: 把缩进空间的设置从字体标签移到新的 Windows 标签；</li> 
 <li>bpo-40468: 将设置对话框的 "常规" 选项卡分成 Windows 和 Shell/ED 选项卡。将帮助菜单的帮助源移至扩展标签。为新选项留出空间，并缩短对话框；</li> 
</ul> 
<p>Python 3.10 的下一个测试版本将是 3.10.0b4，目前计划于 2021 年 7 月 10 日发布。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100b3%2F" target="_blank">https://www.python.org/downloads/release/python-3100b3/</a></p>
                                        </div>
                                      
</div>
            