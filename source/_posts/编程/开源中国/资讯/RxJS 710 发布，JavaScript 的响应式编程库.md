
---
title: 'RxJS 7.1.0 发布，JavaScript 的响应式编程库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9269'
author: 开源中国
comments: false
date: Tue, 25 May 2021 06:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9269'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RxJS 是用于 JavaScript 的响应式编程库。RxJS 7.0 版本是对 RxJS 6.x 的重写，也是 RxJS 的最新生产版本。这次重写是为了有更好的性能，更好的模块化，更好的可调试的调用栈，同时保持大部分向后兼容。</p> 
<p>RxJS 7.1.0 正式发布，该版本更新内容如下：</p> 
<p><strong>Bug 修复：</strong></p> 
<ul> 
 <li>从 multicast 操作符 <code>share</code>、 <code>publish</code>、 <code>publishReplay</code> 返回的操作符函数现在是引用透明的。这意味着如果你把调用 <code>publishReplay(3)</code> 的结果传递给一个以上的 observable 的 <code>pipe</code> 方法，它在每种情况下的行为都是一样的，而不是产生累积效应，这是在第 6 版的某个时候引入的一个回归。</li> 
</ul> 
<p><strong>特性：</strong></p> 
<ul> 
 <li>所有主体现在都有一个 <code>observed</code> 的属性。这将允许用户在无需我们访问 <code>observers</code> 数组的情况下检查一个主体是否有当前的订阅者，而 <code>observers</code> 数组将在未来的版本中成为私有；</li> 
 <li>groupBy：支持命名参数，支持 ObservableInputs 的持续时间选择器；</li> 
 <li>Share：使用另一个 observable 来控制复位；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FReactiveX%2Frxjs%2Fblob%2Fmaster%2FCHANGELOG.md" target="_blank">https://github.com/ReactiveX/rxjs/blob/master/CHANGELOG.md</a></p>
                                        </div>
                                      
</div>
            