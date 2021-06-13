
---
title: '一次性搞懂flex布局的各种属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8d2513acbfb4955abdb55bec15fc63b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 05:17:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8d2513acbfb4955abdb55bec15fc63b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第<strong>12</strong>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">一、概念</h2>
<p><strong>Flex</strong>是<strong>Flexible Box</strong>的缩写，意为”<strong>弹性布局</strong>”，用来为盒状模型提供最大的灵活性。</p>
<p>任何一个容器都可以指定为Flex布局。</p>
<p>是一种一维的布局模型（这里可以对比<a href="https://juejin.cn/post/6952843398235734030" target="_blank">网格布局</a>是二维的布局模型）</p>
<p>-- 注意，设为Flex布局以后，子元素的<code>float、clear</code>和<code>vertical-align</code>属性将失效。</p>
<p>flex容器当中默认存在两根轴：<strong>主轴和交叉轴</strong>。</p>
<p>主轴（main axis）是水平上的，交叉轴（cross axis）是垂直上的
如下图所示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8d2513acbfb4955abdb55bec15fc63b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><strong>主轴main axis</strong>：即水平的这根轴</p>
</li>
<li>
<p><strong>交叉轴cross axis</strong>：即交叉的这根轴</p>
</li>
<li>
<p><strong>主轴空间main size</strong> ：即占据的主轴空间</p>
</li>
<li>
<p><strong>交叉轴空间cross size</strong> :即占据的交叉轴空间</p>
</li>
</ul>
<h2 data-id="heading-1">二、容器的属性：</h2>
<h3 data-id="heading-2">1、flex-direction 决定主轴的方向，也就是项目的排列方向</h3>
<ul>
<li>row（默认值）：主轴为水平方向，起点在左端。</li>
<li>row-reverse：主轴为水平方向，起点在右端。</li>
<li>column：主轴为垂直方向，起点在上沿。</li>
<li>column-reverse：主轴为垂直方向，起点在下沿</li>
</ul>
<p>接下来我们通过例子来使用这个属性。</p>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item"</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.box</span> &#123;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">flex-direction</span>: row-reverse;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">1000px</span>;
        <span class="hljs-attribute">background-color</span>: thistle;
    &#125;
    <span class="hljs-selector-class">.item</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">150px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
        <span class="hljs-attribute">background-color</span>: crimson;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">10px</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bfeafb10ad447a0b5a4cda4d51acdfe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3deb31aaa66649e78aa50a15eda88994~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2、flex-wrap ： 即项目排在轴线上的时候，如果轴线排不下的时候如何换行。</h3>
<ul>
<li><strong>nowrap</strong>（默认）：不换行。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7d5232f25324a33955569f5b40bbaeb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
当不换行的时候，元素会挤在同一行。</p>
<ul>
<li><strong>wrap</strong>：换行，第一行在上方</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/204b72e3df12404e86e926e702d5dca4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>wrap-reverse</strong>：换行，第一行在下方</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1db6ad42f41e4e7fb7a249c83f99d3bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">1、justify-content：定义了项目在主轴上的对齐方式</h3>
<ul>
<li>flex-start（默认值）：左对齐</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/105aa035cb214f20abeb42896a0e22e6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>flex-end：右对齐</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2740f9439e5c4625a5bb62fbcd87b935~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>center： 居中</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10601cf0e82f47578c3ccfe012056a3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>space-between：两端对齐，项目之间的间隔都相等。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8a0d95fecbf45ad9c2d9a8282fe88d8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>space-around：每个项目两侧的间隔相等。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fd4a9fd877d4bff89d17aa66c6da239~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">5、align-items：定义了项目在交叉轴上如何对齐 也就是垂直方向上的对齐</h3>
<ul>
<li>flex-start：交叉轴的起点对齐</li>
<li>flex-end：交叉轴的终点对齐</li>
<li>center：交叉轴的中点对齐</li>
<li>baseline：项目的第一行文字的基线对齐</li>
<li>stretch（默认）：如果项目没有设置高度，或者设置为auto，将占满整个容器的高度</li>
</ul>
<p>这个属性跟上面类似，就不多赘述。</p>
<h2 data-id="heading-6">三、项目的属性</h2>
<p><strong>什么叫项目的属性，就是类似作用例子当中在里面的盒子当中的</strong></p>
<h3 data-id="heading-7">1、flex-grow：定义项目的放大比例。</h3>
<p>当flex-grow为1的时候，该项目会占据剩余的空间，</p>
<p>当flex-grow为2的时候，其他项目不变时，依然是占据剩余的空间，因为它的值最大。</p>
<p>如果其他项目有值为1的时候，值为2的会比值为1的占据空间大一倍。其他默认不变。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62526b9426f649fa97e47d559750731b~tplv-k3u1fbpfcp-watermark.image" alt="flex-grow.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">2、flex-shrink：定义项目的缩小比例，默认值为1</h3>
<p>跟上面这个类似，就不多赘述。</p>
<h3 data-id="heading-9">3、flex-basis：定义了在分配多余空间之前，项目占据的主轴空间。默认值为auto。</h3>
<p>比如我们设置为300px，则</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e31d9a76ef22472881c2e1214592b3d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">4、flex</h3>
<p>flex其实就是前面三个属性的简写，默认值为<strong>0 1 auto</strong> 后两个属性为可选值。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f584ec5f2324f9d803a3bcc4956e0a3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">5、align-self 允许单个项目可以跟其他项目不一样的对齐方式，</h3>
<p>比如我们在做一行内的布局时，需要<strong>左边两个对齐上面，右边两个对齐下面</strong>，则
可以设置最后两个盒子的<code>align-self</code></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.item3</span>,<span class="hljs-selector-class">.item4</span> &#123;
        <span class="hljs-attribute">align-self</span>: flex-end;
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b82f110a9c4209a34027d0068a2fd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            