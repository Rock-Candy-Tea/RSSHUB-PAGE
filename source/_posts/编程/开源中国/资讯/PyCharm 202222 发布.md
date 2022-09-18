
---
title: 'PyCharm 2022.2.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8114'
author: 开源中国
comments: false
date: Sun, 18 Sep 2022 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8114'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#27282c">PyCharm 2022.2.2 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fpycharm%2F2022%2F09%2F2022-2-2%2F" target="_blank">发布</a>，这是第二个错误修复更新。在这个小版本中，开发团队对 Python dataclass 支持进行了重大改进。 </span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>对于 attrs 包，PyCharm 现在可以识别现代 API，比如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attrs.define" target="_blank">attrs.define</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attr.attrs.mutable" target="_blank">attrs.mutable</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attr.attrs.frozen" target="_blank">attrs.frozen</a>，它们的处理方式与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attr.s" target="_blank">attr.s</a> 相同，而 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attrs.field" target="_blank">attrs.field</a> 的处理方式则与 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.attrs.org%2Fen%2Fstable%2Fapi.html%23attr.ib" target="_blank">attr.ib</a> 相同。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">PyCharm 可以识别文档中对类属性的引用，在数据类和命名图元的定义中最为突出。数据类属性的重命名重构已得到改进。在构造函数调用中重命名它们将更新定义，反之亦然。这还包括从文档字符串中重命名属性。 </span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span style="color:#000000"><span style="background-color:#ffffff">具体包括以下修复和改进：</span></span></p> 
<ul> 
 <li>修复回归：Python 控制台适用于使用先前 PyCharm 版本设置远程解释器的项目。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55396" target="_blank">PY-55396</a> ]</li> 
 <li>修复回归：在 SSH 或 WSL 上创建新的 Django 项目，具有特定的目录结构和必要的环境。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-55110" target="_blank">PY-55110</a> ]</li> 
 <li>修复回归：对位于 Docker 镜像中的 non-root 用户的解释器进行自省，现在可以工作了。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-50970" target="_blank">PY-50970</a> ]</li> 
 <li>现在可以在类型提示中识别内置的参数化“类型”。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-46257" target="_blank">PY-46257</a> ]</li> 
 <li>enum.auto() 调用不再报告为需要参数。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FPY-53388" target="_blank">PY-53388</a> ]</li> 
 <li>Markdown 自动格式化操作现在可以正确格式化带有表格的 Markdown 文件。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-262735%2FMarkdown-auto-formatting-messes-up-with-markdown-in-tables-when-it-wraps-the-line" target="_blank">IDEA-262735</a> ]</li> 
 <li>IDE 现在在后台显示一个 balloon 通知，用于以失败结果结束的预提交检查。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-265084%2FPre-commit-checks-in-background-Show-balloon-notification-when-checks-are-finished-with-failing-results" target="_blank">IDEA-265084</a> ]</li> 
 <li>性能改进：启用 watch return values 选项后，调试性能不再下降。[ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FIDEA-300696%2FSlow-stepping-with-Show-Method-Return-Values-option-enabled" target="_blank">IDEA-300696</a> ]</li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#27282c"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyoutrack.jetbrains.com%2Farticles%2FPY-A-233538002%2FPyCharm-202222-222416733-build-Release-Notes" target="_blank">可以在发行说明</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="color:#000000"><span style="background-color:#ffffff">中找到已解决问题的完整列表。</span></span></span></span></span></p>
                                        </div>
                                      
</div>
            