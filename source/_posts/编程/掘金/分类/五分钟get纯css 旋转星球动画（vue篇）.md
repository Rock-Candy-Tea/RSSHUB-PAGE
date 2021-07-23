
---
title: '五分钟get纯css 旋转星球动画（vue篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c1d167841814d1ea5d8cd70b37dc0b2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 18:20:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c1d167841814d1ea5d8cd70b37dc0b2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>有些东西对于代码层次来看<strong>毫无用处</strong>，但是你架不住甲方的喜欢，就是要有旋转效果</p>
<p>得，撸起袖子，淦</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c1d167841814d1ea5d8cd70b37dc0b2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这是小编做的一个简单的效果，gif图不会截取，各位自行脑补下😄
接下来，咱花五分钟一步步做：
first：先画运动轨迹（线条），和第一个球</p>
<pre><code class="copyable">`<div class="wrap>
    <div class='plant'>
      <div class='ball'>ball1</div>
    </div>
</div>`
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">样式：
`<style>
 .wrap &#123;
            display: flex;
            background-image: url('./bg2.jpg');
            background-size: cover;
            width: 500px;
            height: 500px;
            align-items: center;
            justify-content: center;
        &#125;

        .planet &#123;
            position: absolute;
            border: 2px solid #13c2c2;
            width: 300px;
            height: 300px;
           
        &#125;

        .ball &#123;
            width: 50px;
            height: 50px;
            position: absolute;
            border-radius: 50%;
            background-color: rgba(20, 12, 33, .5);
            left: calc(50% - 25px);
            top: -25px;
            text-align: center;
            line-height: 50px;
            color: #13c2c2;
        &#125;
        </style>`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f6e4c38d3674563b99cb673ef9b316e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
分析：轨迹高宽为300px，小球大小为50px，所以定位于top-border的位置的坐标为left:（50% -25px）,top: -25px,用百分比的好处就是你可以根据需要修改轨迹的大小。</p>
<p>second： 旋转缩放轨迹,小球：</p>
<pre><code class="copyable">.planet &#123;
    transform-style: preserve-3d;
    transform: scaleY(0.5) rotateZ(30deg);
    border-radius: 50%;
&#125;
.ball &#123;
    transform: rotateZ(-30deg) scaleY(2);
&#125; 

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e715a351c434bedb8c1636347b75316~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>third：动起来</p>
<pre><code class="copyable">/* // 公转动画 */
        @keyframes planet-rotate &#123;
        0% &#123;
            transform:  rotate(30deg) scaleY(0.5) rotate(0); // 倾斜30度
        &#125;
        100% &#123;
            transform:  rotate(30deg) scaleY(0.5) rotate(360deg);
        &#125;
        &#125;

        /* // 自转动画 */
        @keyframes self-rotate &#123;
        0% &#123;
                transform: rotate(0) scaleY(2) rotate(-30deg);
            &#125;
        100% &#123;
                transform: rotate(-360deg) scaleY(2) rotate(-30deg);
            &#125;
        &#125;
         .planet &#123;
            animation: planet-rotate 16s linear infinite; // 无限次
        &#125;

        .ball &#123;
            animation: self-rotate 16s linear infinite;
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76829e1531df4b84bb42f82c960e57db~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一个实现了，其它的就好办了，最简单的就是在第一次还没旋转轨迹的时候，把需要的小球定位好，附上最终代码</p>
<pre><code class="hljs language-js copyable" lang="js"><style>
       .wrap &#123;
            <span class="hljs-attr">display</span>: flex;
            background-image: url(<span class="hljs-string">'./bg2.jpg'</span>);
            background-size: cover;
            width: 500px;
            height: 500px;
            align-items: center;
            justify-content: center;
        &#125;

        .planet &#123;
            <span class="hljs-attr">position</span>: absolute;
            border: 2px solid #13c2c2;
            width: 300px;
            height: 300px;
            transform-style: preserve-3d;
            transform: scaleY(<span class="hljs-number">0.5</span>) rotateZ(30deg);
            border-radius: <span class="hljs-number">50</span>%;
           
        &#125;

        .ball &#123;
            <span class="hljs-attr">width</span>: 50px;
            height: 50px;
            position: absolute;
            border-radius: <span class="hljs-number">50</span>%;
            background-color: rgba(<span class="hljs-number">20</span>, <span class="hljs-number">12</span>, <span class="hljs-number">33</span>, <span class="hljs-number">.5</span>);
            left: calc(<span class="hljs-number">50</span>% - 25px);
            top: -25px;
            text-align: center;
            line-height: 50px;
            color: #13c2c2;
            transform: rotateZ(-30deg) scaleY(<span class="hljs-number">2</span>);
        &#125;
        .second &#123;
            <span class="hljs-attr">left</span>: calc(<span class="hljs-number">50</span>% + 125px);
            top: 125px;
        &#125;
        .third &#123;
            <span class="hljs-attr">left</span>: calc(<span class="hljs-number">50</span>% - 25px);
            top: 275px;
        &#125;
        .four &#123;
            <span class="hljs-attr">left</span>: calc(<span class="hljs-number">50</span>% - 175px);
            top: 125px;
        &#125;
        
        <span class="hljs-comment">/* // 公转动画 */</span>
        @keyframes planet-rotate &#123;
        <span class="hljs-number">0</span>% &#123;
            <span class="hljs-attr">transform</span>:  rotate(30deg) scaleY(<span class="hljs-number">0.5</span>) rotate(<span class="hljs-number">0</span>);
        &#125;
        <span class="hljs-number">100</span>% &#123;
            <span class="hljs-attr">transform</span>:  rotate(30deg) scaleY(<span class="hljs-number">0.5</span>) rotate(360deg);
        &#125;
        &#125;

        <span class="hljs-comment">/* // 自转动画 */</span>
        @keyframes self-rotate &#123;
        <span class="hljs-number">0</span>% &#123;
            <span class="hljs-attr">transform</span>: rotate(<span class="hljs-number">0</span>) scaleY(<span class="hljs-number">2</span>) rotate(-30deg);
        &#125;
        <span class="hljs-number">100</span>% &#123;
            <span class="hljs-attr">transform</span>: rotate(-360deg) scaleY(<span class="hljs-number">2</span>) rotate(-30deg);
        &#125;
        &#125;

        .planet &#123;
            <span class="hljs-attr">animation</span>: planet-rotate 16s linear infinite;
        &#125;

        .ball &#123;
            <span class="hljs-attr">animation</span>: self-rotate 16s linear infinite;
        &#125; 
    </style>
</head>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'wrap'</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'planet'</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'ball'</span>></span>ball1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'ball second'</span>></span>ball2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'ball third'</span>></span>ball3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'ball four'</span>></span>ball4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
              <span class="hljs-keyword">return</span> &#123;
                  
              &#125;
            &#125;,
            <span class="hljs-attr">methods</span>: &#123;
                
            &#125;,
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            