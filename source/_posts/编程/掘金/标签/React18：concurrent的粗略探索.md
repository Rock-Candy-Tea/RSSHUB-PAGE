
---
title: 'React18：concurrent的粗略探索'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d379da973fe48d99a4807d1e008b606~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 23 Jun 2021 18:16:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d379da973fe48d99a4807d1e008b606~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>concurrent作为react团队提了几年的ui模式，这么久了一直没有在实际工程中落地。虽然我们现在使用的react的reconcile核心已经为concurrent模式从stack重构成了fiber，但现在的react更新仍然是同步模式而不是concurrent模式。react 17版本没有breaking change和新增的api，主要就是为了concurrent模式过渡，或许在react 18中有希望正式发布，所以简单的做一个concurrent模式的前瞻。</p>
<blockquote>
<p><a href="https://juejin.cn/post/6903050346143318023" target="_blank">加入我们</a>，一起搞事</p>
</blockquote>
<h1 data-id="heading-0">什么是concurrent</h1>
<p>concurrent主要指的是“可中断渲染”，并不是真的并发，因为js本身是单线程的。渲染可中断，就可以保持应用快速响应，避免阻塞，可以定义渲染的优先级，让要更优先进行的渲染工作先完成。在没有concurrent模式之前，任何react的组件的更新都是自顶向下递归完成，中间不会被打断，在有了concurrent模式之后，我们就可以避免这种情况，让一些更高优先级的打断渲染的过程，比如动画，用户输入等等。react concurrent模式刚提出的时候网上有 <a href="https://github.com/claudiopro/react-fiber-vs-stack-demo" target="_blank" rel="nofollow noopener noreferrer">demo</a> 比对过两种模式的差异，在这个demo里面可以看到concurrent模式下页面的动画相对流畅很多，不过是4年前的demo了，接下来会使用最新的react的api重构这个demo，体验应用concurrent模式带来的变化。</p>
<h1 data-id="heading-1">Sync更新模式造成卡顿</h1>
<p>我们渲染了一个很多节点的谢尔宾斯基三角形，通过 <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/window/requestAnimationFrame" target="_blank" rel="nofollow noopener noreferrer">raf</a> 用js写了一个伸缩的动画，并设置一个定时器，每一秒钟去更新所有节点的文本，代码如下
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d379da973fe48d99a4807d1e008b606~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
在实际的渲染中发现动画比较卡顿，因为每次更新所有节点的文本花费了大量的时间，打开performance面板看一下具体的js执行。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270b5e9466a643ea9d1c39eee5dc7cd3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
可以看到，每次更新都是js执行超过1s的long task，在这期间raf根本没机会执行，动画自然也会卡顿。</p>
<h1 data-id="heading-2">使用concurrent模式</h1>
<p>如果使用了concurrent模式会怎么样呢，启用concurrent模式很简单，代码如下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6eef9a8f25408c912e7126722c3b82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
使用了concurrent模式之后，页面的卡顿并没有什么变化，打开performance面板看看js的执行
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c671dd87db474e488743ca77dd2d2322~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
可以看到js的执行已经变成了一块一块的执行阶段，不再是超过1s不会中断的情况，我们已经拥有了可中断的更新。但由于我们并没有设置更新的优先级，在更新所有节点的过程中，不会有更高优先级的更新去抢占渲染，所以每个时间片更新完之后在下个任务队列就会立即继续更新流程，页面还是会卡顿。那么接下来如果我们把raf的js动画设置更高的优先级，让动画的更新优先于节点文本的更新，是不是页面就会看起来流畅了呢。</p>
<h2 data-id="heading-3">设置更新的优先级</h2>
<p>那么该如何设置优先级呢，在react concurrent模式有 <a href="https://reactjs.org/docs/concurrent-mode-reference.html#usetransition" target="_blank" rel="nofollow noopener noreferrer">useTranstition</a> 这个hook可以设置更新的过期时间，可以延后组件的更新到过期时间之后。那么我们对于更新所有节点文本这个更新流程设置一下延迟的时间，代码如下。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4364bdeb2094cf28f3163d04692e0a8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
对于文本的更新，我们设置了300毫秒的过期时间，可以看到动画明星流畅了很多，再打开performance面板看看
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe038e01475f4b0da0e9fd623ef249f4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
可以看到很多紫色的表示计算样式的执行，说明我们设置的每一帧的raf动画样式都得到了及时的计算，动画也因此流畅了很多，如果细心的观察，现在跟之前提到的4年前的demo比起来还是会有一下明显的卡顿，4年前的demo全程都是很流畅的，这是为什么呢。因为现在react的reconcile阶段中，update是可以中断的，但commit阶段是不可以中断的，为了保证ui更新的一致性，commit是同步阶段，所以每次同步commit更新所有节点的文本也是比较耗时的，会造成卡顿
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e73c32006a254d03ba848c6ad20fcb97~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
可以看到在众多的时间片中，commit阶段是没有中断的。</p>
<h1 data-id="heading-4">总结与展望</h1>
<p>concurrent模式确实给现在的react更新带来了更多的可能性，但concurrent并不是银弹，在本文的例子中，组件其实是用memo包裹过的，如果不用memo包裹，那么每次更新动画顺带着还会更新所有文本，虽然是一样的文本，但还是会花费比较多的时间，动画还是会卡顿。而且useTransition还有个返回值isPending表示是否正在延迟更新，所以startTransition后的其实是进行了两次更新，一次是立即更新当前组件更新isPending状态，第二次就是延迟的更新，组件的渲染次数变多了。因此memo和shouldComponentUpdate这类api的使用会更加重要。但其实本人在日常开发中很少用到这类阻止重渲染的api，因为需要比较重的心智负担，必须要保证immutable数据流，但由于js原生就不支持，手写保证immutable数据流只要有一个地方是mutable的组件的子树全部前功尽弃。因此最好使用 <a href="https://github.com/immerjs/immer" target="_blank" rel="nofollow noopener noreferrer">immer</a> 这类库保证immutable，但又会带来一定的学习成本。
总之，concurrent模式有好处，学习和使用成本也不一定低，那该怎么办呢？
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eddc76f0156f411fb3f2c9144750a2ec~tplv-k3u1fbpfcp-watermark.image" alt="用这图尤大不会打人吧" loading="lazy" referrerpolicy="no-referrer">
<em>用这图尤大不会打人吧</em></p></div>  
</div>
            