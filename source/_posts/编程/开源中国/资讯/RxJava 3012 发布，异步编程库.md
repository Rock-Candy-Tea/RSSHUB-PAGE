
---
title: 'RxJava 3.0.12 发布，异步编程库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5831'
author: 开源中国
comments: false
date: Tue, 13 Apr 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5831'
---

<div>   
<div class="content">
                                                                                            <p>RxJava 是一个在 Java VM 上使用可观测的序列来组成异步的、基于事件的程序的库。它扩展了 observer pattern 以支持数据/事件序列，并添加了运算符，使您可以声明性地将序列组合在一起，同时抽象化了对低级线程、同步、线程安全和并发数据结构等问题的关注。</p> 
<p>RxJava 3.0.12 正式发布，此次更新内容如下：</p> 
<p>Bug 修复：</p> 
<ul> 
 <li><code>CompositeException.printStackTrace</code> 直接写入 <code>PrintStream</code>/ <code>PrintWriter</code>；</li> 
</ul> 
<p>文档：</p> 
<ul> 
 <li>修正 <code>Single.flattenStreamAsObservable</code> javadoc 中的错误引用；</li> 
 <li>修正违反 Javadoc 的样式；</li> 
</ul> 
<p>其他：</p> 
<ul> 
 <li>修正 POM_URL；</li> 
 <li>升级 Gradle 到 6.8.3；</li> 
 <li>优化 Gradle 配置；</li> 
 <li>添加 Javadoc 检查到 Checkstyle，修正违反 Javadoc 的问题；</li> 
 <li>现代化 Gradle 插件块，将 maven 改为 maven-publish；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FReactiveX%2FRxJava%2Freleases" target="_blank">https://github.com/ReactiveX/RxJava/releases</a></p>
                                        </div>
                                      
</div>
            