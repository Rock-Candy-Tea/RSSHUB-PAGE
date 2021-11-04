
---
title: 'Scala 2.13.7 发布，多范式编程语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2572'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2572'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">Scala 2.13.7 现已发布。这</span><span style="background-color:#ffffff; color:#333333">是一门现代的多范式编程语言，志在以简练、优雅及类型安全的方式来表达常用编程模式。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<h4>Align with Scala 3</h4> 
<ul> 
 <li>更新 TASTy 阅读器以支持 Scala 3.1（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9791" target="_blank">#9791</a>）</li> 
 <li>允许在<code>-Xsource:3</code>下 <code>import x.&#123;*, given&#125;</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9724" target="_blank">#9724</a>）</li> 
 <li>即使没有<code>-Xsource:3</code>也允许在模式绑定中使用大小写（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9721" target="_blank">#9721</a>）</li> 
 <li>弃用顶级通配符类型参数（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9712" target="_blank">#9712</a>）</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>JDK 和 Java 兼容性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>支持 JDK 18（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9702" target="_blank">#9702</a> ）</li> 
 <li>在 Java sources 中支持 JDK 16 records（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9551" target="_blank">＃9551</a>）</li> 
 <li>允许在 Java sources 中使用具体的私有接口方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9748" target="_blank">#9748</a>）</li> 
 <li>在 JDK 9+ 上使用<code>StringConcatFactory</code>进行字符串连接（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9556" target="_blank">＃9556</a>）</li> 
</ul> 
<h4>Android <span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>兼容性</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>添加<code>ClassValueCompat</code>，以支持没有<code>java.lang.ClassValue</code>的系统（例如 Android）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9752" target="_blank">#9752</a>）</li> 
 <li>为了 Android 兼容性，使<code>Statics.releaseFence()</code>也可以捕获<code>java.lang.invoke.VarHandle.releaseFence()</code>调用的<code>NoSuchMethodException</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9739" target="_blank">#9739</a>）</li> 
</ul> 
<h4>Concurrency</h4> 
<ul> 
 <li>修复<code>Future#&#123;zip,zipWith,traverse,sequence&#125;</code>的非对称失败行为，使其无论如何排序都能快速失败。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9655" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flihaoyi" target="_blank">9655</a>）</li> 
</ul> 
<h4>Collections</h4> 
<ul> 
 <li>让<code>ArrayBuffer</code>的迭代器在缓冲区发生变异时快速失效（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9258" target="_blank">#9258</a>）</li> 
 <li>修复<code>ArrayOps</code>错误（通过避免<code>ArraySeq#array</code>，不保证元素类型）（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9641" target="_blank">#9641</a>）</li> 
 <li>弃用<code>IterableOps.toIterable</code>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9774" target="_blank">#9774</a>）</li> 
</ul> 
<h4><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h4> 
<ul> 
 <li>接受标识符中的补充 Unicode 字符（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9687" target="_blank">#9687</a>）</li> 
 <li>改进 REPL 中的 tab completion 和 code assist（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Fpull%2F9656" target="_blank">#9656</a>）</li> 
</ul> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更多详情可查看：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fscala%2Fscala%2Freleases%2Ftag%2Fv2.13.7" target="_blank">https://github.com/scala/scala/releases/tag/v2.13.7</a></p>
                                        </div>
                                      
</div>
            