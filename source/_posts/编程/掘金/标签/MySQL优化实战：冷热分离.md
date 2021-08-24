
---
title: 'MySQL优化实战：冷热分离'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe966257d104b42b65d57f0388dd73a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 08:00:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe966257d104b42b65d57f0388dd73a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家在用淘宝，饿了么，美团等app的时候，相信都看到过历史订单中，只能查询到最近几个月的订单。这是因为，随着业务发展，数据库增长的很快。数据量达到几千万，甚至上亿。这么庞大的数据量，让平台的订单查询非常缓慢，我之前也说到过，千万的表查询就已经很慢了。这时候要是操作人员手欠，多点几次，CPU飙升，请求阻塞，最后宕机。所以，这个时候就有一种优化手段，叫做冷热分离，也就是大家在app中看到的，只能查询最近几个月的数据（热数据）想要查询冷数据就不能在你的app上查询到了。</p>
<h1 data-id="heading-0">什么是冷热分离</h1>
<p>顾名思义就是分成两个库，一个是冷库一个是热库，几个月之前不常用的数据放到冷库中，最新的数据比较新的数据放到热库中。这里其实就和JVM里面的新生代和老年代是类似的，有些数据经常用的，最终会放到老年代，不经常用的数据会在新生代GC的时候就会销毁，没GC的时候会存在新生代中</p>
<h1 data-id="heading-1">什么情况下用冷热分离？</h1>
<ol>
<li>旧的数据不在会修改，也就是只有读没有写的情况下</li>
<li>用户不在意老的数据，老的数据对用户来说没有什么用的情况下，如订单，学校管理系统中，班任带的之前届的学生等。</li>
</ol>
<h1 data-id="heading-2">如何设计冷热数据分离？</h1>
<p>以订单为例，我们只需要判断下单时间和是否完成就行了。比如，一个订单是大于半年且已完成的订单，那这个订单其实就可以认为是冷数据，一个用户不可能去找申请退款半年之前的订单吧，那只能说这用户是碰瓷的，那更得阻止这种用户让他查不到半年之前订单。当然，是半年还是三个月还是一个月，这就得看你们实际场景了。也可以根据其他条件，比如是否完成啊，完成的就算冷数据，不完成就热数据等</p>
<h1 data-id="heading-3">如何实现冷热数据分离？</h1>
<p>这里其实很多人都会想到用监听数据库变更日志binlog的方式来触发，但是这种方式的话，阿里云rds是没有super权限的。而且也无法按照时间来区分冷热，当数据为冷数据，期间没有进行任何操作，同时也需要考虑数据并发问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe966257d104b42b65d57f0388dd73a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二种方式就是通过定时任务：</p>
<p>可以每天半夜进行定时扫描热数据，进行冷热识别，之后同步到冷数据库里面。定时任务也有个缺点就是无法做到实时，并且会出现数据量比较大，一次性处理不完的情况。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f2b12bcc4f9476aafda28b9149e4808~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们还需要保证数据的一致性。可以通过分布式事务来保证数据的一致性。但是一删一增比较耗性。还有一种方案：</p>
<ol>
<li>在热数据库中，给要搬的数据加个标识：flag=1。（实际处理中标识字段的值用数字就可以，这里是为了方便理解。）</li>
<li>找出所有待搬的数据（flag=1）：这步是为了确保前面有些线程因为部分原因失败，出现有些待搬的数据没有搬的情况</li>
<li>在冷数据库中保存一份数据，但在保存逻辑中需加个判断以此保证幂等性（这里需要用事务包围起来），通俗点说就是假如我们保存的数据在冷数据库已经存在了，也要确保这个逻辑可以继续进行</li>
<li>从热数据库中删除对应的数据</li>
</ol>
<h2 data-id="heading-4">针对定时任务方式，假设数据量比较大，一次性处理不完，怎么办？</h2>
<p>这里可以结合缓冲区的理念，我们进行分批执行，比如，一百条来执行</p>
<ol>
<li>在热数据库中给要搬的数据加个标识：flag=1；</li>
<li>找出前 50 条待搬的数据</li>
<li>在冷库中保存一份数据</li>
<li>从热库中删除对应数据</li>
<li>循环执行</li>
</ol>
<p>同时，如果实在太大，我们也可以开启多线程并发执行。但是这就需要好好设计并发代码了。</p>
<p>冷热分离的不足：</p>
<ol>
<li>用户查询冷数据还是很慢</li>
<li>业务无法修改冷数据，冷数据量大了之后需要通过分库分表来解决</li>
</ol></div>  
</div>
            