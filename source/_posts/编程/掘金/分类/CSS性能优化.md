
---
title: 'CSS性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9445'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 19:00:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=9445'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第<strong>18</strong>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>总结一下关于CSS的性能优化方法。</p>
</blockquote>
<h2 data-id="heading-0">1、避免使用@import</h2>
<p>在<a href="https://juejin.cn/post/6974740846767767559" target="_blank">CSS模块化</a>的时候有说到可以通过 <strong>@import</strong>来实现CSS模块化，但是这种方式是不建议使用的。
因为我们使用@import来引入css文件，<strong>会使得页面在加载的时候增加延迟</strong>。</p>
<p>所以我们在引入外部CSS文件的时候一般都是通过头部的<code>link</code>标签。</p>
<h2 data-id="heading-1">2、避免过分重排</h2>
<p>修改某些css样式会使得部分或整个页面重新渲染，我们应该尽量<strong>减少重新渲染</strong>。</p>
<p>（1）. 不要一条条的修改<code>dom</code>的样式，预先定义好<code>class</code>，然后修改<code>dom</code>的<code>classname</code></p>
<p>（2）. 不要修改影响范围较大的<code>dom</code></p>
<p>（3）. 为动画元素使用绝对定位</p>
<p>（4）. 尽量不要使用table布局，因为一个很小的改动会造成整个table重新布局</p>
<p>（5）. 避免设置大量的style属性，通过设置style属性改变节点样式的话，每一次设置都会触发一次reflow，所以最好使用class属性</p>
<p>（6）. 如果css里面有计算表达式，每次都会重新计算一遍，触发一次<code>reflow</code></p>
<h2 data-id="heading-2">3、删除无用的css代码</h2>
<p>我们在页面开发过程中经常会出现很多无用的css代码，</p>
<p>它们或许是<strong>调试的时候设置的background</strong>，或许是<strong>被后面的样式覆盖的样式</strong>，或许是<strong>设置了之后没有生效的样式</strong>。</p>
<p>这些CSS代码都是可以删除的。</p>
<h2 data-id="heading-3">4、选择合适的选择器</h2>
<p><a href="https://juejin.cn/post/6970500385479852040" target="_blank">CSS的选择器</a>有很多很多种，也许同一个元素对象可以使用不同的选择器，我们的原则应该是<strong>精确而简单</strong>的选择器。
<strong>不要嵌套很多复杂的选择器，不利于渲染也不利于我们阅读。</strong></p>
<p>另外，<strong>通配符</strong>和<strong>属性选择器</strong>效率最低，需要匹配的元素最多，尽量避免使用。</p>
<h2 data-id="heading-4">5、慎重选择高消耗的样式</h2>
<p>有一些样式在绘制前需要进行大量计算。</p>
<p>比如<code>border-radius</code>、<code>box-shadow</code>、<code>transform</code>，我们应该根据业务需求选择合适的属性。</p>
<h2 data-id="heading-5">6、尽量少用CSS表达式</h2>
<p>表达式会让你的代码显得更加酷炫，但是对性能的浪费可能是超乎你想象的。</p>
<h2 data-id="heading-6">7、合成icon图片</h2>
<p>利用<code>cssSprite</code>合成icon图片，用宽高加上<code>background-position</code>的背景图方式显现icon图，这样很实用，减少了http请求。</p>
<h2 data-id="heading-7">8、减少css嵌套</h2>
<p>我们在书写css代码的时候很容易就嵌套起来，但这对性能也会产生浪费，最好不要嵌套三层以上。</p>
<h2 data-id="heading-8">9、合并公共样式</h2>
<p>拆分出公共css文件，对于比较大的项目可以将大部分页面的公共结构样式提取出来放到单独css文件里，这样一次下载 后就放到缓存里，</p>
<h2 data-id="heading-9">10、CSS文件压缩</h2>
<p>是最容易想到的一个性能优化方式了，文件的大小会直接影响浏览器的加载速度，这一点在网络较差时表现地尤为明显。
<code>webpack</code>、<code>gulp/grunt</code>、<code>rollup</code>等也都支持CSS压缩功能。压缩后的文件能够明显减小，可以大大降低了浏览器的加载时间。</p>
<p><strong>以上便是我总结的关于CSS性能优化方式，欢迎批评指正~~</strong></p></div>  
</div>
            