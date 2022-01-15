
---
title: 'Scala 2.13.8 发布，多范式编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=426'
author: 开源中国
comments: false
date: Sat, 15 Jan 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=426'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">Scala 2.13.8 现已发布，这是一个适度的增量版本，主要是解决2.13.7中的回归问题。这</span><span style="background-color:#ffffff; color:#333333">是一门现代的多范式编程语言，志在以简练、优雅及类型安全的方式来表达常用编程模式。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">Highlights</span></strong></p> 
<ul> 
 <li>让 REPL 在 Mac M1 上再次工作（升级 JLine 和 JNA）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9807" target="_blank">#9807</a> by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FSethTisue" target="_blank">@SethTisue</a>）</li> 
 <li>修复 IndexedSeqs 视图的切片问题（包括修复 2.13.7<code>reverseIterator</code>回归）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9799" target="_blank">#9799</a> by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsom-snytt" target="_blank">@som-snytt</a>）</li> 
 <li>修复 2.13.7 隐式解析的回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9829" target="_blank">#9829</a> by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FjoroKr21" target="_blank">@joroKr21</a>）</li> 
 <li>修复 2.13.7<code>releaseFence</code>回归，影响 GraalVM 兼容性（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9825" target="_blank">#9825</a> by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flrytz" target="_blank">@lrytz</a>）</li> 
 <li>修复 2.13.7 影响通配符和 F-bounded 类型的回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9806" target="_blank">#9806</a> by <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FjoroKr21" target="_blank">@joroKr21</a>）</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>此版本中还包含一些将在 2.12.16 中发布的小更改。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>有关完整的 2.13.8 更改列表，可参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpulls%3Fq%3Dis%253Amerged%2520milestone%253A2.13.8" target="_blank">所有合并的 PR</a> 和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fbug%2Fissues%3Futf8%3D%25E2%259C%2593%26q%3Dis%253Aclosed%2Bmilestone%253A2.13.8" target="_blank">所有已关闭的</a> </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fbug%2Fissues%3Futf8%3D%25E2%259C%2593%26q%3Dis%253Aclosed%2Bmilestone%253A2.13.8" target="_blank">bug</a><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>兼容性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>与次要版本一样，Scala 2.13.8 与整个 Scala 2.13 系列二进制兼容。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>从 2.12 升级？升级时启用<code>-Xmigration</code>以向编译器请求迁移建议。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更新说明：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Freleases%2Ftag%2Fv2.13.8" target="_blank">https://github.com/scala/scala/releases/tag/v2.13.8</a></p>
                                        </div>
                                      
</div>
            