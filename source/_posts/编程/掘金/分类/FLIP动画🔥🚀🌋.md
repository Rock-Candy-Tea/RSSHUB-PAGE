
---
title: 'FLIP动画🔥🚀🌋'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe99c1de81444bf898ee23da8b372d1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 06:36:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe99c1de81444bf898ee23da8b372d1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>先拿个不太恰当的例子：</p>
</blockquote>
<p>去年实习期间做过一个小组件，自己想实现左边框中选择一条case，右边的已选集合框中需要出现这条case，同时需要有上下移动的动效标识。（原谅图做了虚化处理）</p>
<p>现在回首看那次的代码深感千疮百孔，且有更加简单和高效的做法，不过在当时，刚好听闻<strong>FLIP动画</strong>这个名词，所以本着学习的心态没想那么多就用了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afe99c1de81444bf898ee23da8b372d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在点选左边第一条case时，代码会在代表右边case集合的state中unshift一个case item，其余的case item都依次向下滑动，讲道理不管是插入元素还是删除元素，我都只需要知道这个元素的高度就行了，因为其余元素的相对位移值都是这个元素的高度数值。</p>
<p>但是当时脑子一热，我偏不！我在幻想中给它增加难度！</p>
<p>我假设，需要做动画的所有item都不知道自己具体要向下滑动多少像素，在这种天真的设想下，该如何实现呢？</p>
<h2 data-id="heading-0">FLIP思想</h2>
<p>首先来看一下<strong>FLIP</strong>的意思，<strong>FLIP</strong>其实是一种思想而不是一种技术：</p>
<blockquote>
<p><strong>F: First，盘古开天辟地之初</strong>，指参加过渡元素的初始状态，或者可以理解为还未发生变化的上一帧的信息和布局。</p>
</blockquote>
<blockquote>
<p><strong>L: Last，万物行将终结之时</strong>，指参加过渡元素的终止状态，或者可以理解为将发生变化时这帧的信息和布局。</p>
</blockquote>
<blockquote>
<p><strong>I: Invert，旋转跳跃闭着眼，假装一切没发生</strong>。我们可以通过这个元素的初始状态(First)和终止状态(Last)计算出元素改变了什么，比如其宽高、透明度，或者距离某个元素的像素值，然后我们翻转这个改变。<br>
举个例子，如果一个元素的初始状态和终止状态之间偏移了90px，而页面此时还处于First状态帧，并未到达Last状态帧，你应该设置这个元素<code>transform: translateY(-90px)</code>，因为在即将渲染的下一帧里，元素会瞬间处于<strong>Last</strong>的位置（如果你没有加任何动画处理的话），所以给元素一个<strong>invert</strong>就可以保证在下一帧的视觉上元素仍处于这一帧的位置。</p>
</blockquote>
<blockquote>
<p><strong>P: Play，神功大成之日</strong>，为你要改变的任何属性启用tansition/animation，移除你在<strong>invert</strong>阶段的改变。这时你的元素会启动动画，从起始点到终止点。</p>
</blockquote>
<h2 data-id="heading-1">思想实现</h2>
<p>参照最初的例子，与FLIP思想对应地：</p>
<blockquote>
<p><strong>F: First 盘古开天辟地之初</strong></p>
</blockquote>
<p>在最开始的时候，获取右侧所有列表项元素到某个参照物(_ulEleTop)_的距离：</p>
<pre><code class="copyable">const preTops = eleLiArray.map(item => item.getBoundingClientRect().top - ulEleTop);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>L: Last 万物行将终结之时</strong></p>
</blockquote>
<p>改变对应的state状态，比如向其中push了某个元素，或者delete了某个元素，这之后将渲染的结果就是我们期望的Last状态，而我们要做的事就是从当下向未来要布局结果，争取在页面还没有绘制下一帧之前拿到最新的布局。</p>
<p>代码如下：</p>
<pre><code class="copyable">const newTops = eleLiArray.map(item => item.getBoundingClientRect().top - ulEleTop);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码看起来和 <strong>F</strong> 阶段似乎没什么区别，但是这里需要注意以下三点：</p>
<ul>
<li>
<p>如果是对已存在元素的直接dom操纵那一般没什么问题，我们更加常见的场景是在<strong>声明式</strong>的代码中增删元素，比如此处在<code>React.useState<Array<liEleList>>([])</code>这么一个state中push一个<code>liEle</code>，这时我们需要在下一帧之前且dom元素构建完成后拿到这个真实dom。例如在Vue中我们可以使用<code>nextTick</code>函数，执行时机类似于React中的<code>useLayoutEffect</code>。<code>nextTick</code>其实就是把你要做的事情推进event loop的微任务列表中，等到dom元素真正被构建后进行回调。经过实验发现，<code>nextTick</code>的时机正是在当前渲染帧（即当前event loop）的微任务队列中执行，所以不用担心我们会意外地来到下一帧的时间结点；同时需要注意的是，<code>nextTick</code>中我们只能拿到dom相关信息，无法拿到有关未来的style相关信息，因为此时还没有执行样式计算和布局。</p>
</li>
<li>
<p>一般来说，浏览器会尽可能以固定的频率渲染页面，如果以60fps算的话大约是16.6ms一帧，此时规律而优美：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7401dbe033674a77bc286793eae8dea4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">那我们如何去在前一帧和后一帧的中间拿到最新的样式呢？代码里给出的答案是<code>_getBoundingClientRect_</code>_，_这是因为它触发了<strong>强制同步布局</strong>，这会使浏览器不得不在两帧之间强加一个<strong>Recalculate Style</strong>即样式重算，更多触发强制同步布局的方法见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgist.github.com%2Fpaulirish%2F5d52fb081b3570c81e3a" target="_blank" rel="nofollow noopener noreferrer" title="https://gist.github.com/paulirish/5d52fb081b3570c81e3a" ref="nofollow noopener noreferrer">🔗What forces layout / reflow</a>。注意这里只是执行style重算，页面并没有重新绘制哦，所以我们只是拿到了下一帧的相关样式，但是眼睛看到的还是上一帧的图，所以可以类比成我们向“未来”拿到了值。</p>
</li>
<li>
<p><strong>强制同步布局会引起一定的性能下降</strong>，甚至带来不良的用户体验，请合理使用和优化。上面提到了，浏览器是以一定的时间段循环去执行任务的，在一帧的事件单中，它需要去执行js代码，需要去计算样式，确定布局，并绘制页面等，如果你在井井有条的“计划刷新”中不断强制回流，那势必会带来性能上的降低，特别是在循环中去触发，这样会造成页面卡顿和非常差的用户体验。浏览器也会给出相应警告❗️⚠️❗️。</p>
</li>
</ul>
<p>比如下面这张图就是我在一个循环中不断强制回流的结果，密密麻麻的红色小三角警告，这种情况一般称之为“布局抖动”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acf403d005964b52af933d343a13efa9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>I: Invert 旋转跳跃闭着眼，假装一切没发生</strong></p>
</blockquote>
<p>我们知道，下一帧的时候页面会渲染出新状态，但是如果我们不加动画的话，那下一帧就会是“突变式”的渲染。其实现在右边的case栏中所有item的style都已经变成下一帧的样子了，只不过页面还没有paint而已，这时候我们需要先让这些元素保持这一帧的样子，好骗过我们的眼睛认为什么都没有发生。</p>
<p>这时我们可以利用前后样式的差值去给元素加style：</p>
<pre><code class="copyable">// 代表用之前的top数组减去新的top数组，得到一个差值数组
invertTops = preTops - newTops;
// 代表设置transform属性
transform: `translateY($&#123;invertTops[liIndex] || 0&#125;px)`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这样的<strong>invert</strong>反转，才不会引起下一帧渲染的突变或错位。</p>
<blockquote>
<p><strong>P: Play 神功大成之日</strong></p>
</blockquote>
<p>仅仅是16.6ms的时间就用了上面这么大的篇幅去描述，而下面我们终于可以把这个动画给运行起来了！可以用<strong>rAF</strong>，或者使用更加人性化更具可读性的<strong>Animation API</strong>来做动画：</p>
<pre><code class="copyable">requestFrameLi &&
      requestFrameLi.forEach((liRef, liIndex) => &#123;
        const keyframes = [
          &#123;
            // Invert to First
            transform: `translateY($&#123;invertTops[liIndex] || 0&#125;px)`,
          &#125;,
            // Last
          &#123; transform: 'translateY(0)' &#125;,
        ];
        const options = &#123;
          duration: 300
        &#125;;
        // Play
        liRef.animate(keyframes, options);
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到最后<strong>Last</strong>下_transform_的状态是下帧的原始状态，与写空字符串效果一样。</p>
<p>因为元素下帧的原始状态就是最终状态，我们做的<strong>invert</strong>只是为了先让其回到前一帧的位点，最后肯定是需要回归下帧原始状态的。</p>
<h2 data-id="heading-2">更佳实践</h2>
<blockquote>
<p>上面也提到了，这个🌰不太恰当，因为这个例子中，元素位移其实是已知的，这个时候我们还要通过强制回流拿到未来状态做FLIP动画显然有些脑子不太灵光的嫌疑。</p>
</blockquote>
<p>这里拿另一个demo做展示，这个demo类似于Vue官网上的动画案例，每个元素的位移都是二维的，并且每个元素乱序的位置是随机的，我们无法拿到任何确定的数据，这个时候FLIP思想就很有帮助了，具体代码和效果见沙盒链接 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fmy-vue-w0u5j%3Ffile%3D%2Fsrc%2FApp.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/my-vue-w0u5j?file=/src/App.vue" ref="nofollow noopener noreferrer">🔗 数字二维乱序 - FLIP思想</a>。</p></div>  
</div>
            