
---
title: 'Python 3.10.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8354'
author: 开源中国
comments: false
date: Fri, 09 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8354'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Python 3.10.7 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.python.org%2F2022%2F09%2Fpython-releases-3107-3914-3814-and-3714.html" target="_blank">发布</a>，这个错误修复版本是为了解决 CVE 问题而提前发布的。因此与同一阶段的 3.10.6（200 次 commit）或者一年前发布周期的同一阶段的 3.9.7（187 次 commit）相比，其包含的修改数量要较少。但是在这个最新的 Python 版本中仍有超过 100 次 commit，详情可</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.10.7%2Fwhatsnew%2Fchangelog.html" target="_blank">查看</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.10.7%2Fwhatsnew%2Fchangelog.html" target="_blank">change log</a>。</p> 
<p><span style="color:#000000">与 3.9 相比，3.10 系列中的主要新功能包括有：</span></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0623%2F" target="_blank">PEP 623</a> – 弃用并准备移除 PyUnicodeObject 中的 wstr 成员</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0604%2F" target="_blank">PEP 604</a> – 支持以 X | Y 的形式编写联合类型 (union types)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0612%2F" target="_blank">PEP 612</a> – 引入参数规范变量 (Parameter Specification Variables)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0626%2F" target="_blank">PEP 626</a> – 为调试和其他工具添加精确的行号</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0618%2F" target="_blank">PEP 618 </a>– 将 Optional Length-Checking 添加到 zip</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue12782" target="_blank">bpo-12782</a>: 现在正式支持 Parenthesized context managers</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0632%2F" target="_blank">PEP 632 </a>– 弃用 distutils 模块</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0613%2F" target="_blank">PEP 613 </a>– 引入显式类型别名</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0634%2F" target="_blank">PEP 634 </a>– 结构化模式匹配 (Structural Pattern Matching)：Specification</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0635%2F" target="_blank">PEP 635 </a>– 结构化模式匹配 (Structural Pattern Matching)：Motivation & Rationale</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0636%2F" target="_blank">PEP 636 </a>– 结构化模式匹配 (Structural Pattern Matching)：Tutorial</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0644%2F" target="_blank">PEP 644 </a>– 要求使用 OpenSSL 1.1.1 或更高版本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0624%2F" target="_blank">PEP 624 </a>– 删除 Py_UNICODE encoder API</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0597%2F" target="_blank">PEP 597 </a>– 增加可选的 EncodingWarning</li> 
</ul> 
<p>该列表此前还曾包括 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue38605" target="_blank">bpo-38605</a><span style="background-color:#f9f9f9; color:#444444">:<span> </span></span><code>from <strong>future</strong> import annotations</code><span style="background-color:#f9f9f9; color:#444444"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0563%2F" target="_blank">PEP 563</a><span style="background-color:#f9f9f9; color:#444444">)</span><span style="color:#000000">，但由于一些兼容性问题，它已被推迟到 Python 3.11。可以在</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmail.python.org%2Farchives%2Flist%2Fpython-dev%40python.org%2Fthread%2FCLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ%2F" target="_blank">此处</a><span style="color:#000000">了解更多信息。</span></p>
                                        </div>
                                      
</div>
            