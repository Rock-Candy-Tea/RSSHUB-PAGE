
---
title: 'IPython 8.5 发布，Python 交互式解释器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4437'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4437'
---

<div>   
<div class="content">
                                                                                            <p>IPython 是一个综合环境，可以帮助程序员或开发人员等高级计算机用户测试或探索各种功能。尽管 Python 附带了一个强大的交互式解释器，使用户无需在目标计算机上创建额外的文件即可运行测试，但它在用户与软件交互方面存在一些限制。</p> 
<p>IPython 的三个核心部分包括一个高度交互式的 Python shell，一个解耦的双进程通信模型和交互式并行计算的架构。</p> 
<p>IPython 8.5 是 8.0 之后的第五个小版本，更新内容如下：</p> 
<ul> 
 <li>增加了接受自动建议的快捷方式</li> 
 <li>当生成 latex 时，没有弹出窗口显示在 Windows 下</li> 
 <li>修正了当试图用 tab 补全一个带有连续句号或正斜杠的输入字符串时（如 "file:///var/log/..."）出现的错误</li> 
 <li>Latex 渲染中的相对文件名： <code>latex_to_png_dvipng</code> 命令在内部生成了输入和输出文件参数给 <code>latex</code> 和 <code>dvipis</code>。这些参数现在被生成为当前工作目录的相对文件，而不是绝对文件路径。这解决了一个问题，即当前工作目录包含的字符不能被 <code>latex</code> 和 <code>dvips</code> 正确处理。</li> 
 <li>修正了一个错误，即用 ipython-sphinx 扩展执行的重组文本文件中的 ipython 代码块会跳过任何包含 python 装饰器的代码行</li> 
 <li>允许重新加载一些有冻结数据类的模块</li> 
 <li>在 deque 的 repr 中显示 maxlen</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fipython%2Fipython%2Freleases%2Ftag%2F8.5.0" target="_blank">https://github.com/ipython/ipython/releases/tag/8.5.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            