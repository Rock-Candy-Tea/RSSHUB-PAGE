
---
title: 'AWS领导力原则解读（四）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3864'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 17:52:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3864'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">正确决策</h2>
<p>正确抉择在我看来需要经过以下几个过程：</p>
<h3 data-id="heading-1">搞清问题本质</h3>
<p>我们一定要对问题有个准确的定义，搞清楚它的<code>root cause</code>。比如对一个线上的问题，要分析它是每天固定时间产生还是随机产生，使用户误操作还是潜在的<code>bug</code>，是平时就会有还是高并发环境下才会有。当然这个过程还要配合各种日志分析和工具诊断。比如应用系统本身日志，操作系统日志，对于<code>java</code>来说通过<code>jstack</code>等工具来辅助分析，另外还有系统的监控等。通过这一系列的分析我们一般情况下能拿到<code>root cause</code>的。如果有人问如果做完各种分析还是不知道<code>root cause</code>怎么办？ 像这种问题一般都是性能问题，我也遇到过，当时就采取了定时重启的方式，当然这是建立一种高可用架构上的，也就是说不会在某一台<code>server</code>重启过程中整个系统都不可用。当然，这种方式有它的局限性，比如何时去重启最合适等。</p>
<h3 data-id="heading-2">群策群力</h3>
<p>孔子说过，三人行必有我师。单靠个人即使经验再丰富也有想不到的点，而这些点很可能就隐藏着一个巨大风险。</p>
<p>对于一般的问题，通过自身积累的经验并配合网上类似问题的答案，我们是可以快速解决的。但是对于重大问题，比如会影响整个架构的问题，这个时候要群策群力。群策群力的形式很多，拿我自己来说，一般情况下我会<code>call a meeting</code>,<code>involve</code>直线领导，其他资深架构师来一起讨论。有时比如遛弯时跟其他同事咨询一下，很可能别人的一句话就真的点醒梦中人了。</p>
<h3 data-id="heading-3">要有兜底措施</h3>
<p>即使我们前期考虑的再全面，执行再细致，实际过程中还是会出现这样那样的问题。所以此时我们一定要有个兜底的措施。一般来说就是要为最坏情况设置应急措施，比如电商网站采用的服务降级的方案。在天猫“双十一”或者京东“618”这几天，并发量会非常大，如果真的出现并发问题，一定要保证核心业务不受影响。比如坚决不能影响用户下单，但是物流信息可以暂时做降级处理，用户可能在活动期间无法及时刷出物流信息。</p>
<h3 data-id="heading-4">决策失败的例子</h3>
<p>有一次做实时数据传输的项目，因为之前刚做了一个类似的，而且成功上线了。所以这次拿到需求后心里还是很有把握的。对于实时数据传输，我们的重点要保证数据在传输过程中不丢，不重，不乱序以及实时性。所以当时重心还是放在了传输本身这块。但是却忽视了需求中的一句话：支持用户灵活定制报表。其实这句话当时也看到了，但是没有引起足够重视，觉得用户要求的定制度没那么高，可在跟用户进行原型沟通的时候发现我们自己开发的界面远远不能满足用户的定制化需求。所以我们下来又紧急开会，寻找替代方法。最后我们找了个第三方的专业报表组件，组件找到又发现另外的问题，就是它要求的数据格式我们提供的不一样，所以我们又开发一个适配器来做转换。虽然最终满足了用户需求，但是这段时间搞的很狼狈，给客户造成的感觉也不是很好。这个案例其实就是对问题考虑的不够全面。</p>
<h3 data-id="heading-5">总结</h3>
<p>上面提到的那三点其实就是对应决策的三个阶段：事前，事中和事后。
事前：就是要对问题就行深入全面的分析
事中：要群策群力，发挥集体的智慧对决策进行深入讨论
事后：一定要有兜底方案，当出现意外情况时，要有应急措施</p></div>  
</div>
            