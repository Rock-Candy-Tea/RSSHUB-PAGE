
---
title: '深入理解js中的yield'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb78a19fcb346ac8c9fd7b94251ed85~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 23:52:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb78a19fcb346ac8c9fd7b94251ed85~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">深入理解js中的yield</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fu%2F6183038717af" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/u/6183038717af" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebb78a19fcb346ac8c9fd7b94251ed85~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-1">yield是什么</h2>
<ul>
<li>yield是ES6的新关键字，使生成器函数执行暂停，yield关键字后面的表达式的值返回给生成器的调用者。它可以被认为是一个基于生成器的版本的return关键字。</li>
<li>yield关键字实际返回一个IteratorResult（迭代器）对象，它有两个属性，value和done，分别代表返回值和是否完成。</li>
<li>yield无法单独工作，需要配合generator(生成器)的其他函数，如next，懒汉式操作，展现强大的主动控制特性。</li>
</ul>
<h2 data-id="heading-2">yield应用的简单例子</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85916cee03394e0abb0101b971056c1c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>demo1</p>
<ol>
<li>如果你看到某个函数中有yield，说明这个函数已经是个生成器了</li>
<li>yield可以用来加强控制，懒汉式加载</li>
<li>调用函数指针和调用生成器是两码事，注意上面的运行结果，countAppleSales和myArr。</li>
<li>需要next()函数配合使用，每次调用返回两个值：分别是value和done，代表迭代结果和是否完成</li>
<li>函数next()是个迭代器对象，传参可以缺省，默认调用函数。</li>
</ol>
<h2 data-id="heading-3">错误的调用</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dab19a4079804dedbd9ac3ffd5950325~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>demo2</p>
<p>上述错误的调用中，会的到如下结果<br>
&#123; value: 7, done: false &#125;<br>
&#123; value: undefined, done: true &#125;</p>
<p>因为在while判断中的next也会进行消耗，导致输出结果与预期不符，得到的只是符合条件的偶数项</p>
<h2 data-id="heading-4">一些说明</h2>
<ol>
<li>yield并不能直接生产值，而是产生一个等待输出的函数</li>
<li>除IE外，其他所有浏览器均可兼容（包括win10 的Edge）</li>
<li>某个函数包含了yield，意味着这个函数已经是一个Generator</li>
<li>如果yield在其他表达式中，需要用()单独括起来</li>
<li>yield表达式本身没有返回值，或者说总是返回undefined(由next返回)</li>
<li>next()可无限调用，但既定循环完成之后总是返回undeinded</li>
</ol>
<h2 data-id="heading-5">next()函数及参数</h2>
<ol>
<li>在js中，虽然借鉴了python的函数，但是也进行了自己的改造，由于没有send()函数，所以无法直接传递yield的值。</li>
<li>next()可以带一个参数，该参数会被认为是上一个yield整体的返回值，稍后将在代码中展示。</li>
<li>在某种程度上，next()可以直接当做send()使用</li>
</ol>
<p><strong>它的意义在于，可以在不同阶段从外部直接向内部注入不同的值来调整函数的行为(这一点是其他循环很难做到的，或要付出较大的代价才可以做到)</strong></p>
<h2 data-id="heading-6">yield参数的对比</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/277118682114403bb94eff7fcff2abf4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>js</p>
<p>\</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59c753ee436649338b9dcf18af9984aa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>python</p>
<ol>
<li>对js中generator函数进行改造，对比右边的python中的yield，它们原理一样，只是调用方式不同</li>
<li>调用next()，会产生许多i的值, 但是不会影响reset，因为yield直接将值return出来了。</li>
<li>当传值true后，yield及他的参数整体变为true赋值给reset，这是reset会被执行，从而满足循环内的判断条件</li>
<li>这里的使用 next(参数) 已经达到了send(参数)的效果</li>
<li>这并不会平白增加循环的时间复杂度，因为不传参的时候，并不会占用更多的内存</li>
</ol>
<h2 data-id="heading-7">更深层次的理解yield</h2>
<p>如果刚才没有让你有一个清晰的认识，那么这个例子一定会让你彻底明白的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a1dbee1dd414eff90fbb43b7b9e9380~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>传参</p>
<h3 data-id="heading-8">分析</h3>
<p><strong>next() 传参是对yield整体的传参，否则yield类似于return</strong></p>
<h4 data-id="heading-9">A组</h4>
<ol>
<li>x恒为5，所以第一次调用传空没问题，可得到对应的第一个yield返回值:yield (x + 1)</li>
<li>第二次调用，无参数传入，所以y为NaN(2* undefined)，自然得不到z</li>
<li>第三次调用同上分析</li>
</ol>
<h4 data-id="heading-10">B组</h4>
<ol>
<li>x恒为5，所以第一次调用传空没问题，可得到对应的第一个yield返回值:yield (x + 1)</li>
<li>第二次调用，传入12，所以y为24(yield (x + 1)=入参)，得到第二个yield: yield (y / 3)=8</li>
<li>第三次调用同上分析,得到最后的z值并return=42</li>
</ol>
<h2 data-id="heading-11">目前项目中的可用性</h2>
<p>在前端项目中，用的机会很少，完全可以忽略他的存在，但是在后台项目中，就显得比较重要了，因为其优越的可控性，可是极大的提升线程的效率。</p>
<p>目前只是根据官网，ES6规范，大站等总结出来的，但是很遗憾，目前我们的项目中由于node项目较简单，并不需要进行实际改造。</p>
<p>如果需要实例的话，可参考github上的一些python后端项目，调用方式稍有不同，由于js参考的python语言，他们又同为动态语言，所以原理都是相同的，用处也一样。</p></div>  
</div>
            