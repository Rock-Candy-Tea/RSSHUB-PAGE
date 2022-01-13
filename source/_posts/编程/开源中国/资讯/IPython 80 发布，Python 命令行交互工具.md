
---
title: 'IPython 8.0 发布，Python 命令行交互工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0113/073745_jZkn_5430600.png'
author: 开源中国
comments: false
date: Thu, 13 Jan 2022 07:51:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0113/073745_jZkn_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px">IPython 是 Python 的原生交互式 shell 的增强版，可以完成许多不同寻常的任务，比如帮助实现并行化计算；主要使用它提供的交互性帮助，比如代码着色、改进了的命令行回调、制表符完成、宏功能以及改进了的交互式帮助。</p> 
<p style="margin-left:0px">IPython 8.0 酝酿了许久，主要对现有代码库和几个新功能进行了改进。新功能包括在 CLI 中使用 Black 重新格式化代码、ghost 建议以及突出错误节点的更好的回溯，从而使复杂的表达式更易于调试。</p> 
<h3 style="margin-left:0px">追溯改进</h3> 
<p style="margin-left:0px">之前的错误回溯显示一个散列表（hash），用于编译 Python AST：</p> 
<pre><code class="language-python">In [1]: def foo():
...:     return 3 / 0
...:

In [2]: foo()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-2-c19b6d9633cf> in <module>
----> 1 foo()

<ipython-input-1-1595a74c32d5> in foo()
    1 def foo():
----> 2     return 3 / 0
    3

ZeroDivisionError: division by zero</code></pre> 
<p>现在错误回溯的格式正确，会显示发生错误的单元格编号：</p> 
<pre><code class="language-python">In [1]: def foo():
...:     return 3 / 0
...:

Input In [2]: foo()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
input In [2], in <module>
----> 1 foo()

Input In [1], in foo()
    1 def foo():
----> 2     return 3 / 0

ZeroDivisionError: division by zero</code></pre> 
<p>第二个回溯改进是 stack_data 包的集成；在回溯中提供更智能的信息；它会突出显示发生错误的 AST 节点，这有助于快速缩小错误范围，比如</p> 
<pre><code>def foo(i):
    x = [[[0]]]
    return x[0][i][0]


def bar():
    return foo(0) + foo(
        1
    ) + foo(2)</code></pre> 
<p>调用 bar() 会在 IndexError 的返回行上引发一个 foo，IPython 8.0 可以告诉你索引错误发生在哪里：</p> 
<pre><code class="language-python">IndexError
Input In [2], in <module>
----> 1 bar()
        ^^^^^

Input In [1], in bar()
      6 def bar():
----> 7     return foo(0) + foo(
                            ^^^^
      8         1
         ^^^^^^^^
      9     ) + foo(2)
         ^^^^

Input In [1], in foo(i)
      1 def foo(i):
      2     x = [[[0]]]
----> 3     return x[0][i][0]
                   ^^^^^^^</code></pre> 
<p><span style="background-color:#ffffff">用</span><span style="background-color:#ffffff; color:#e74c3c"> ^ </span><span style="background-color:#ffffff">标记的位置在终端会高亮显示。</span></p> 
<p>第三个回溯改进是最谨慎的，但对生产力有很大影响，在回溯中的文件名后面附加一个冒号 :: 和行号：</p> 
<pre><code class="language-python">ZeroDivisionError               Traceback (most recent call last)
File ~/error.py:4, in <module>
      1 def f():
      2     1/0
----> 4 f()

File ~/error.py:2, in f()
      1 def f():
----> 2     1/0</code></pre> 
<p>许多终端和编辑器具有的集成功能，允许在使用此语法时<strong>直接跳转到错误相关的文件/行</strong>。</p> 
<h3 style="text-align:start">自动建议</h3> 
<p>Ptpython 允许用户在 ptpython/config.py 中启用自动建议功能，此功能包含丰富的代码补全建议，如图：</p> 
<p><img alt height="212" src="https://static.oschina.net/uploads/space/2022/0113/073745_jZkn_5430600.png" width="350" referrerpolicy="no-referrer"></p> 
<p>目前，自动建议仅在 emacs 或 vi 插入编辑模式中显示：</p> 
<ul> 
 <li>ctrl e、ctrl f 和 alt f 快捷键默认在 emacs 模式下工作。</li> 
 <li>要在 vi 插入模式下使用这些快捷键，必须在 config.py 中创建自定义键绑定。</li> 
</ul> 
<h2>使用“?”和"??"查看对象信息</h2> 
<p>在 IPDB 中，现在可以使用“?”和”? ?“来显示对象的信息，在使用 IPython 提示符时也可如此操作：</p> 
<pre><code class="language-python">ipdb> partial?
Init signature: partial(self, /, *args, **kwargs)
Docstring:
partial(func, *args, **keywords) - new function with partial application
of the given arguments and keywords.
File:           ~/.pyenv/versions/3.8.6/lib/python3.8/functools.py
Type:           type
Subclasses:</code></pre> 
<h2>历史范围全局功能</h2> 
<p><span style="background-color:#ffffff">之前使用</span><span style="background-color:#ffffff; color:#e74c3c"> %history</span><span style="background-color:#ffffff"> 功能时</span><span style="background-color:#ffffff; color:#e74c3c">，</span><span style="background-color:#fcfcfc; color:#404040">用户可以指定会话和行的范围，例如：</span></p> 
<pre><code class="language-python">~8/1-~6/5   # see history from the first line of 8 sessions ago,
            # to the fifth line of 6 sessions ago.``</code></pre> 
<p>或者可以指定全局模式（global）：</p> 
<pre><code class="language-python">-g <pattern>  # glob ALL history for the specified pattern.</code></pre> 
<p>但无法同时指定两者，如果用户确实指定了范围和全局模式，则将使用 glob 模式（通配所有历史记录），并且将<strong>忽略范围</strong>。</p> 
<p>现在此功能获得了增强，如果用户同时指定范围和 glob 模式，则 glob 模式将应用于指定的历史范围。</p> 
<p> </p> 
<p>此外，Ipython 8.0 还取消了对 Python 3.7 的支持，仅支持 3.8 以上版本。有关 Ipython 8.0 的更多新功能，可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fipython.readthedocs.io%2Fen%2Fstable%2Fwhatsnew%2Fversion8.html%23ipython-8-0" target="_blank">发布页面</a>查看。</p>
                                        </div>
                                      
</div>
            