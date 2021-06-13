
---
title: 'Android弹窗管理设计及在招聘首页实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ff0fab8f6e24faeb6e24ac97e7a12fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 19:23:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ff0fab8f6e24faeb6e24ac97e7a12fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、背景</h2>
<p>   由于业务需要，页面中通常会有很多弹窗功能。并且由于叠加展示的用户体验不好的原因，这些弹窗通常会被要求互斥出现。</p>
<p>  在之前的设计里，这些弹窗是杂乱没有管理的。每次新添加一个弹窗业务，需要考虑与已有弹窗的互斥出现。这种无管理弹窗的实现方式主要有以下缺点：</p>
<p>1、需要对各弹窗出现逻辑进行状态区分，以达到互斥。每添加一个新弹窗，就需要添加对应的状态进行管理判断。弹窗业务杂糅，且容易遗漏互斥关系。</p>
<p>2、进入页面根据每个弹窗业务的展示逻辑来判断是否触发该弹窗的展示，因此无论触发的弹窗业务是否成功，其余弹窗都没有机会展示。弹窗少了当次可能的曝光机会。</p>
<p>3、目前没支持弹窗的顺序展现，如果要支持，各弹窗逻辑会互相耦合。</p>
<p>   针对上述痛点，需要对业务弹窗进行抽象和统一管理，以达到按权重自行进行排序弹出的目的。最终实现以下功能：</p>
<p>1、各弹窗逻辑隔离，是否弹出完全由弹窗管理类决定。高优先级弹窗失败，会按照优先级高低弹出低优先级弹窗。</p>
<p>2、弹窗出现的优先级由接口动态下发，可以根据产品需要，动态调整弹窗出现优先级。</p>
<h2 data-id="heading-1">二、实现</h2>
<p>1、弹窗抽象</p>
<p>1）弹窗类型定义：PopType</p>
<p>使用枚举实现，用于区分不同的弹窗。</p>
<p>2）弹窗实体对象：PopData</p>
<p>针对弹窗数据的抽象，弹窗的数据实体，定义了弹窗类型、唯一标识id、弹窗内容。</p>
<p>3）弹窗任务：Task</p>
<p>弹窗业务逻辑的具体执行体，包括但不限于网络请求等任务，用于产生弹窗数据和优先级排序。定义了任务唯一标识id、优先级，并且实现了Comparable接口用于排序。</p>
<p>2、弹窗任务管理类TaskManager</p>
<p>用于管理弹窗出现，主要维护一个弹窗任务优先级队列，按优先级顺序决定哪个弹窗可以弹出。</p>
<p>首先弹窗Task实现了Comparable接口 使其具备通过优先级比较大小的能力</p>
<p>TaskManager内部使用PriorityQueue作为弹窗任务容器，PriorityQueue内部使用**堆排序对内部元素进行排序，**每添加或删除一个Task元素都会对队列按优先级进行调整。</p>
<p>每次任务返回数据时，如果该任务是顶部Task，则直接弹出该任务对应的弹窗。否则，将弹窗数据入队列。</p>
<p>如果弹窗Task未返回正常数据，则将任务队列中该Task移除。并判断当前TaskQueue中的顶部Task是否有返回值，有则弹出；否则，继续等待下个任务的返回结果，重复上述过程。</p>
<p> 架构设计如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ff0fab8f6e24faeb6e24ac97e7a12fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            