
---
title: 'canvas中模拟多种光照效果——光照下颜色计算'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed14c094e8b415693f98ed8d69ba018~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 08:21:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed14c094e8b415693f98ed8d69ba018~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h1 data-id="heading-0">前言</h1>
<p>可视化开发中，尤其是在2d视图下，看到一些非常的好玩的特效，五颜六色的光。 好的本篇文章就带你去用canvas去模拟你自己想要的效果。涉及到一些数学知识，不过的都是基础的。我还是争取讲的更加通俗易懂一点。</p>
<h1 data-id="heading-1">光照</h1>
<p>我们能看到物体，是因为光照照射在物体上然后反射到我们的眼睛中，影响光照的因素非常多，位置，光的颜色，物体表面的颜色，材质和粗糙程度。 本篇文章讨论一下光源， 光源又分为环境光， 点光源，平行光， 聚光灯。如下图显示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ed14c094e8b415693f98ed8d69ba018~tplv-k3u1fbpfcp-watermark.image" alt="image-20210617213725914.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">平行光</h1>
<p>平行光顾名思义光线平行，对于一个平面而言，平面不同区域接收到平行光的入射角一样。对于平行光而言,主要是确定光线的方向,光线方向设定好了，光线的与物体表面入射角就确定了，仅仅设置光线位置是不起作用的。</p>
<p>模拟平行光源的光照非常简单，当光垂直照射到平面上，即光线方向和平面呈90度角时，这时光照是最强的。如果照射的角度不断变大（或者说光线和平面的夹角不断变小），光照也会随之变弱，当光线方向完全和平面平行时，这时没有光能照射到平面上，光强变成了0。</p>
<p>我们用一个垂直于平面的向量去描述平面的朝向，在图形学中，一般把这个向量称为“法向量”。 法向量一般只有方向没有长度，下面有个normalize 就是单位长度的1的向量。</p>
<p>我们可以用向量的“点乘”运算来计算光强变化。</p>
<blockquote>
<p>点乘也叫数量积，是接受在实数R上的两个向量并返回一个实数值标量的二元运算。点乘运算规则非常简单，将两个向量对应坐标的乘积求和就行了。</p>
</blockquote>
<p>但是这个只是点乘的数学意义， 但是点乘更重要的是他的几何意义：</p>
<ol>
<li><strong>用来判断两个向量是否在同一个方向</strong></li>
<li><strong>判断一个多边形是否正对摄像机</strong></li>
<li><strong>一个向量在另一个向量上的投影</strong></li>
</ol>
<p>看图我给大家解释：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bebbca5b5e1549fbab8899e84139aca0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210617215019027.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为点乘的结果是一个标量，所以决定大小的就是向量之间的夹角，cos的函数图像是0-90 是正的， 90-180 是负数嘛。 所以点乘和光强的变化十分符合。 这里我们计算的是三维向量，我们用数组来表示向量。 然后实现一些方法。 代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vector3</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">x, y, z</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = x || <span class="hljs-number">0</span>
    <span class="hljs-built_in">this</span>.y = y || <span class="hljs-number">0</span>
    <span class="hljs-built_in">this</span>.z = z || <span class="hljs-number">0</span>
  &#125;
  <span class="hljs-comment">//点乘</span>
  <span class="hljs-function"><span class="hljs-title">dot</span>(<span class="hljs-params">vec</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.x * vec.x + <span class="hljs-built_in">this</span>.y * vec.y + <span class="hljs-built_in">this</span>.z * vec.z
  &#125;
  
  <span class="hljs-comment">// 克隆</span>
  <span class="hljs-function"><span class="hljs-title">clone</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">this</span>.constructor(<span class="hljs-built_in">this</span>.x, <span class="hljs-built_in">this</span>.y, <span class="hljs-built_in">this</span>.z)
  &#125;
  
  <span class="hljs-comment">//求长度</span>
  <span class="hljs-function"><span class="hljs-title">length</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.sqrt(<span class="hljs-built_in">this</span>.x * <span class="hljs-built_in">this</span>.x + <span class="hljs-built_in">this</span>.y * <span class="hljs-built_in">this</span>.y + <span class="hljs-built_in">this</span>.z * <span class="hljs-built_in">this</span>.z)
  &#125;
 
  <span class="hljs-function"><span class="hljs-title">multiplyScalar</span>(<span class="hljs-params">scalar</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x *= scalar
    <span class="hljs-built_in">this</span>.y *= scalar
    <span class="hljs-built_in">this</span>.z *= scalar
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
  
  <span class="hljs-comment">//向量相减</span>
  <span class="hljs-function"><span class="hljs-title">sub</span>(<span class="hljs-params">v</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x -= v.x
    <span class="hljs-built_in">this</span>.y -= v.y
    <span class="hljs-built_in">this</span>.z -= v.z

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
  <span class="hljs-comment">// 单位化</span>
  <span class="hljs-function"><span class="hljs-title">normalize</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.multiplyScalar(<span class="hljs-number">1</span> / <span class="hljs-built_in">this</span>.length())
  &#125;
  <span class="hljs-comment">// 取反</span>
  <span class="hljs-function"><span class="hljs-title">negate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.x = -<span class="hljs-built_in">this</span>.x
    <span class="hljs-built_in">this</span>.y = -<span class="hljs-built_in">this</span>.y
    <span class="hljs-built_in">this</span>.z = -<span class="hljs-built_in">this</span>.z
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们假设页面的左上角为原点O，右方向为x轴正方向，下方向为y轴正方向，垂直屏幕向外的方向为z轴正方向。我们可以这样定义一个宽高都为500的平面:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> plane = &#123;

  <span class="hljs-attr">center</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">250</span>, <span class="hljs-number">250</span>, <span class="hljs-number">0</span>), <span class="hljs-comment">// 平面中心点坐标</span>

  <span class="hljs-attr">width</span>: <span class="hljs-number">500</span>, <span class="hljs-comment">// 宽</span>

  <span class="hljs-attr">height</span>: <span class="hljs-number">500</span>, <span class="hljs-comment">// 高</span>

  <span class="hljs-attr">normal</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>), <span class="hljs-comment">// 朝向，即法向量</span>

  <span class="hljs-attr">color</span>: &#123; <span class="hljs-attr">r</span>: <span class="hljs-number">255</span>, <span class="hljs-attr">g</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">0</span> &#125;, <span class="hljs-comment">// 颜色为红色</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于平行光，只需要关心它的方向和颜色，我们可以这样来定义一个平行光源：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> directionalLight = &#123;

  <span class="hljs-attr">direction</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, -<span class="hljs-number">1</span>), <span class="hljs-comment">// 从屏幕外垂直照向屏幕</span>

  <span class="hljs-attr">color</span>: &#123; <span class="hljs-attr">r</span>: <span class="hljs-number">255</span>, <span class="hljs-attr">g</span>: <span class="hljs-number">255</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">255</span> &#125;, <span class="hljs-comment">// 颜色为纯白色</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>平行光的光线都是平行的，所以它照射到平面上各个位置的效果都是一样的，换言之，整个平面都应该是同一个颜色。
根据上面的规则(光强等于光线反方向向量<strong>点乘</strong>平面法向量)，我们可以计算出这个颜色：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> reverseLightDirection = directionalLight.direction.clone().negate() <span class="hljs-comment">// 计算平行光的反方向向量</span>
<span class="hljs-keyword">const</span> intensity = reverseLightDirection.dot(plane.normal) <span class="hljs-comment">// 计算两向量点乘</span>
<span class="hljs-comment">// 计算有光照时的颜色</span>
<span class="hljs-keyword">const</span> color = &#123;
    <span class="hljs-attr">r</span>: intensity * plane.color.r + intensity * directionalLight.r,
    <span class="hljs-attr">g</span>: intensity * plane.color.g + intensity * directionalLight.g,
    <span class="hljs-attr">b</span>: intensity * plane.color.b + intensity * directionalLight.g,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我写了例子去模拟下这个情况：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d0547b220474ec8859804428d55e9d3~tplv-k3u1fbpfcp-watermark.image" alt="平行光.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码例子在我的<a href="https://github.com/wzf1997/MyPolyfill" target="_blank" rel="nofollow noopener noreferrer">github</a>上欢迎fork
例子中比较难以理解的可能是角度的计算，不过我都做了说明。</p>
<h1 data-id="heading-3">点光源</h1>
<p>在日常生活中，点光源更加常见，白炽灯、台灯等都可以认为是点光源。</p>
<p>首先，我们先定义一个点光源，对于一个点光源来说，我们只需要关心它的位置和颜色：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> plane = &#123;
    <span class="hljs-attr">center</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">250</span>,<span class="hljs-number">250</span>,<span class="hljs-number">0</span>),    <span class="hljs-comment">// 平面中心点坐标</span>
    <span class="hljs-attr">width</span>: <span class="hljs-number">500</span>,                 <span class="hljs-comment">// 宽</span>
    <span class="hljs-attr">height</span>: <span class="hljs-number">500</span>,                <span class="hljs-comment">// 高</span>
    <span class="hljs-attr">normal</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>),        <span class="hljs-comment">// 朝向，即法向量</span>
    <span class="hljs-attr">color</span>: &#123; <span class="hljs-attr">r</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">g</span>: <span class="hljs-number">255</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">0</span> &#125;   <span class="hljs-comment">// 颜色为绿色</span>
&#125;

<span class="hljs-keyword">const</span> pointLight = &#123;
    <span class="hljs-attr">position</span>: <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">250</span>,<span class="hljs-number">250</span>,<span class="hljs-number">60</span>),
    <span class="hljs-attr">color</span>: &#123;
        <span class="hljs-attr">r</span>: <span class="hljs-number">255</span>,
        <span class="hljs-attr">g</span>: <span class="hljs-number">255</span>,
        <span class="hljs-attr">b</span>: <span class="hljs-number">255</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始值设置之后， 这里其实要知道canvas 的<strong>createImageData</strong> 和 <strong>putImageData</strong> 这个方法可以直接填入一个区域的像素颜色值来绘图。 光照的效果原理主要是改变图片的每一个像素值， 达到光照的效果;</p>
<p>光强的计算：光强等于光线反方向向量点乘平面法向量。<strong>但是点光源的光是从一个点发射出来，它们照射到平面上时，所有光线的方向都不一样。所以，我们必须挨个计算平面上所有像素的光强。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> imageData = ctx.createImageData( plane.width, plane.height );
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">render</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">let</span> x = <span class="hljs-number">0</span>; x < imageData.width; x++ ) &#123;
      <span class="hljs-keyword">for</span> ( <span class="hljs-keyword">let</span> y = <span class="hljs-number">0</span>; y < imageData.height; y++ ) &#123;
        <span class="hljs-keyword">let</span> index = y * imageData.width + x;
        <span class="hljs-comment">// 每一个像素点</span>
        <span class="hljs-keyword">let</span> position = <span class="hljs-keyword">new</span> Vector3(x,y,<span class="hljs-number">0</span>);
        
        <span class="hljs-keyword">let</span> normal = <span class="hljs-keyword">new</span> Vector3(<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">1</span>);
        <span class="hljs-comment">// 点光源与每个像素点 之间的方向就是 光线的方向</span>
        <span class="hljs-keyword">let</span> currentToLight = pointLight.position.clone().sub(position).normalize();
        <span class="hljs-keyword">let</span> light = currentToLight.dot(normal);
        imageData.data[ index * <span class="hljs-number">4</span> ] = <span class="hljs-built_in">Math</span>.min( <span class="hljs-number">255</span>, ( pointLight.color.r + plane.color.r ) * light);
        imageData.data[ index * <span class="hljs-number">4</span> + <span class="hljs-number">1</span> ] =  <span class="hljs-built_in">Math</span>.min( <span class="hljs-number">255</span>, ( pointLight.color.g + plane.color.g ) * light );
        imageData.data[ index * <span class="hljs-number">4</span> + <span class="hljs-number">2</span> ] =  <span class="hljs-built_in">Math</span>.min( <span class="hljs-number">255</span>, ( pointLight.color.b + plane.color.b ) * light );
        imageData.data[ index * <span class="hljs-number">4</span> + <span class="hljs-number">3</span> ] = <span class="hljs-number">255</span>;
        &#125;
      &#125;
      ctx.putImageData( imageData, <span class="hljs-number">100</span>, <span class="hljs-number">100</span> );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图如下所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6281a4f1895244cc8f6246b12d78d867~tplv-k3u1fbpfcp-watermark.image" alt="image-20210620000157228.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了看起来更加炫酷， 我增加了move 和 wheel 事件， move 就是改变点光源的x, y  坐标。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">document</span>.addEventListener( <span class="hljs-string">'mousemove'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> e </span>) </span>&#123;
      pointLight.position.x = e.clientX - <span class="hljs-number">100</span>
      pointLight.position.y = e.clientY - <span class="hljs-number">100</span>

      render()
  &#125;, <span class="hljs-literal">false</span> )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88fc75ade032433396dab6746ddb7281~tplv-k3u1fbpfcp-watermark.image" alt="点光源.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>有没有爱是一道光， 绿的你发慌的感觉😁。哈哈哈哈！</p>
<h1 data-id="heading-4">总结</h1>
<p>本篇主要是简单的介绍了几种光照并在canvas 下的模拟实现， 主要是理解光强的计算方式： 反向向量 和 平面的法向量 做点乘。本篇文章所有代码都在我的<a href="https://github.com/wzf1997/MyPolyfill" target="_blank" rel="nofollow noopener noreferrer">github</a>上欢迎自己copy下来玩一玩。最后，文章写作不易，如果看完对你有帮助的话，你的点赞和关注是我持续更新的最大动力。 如果你也喜欢图形，喜欢可视化，你可以点个关注，后面我会持续分享高质量的文章， 勿忘初心！</p></div>  
</div>
            