
---
title: 'iview中form表单组件动态校验源码分析和正确使用（vue）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc079b0d5834c8ba326a89ecdfb196d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:14:06 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc079b0d5834c8ba326a89ecdfb196d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">需求场景和问题</h2>
<p>声明：<strong>本文章所讲的内容都是以iview中form表单的校验规则属性 rules，model为前提的，并没用到单项form-item的校验规则属性。</strong></p>
<p>大家在做前端开发的时候，可能会经常使用到form表单组件，在开发新需求的时候pm可能会提出一些规则会变化的校验需求，比如说某一个表单项在某些条件下是需要做必填校验的，而在另一种条件下又不是必填项，这就需要我们在开发的时候，动态地设置校验规则。在这种需求下，就会出现一个问题不知道大家是否也碰到过，就是上一次的变化前的规则的校验结果也会一直显示在页面上，而这时候我们新的校验规则已经生成了，某些表单项的校验规则也发生变化了，比如说从必填校验变成了非必填校验，这时候原来的校验结果按理说应该消失掉，可结果却不如人意，小编为此困惑了好久，在百度上搜了好多文章，发现大家的用法一般是调用restFields强行清除掉校验结果，可是使用这个方法的时候，我们在各个表单项中填写的数据也都会一并清除掉，所以我觉得这种方法不能算是一种优雅的解决方式，我就索性看了form表单组件的源码，幸运的是终于找到了一种优雅的解决方式，下面就让我跟大家分享下form的源码吧。</p>
<p>在分享源码之前，我先给大家总结下关于表单规则动态变化的时候，如何让规则和显示效果实时对应。</p>
<ol>
<li>整体给表单rules这个prop赋值，不要单独的在原对象中添加一个属性，即使是用$set()添加某个属性也无法触发表单的重新校验整个表单的方法（<strong>原因在下面的源码分析中会分享到</strong>）。推荐大家使用object.assign(&#123;&#125;, obj1, obj2)方法给rules赋值。</li>
<li>动态设置规则的时候，如果取消某一项为非必填的时候，不要直接将这一项的规则直接设为[]数组 (<strong>原因下面的源码中会具体分析</strong>)。例如表单中某一项不是必填项的时候要将它设置为</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"> prop: [
   &#123;
     <span class="hljs-attr">required</span>: <span class="hljs-literal">false</span>
   &#125;
 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc079b0d5834c8ba326a89ecdfb196d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-09 00.20.32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>form组件有两个关于校验表单必须用的属性，一个是<strong>model</strong>，另一个是<strong>rules</strong>，这两个都是对象。我们在使用的时候会在form表单中传进去两个对象，这两个属性的意思想必大家都知道。接下来跟大家讲一些重点地方。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/130f4a8d0cfc4aaea44c88ec8c674f89~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-09 00.26.05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>首先form表单组件中有一个watch属性，专门监听这个rules，只要rules发生变化，组件就会调用validate方法，看到这里大家应该都会注意到这个rules对象并没有使用深度监听，也就是说在组件初次渲染完毕之后，你想再去改变rules对象下某些校验规则的话，这个validate方法并不会触发。validate方法的代码如下图。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a8c3e0c55824d08ac1188afb90ec406~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-09 00.29.10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>validate方法主要干的事情就是遍历所有的表单子项也就是我们定义的所有的form-item，form-item也就是上图中的field，而fields是form表单的data里的一个属性，这个fields是一个数组，在form表单created的时候，这个fields会被推入所有的form-item。然后在这里循环遍历每一项form-item，并且会调用form-item的validate方法（源码如下图）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51775bdd46464fa2886eda9c304c12b3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
下面简单介绍下这个方法，这个方法会先拿到自己的rules，也就是第一行代码，然后紧接着有一个判断rules是否为空或者不存在，判断代码块下面就是该项规则的校验了，校验的结果反馈在页面上就是框的高亮为红色和校验的提示信息等。红色框圈住的代码里的validateState属性就是校验状态，它可以为success或者error。validateMessage属性是校验结果的提示信息，一般就是你在规则里设置的message属性的值。这两个值是data属性里的值，就是这两个值控制了页面上的红色的提示信息的出现和消失。所以说看到这里你应该就明白了，如果想要改变页面上的校验状态的显示效果，你只要能够改变这两个值就好了，而这两个值是什么又是根据你设置的校验规则决定的，所以说我们只要保证校验规则变的时候，这个validate方法能够被调用执行就好了。这样这两个的值也会实时的更新，页面上的显示效果也会更新。这样就达到了我们想要去除掉校验失败状态的初衷。到这里有一个注意的点就是我们必须让变化后的规则不能为空，因为它一旦为空，代码的执行就会进入validate方法的if代码块中，这时候this.required的值是该form-item的prop属性，外面不传默认为false，这时候外面不传这个值的话，代码的执行就会return出去，下面的validateState，validateMessage属性的值无法取得更新，所以页面上的校验状态就不会去掉，这是大家要留心的地方。<br>
<em>好了，今天内容就先分享到这里，谢谢大家耐心的看完本篇文章，如果关于以上内容有什么疑问或是意见的话，欢迎大家在此评论，我一定会及时回复的，拜拜...</em></p>
<h3 data-id="heading-1">如何让必填项前面的小红星也根据规则老实出现，请看小编下篇文章吧</h3></div>  
</div>
            