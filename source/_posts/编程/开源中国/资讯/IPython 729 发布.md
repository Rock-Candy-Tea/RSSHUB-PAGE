
---
title: 'IPython 7.29 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7969'
author: 开源中国
comments: false
date: Sun, 31 Oct 2021 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7969'
---

<div>   
<div class="content">
                                                                                            <p>IPython 是一个综合环境，可以帮助程序员或开发人员等高级计算机用户测试或探索各种功能。尽管 Python 附带了一个强大的交互式解释器，使用户无需在目标计算机上创建额外的文件即可运行测试，但它在用户与软件交互方面存在一些限制。</p> 
<p>IPython 的三个核心部分包括一个高度交互式的 Python shell，一个解耦的双进程通信模型和交互式并行计算的架构。</p> 
<p>IPython 7.29 发布，更新内容如下：</p> 
<ul> 
 <li>修复了显示数字时返回 base64 而不是字节的问题；</li> 
 <li>修正与 PyQt6、PySide 6 的兼容性；</li> 
 <li>修复 matplotlib qtagg eventloop；</li> 
 <li>修复多个文档及其中的错别字；</li> 
 <li>调试器现在会在 SigInt 时默认退出，如果你忘记退出调试器，这在笔记本中会很有用。"Interrupt Kernel" 现在将存在于调试器中；</li> 
 <li>它使 Pdb 有能力跳过装饰器中的代码。如果函数包含一个特殊的值名 <code>__debuggerskip__ = True|False</code>，函数将不会被步进，只有当该值被设置为 <code>False</code> 时，Pdb 才会步进下层框架；</li> 
 <li>IPython 的主分支正在接受一些改变，因为我们收到了 NumFOCUS 的 SDG（4800美元），以帮助我们完成用 pytest 替换 nose 的工作，并使 IPython 在未来的 8.0 版本中得到验证；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fipython.readthedocs.io%2Fen%2Fstable%2Fwhatsnew%2Fversion7.html%23ipython-7-29" target="_blank">https://ipython.readthedocs.io/en/stable/whatsnew/version7.html#ipython-7-29</a></p>
                                        </div>
                                      
</div>
            