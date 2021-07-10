
---
title: 'CSS实现吃豆豆动画'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e320a2a335f64b798b9025eade3f639b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 18:43:07 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e320a2a335f64b798b9025eade3f639b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAQlBMVEVHcEwlRnqtZBj76q4lRnolRnolRnolRnolRnokRnr/gGtrVUeLXDBKTl+hYSHasW7Ik0zs0JG4dCvUdEE0SW+rYxrLQJfjAAAACnRSTlMA////0H/xUaMi5MCoTwAACfVJREFUeNrtnQl3qygUgJ9GXAqosfL//+pgmgXwXmRNJGdu55xO+6rx8+6I8O9fehmGriN93zdN07bVXdpW/ih/SbpuGP6dXbpOXv7z2i3S9ISck2eQOnAhMHG64VQQbmrAaM4B05GmipaGdB+m6BNQPBXzMYtKR3EPbB/RS5eY4g+lIW9WBqnySCvVMrzRpqqs0g9nwVg5p1KYlHEchRT5bftp+y3n6xlQDjAkABtrKULU9f377ev+4/1/NiT+URRiZRhrcZP6WLa/Gq005BORaqXsdYEuHPIP798ZxSyt6d5sVfxJESRCsvB32lfXwhRjnUBGmKXNoJQe04VIASJqRC/9G7yDsyQMiloYz+0pHYghEoPISAGgpDSvHsCoMwmA0mfjSG5UOsqah2RodkljzMkhZZdamiEDB8+Nsbk9T04yGNljDXGOZZ6u0+Tj9DuvbyNJBuPO0ABtLNPlJtfZJ4CNNCWJoY8gddwxNpm9YrHh9DEkBoeMud4Kma8XRZaYpBJOYvg59U9wOsblMvmGrzQe30dyqFZ1dxPfO0FT5BOdw989THVs4q1TFk+iN4PMu7CaLpd4EJOExNaJLE4d0xQKYpJ0cY5Ozcwwu6WOu2cs9TUYxPB4b4fvLRzTUXbT1HH7y0BnB0j6CAehkPFfFzd1TMsi6sU1/P4VM9NiISHBlYnBMR+kad075sXlmMehj1twnfTUqJH4GJfqIKte7S72emPnHbdiYHIB0e6ATjKq1UoTaFh6wBL2csMIVo9fH/v6QRHAgoxrOHQQxG/36tC1ODmGOeBGBRmXalgcdhDQ1xF1vI6a3DF2d4r7G1enOUgNOshlFq7qUCxrca9ldiCam7ilxRbP6JbOYsYtfLFmkcXEgLG1DN/6eroxHjqh5bh+Uw27e1oWVK7pN+AqwzUcq/UYTPw8nWufLFBHN2zcxLRYlmGPs6rA2Wy0uJe/E7TknbHIa1WH1bLA8DAj3JpxET+FCNCWZ5uNT6jxTPZK/1mXoCBeKlGLRT2lP69XN3XdqqCojKX1ZVda6iD2McjeXSHa0I+AHd2InGAJgjRVM6gOBfygDrarRJnho6eQBbrns+HkcNUCWtYClJa66qFgPbqqZEBTCOAgRqxCOhQBWpZeIC6QBq91hEoI5unTjsMsK9DCFigY9WNn19hgVCrELalrTw6WnYMYzjHhQ2/7G2xTx1HvwpzSe4cVi5ORQQwMW9+72FU5L4gGsa6Yu1RcDeIhs64Qs8izt0vGH+n9/IKaIlYpM2UqkYOrwwq5CgBjWpyGtxaonxe4KaJ3hx+7O0HaqVkxLBPj8FmBVmjNevIUFhUuDmMq5NDV9RwyPe/95IvxAhG7ymqxHGE5sZJL2kPLUhUinkXfrnFwGFwXD99djNLSFh/meXEb2B6Oyiwm0I7BC+OlTlOVPk9K8CIYzu5YHwKDTI6XAo5lz3WEqEXwQRKhh5cyLa6D81P4PXBw984as9YaGXHwx4Ba8rmOldUat/BHt9cQ38AaljnBdCJqs60OcXVDJZP//ZwSWtV9FpHNtgg22KuYx/U2tB5Mcp1TYOiphNhiFjgWeJ3DL2OZpuuUisIoUyzZEJ76I+LmyqWdv8LwnEiwMYczihjxeqtBsuFJSTg2oD1ETQx4v6D1VleSZW1xCwvAfVGWpQ069kgrQksAUW2rReYzsboIjSABuDQX0QJwB9cnZVgWVgE31vrklAJnEmVObykgYCk/VGX5OlpuKb5eiovUAvJ2tMstw0kIkNdpiSA91K6XA6K8CVCyr4PePhTo65q3DyX7OpTbSVk1PB62mhJ9HSpSqtKaESxsFRm0tLBVcvTV+vbBrLRK4hC7aitN9B0ZpX6vNMgjGIt5ZdmMv32KrmprD1afsPd4FEhThK0+WfTl3kpd482AGvG3jQdZK1+t8ireDswhofigRb3fxfI/4jj+xkffUX/1ccxxhEP9qyyBEH9Cx9vhf8TB7eiSpBHjZVSa4whQMJC1TqIR6q8RERtjOr2ID0yx3oYi0oAIvZCPz4eG64p3ObuREeOHUIR3MBVJwq9yll5P7KHdiPBOiOoRa/AjXz21J3k04l+i8OjErj4kaXWQiIVO/EvA+KLRAEnUVomtjPd6SvR3RLoeMT54nKFH1EqtkkEGFaQuTlSQrsxhRiOIt51S/Ho8B11+FUlwRaHnU4utEI38/mgSjRJ8PhWEtN6Z6WcncQOU4efjKoh3zfi7/+DfhPrwOZ9a/iYBiVJJxPlei3CqIDTYEqAPFow5/c71fAdVIwmo4n+cTIGbr2n9NULAE5ifcNNS63hvEOFk0wxYnICBBZ0I9xERBVILF0uggNdxuOkR4S6ngvgPmArzHv4KpMKGQFjQ+Rw6q9dC6R6dgZaJF7RVWIH0BTY9h+fz0ohHOyLuy+He/hN4GUR3/RxcBx2f76izarI9CaXmzRmhNQuSfIgJkva5GzN6HJbhQxCNsDGDSh56plmef6sg2eaXPsYBt5W+H6VE6omG6hOS1w4hiTWiThbJ1YO+RSO1vrpMlomf6nhQGz0m7qT6W04XOUHyzhZ4rkG+0hxL66oDW9mnPWyL3TMmssxyQUwr01CHX7b2OvUIaqS48TnMtAoEQTQixJeAlDfSiGmk/l8jpwIpTyFqOfeNIHWBooC036ERtUQp2tm/CKT5jjySbxTlvUVj2yhjvyWDVL3yfKRojXwLSEWUp7q0PBAKPp7m5YGoT3WH7wAZ1BeOywNZv3Gak/LIqriwxbQ5jaTcsEW1eb+FvoWo+zr5V/IUOvNtsapU2zJXSyj0xVB13sPfq0kkZA7dubIIKXIlJ8Cy7u+BN22RVcr+peOuxHdcBbA04FAVmEoEtO5vX55K4KVZS1QJvBBzU1rgUl8JapBNYIowLoZtD9NWRTWKqqe36L48BSz8QPH9epqqIDehlh2UuqocEmrdV7AvhuRoM74m80yeDIEX3ppreNN235FxV58DNjhswn5K8zK21+5ctjut6NmUIoy9tVvitnHr2VDM3ahtW8KQ/Vbsp9GGiWHfk8skyTSFz9/HdxhHe4uR/RxX/mG1SGXwypcDJNmCMfucZ/C1CuCQUbiBUDYbe7tiRkZX8GIat50d+wqR1fdN7ygGzrHrcN4kGFHK02cil5M6INgQVsvnNz77T5PqUFYJJInYmIBplJfP5On4eiOwYfhuCD44oLyYVs43rI1rk3H7usttzq8Qo3j84vavN9mOkAeuq8dHEd9NtCVKX51Oen+MM6IEYvz5StOehKLpIjD+nKU5AQWJpLizdB+1sb5LQvFRxbSJVGHmSdK/0WWaPguEYmcSJ68aWkK6rAw6jwSSCmrTWVHT96R7HwHANEgqybVJL+E2vE2q7Uu91Gr73SbbNUvZDtiOlCeIv4r/AI+0XUwz1lvcAAAAAElFTkSuQmCC")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h1 data-id="heading-0">介绍</h1>
<p>在此之前啊，看到一个吃豆豆的游戏。那我们今天就用css3来搞一个吃豆豆的动画啊。</p>
<p>其实实现的方法也很简单。使用CSS3 <strong>@keyframes</strong> 动画和<strong>rotate()</strong> 属性进行一个旋转的控制，再加上一个<strong>box-shadow</strong>属性基本是就差不多了。</p>
<p><strong>效果图</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e320a2a335f64b798b9025eade3f639b~tplv-k3u1fbpfcp-watermark.image" alt="吃豆豆.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到啊，小圆点一直做从右往左的动作，左边一个圆球又开又闭合，看起来就行往嘴里送东西的样子。</p>
<p><strong>实现步骤</strong></p>
<ul>
<li>简单写个布局样式</li>
<li>圆球的上下闭合动画</li>
<li>小圆点动画</li>
</ul>
<h1 data-id="heading-1">布局样式</h1>
<h2 data-id="heading-2">布局</h2>
<p>我们这里只需要一个圆球和小圆点组成就够了</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pacman"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">圆球样式</h2>
<p>接下来搞点样式，这里我们用伪元素来写。注意这里给它加上<strong>绝对定位（absolute）</strong>，因为要做上下闭合的动画，我们先给加上。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:before &#123;
      content: <span class="hljs-string">''</span>;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">background</span>: <span class="hljs-number">#fb07ff</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-comment">/*保持居中位置*/</span>
      <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-comment">/*保持居中位置*/</span>
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">50px</span>;
      <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">50px</span>;
      <span class="hljs-comment">/*上半圆效果*/</span>
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50px</span> <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就长这样啊</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/142338bd851e4743ac9167892d24e761~tplv-k3u1fbpfcp-watermark.image" alt="d1.png" loading="lazy" referrerpolicy="no-referrer">
然后给after也加上</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:before,
body .pacman:after
&#123;
      content: <span class="hljs-string">''</span>;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">background</span>: <span class="hljs-number">#fb07ff</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-comment">/*保持居中位置*/</span>
      <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-comment">/*保持居中位置*/</span>
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">50px</span>;
      <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">50px</span>;
      <span class="hljs-comment">/*上半圆效果*/</span>
      <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50px</span> <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d9ad7bfd6134944b81efe735bc09fb7~tplv-k3u1fbpfcp-watermark.image" alt="d2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里可能又会问怎么长这样，都重叠一起咯。:before和:after都设置了在<code>页面居中</code>的效果，不重叠在一起才奇怪呢！所以啊莫惊慌！</p>
</blockquote>
<h2 data-id="heading-4">圆点样式</h2>
<p>这里喜欢啥颜色就搞啥颜色就完事了，也要加<strong>绝对定位</strong>哦</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.dot</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#02ec2a</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">圆球动画</h1>
<blockquote>
<p>这里有个注意的小点啊，我们上面不是对圆球的:before和:after都写了相同的样式么，为了方便我们先对其中之一进行操作，等最后效果写完了加上就完事了。这里我们对 <strong>:before进行操作</strong></p>
</blockquote>
<p>在此之前先搞个上下会动的效果先，用到我们的 <strong>@keyframes</strong> 动画配合上<strong>transform: rotate()</strong> 来完成。</p>
<h2 data-id="heading-6">@keyframes是什么？</h2>
<p><code>@keyframes</code>：以百分比来规定改变发生的时间，或者通过关键词 "<code>from</code>" 和 "<code>to</code>"，等价于 0% 和 100%。0% 是动画的<code>开始时间</code>，100% 动画的<code>结束时间</code>。</p>
<h2 data-id="heading-7">注意</h2>
<ul>
<li>
<p>Internet Explorer 10、Firefox 以及 Opera 支持 @keyframes 规则和 animation 属性。</p>
</li>
<li>
<p>Chrome 和 Safari 需要前缀 -webkit-。</p>
</li>
<li>
<p>Internet Explorer 9，以及更早的版本，不支持 @keyframe 规则或 animation 属性。</p>
</li>
</ul>
<h2 data-id="heading-8">上半球动画（up）</h2>
<p>所以我们这里做一个<code>适配</code>，然后<code>rotate</code>的旋转角度搞到合适即可。是一个<code>向下咬合</code>的效果。代码如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* up */</span>
<span class="hljs-keyword">@-webkit-keyframes</span> up &#123;

  <span class="hljs-number">0%</span>,
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-comment">/*咬合张开的角度*/</span>
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@-moz-keyframes</span> up &#123;

  <span class="hljs-number">0%</span>,
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@-o-keyframes</span> up &#123;

  <span class="hljs-number">0%</span>,
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
  &#125;
&#125;

<span class="hljs-keyword">@keyframes</span> up &#123;

  <span class="hljs-number">0%</span>,
  <span class="hljs-number">100%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
  &#125;

  <span class="hljs-number">50%</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来给<code>上半圆球</code>加上无限循环的动画</p>
<blockquote>
<p>这里是动画是上半球的，所以只需加在:before身上即可</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:before&#123;
  content: <span class="hljs-string">''</span>;
  <span class="hljs-attribute">position</span>: absolute;
  <span class="hljs-attribute">background</span>: <span class="hljs-number">#fb07ff</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
  <span class="hljs-comment">/*保持居中位置*/</span>
  <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
  <span class="hljs-comment">/*保持居中位置*/</span>
  <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">50px</span>;
  <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">50px</span>;
  <span class="hljs-comment">/*上半圆效果*/</span>
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50px</span> <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
  
  <span class="hljs-comment">/**** 添加动画 ****/</span>
  -webkit-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
  <span class="hljs-comment">/* 0.6s 动画的速度，越大越慢  infinite --- 无限循环 */</span>
  -moz-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
  -o-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
  <span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看看效果
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0103f031e0054f24b244bdb3ba436680~tplv-k3u1fbpfcp-watermark.image" alt="d4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">下半球动画（down）</h2>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* down */</span>
  <span class="hljs-keyword">@-webkit-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@-moz-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@-o-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>加在:after上</p>
</blockquote>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:after &#123;
      /*下半圆效果*/
    border-radius: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">50px</span>;
    -webkit-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    -moz-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    -o-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上下动画都写完了，我们来看看现在的效果先，激动人心的时候到了，<code>上才艺</code>！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe27fbe012f0432da25498d800e15291~tplv-k3u1fbpfcp-watermark.image" alt="d3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>咿呀我去！这什么玩意啊？怎么跟想象的不一样的。这时候肯定是骂骂咧咧退出群聊，搞这么久就搞成这样啊！你这也不行啊</p>
</blockquote>
<p>那我们只需给 <strong>:after</strong> 加上一个<strong>margin-top</strong>即可，这才是<code>最终时刻</code>。</p>
<p>来人！给我上图！上代码！</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:after &#123;
  /*为了使两个半圆咬合时不出现缝隙*/
  margin-top: -<span class="hljs-number">1px</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cde5529ab7fe41e5bf924352fed469dd~tplv-k3u1fbpfcp-watermark.image" alt="d5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>哎，现在没话说了吧（打不着打不着...），就是玩儿~</p>
</blockquote>
<p>接下来搞点正经的，圆点动画，简直不要太简单！</p>
<h1 data-id="heading-10">圆点动画</h1>
<p>这里是一个从左到右的动画，我们要改变的是<code>margin-left</code>值，改变当前的位置。到了这你就应该明白之前我们为什么要设置<code>绝对定位</code>了</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* r-to-l */</span>
  <span class="hljs-keyword">@-webkit-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@-moz-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@-o-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给小圆点加上，效果就出来了</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.dot</span> &#123;
    -webkit-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    -moz-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    -o-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aae9ae967aa042958826c4daed36c87a~tplv-k3u1fbpfcp-watermark.image" alt="d6.gif" loading="lazy" referrerpolicy="no-referrer">
我们可以明显的看到小圆点是从右到左的一个动作啊！</p>
<blockquote>
<p>哎呀，你这也不像开头那样那么多圆点啊，你这又忽悠我？</p>
</blockquote>
<p>上才艺！咋们给它加上<strong>box-shadow</strong>就完事了啊，然后再加上z-index让小圆点在圆球的下方，这时候再来看看效果的话，就像是无限产生的小圆点。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.dot</span> &#123;
    <span class="hljs-comment">/*层级关系 越大越在上层*/</span>
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>; 
      
    <span class="hljs-comment">/*实际上只有一个圆点，用了box-shadow的阴影属性。*/</span>
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">30px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">60px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">90px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">120px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">150px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不着急，咋先解释一波啊！</p>
<h2 data-id="heading-11">box-shadow</h2>
<ol>
<li>
<p>box-shadow: offset-x | offset-y | blur-radius | spread-radius | color ()</p>
<p>(1) <code><offset-x></code> <code><offset-y></code>: 这是头两个 <code><length></code>值，用来设置阴影偏移量。<code><offset-x></code> 设置水平偏移量，如果是负值则阴影位于元素左边。 <code><offset-y></code> 设置垂直偏移量，如果是负值则阴影位于元素上面。可用单位请查看 <code><length></code>。如果两者都是0，那么阴影位于元素后面。这时如果设置了 <code><blur-radius></code> 或 <code><spread-radius></code> 则有模糊效果。</p>
<p>(2) <code><blur-radius></code>: 这是第三个 <code><length></code> 值。值越大，模糊面积越大，阴影就越大越淡。 不能为负值。默认为0，此时阴影边缘锐利。</p>
<p>(3) <code><spread-radius></code> : 这是第四个 <code><length></code> 值。取正值时，阴影扩大；取负值时，阴影收缩。默认为0，此时阴影与元素同样大。（默认为 0 ，所以这里只设置了前3个值）</p>
<p>(4)  <code><color></code> : 相关事项查看 <code><color></code> 。如果没有指定，则由浏览器决定——通常是color的值，不过目前Safari取透明。</p>
</li>
<li>
<p>这里用的<code>border-style</code>: type(类型)是<code>outset</code>而不是inset(定义 3D outset 边框。其效果取决于 border-color 的值);</p>
</li>
</ol>
<p><strong>效果</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a759a42f65a493690052b7af461b749~tplv-k3u1fbpfcp-watermark.image" alt="d7.gif" loading="lazy" referrerpolicy="no-referrer">
到这里，我们的代码编写就全部完成啦！</p>
<h1 data-id="heading-12">完整代码</h1>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>吃豆豆<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/* up */</span>
  <span class="hljs-keyword">@-webkit-keyframes</span> up &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-comment">/*咬合张开的角度*/</span>


  <span class="hljs-keyword">@-moz-keyframes</span> up &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@-o-keyframes</span> up &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@keyframes</span> up &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(-<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-comment">/* down */</span>
  <span class="hljs-keyword">@-webkit-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@-moz-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@-o-keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">@keyframes</span> down &#123;

    <span class="hljs-number">0%</span>,
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0</span>);
    &#125;

    <span class="hljs-number">50%</span> &#123;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">30deg</span>);
    &#125;
  &#125;

  <span class="hljs-comment">/* r-to-l */</span>
  <span class="hljs-keyword">@-webkit-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@-moz-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@-o-keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-keyword">@keyframes</span> r-to-l &#123;
    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">1px</span>;
    &#125;
  &#125;

  <span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#d44747</span>;
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
  &#125;

  <span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:before,
  body .pacman:after &#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#fb07ff</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-comment">/*保持居中位置*/</span>
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-comment">/*保持居中位置*/</span>
    <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">50px</span>;
    <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">50px</span>;
    <span class="hljs-comment">/*上半圆效果*/</span>
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50px</span> <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
    <span class="hljs-comment">/*动画*/</span>
    -webkit-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-comment">/* 0.6s 动画的速度，越大越慢  infinite --- 无限循环 */</span>
    -moz-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
    -o-<span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-attribute">animation</span>: up <span class="hljs-number">0.6s</span> infinite;
  &#125;

  <span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.pacman</span>:after &#123;
    /*为了使两个半圆咬合时不出现缝隙*/
    margin-top: -<span class="hljs-number">1px</span>;
    <span class="hljs-comment">/*下半圆效果*/</span>
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">50px</span> <span class="hljs-number">50px</span>;
    -webkit-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    -moz-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    -o-<span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-attribute">animation</span>: down <span class="hljs-number">0.6s</span> infinite;
  &#125;

  <span class="hljs-selector-tag">body</span> <span class="hljs-selector-class">.dot</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">12px</span>;
    <span class="hljs-attribute">margin-top</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-number">#02ec2a</span>;
    <span class="hljs-comment">/*层级关系 越大越在上层*/</span>
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
    <span class="hljs-comment">/*实际上只有一个圆点，用了box-shadow的阴影属性。*/</span>
    <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">30px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">60px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">90px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">120px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>, <span class="hljs-number">150px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">#02ec2a</span>;
    <span class="hljs-comment">/*
   1、box-shadow: offset-x | offset-y | blur-radius | spread-radius | color ()
    （1）<offset-x> <offset-y>: 这是头两个 <length>值，用来设置阴影偏移量。<offset-x> 设置水平偏移量，如果是负值则阴影位于元素左边。 <offset-y> 设置垂直偏移量，如果是负值则阴影位于元素上面。可用单位请查看 <length>。如果两者都是0，那么阴影位于元素后面。这时如果设置了 <blur-radius> 或 <spread-radius> 则有模糊效果。
    （2）<blur-radius>: 这是第三个 <length> 值。值越大，模糊面积越大，阴影就越大越淡。 不能为负值。默认为0，此时阴影边缘锐利。
    ※（3）<spread-radius> : 这是第四个 <length> 值。取正值时，阴影扩大；取负值时，阴影收缩。默认为0，此时阴影与元素同样大。（默认为 0 ，所以这里只设置了前3个值）
（4）<color> : 相关事项查看 <color> 。如果没有指定，则由浏览器决定——通常是color的值，不过目前Safari取透明。

   2、这里用的border-style:type(类型)是outset而不是inset(定义 3D outset 边框。其效果取决于 border-color 的值);

  */</span>
    -webkit-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    -moz-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    -o-<span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
    <span class="hljs-attribute">animation</span>: r-to-l <span class="hljs-number">0.6s</span> infinite;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>

  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"demo"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pacman"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">效果图</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b076dc8653f145a485ee629ef8a2fbcf~tplv-k3u1fbpfcp-watermark.image" alt="吃豆豆.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">结尾</h1>
<p>今天就先到这里啦！我们下期再见！码字不易，觉得不错的可以动动小指头点点赞哟~</p></div>  
</div>
            