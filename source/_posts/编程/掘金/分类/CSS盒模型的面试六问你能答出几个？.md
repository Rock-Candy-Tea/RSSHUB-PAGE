
---
title: 'CSS盒模型的面试六问你能答出几个？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5f0ceb20ce47e6ac62489cf2ae588a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 06:56:28 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5f0ceb20ce47e6ac62489cf2ae588a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>对于前端面试来说，css盒模型肯定是必考必问的前端知识点，因为这是CSS基石中非常重要的内容，而且它关联的知识也非常多，那面试中一般都是如何层层递进的提问呢？下面一起来看看吧！</p>
<h1 data-id="heading-0">谈谈你对CSS盒模型的认识？</h1>
<h2 data-id="heading-1">问题简答</h2>
<p>所有 HTML 元素都可以视为方框。在 CSS 中，在谈论设计和布局时，会使用术语“盒模型”或“框模型”。CSS 框模型实质上是一个包围每个 HTML 元素的框。</p>
<p>它包括：</p>
<ul>
<li>外边距 → margin</li>
<li>边框 → border</li>
<li>内边距 → padding</li>
<li>实际的内容 → content</li>
</ul>
<p>它有标准模型和IE模型两种；</p>
<h2 data-id="heading-2">知识解析</h2>
<p>盒模型，英文box model。</p>
<ul>
<li>无论是div、span、还是a都是盒子。</li>
<li>图片、表单元素一律看作是文本，它们并不是盒子，因为一张图片里面并不能放东西，它自己就是自己的内容。</li>
</ul>
<p>盒模型各部分说明：</p>
<ul>
<li>Margin(外边距) ：清除边框外的区域，外边距是透明的（可以为负值）。</li>
<li>Border(边框) ：围绕在内边距和内容外的边框。</li>
<li>Padding(内边距) ：清除内容周围的区域，内边距是透明的（不允许负值）。</li>
<li>Content(内容) ：盒子的内容，显示文本和图像。</li>
</ul>
<h1 data-id="heading-3">标准模型和IE模型的区别？</h1>
<h2 data-id="heading-4">问题简答</h2>
<p>标准模型和ie模型的区别是计算宽width高height的不同。</p>
<ul>
<li>标准模型width不计算padding和border；</li>
<li>ie模型width计算padding 和border；</li>
</ul>
<h2 data-id="heading-5">知识解析</h2>
<h3 data-id="heading-6">标准盒模型（W3C盒子模型）</h3>
<p>设置的<strong>宽高</strong>是对<strong>实际内容content</strong>的<strong>宽高</strong>进行设置，内容周围的border和padding另外设置;</p>
<p>即元素实际占位的宽高为：</p>
<p><strong>width【height】= 设置的content的宽【高】 + padding + border + margin</strong></p>
<p>可以通过实例来理解：写一个div，同时设置了宽、高、边框、内边距、外边距；</p>
<pre><code class="copyable">//注：如果下面示例未写html和css,说明与此处相同
.box &#123;
    width: 100px;
    height: 100px;
    border: 10px solid #CC9966;
    padding: 30px;
    margin: 40px;
    background: #66FFFF;
&#125;
<div class="box">Axjy</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果及Chrome的开发者工具中显示的盒模型如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b5f0ceb20ce47e6ac62489cf2ae588a~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到content部分即为100×100，内容周围都是另外设置的，<code>width=40+10+30+100+30+10+40=180</code>；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7bf72299d9547038ce7e6ed3242b711~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">IE盒子模型（怪异盒模型）</h3>
<p>设置的宽高是对<code>实际内容content + 内边距（padding）+边框（border）之和</code>的width和height进行设置的;</p>
<p>即元素实际占位的宽高为：</p>
<p><strong>width（height）= 设置的width（height）+外边距margin</strong></p>
<p>和上面使用同样的例子，但是通过设置<code>box-sizing:border-box;</code>，把它变为IE盒模型；</p>
<pre><code class="copyable">.box &#123;
    width: 100px;
    height: 100px;
    border: 10px solid #CC9966;
    padding: 30px;
    margin: 40px;
    background: #66FFFF;
    box-sizing: border-box;//注意
&#125;
<div class="box">Axjy</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果及Chrome的开发者工具中显示的盒模型如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af90028ea0a04fdb9068dc8a3f75f03c~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以很明显的看到，正方形和上面的比小了一圈，<code>width=40+10+30+20+30+10+40=100</code>;</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/145039c060f94674b9d57a783cdcdf2f~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">CSS如何设置这两种模型？</h1>
<h2 data-id="heading-9">问题简答</h2>
<p>上面的示例其实已经用到了这个设置</p>
<ul>
<li>css设置标准模型：Box-sizing:context-box (也是浏览器默认的盒模型)；</li>
<li>css设置Ie模型：<code>box-sizing:border-box</code>;</li>
</ul>
<h1 data-id="heading-10">JS如何设置/获取盒模型对应的宽和高？</h1>
<h2 data-id="heading-11">问题简答</h2>
<pre><code class="copyable">1) dom.style.width/height【只能取到内联元素】
2) dom.currentStyle.width/height【只有IE支持】
3) document.getComputedStyle(dom,null).width/height  
4) dom.getBoundingClientRect().width/height 
5) dom.offsetWidth/offsetHeight【常用】
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">知识解析</h2>
<h3 data-id="heading-13">dom.style.width/height</h3>
<p>通过dom节点的style样式获取，只能取到行内样式的宽和高，style 标签中和 link 外链的样式取不到</p>
<pre><code class="copyable">.box&#123;...&#125;
----------------------------

let targetDom = document.querySelector('.box');
let width = targetDom.style.width;
let height = targetDom.style.height;

console.log("width",width)
console.log("height",height)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用类设置宽高时</strong></p>
<p>获取的宽高为空</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d880d4ea886e49ff9f7540d89cf875d6~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>在行内设置宽高时</strong></p>
<p>获取的是行内设置的宽高</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0190493829b145a9b8d9ab3e6e148d3c~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>element.style.xxx 这种只能取得内嵌样式的属性，获取样式能读能写</p>
</blockquote>
<h3 data-id="heading-14">dom.currentStyle.width/height</h3>
<p>取到的是最终渲染后的宽和高，如果有设置宽高，则不论哪种盒模型获取到的都是设置的宽高,<strong>只有IE兼容</strong></p>
<pre><code class="copyable">.box &#123;...同上&#125;
----------------------------

let targetDom = document.querySelector('.box');
let width = targetDom.currentStyle.width;
let height = targetDom.currentStyle.height;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>element.currentStyle[xxx] 可以取得内部和外部样式，但是只兼容ie浏览器，获取的样式只能读</p>
</blockquote>
<h3 data-id="heading-15">document.getComputedStyle(dom,null).width/height</h3>
<p>取到的是最终渲染后的宽和高，<strong>如果有设置宽高，则不论哪种盒模型获取到的都是设置的宽高</strong>，和currentStyle相同，但是兼容性更好，IE9 以上支持。</p>
<p>getComputedStyle()方法,</p>
<ul>
<li>第一个参数：取得计算样式的元素；</li>
<li>第二个参数：一个伪元素字符串（例如“:after”），如果不需要伪元素信息，默认为null；</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c28204b30754aa9bba351be9bc5d07f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.box &#123;...同上&#125;
----------------------------

let targetDom = document.querySelector('.box');
let width =  window.getComputedStyle(targetDom).width
let height = window.getComputedStyle(targetDom).height

console.log("width",width)
console.log("height",height)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/345d260055e145febea76597cbf3fbe7~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>『小扩展』</strong></p>
<p>如果box类不设置宽高，而是由内容自动撑开；</p>
<p>则<strong>标准盒模型</strong>通过<code>getComputedStyle</code>获取到的宽高是<code>content</code>的值；</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa8d5f29318544bea75ec134402d7a17~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ed03625d82d4ccab35eb924f9bade21~tplv-k3u1fbpfcp-watermark.image" alt="9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>IE盒模型</strong>通过<code>getComputedStyle</code>获取到的宽高 = border + padding + content，不包括外边距；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3442961006014fbc84db75154d19de39~tplv-k3u1fbpfcp-watermark.image" alt="10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8303ac9b1284314859b6c7cb0e09766~tplv-k3u1fbpfcp-watermark.image" alt="11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">dom.getBoundingClientRect().width/height</h3>
<p>得到渲染后的宽和高，大多浏览器支持。IE9以上支持。</p>
<pre><code class="copyable">.box &#123;...同上&#125;
----------------------------
let targetDom = document.querySelector('.box');
let width = targetDom.getBoundingClientRect().width;
let height = targetDom.getBoundingClientRect().height
console.log('width',width)
console.log('height',height)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>标准模型</strong>，宽高设置为100的结果，额外包括了padding和border的值；</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a076ab0f1a494cec83cb21b712c53cd5~tplv-k3u1fbpfcp-watermark.image" alt="12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>IE模型</strong>，宽高设置为100的结果；</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a59e362520c42ee824b585b0561c226~tplv-k3u1fbpfcp-watermark.image" alt="13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>『小扩展』</strong></p>
<p>如果box类<strong>不设置宽高</strong>，而是由内容自动撑开；</p>
<p>不论是哪种模型，获取到的都是（<strong>border + padding + content</strong>)，不包括外边距；</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5502fdaa75243b180b34c92bb648261~tplv-k3u1fbpfcp-watermark.image" alt="14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>getBoundingClientRect还可以取到相对于视窗的上下左右的距离（用于获取某个元素相对于视窗的位置集合）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18aff723736e450798f4b60442f2f595~tplv-k3u1fbpfcp-watermark.image" alt="18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">dom.offsetWidth/offsetHeight（常用）</h3>
<p>包括高度（宽度）、内边距和边框，不包括外边距。最常用，兼容性最好。</p>
<pre><code class="copyable">.box &#123;...同上&#125;
----------------------------
let targetDom = document.querySelector('.box');
let width = targetDom.offsetWidth;
let height = targetDom.offsetHeight;
console.log('width',width)
console.log('height',height)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>标准模型，宽高设置为100的结果；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab8dac17f03c45309f7553f0bc937b9b~tplv-k3u1fbpfcp-watermark.image" alt="15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>IE模型，宽高设置为100的结果；</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e11a2e7a25f14eb3a3650710eddd0737~tplv-k3u1fbpfcp-watermark.image" alt="16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小扩展</p>
<p>如果box类<strong>不设置宽高</strong>，而是由内容自动撑开；</p>
<p>不论是哪种模型，获取到的都是（<strong>border + padding + content</strong>)，不包括margin；</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4f80c6b1cc447249229d543fe043b3a~tplv-k3u1fbpfcp-watermark.image" alt="17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>从上面可以看出，dom.getBoundingClientRect().width/height 和 dom.offsetWidth/offsetHeight 结果是一样的</p>
</blockquote>
<h1 data-id="heading-18">根据盒模型解释边距重叠</h1>
<h2 data-id="heading-19">问题简答</h2>
<p>外边距重叠是指两个【<strong>垂直</strong>】 【<strong>相邻</strong>】的块级元素，当上下两个边距相遇时，其外边距会产生重叠现象，且重叠后的外边距，等于其中较大者。（水平方向不会发生）</p>
<p><strong>『原因』</strong></p>
<p>根据<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FCSS22%2Fbox.html%23collapsing-margins" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/CSS22/box.html#collapsing-margins" ref="nofollow noopener noreferrer">W3C文档</a>的说明，当符合以下条件时，就会触发外边距重合</p>
<ul>
<li>都是普通流中的元素且属于同一个 BFC</li>
<li>没有被 padding、border、clear 或非空内容隔开</li>
<li>两个或两个以上垂直方向的「相邻元素」</li>
</ul>
<blockquote>
<p>相邻元素包括父子元素和兄弟元素</p>
</blockquote>
<p><strong>『重叠后的margin计算』</strong></p>
<ul>
<li>
<p>1、margin都是正值时取较大的margin值</p>
</li>
<li>
<p>2、margin都是负值时取绝对值较大的，然后负向位移。</p>
</li>
<li>
<p>3、margin有正有负，从负值中选绝对值最大的，从正值中选取绝对值最大的，然后相加</p>
</li>
</ul>
<h2 data-id="heading-20">边距重叠详解及解决方案</h2>
<h3 data-id="heading-21">嵌套块（父子）元素垂直外边距的合并</h3>
<p>对于两个嵌套关系的块元素，如果父元素没有<code>padding-top</code>及<code>border</code>，则父元素的<code>margin-top</code>会与子元素的<code>margin-top</code>发生合并，合并后的外边距为两者中的较大者，即使父元素的上外边距为0，也会发生合并。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b73a4bdf13f41fe922f16d9732320f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>『解决办法』</strong></p>
<ul>
<li>1、为<strong>父元素</strong>定义1px的border-top或padding-top。</li>
<li>2、为<strong>父元素</strong>添加overflow:hidden。</li>
<li>3、子元素或父元素设置display:inline-block。</li>
<li>4、父元素加前置内容（::before）生成。（推荐）</li>
</ul>
<p><strong>『示例』</strong></p>
<p>在页面放两个正方形</p>
<pre><code class="copyable"><div class="parent-box">
    <div class="child-box"></div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父元素<code>margin-top</code>设为0，子元素设置20px;</p>
<pre><code class="copyable">.parent-box&#123;
    width: 100px;
    height: 100px;
    margin-top: 0;
    background: #99CCFF;
&#125;
.child-box&#123;
    width: 50px;
    height: 50px;
    margin-top: 20px;
    background: #FF9933;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>预期效果：应该是父级元素没有边距，子元素顶部和父元素顶部之间的距离为20</p>
<p>实际效果：父子盒子重叠，父级与外面的间隔变成了20（会取较大的值，因为父级为0，所以取的是子级的margin）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92aeb62bd0404b649104ade96ced7062~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的解决办法处理之后</p>
<p>方法一、二、三</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3e106ccef0d4ccbba4651dbe1e0c4c9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>方法四</p>
<pre><code class="copyable">.parent-box::before &#123;
    content : "";
    display :table;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbf38e45c6ab423989b086c61bf34c26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>达到的效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/177eb3d048a044938583ca746ef56f58~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">相邻块（兄弟）元素垂直外边距的合并（外边距塌陷）</h3>
<p>当上下相邻的两个块元素相遇时，如果</p>
<ul>
<li>上面的元素有下外边距margin-bottom，</li>
<li>下面的元素有上外边距margin-top，</li>
</ul>
<p>则他们之间的垂直间距<strong>不是margin-bottom与margin-top之和</strong>，而是<strong>两者中的较大者</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b587a2513dff4c0b92aaa2fd110e3922~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>『解决办法』</strong></p>
<p>1）为了达到想要的间距，最好在设置margin-top/bottom值时统一设置上或下；</p>
<p>2）或者用以下的BFC解决，下面有详解</p>
<h1 data-id="heading-23">谈谈BFC</h1>
<h2 data-id="heading-24">BFC的基本概念</h2>
<p>BFC全称为块格式化上下文 (Block Formatting Context) ，是 Web 页面中盒模型布局的 CSS 渲染模式，指一个独立的渲染区域或者说是一个隔离的独立容器。</p>
<blockquote>
<p><strong>BFC的通俗理解</strong>：首先BFC是一个名词，就是一个有特定规则的区域。我们可以理解为一个箱子（实际上是看不见摸不着的），箱子里面物品的摆放是不受外界的影响的。</p>
</blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FTR%2FCSS22%2Fvisuren.html%23block-formatting" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/TR/CSS22/visuren.html#block-formatting" ref="nofollow noopener noreferrer">W3C 规范</a>对此作了详细的描述：<br></p>
<ul>
<li>
<p>浮动元素和绝对定位元素，非块级盒子的块级容器（例如 <code>inline-blocks</code>, <code>table-cells</code>, 和 <code>table-captions</code>），以及 <code>overflow</code> 值不为<code>visiable</code> 的块级盒子，都会为他们的内容创建新的 BFC（块级格式上下文）。</p>
</li>
<li>
<p>在 BFC 中，盒子从顶端开始垂直的一个接一个排列，两个盒子之间的垂直间距由他们的 <code>margin</code> 值决定，在同一个 BFC 中，两个相邻块级盒子的垂直外边距会产生折叠。</p>
</li>
<li>
<p>在 BFC 中，每一个盒子的左外边缘会触碰到容器的左边缘，对于从右到左的格式来说，则触碰到右边缘。即使在浮动里也是这样的（尽管一个盒子的 <code>line boxes</code> 会因为浮动而收缩），除非这个盒子的内部创建了一个新的 BFC（由于浮动，在这种情况下盒子本身将会变得更窄）</p>
</li>
</ul>
<h2 data-id="heading-25">BFC的布局规则（原理/渲染规则）</h2>
<ol>
<li>计算BFC高度时，浮动元素也会参与计算（清除浮动）</li>
<li>BFC的区域不会与浮动元素的box重叠。（防止浮动文字环绕）</li>
<li>BFC在页面上是一个独立的容器，内外元素不相互影响。（解决外边距重叠问题）</li>
<li>Box垂直方向的距离由margin决定。属于<strong>同一个</strong>BFC的两个相邻Box的margin会发生重叠。</li>
</ol>
<blockquote>
<p>下面的使用场景会通过这些规则来处理一些实际的问题。</p>
</blockquote>
<h2 data-id="heading-26">如何创建BFC</h2>
<p><em>括号里面是一些副作用</em></p>
<ul>
<li><strong>浮动元素</strong>：float:left | float:right;【会导致父元素的宽度丢失,也会导致下边的元素上移】</li>
<li><strong>定位元素</strong>：position:absolute | position:fixed；</li>
<li><strong>display的一些值</strong>：display:inline-block【转为行内块会导致宽度丢失】 | display:flex | display:table | table-cell、table-caption、inline-table、inline-flex、grid、inline-grid；</li>
<li><strong>overflow值不为visible</strong>：overflow:hidden;【将会剪切掉溢出的元素】 | overflow:auto、overflow:scroll;</li>
<li><strong>display:flow-root</strong>【新属性，BFC创建新方式，没有任何副作用，注意浏览器兼容】</li>
</ul>
<p><strong>『注意』</strong></p>
<p>display:table也可以生成BFC的原因在于Table会默认生成一个匿名的table-cell，是这个匿名的table-cell生成了BFC。</p>
<blockquote>
<p>并不是任意一个元素都可以被当做BFC，只有当这个元素满足以上任意一个条件的时候，这个元素才会被当做一个BFC</p>
</blockquote>
<h2 data-id="heading-27">BFC的使用场景</h2>
<h3 data-id="heading-28">清除浮动</h3>
<p>浮动的元素会脱离普通文档流，如下,父级容器只剩下2px的边距高度。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/093b11174aba4521979d06534fd9cd0c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>利用<code>overflow: hidden</code>给父级创建BFC之后</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af76318a2e244911be0d62ed879f7f4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>以上方法可以实现清楚浮动，但是还是推荐使用伪类的方式。</em></p>
<blockquote>
<p><strong>为什么要清除浮动?</strong> 浮动塌陷,包含块没有设置高度或者是自适应的时候、包含块就不能撑起来，变成塌陷的状态。</p>
</blockquote>
<h3 data-id="heading-29">防止浮动文字环绕</h3>
<p>有如下文字环绕效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5e236a387014d9c86097c832cc3552d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>brother-box有部分被浮动元素所覆盖（文本信息不回被浮动元素覆盖），如果想避免元素被覆盖，可利用创建BFC的方法，如给brother-box加<code>overflow: hidden</code>，则可得到以下效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a51bd098c0c4ffeb1ef20b02b05f49c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>『理由』</strong>
上面的规则二：BFC的区域不会与浮动元素的box重叠</p>
<blockquote>
<p>这个方法可以用来实现两列自适应布局，左边的宽度固定，右边的内容自适应宽度。</p>
</blockquote>
<h3 data-id="heading-30">利用BFC解决边距重叠问题</h3>
<p>根据前面的边距重合条件来看，想要解决边距重叠，只需要破坏其中的某个触发条件即可，比如创建一个BFC。</p>
<p>根据 BFC 的定义，两个元素只有在同一BFC 内，才有可能发生垂直外边距的重叠，包括相邻元素、嵌套元素。</p>
<p>===============================</p>
<p>要解决 margin 重叠问题，只要让它们不在同一个 BFC 内就行。</p>
<ul>
<li>对于相邻元素，只要给它们<strong>加上 BFC 的外壳</strong>，就能使它们的 margin 不重叠；</li>
<li>对于嵌套元素，只要让父级元素<strong>触发 BFC</strong>（比如给父级加overflow：hidden)，就能使父级 margin 和当前元素的 margin 不重叠。</li>
</ul>
<p>===============================</p>
<p>在没有新建BFC时，边距重叠了，margin-bottom + margin-top，应该等于20
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/979eb1a0c2304293a7f9575fe1b55b5e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>新建了BFC之后
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2e2ec612f6a40b8a540d535e73ff245~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的例子中，为了使两个正方形的外边距不重叠，就给其中一个div包裹一层container，触发BFC。</p>
<p><strong>注意:</strong> 边距折叠的问题可以用 BFC 来解决，但触发 BFC 并不是解决边距折叠的充分条件，还要得到合理的运用</p>
<blockquote>
<p>来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F19823139%2Fanswer%2F50075651" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhihu.com/question/19823139/answer/50075651" ref="nofollow noopener noreferrer">知乎用户回答</a></p>
</blockquote>
<p>🌺以上内容如果错误或其他观点，欢迎在评论区留言！🌺</p>
<h2 data-id="heading-31">参考：
<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fcss%2Fcss_boxmodel.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/css/css_boxmodel.asp" ref="nofollow noopener noreferrer">CSS 框模型</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2FCSS_Box_Model%2FIntroduction_to_the_CSS_box_model" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model" ref="nofollow noopener noreferrer">CSS 基础框盒模型介绍</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3cplus.com%2Fcss%2Funderstanding-bfc-and-margin-collapse.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3cplus.com/css/understanding-bfc-and-margin-collapse.html" ref="nofollow noopener noreferrer">深入理解BFC和Margin Collapse</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3cplus.com%2Fcss%2Funderstanding-css-layout-block-formatting-context.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3cplus.com/css/understanding-css-layout-block-formatting-context.html" ref="nofollow noopener noreferrer">理解CSS布局和BFC</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3cplus.com%2Fcss%2Funderstanding-block-formatting-contexts-in-css.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3cplus.com/css/understanding-block-formatting-contexts-in-css.html" ref="nofollow noopener noreferrer">理解CSS中BFC</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sitepoint.com%2Funderstanding-block-formatting-contexts-in-css%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sitepoint.com/understanding-block-formatting-contexts-in-css/" ref="nofollow noopener noreferrer">Understanding Block Formatting Contexts in CSS</a></h2>
<p>小可爱看完就点个赞再走吧！🤞🤞🤞</p></div>  
</div>
            