
---
title: 'IPython 8.1 发布，Python 交互式解释器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4710'
author: 开源中国
comments: false
date: Sun, 27 Feb 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4710'
---

<div>   
<div class="content">
                                                                                            <p>IPython 是一个综合环境，可以帮助程序员或开发人员等高级计算机用户测试或探索各种功能。尽管 Python 附带了一个强大的交互式解释器，使用户无需在目标计算机上创建额外的文件即可运行测试，但它在用户与软件交互方面存在一些限制。</p> 
<p>IPython 的三个核心部分包括一个高度交互式的 Python shell，一个解耦的双进程通信模型和交互式并行计算的架构。</p> 
<p>IPython 8.1 是 8.0 之后的第一个小版本，和许多新的主要版本一样，它修复了 8.0 中的一些 bug 并更新了一些有问题的行为：</p> 
<ul> 
 <li>围绕引号自动关闭的多项修正。现在默认是禁用的，使用 <code>TerminalInteractiveShell.auto_match=True</code> 运行，可以重新启用。</li> 
 <li>要求 pygments>=2.4.0，之前这在代码中是隐含的，但现在在 <code>setup.cfg/setup.py</code> 中是明确的</li> 
 <li>文档中改进了 <code>core.magic_arguments</code> 的例子</li> 
 <li>多行编辑在使用 await 时执行得太早</li> 
 <li><code>black</code> 重新成为一个可选依赖项，并默认禁用自动格式化</li> 
 <li>修复了 <code>display</code> 没有定义的问题</li> 
 <li>自动建议现在是可配置的。目前只有 <code>AutoSuggestFromHistory</code>（默认）和 <code>None</code></li> 
 <li>多个打包/测试改进，以简化下游打包</li> 
 <li>更新弃用。 <code>InteractiveShell.magic</code> 内部方法已被废弃多年，但直到现在才发出警告</li> 
 <li>内部 <code>appended_to_syspath</code> 上下文管理器已被弃用</li> 
 <li>修复 virtualenv 中符号链接的问题</li> 
 <li>修正 vim 模式的问题，即退出时光标不会被重置</li> 
 <li>ipython 指令现在只删除已知的伪装饰器</li> 
 <li>过去用于 jupyter notebook 的 <code>IPython/lib/security</code> 已被删除</li> 
 <li>修复了 <code>async with</code> 会在新行上执行的问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fipython.readthedocs.io%2Fen%2Fstable%2Fwhatsnew%2Fversion8.html" target="_blank">https://ipython.readthedocs.io/en/stable/whatsnew/version8.html</a></p>
                                        </div>
                                      
</div>
            