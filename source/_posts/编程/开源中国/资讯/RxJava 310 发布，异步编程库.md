
---
title: 'RxJava 3.1.0 发布，异步编程库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2146'
author: 开源中国
comments: false
date: Wed, 11 Aug 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2146'
---

<div>   
<div class="content">
                                                                                            <p>RxJava 是一个在 Java VM 上使用可观测的序列来组成异步的、基于事件的程序的库。它扩展了 observer pattern 以支持数据/事件序列，并添加了运算符，使您可以声明性地将序列组合在一起，同时抽象化了对低级线程、同步、线程安全和并发数据结构等问题的关注。</p> 
<p>RxJava 3.1.0 正式发布，此次更新内容如下：</p> 
<ul> 
 <li>随着这个版本的发布，最低要求的 Android API 级别是 API 21（Android 5.0）；</li> 
</ul> 
<p>增加的 API：</p> 
<ul> 
 <li><code>subscribe([...], DisposableContainer)</code>，以便更好地 <code>Disposable</code> 管理和清理引用；</li> 
 <li><code>RxJavaPlugins.createExecutorScheduler()</code> 用于在 <code>Schedulers</code> 类被初始化之前创建一个基于 <code>Scheduler</code> 的 <code>Executor</code>；</li> 
</ul> 
<p>行为改变：</p> 
<ul> 
 <li>调度器清除线程已被删除，删除已取消的定时操作现在由底层 <code>ScheduledExecutorService</code> 的 <code>setRemoveOnCancelPolicy</code> 管理；</li> 
</ul> 
<p>文档：</p> 
<ul> 
 <li>修复了 <code>Schedulers.from</code> 的 <code>fair</code> 参数的措辞；</li> 
 <li>更新 <code>withLatestFrom</code> 的 javadoc，关于上游的早期完成；</li> 
</ul> 
<p>其他</p> 
<ul> 
 <li>对通用类型参数的 <code>@NonNull</code> 注解进行了统一；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FReactiveX%2FRxJava%2Freleases%2Ftag%2Fv3.1.0" target="_blank">https://github.com/ReactiveX/RxJava/releases/tag/v3.1.0</a></p>
                                        </div>
                                      
</div>
            