
---
title: 'Python 3.10 beta 4 发布，下个版本进入 RC 阶段'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3932'
author: 开源中国
comments: false
date: Mon, 12 Jul 2021 06:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3932'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Python 3.10 的第四个 beta 测试预览版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpythoninsider.blogspot.com%2F2021%2F07%2Fpython-3100b4-is-available.html" target="_blank">已发布</a>。Python 开发团队称这也是计划中的最后一个测试版，下一次发布的更新将会是 RC 版本。</p> 
<p>虽然 Python 开发团队的计划是在 beta 阶段完成所有已确定的 feature，但在 RC 版本发布之前仍可能会对个别 feature 进行修改，或在极少数情况下进行删除。其目标是在 beta 4 发布后不再变更 ABI，并且在第一个 RC 版本 3.10.0rc1 发布之后尽可能少地修改代码。为实现这一目标，在 beta 阶段进行广泛的测试极其重要。</p> 
<p>Python 3.10 系列的主要新 feature 如下（目前仍在编写中，最终发布的版本会有所变动）：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0623%2F" target="_blank">PEP 623</a> – 弃用并准备移除 PyUnicodeObject 中的 wstr 成员</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0604%2F" target="_blank">PEP 604</a> – 更清晰的 union 类型语法：X | Y</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0612%2F" target="_blank">PEP 612</a> – 引入参数规范变量 (Parameter Specification Variables)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0626%2F" target="_blank">PEP 626</a> – 为调试和其他工具提供准确的代码行号</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0618%2F" target="_blank">PEP 618 </a>– 为内置的 zip 函数添加可选的长度检查 (Length-Checking) 功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue12782" target="_blank">bpo-12782</a>：带括号的上下文管理器 (Context Manager)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0632%2F" target="_blank">PEP 632 </a>– 弃用 distutils 模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0613%2F" target="_blank">PEP 613 </a>– 显示的类型别名 (Type Aliases) </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0634%2F" target="_blank">PEP 634 </a>– 结构化的模式匹配 (Structural Pattern Matching)：Specification</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0635%2F" target="_blank">PEP 635 </a>– 结构化的模式匹配 (Structural Pattern Matching)：Motivation and Rationale</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0636%2F" target="_blank">PEP 636 </a>– 结构化的模式匹配 (Structural Pattern Matching)：Tutorial</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0644%2F" target="_blank">PEP 644 </a>– 要求使用 OpenSSL 1.1.1 或更高版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0624%2F" target="_blank">PEP 624 </a>– 移除 Py_UNICODE 编码器 API</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0597%2F" target="_blank">PEP 597 </a>– 添加可选的 EncodingWarning</li> 
</ul> 
<p><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100b4%2F" target="_blank">Python 3.10 beta 4 下载地址</a></strong></p> 
<p>按照计划，下一次发布的更新将会是 Python 3.10.0 的第一个 RC 版本，即 3.10.0rc1，暂定的发布时间为 2021-08-02，稳定版则<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0619%2F" target="_blank">计划</a>于 2021-10-04 发布。</p>
                                        </div>
                                      
</div>
            