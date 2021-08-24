
---
title: 'CSS揭秘——灵活的背景定位'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a663239244924d1eae70489a12331511~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 02:45:19 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a663239244924d1eae70489a12331511~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>对于容器内的背景图做偏移定位，在 CSS 2.1 中，只能指定距离左上角的偏移量，或者完全偏移到其他三个角，但经常是希望图片和边角可以有一定空隙，像下图一样，没有空隙会让视觉感受上就不友好。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a663239244924d1eae70489a12331511~tplv-k3u1fbpfcp-watermark.image" alt="epub_26211795_57.jfif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果容易是固定尺寸，在 CSS 2.1 还是可以实现，就是计算距离左上角的偏移量。但是当容器尺寸不固定，这就无法去做到了。通常就只能把 background-position 设置为某个接近 100% 的百分比值，得到近似地效果。再有就是使用伪类去用绝对定位去实现，这样都是不够 DRY。</p>
<h2 data-id="heading-0">background-position 的扩展语法方案</h2>
<p>在新的 CSS 特性，已经允许指定背景图片距离任意角的偏移量，只需要在偏移量前面指定关键字。</p>
<pre><code class="copyable">background: url(bushu.svg) no-repeat #58a;
background-position: right 20px bottom 10px;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b78196be3eed429bbc7918a373d470b0~tplv-k3u1fbpfcp-watermark.image" alt="epub_26211795_58.jfif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果需要回退方案，可以把老套的 bottom right 定位值写进 background 的简写中：</p>
<pre><code class="copyable">background: url(bushu.svg) no-repeat bottom right #58a;
background-position: right 20px bottom 10px;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">background-origin 方案</h2>
<p>在给背景图设置偏移量时，如若偏移量与容器的内边距一致。使用上面的方案：</p>
<pre><code class="copyable">padding: 10px;
background: url(bushu.svg) no-repeat #58a;
background-position: right 10px bottom 10px;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54ad4628ac2443ca9a31abe21cbdcebc~tplv-k3u1fbpfcp-watermark.image" alt="epub_26211795_60.jfif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，实现没有任何问题，但是代码就不够 DRY，每次改动内边距，都需要同时去改动 background-position 中的距离。更简单的方法就是，让这个距离跟着内边距走，就不用再声明偏移量的值。</p>
<p>都知道每个元素都有 border box，padding box，content box 三个矩形框，background-position 这个属性默认情况是以 padding box 为准的，这样边框不会遮住背景图片。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e42f0eeb8f6745a0ad3db26c13cf46d6~tplv-k3u1fbpfcp-watermark.image" alt="epub_26211795_61.jfif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在新的 CSS 中多了一个 background-origin 这个属性，可以用来改变来改变这种行为，当然默认值也就是 padding-box，如果改为 content-box，就可以实现上述一样的效果：</p>
<pre><code class="copyable">padding: 10px;
background: url(bushu.svg) no-repeat #58a bottom right;
background-origin: content-box;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样代码就变得更 DRY，只需改变 padding 一个地方即可。</p>
<p>上面的两种方法也可以组合起来，可以在 background-origin 设置为 content-box 的同时，再设置 background-position，就可以让偏移量与内边距稍稍有些不同。</p>
<h2 data-id="heading-2">calc() 方案</h2>
<p>因为多了 calc() 函数可以进行长度计算，我们也可以就用 background-position 设置左上角的偏移量来实现效果：</p>
<pre><code class="copyable">background: url(bushu.svg) no-repeat #58a;
background-position: calc(100% - 20px) calc(100% - 10px);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ps：需要注意 calc() 函数的写法，内部的 - 和 + 运算符的两侧是要各加一个空白符，否则会产生解析错误。这个规则是为了向前兼容，在以后，calc() 内部可能会允许使用关键字，而这些关键字就可能包含连字符（即减号）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17e3c4e53ffc4d30bd5c25217812c753~tplv-k3u1fbpfcp-watermark.image" alt="塔克拉玛干沙漠.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>浙江大华技术股份有限公司-软研-智慧城市产品研发部招聘高级前端！！！！！ 欢迎大家来聊，有意向可发送简历到 chen_<a href="https://link.juejin.cn/?target=mailto%3Azhen%40dahuatech.com" target="_blank" title="mailto:zhen@dahuatech.com" ref="nofollow noopener noreferrer">zhen@dahuatech.com</a>，加入我们，可以一起进步，一起聚餐，一起旅游，让我们从世界村的小伙伴变成大华村的小伙伴。</p>
</blockquote></div>  
</div>
            