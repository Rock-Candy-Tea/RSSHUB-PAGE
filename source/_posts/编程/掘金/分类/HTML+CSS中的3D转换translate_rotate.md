
---
title: 'HTML+CSS中的3D转换translate_rotate'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32bf34ba8a694f9da4d6995e1466b531~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 20:34:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32bf34ba8a694f9da4d6995e1466b531~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>前面我们已经介绍过了2D转换，那么我们即将学习的3D转换又是什么呢，它跟2D转换有什么不同呢？</p>
</blockquote>
<blockquote>
<p>在我们日常生活的环境就是3D的，我们多看到的物体也都是3D的，而我们拍的照片就是3D物体在2D平面中呈现的样子 。</p>
</blockquote>
<h3 data-id="heading-0"> 3D的特点</h3>
<ul>
<li>近大远小（离我们眼睛越近看上去越大，而离眼睛越远则看上去越小）</li>
<li>物体后面遮挡不可见</li>
</ul>
<p>根据这些特点我们就可以在网页上模拟构建出3D效果。</p>
<h3 data-id="heading-1">三维坐标系</h3>
<p>我们前面讲过的2D是一个平面坐标系，而3D则是三维坐标系。三维坐标系其实就是指立体空间，立体空间是由3个轴共同组成的。</p>
<ul>
<li>x轴：水平向右。x右边是正值，左边是负值</li>
<li>y轴：垂直向下。y下面是正值，上面是负值</li>
<li>z轴：垂直屏幕。往外面是正值，往里面是负值</li>
</ul>
<p>在我们的网页中的左边原点就是我们屏幕的左上角。</p>
<h3 data-id="heading-2"> 3D转换</h3>
<p>3D转换中我们主要来学习工作中最常用的3D位移和3D旋转</p>
<p><strong>主要知识点</strong></p>
<ul>
<li>3D位移：translate3d(x,y,z)</li>
<li>3D旋转：rotate3d(x,y,z)</li>
<li>透视： perspective</li>
<li>3D呈现transfrom-style</li>
</ul>
<p><strong>3D移动 - translate3d</strong></p>
<p>3D移动在2D移动的基础上多加了一个可以移动的方向，就是z轴方向</p>
<ul>
<li>transform:translateX(200px)仅在x轴上移动</li>
<li>transform:translateY(200px)仅在y轴上移动</li>
<li>transform:translateZ(200px)仅在z轴上移动</li>
<li>transform:translate3d(x,y,z)其中x、y、z分别指要移动的轴的方向的距离</li>
</ul>
<p>下面我们用代码来演示一下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3d demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">background-color</span>: pink;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">100px</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">100px</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">100px</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32bf34ba8a694f9da4d6995e1466b531~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在上面这段代码中，我们让这个粉色盒子分别沿着x轴、y轴和z轴各移动了100像素，但是当我们运行起来是发现，z轴方向好像并没有明显的变化。这是因为z轴方向上的移动需要借助透视才能看出效果。接下来我们来看看什么是透视。</p>
<p><strong>透视perspective</strong></p>
<p>perspective 属性定义 3D 元素距视图的距离，以像素计。该属性允许您改变 3D 元素查看 3D 元素的视图。当为元素定义 perspective 属性时，其子元素会获得透视效果，而不是元素本身。</p>
<p>我们平时去电影院看3D电影时，如果直接用眼睛去看其实并看不出明显的3D效果，而是每次电影院都会发给我们一个3D眼镜，那么借助3D眼镜我们再看电影3D效果就非常明显了。那么在我们的网页中如果也需要让我们看到的3D效果明显一些，那就需要借助<strong>透视</strong>了</p>
<ul>
<li>如果想要在网页产生3D效果需要借助透视（理解成3D物体投影在2D平面上）</li>
<li>模拟人类的视觉位置，借助perspective和translateZ可以模拟实现元素的近大远小的效果</li>
<li>透视的单位是像素</li>
<li>透视越小效果越明显</li>
</ul>
<p>注意：</p>
<ol>
<li>透视必须写在被观察元素的父盒子上面</li>
<li>perspective 属性只影响 3D 转换元素</li>
<li>要想改变translateZ实现近大远小效果，则必须要借助透视，否则translateZ是没有效果的</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>3d demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">body</span>&#123;
            <span class="hljs-attribute">perspective</span>: <span class="hljs-number">200px</span>;
        &#125;
        <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">200px</span>;
            <span class="hljs-attribute">background-color</span>: pink;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(<span class="hljs-number">100px</span>) <span class="hljs-built_in">translateY</span>(<span class="hljs-number">100px</span>) <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">100px</span>);
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码中我们给div的父元素body添加一个透视，这时再看这个粉色盒子发现明显比不加透视时变大了很多。这就是透视的作用。上面的示例可能还不够明显，接下来我们再看一个rotat3d的例子效果会更明显</p>
<p><strong>3D旋转 rotate3d</strong></p>
<p>3D旋转指可以让元素在三维平面内沿着x轴、y轴、z轴或自定义轴进行旋转</p>
<p>语法：</p>
<ul>
<li>transform:rotateX(Xdeg)：沿着x轴正向旋转X度</li>
<li>transform:rotateY(Ydeg)：沿着y轴正向旋转Y度</li>
<li>transform:rotateZ(Zdeg)：沿着z轴正向旋转Z度</li>
<li>transform:rotate3d(x,y,z,deg)：沿着自定义轴旋转deg为旋转度数</li>
</ul>
<p>对于元素的旋转方向也是正负之分的，那么如何区分元素旋转方向的正负呢，下面我们来学习一下左手准则，用我们的左手即可判断方向的正负</p>
<p>左手准则：</p>
<ul>
<li>左手的手指指向x轴、y轴、z轴的正方向</li>
<li>其余手指的弯曲方向就是该元素沿着x轴、y轴、z轴旋转的方向</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c583e5103d8148a28e414505f7dc6b76~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/7001333383313768485" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p> 下面的代码是沿着x轴正向旋转的示例</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-id">#div1</span>
&#123;
<span class="hljs-attribute">position</span>: relative;
<span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
<span class="hljs-attribute">width</span>: <span class="hljs-number">150px</span>;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">50px</span>;
<span class="hljs-attribute">padding</span>:<span class="hljs-number">10px</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
<span class="hljs-attribute">perspective</span>:<span class="hljs-number">50</span>;
-webkit-<span class="hljs-attribute">perspective</span>:<span class="hljs-number">150</span>; <span class="hljs-comment">/* Safari and Chrome */</span>
&#125;

<span class="hljs-selector-id">#div2</span>
&#123;
<span class="hljs-attribute">padding</span>:<span class="hljs-number">50px</span>;
<span class="hljs-attribute">position</span>: absolute;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid black;
<span class="hljs-attribute">background-color</span>: pink;
<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">45deg</span>);
-webkit-<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotateX</span>(<span class="hljs-number">45deg</span>); <span class="hljs-comment">/* Safari and Chrome */</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div2"</span>></span>HELLO<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
 
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 上述代码中如果我们不加透视效果则运行后就是下面第一个图的样子，如果使用了透视则就是第二张图的样子，这样来看透视的作用就很明显了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6ae0c91e63489e8ebf52428b6f2c89~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3D呈现 transform-style</strong></p>
<p>transform-style 属性规定如何在 3D 空间中呈现被嵌套的元素。</p>
<p>注释：</p>
<ol>
<li>该属性必须与 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fpr_transform.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/cssref/pr_transform.asp" ref="nofollow noopener noreferrer">transform</a> 属性一同使用</li>
<li>代码与透视一样必须写在父级元素上，但会作用在子元素上</li>
</ol>
<p>语法：transform-style: flat | preserve-3d;</p>

















<table><thead><tr><th>值</th><th>描述</th></tr></thead><tbody><tr><td>flat</td><td>子元素将不保留其 3D 位置。</td></tr><tr><td>preserve-3d</td><td>子元素将保留其 3D 位置。</td></tr></tbody></table>
<p>下面来看个例子：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">body</span>&#123;
<span class="hljs-attribute">perspective</span>: <span class="hljs-number">300px</span>;
&#125;
<span class="hljs-selector-class">.box</span>&#123;
<span class="hljs-attribute">position</span>:relative;
<span class="hljs-attribute">width</span>:<span class="hljs-number">200px</span>;
<span class="hljs-attribute">height</span>:<span class="hljs-number">200px</span>;
<span class="hljs-attribute">margin</span>:<span class="hljs-number">100px</span> auto;
    <span class="hljs-attribute">transition</span>:all <span class="hljs-number">1s</span>;
    <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
&#125;
<span class="hljs-selector-class">.box</span><span class="hljs-selector-pseudo">:hover</span>&#123;
<span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotateY</span>(<span class="hljs-number">45deg</span>)
&#125;
<span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">position</span>:absolute;
    <span class="hljs-attribute">top</span>:<span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>:<span class="hljs-number">0</span>;
    <span class="hljs-attribute">width</span>:<span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background-color</span>: pink;
&#125;

<span class="hljs-selector-class">.box</span> <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:last-child</span>&#123;
<span class="hljs-attribute">background-color</span>:green;
    <span class="hljs-attribute">transform</span>:<span class="hljs-built_in">rotateX</span>(<span class="hljs-number">60deg</span>)
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中一个大盒子中嵌套两个小盒子，当我们鼠标悬浮到大盒子上时，我们先让绿色小盒子沿着X轴正向旋转60度，然后再让大盒子沿着Y轴正向旋转45度 。那么在我们不用transform-style修饰时会得到如下第一个图的效果，而使用了transform-style后会出现第二张图的样子。这个例子很好的描述了transform-style的作用(保留子元素的3D效果)。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d25716ca8045dc9a134a36a5875e83~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            