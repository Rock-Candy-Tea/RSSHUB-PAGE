
---
title: '【盲目分析系列】为什么img与img之间不能过度亲密'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0944591221450dada9814f397ec9fa~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 05:13:40 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0944591221450dada9814f397ec9fa~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>说：为什么img之间总是有间隔，横向或者纵向上的，都不能靠在一起，显得亲密点。</p>
<p>应领导要求，来盲目分析一波。</p>
<h2 data-id="heading-1">问题</h2>
<p>先来看看问题。如图。html结构很简单，就是一个父盒子div里套了很多小黄鸭img，还有一些文字。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f0944591221450dada9814f397ec9fa~tplv-k3u1fbpfcp-watermark.image" alt="codepen.io_Dosph_pen_PoWGPbw.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显，每个小黄鸭img都不能与周围的小黄鸭亲密接触，乃至周围文字也不行。</p>
<p>现在领导要求小黄鸭睡在一起。</p>
<h2 data-id="heading-2">分析</h2>
<h3 data-id="heading-3">小别致img</h3>
<p>MDN的原话：<strong>img</strong>是一个可替换元素。它的 display 属性的默认值是 <strong>inline</strong>，但是它的默认分辨率是由被嵌入的图片的原始宽高来确定的，使得它就像** inline-block** 一样。</p>
<p>翻译翻译：img是行内元素——（内联元素宽高无效，不换行）</p>
<p>但又不完全是——哎，设置宽高是有效的，还会影响分辨率。</p>
<p>原话：<strong>img</strong> 没有基线（<strong>baseline</strong>），这意味着，当在一个行内格式的上下文（an inline formatting context）中使用 vertical-align: baseline 时，图像的底部将会与容器的文字基线对齐。</p>
<p>翻译：基线，就是基友与普通朋友的边界线（当然不是）。</p>
<h3 data-id="heading-4">基线</h3>
<p>有句俗话：虽然人的xp是不同的，但我还是建议你去看下医生。</p>
<p>这个xp就足以解释基线。仔细看x的底端比p的低端高。x的底端就是基线。</p>
<p>来看下面这个字帖，老实说写得不咋地。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f71887a044d044878b6b881bde4ab0d3~tplv-k3u1fbpfcp-watermark.image" alt="src=http___img30.360buyimg.com_popWaterMark_jfs_t247_281_974099685_51237_c19b365_53f457e6Nb313a385.jpg&refer=http___img30.360buyimg.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一行四线中从上往下数：第三根线就是为基线baseline 。</p>
<p>vertical-align还有bottom和top：但并不是第一根线和最下的线。我盲目猜测应该是行高的顶与底。这个东西很复杂，想要深入了解的可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fstarof%2Fp%2F4512284.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/starof/p/4512284.html" ref="nofollow noopener noreferrer">这篇文章</a></p>
<p>由于父div默认为文字基线对齐vertical-align: baseline ，所以img也这样，而baseline与bottom之间有小段距离，这段距离便导致了img垂直缝隙间隔。</p>
<p>可以试着增大父元素fontsize，空隙还会变大。</p>
<h3 data-id="heading-5">垂直缝隙解决方法</h3>
<ol start="0">
<li>
<p>img设置css display：block；</p>
<ul>
<li>原理：改变了display，变成块级元素。</li>
<li>缺点：很明显，换行了，一行只有一个图了</li>
</ul>
</li>
<li>
<p>div 设置font-size:0px;</p>
<ul>
<li>原理：文字大小为了，基线到bottom的距离也变成了0，所以缝隙没了，包括水平</li>
<li>缺点：文字也没淦没了。。。。。</li>
</ul>
</li>
<li>
<p>div 设置display:flex；flex-direction:column;</p>
<ul>
<li>原理：不清楚，应该是flex布局的特性</li>
<li>缺点：变单行，img大小放飞自我了，有点脑淤血才做才这样处理吧</li>
</ul>
</li>
<li>
<p>img设置float:left</p>
<ul>
<li>原理：float起飞；文本开始环绕文字</li>
<li>缺点：呃，要清除浮动，还有就是你可能不想它起飞。</li>
</ul>
</li>
<li>
<p>img 设置vertical-align: bottom;或者top</p>
<ul>
<li>原理：改变对齐方式</li>
<li>缺点：行高不能大于img的高度，仍在会存在空隙</li>
</ul>
</li>
</ol>
<h3 data-id="heading-6">水平间隙这么来的？</h3>
<p>这是html的问题，试想一下当你写完了代码，右键，选择格式化文档。</p>
<p>vscode已经给你排版得飘飘亮亮，like this</p>
<pre><code class="copyable"><div>
    <img src='' alt=''>
    <img src='' alt=''>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，上诉每次换行都会产生一个textNode。关于空白结点：有兴趣的可以看这篇<a href="https://juejin.cn/post/6994587482851541005#heading-14" target="_blank" title="https://juejin.cn/post/6994587482851541005#heading-14">大佬的文章</a>。</p>
<p>不仅是换行，空格也会形成文本结点，而且多个换行和空格只会产生一个空结点，使得img水平间隔一个空格的距离。</p>
<p>那么问题来了，为什么第一个空结点没有在第一个img左边显示出来？。</p>
<p>盲目分析可能是甲鱼的臀部：龟腚 ，行内第一个空结点不显示，毕竟也不需要在第一元素之前间隔。</p>
<p>有知道的大佬可以评论告知。</p>
<h3 data-id="heading-7">水平间隙消除方法</h3>
<ol start="0">
<li>手动删除换行和空格；</li>
</ol>
<pre><code class="copyable"><div>
    <img src='' alt=''><img src='' alt=''>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>原理：物理上解决问题。</li>
<li>缺点：你可能会变得无聊</li>
</ul>
<ol start="2">
<li>div 设置font-size:0px;</li>
</ol>
<ul>
<li>原理：同上，文字结点不显示了</li>
<li>缺点：同上，淦没了。。。。。</li>
</ul>
<ol start="3">
<li>div 设置letter-spacing:-800px;</li>
</ol>
<ul>
<li>原理：同2</li>
<li>缺点：同2</li>
</ul>
<ol start="4">
<li>
<p>div 设置 word-spacing:-0.3em</p>
<ul>
<li>原理：直接设置标签与文本间隔，文本与文本间隔</li>
<li>缺点：真实到2个单词连在一起变一个，甚至重叠</li>
</ul>
</li>
<li>
<p>img 设置 margin-left:-0.3em</p>
<ul>
<li>原理：定位了</li>
<li>缺点：麻烦，每行第一个图还得特殊处理。</li>
</ul>
</li>
</ol>
<h2 data-id="heading-8">结论</h2>
<p>别把文字和img写成同级，直接fontsize：0；解决一切烦恼。</p>
<p>要么就vertical-align: bottom;然后物理删除回车。</p>
<p>你可以在我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodepen.io%2FDosph%2Fpen%2FPoWGPbw" target="_blank" rel="nofollow noopener noreferrer" title="https://codepen.io/Dosph/pen/PoWGPbw" ref="nofollow noopener noreferrer">codepen</a>上尝试上述各种方案</p>
<p>如有错误敬请指正。</p></div>  
</div>
            