
---
title: 'IPython 8.3.0 发布，Python 交互式解释器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9282'
author: 开源中国
comments: false
date: Sun, 01 May 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9282'
---

<div>   
<div class="content">
                                                                                            <p>IPython 是一个综合环境，可以帮助程序员或开发人员等高级计算机用户测试或探索各种功能。尽管 Python 附带了一个强大的交互式解释器，使用户无需在目标计算机上创建额外的文件即可运行测试，但它在用户与软件交互方面存在一些限制。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">IPython 的三个核心部分包括一个高度交互式的 Python shell，一个解耦的双进程通信模型和交互式并行计算的架构。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">IPython 8.3.0 现已发布，更新内容如下：</p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fipython%2Fipython%2Fpull%2F13625%2F" target="_blank">PR #13625</a>，使用</span></span></span><code><span>?</span></code><span style="background-color:#fcfcfc; color:#404040">,<span> </span></span><code><span>??</span></code><span style="background-color:#fcfcfc; color:#404040">,<span> </span></span><code><span>*?</span></code><span><span><span>不会调用<code><span>set_next_input</span></code>，因为大多数前端允许适当的多行编辑，这给 multi-cell frontends 的许多用户带来了问题。这已被向后移植到了 7.33 版本。</span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fipython%2Fipython%2Fpull%2F13600%2F" target="_blank">PR #13600</a>，<code><span>pre_run_*</span></code>-hooks 在前端提供的 info object 上现在会有一个<code><span>cell_id</span></code>属性。这已被向后移植到了 7.33 版本。</span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fipython%2Fipython%2Fpull%2F13624%2F" target="_blank">PR #13624</a> 修复了接受 auto-suggestion 后 End key 被破坏的问题</span></span></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fipython%2Fipython%2Fpull%2F13657%2F" target="_blank">PR #13657</a> 修复了来自不同会话的历史记录会混合的问题。</span></span></span></p> </li> 
</ul> 
<p>详情<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fipython.readthedocs.io%2Fen%2Fstable%2Fwhatsnew%2Fversion8.html%23ipython-8-3-0" target="_blank">可查看官方公告</a>。</p>
                                        </div>
                                      
</div>
            