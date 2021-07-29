
---
title: '微信炸屎？红包雨？拿来吧你 —— SVG不完全指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/950c1b618da2405299ede24929d28c0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 18:56:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/950c1b618da2405299ede24929d28c0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAQlBMVEVHcEwlRnqtZBj76q4lRnolRnolRnolRnolRnokRnr/gGtrVUeLXDBKTl+hYSHasW7Ik0zs0JG4dCvUdEE0SW+rYxrLQJfjAAAACnRSTlMA////0H/xUaMi5MCoTwAACfVJREFUeNrtnQl3qygUgJ9GXAqosfL//+pgmgXwXmRNJGdu55xO+6rx8+6I8O9fehmGriN93zdN07bVXdpW/ih/SbpuGP6dXbpOXv7z2i3S9ISck2eQOnAhMHG64VQQbmrAaM4B05GmipaGdB+m6BNQPBXzMYtKR3EPbB/RS5eY4g+lIW9WBqnySCvVMrzRpqqs0g9nwVg5p1KYlHEchRT5bftp+y3n6xlQDjAkABtrKULU9f377ev+4/1/NiT+URRiZRhrcZP6WLa/Gq005BORaqXsdYEuHPIP798ZxSyt6d5sVfxJESRCsvB32lfXwhRjnUBGmKXNoJQe04VIASJqRC/9G7yDsyQMiloYz+0pHYghEoPISAGgpDSvHsCoMwmA0mfjSG5UOsqah2RodkljzMkhZZdamiEDB8+Nsbk9T04yGNljDXGOZZ6u0+Tj9DuvbyNJBuPO0ABtLNPlJtfZJ4CNNCWJoY8gddwxNpm9YrHh9DEkBoeMud4Kma8XRZaYpBJOYvg59U9wOsblMvmGrzQe30dyqFZ1dxPfO0FT5BOdw989THVs4q1TFk+iN4PMu7CaLpd4EJOExNaJLE4d0xQKYpJ0cY5Ozcwwu6WOu2cs9TUYxPB4b4fvLRzTUXbT1HH7y0BnB0j6CAehkPFfFzd1TMsi6sU1/P4VM9NiISHBlYnBMR+kad075sXlmMehj1twnfTUqJH4GJfqIKte7S72emPnHbdiYHIB0e6ATjKq1UoTaFh6wBL2csMIVo9fH/v6QRHAgoxrOHQQxG/36tC1ODmGOeBGBRmXalgcdhDQ1xF1vI6a3DF2d4r7G1enOUgNOshlFq7qUCxrca9ldiCam7ilxRbP6JbOYsYtfLFmkcXEgLG1DN/6eroxHjqh5bh+Uw27e1oWVK7pN+AqwzUcq/UYTPw8nWufLFBHN2zcxLRYlmGPs6rA2Wy0uJe/E7TknbHIa1WH1bLA8DAj3JpxET+FCNCWZ5uNT6jxTPZK/1mXoCBeKlGLRT2lP69XN3XdqqCojKX1ZVda6iD2McjeXSHa0I+AHd2InGAJgjRVM6gOBfygDrarRJnho6eQBbrns+HkcNUCWtYClJa66qFgPbqqZEBTCOAgRqxCOhQBWpZeIC6QBq91hEoI5unTjsMsK9DCFigY9WNn19hgVCrELalrTw6WnYMYzjHhQ2/7G2xTx1HvwpzSe4cVi5ORQQwMW9+72FU5L4gGsa6Yu1RcDeIhs64Qs8izt0vGH+n9/IKaIlYpM2UqkYOrwwq5CgBjWpyGtxaonxe4KaJ3hx+7O0HaqVkxLBPj8FmBVmjNevIUFhUuDmMq5NDV9RwyPe/95IvxAhG7ymqxHGE5sZJL2kPLUhUinkXfrnFwGFwXD99djNLSFh/meXEb2B6Oyiwm0I7BC+OlTlOVPk9K8CIYzu5YHwKDTI6XAo5lz3WEqEXwQRKhh5cyLa6D81P4PXBw984as9YaGXHwx4Ba8rmOldUat/BHt9cQ38AaljnBdCJqs60OcXVDJZP//ZwSWtV9FpHNtgg22KuYx/U2tB5Mcp1TYOiphNhiFjgWeJ3DL2OZpuuUisIoUyzZEJ76I+LmyqWdv8LwnEiwMYczihjxeqtBsuFJSTg2oD1ETQx4v6D1VleSZW1xCwvAfVGWpQ069kgrQksAUW2rReYzsboIjSABuDQX0QJwB9cnZVgWVgE31vrklAJnEmVObykgYCk/VGX5OlpuKb5eiovUAvJ2tMstw0kIkNdpiSA91K6XA6K8CVCyr4PePhTo65q3DyX7OpTbSVk1PB62mhJ9HSpSqtKaESxsFRm0tLBVcvTV+vbBrLRK4hC7aitN9B0ZpX6vNMgjGIt5ZdmMv32KrmprD1afsPd4FEhThK0+WfTl3kpd482AGvG3jQdZK1+t8ireDswhofigRb3fxfI/4jj+xkffUX/1ccxxhEP9qyyBEH9Cx9vhf8TB7eiSpBHjZVSa4whQMJC1TqIR6q8RERtjOr2ID0yx3oYi0oAIvZCPz4eG64p3ObuREeOHUIR3MBVJwq9yll5P7KHdiPBOiOoRa/AjXz21J3k04l+i8OjErj4kaXWQiIVO/EvA+KLRAEnUVomtjPd6SvR3RLoeMT54nKFH1EqtkkEGFaQuTlSQrsxhRiOIt51S/Ho8B11+FUlwRaHnU4utEI38/mgSjRJ8PhWEtN6Z6WcncQOU4efjKoh3zfi7/+DfhPrwOZ9a/iYBiVJJxPlei3CqIDTYEqAPFow5/c71fAdVIwmo4n+cTIGbr2n9NULAE5ifcNNS63hvEOFk0wxYnICBBZ0I9xERBVILF0uggNdxuOkR4S6ngvgPmArzHv4KpMKGQFjQ+Rw6q9dC6R6dgZaJF7RVWIH0BTY9h+fz0ohHOyLuy+He/hN4GUR3/RxcBx2f76izarI9CaXmzRmhNQuSfIgJkva5GzN6HJbhQxCNsDGDSh56plmef6sg2eaXPsYBt5W+H6VE6omG6hOS1w4hiTWiThbJ1YO+RSO1vrpMlomf6nhQGz0m7qT6W04XOUHyzhZ4rkG+0hxL66oDW9mnPWyL3TMmssxyQUwr01CHX7b2OvUIaqS48TnMtAoEQTQixJeAlDfSiGmk/l8jpwIpTyFqOfeNIHWBooC036ERtUQp2tm/CKT5jjySbxTlvUVj2yhjvyWDVL3yfKRojXwLSEWUp7q0PBAKPp7m5YGoT3WH7wAZ1BeOywNZv3Gak/LIqriwxbQ5jaTcsEW1eb+FvoWo+zr5V/IUOvNtsapU2zJXSyj0xVB13sPfq0kkZA7dubIIKXIlJ8Cy7u+BN22RVcr+peOuxHdcBbA04FAVmEoEtO5vX55K4KVZS1QJvBBzU1rgUl8JapBNYIowLoZtD9NWRTWKqqe36L48BSz8QPH9epqqIDehlh2UuqocEmrdV7AvhuRoM74m80yeDIEX3ppreNN235FxV58DNjhswn5K8zK21+5ctjut6NmUIoy9tVvitnHr2VDM3ahtW8KQ/Vbsp9GGiWHfk8skyTSFz9/HdxhHe4uR/RxX/mG1SGXwypcDJNmCMfucZ/C1CuCQUbiBUDYbe7tiRkZX8GIat50d+wqR1fdN7ygGzrHrcN4kGFHK02cil5M6INgQVsvnNz77T5PqUFYJJInYmIBplJfP5On4eiOwYfhuCD44oLyYVs43rI1rk3H7usttzq8Qo3j84vavN9mOkAeuq8dHEd9NtCVKX51Oen+MM6IEYvz5StOehKLpIjD+nKU5AQWJpLizdB+1sb5LQvFRxbSJVGHmSdK/0WWaPguEYmcSJ68aWkK6rAw6jwSSCmrTWVHT96R7HwHANEgqybVJL+E2vE2q7Uu91Gr73SbbNUvZDtiOlCeIv4r/AI+0XUwz1lvcAAAAAElFTkSuQmCC")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>对于前端的2D动画需求，一般首先会考虑CSS动画，其次是直接贴图，实在不行可能还要上Canvas。</p>
<p>其实有一大部分需求如果用SVG会更加简单，SVG可以和Js很好的融合在一起，写法上与熟知的CSS动画也大同小异，又可以实现一些纯CSS不好实现的动画，因为其矢量图的性质还可以在微信公众号内直接使用，用来实现一些<strong>交互式动画</strong>让运营小姐姐惊呼卧槽再好不过。</p>
<p>可缩放矢量图形相比位图的优势除了可以无限放大而没有质量损失外的一大优势是一旦掌握其原理，无需打开绘图工具即可手撸图形。</p>
<p>本文会实现几个实用(和不实用)的SVG动画，来熟悉一下SVG的基础和感受一下SVG的魅力((๑＞ڡ＜)☆)。</p>
<h1 data-id="heading-1">SVG基础</h1>
<p>SVG的写法上与HTML一致，都是以闭合的标签来定义：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"svg-board"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"width: 300px;height: 300px;"</span>></span><span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>xmlns用来标识应用的命名空间，不写的话某些浏览器可能会解析不正常。</p>
<p>与普通HTML标签一样，可以为它定义class，id等属性，可以通过Js来索引到，也可以为其添加CSS。</p>
<h2 data-id="heading-2">SVG坐标系</h2>
<p>与数学中的坐标系不同，计算机中的图形坐标系一般都是以左上角为0,0点，向下移动时增加y，向右移动时增加x，可以设置多种单位，不写的话是px。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/950c1b618da2405299ede24929d28c0c~tplv-k3u1fbpfcp-watermark.image" alt="5-2.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">基本形状和属性</h2>
<h3 data-id="heading-4">基本形状</h3>
<p>SVG中基本的形状有以下几种：</p>
<pre><code class="copyable"><rect>、<circle>、<ellipse>、<line>、<polyline>、<polygon>、<path>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分别用来定义矩形，圆形，椭圆，线段，多段连续线段，多边形，以及多种图形的组合。</p>
<p><code><rect></code>:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f84df08051a484b8845dbdd699eb10e~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104643.jpg" loading="lazy" referrerpolicy="no-referrer">
<code><circle></code>:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e792027a827470eb037cd0c451bcb4d~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104726.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><ellipse></code>:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e28f7d401d944b8b9bc2b6ad93b1644~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104759.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><line></code>:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd5f335730134964938d25d0fef227a7~tplv-k3u1fbpfcp-watermark.image" alt="11-1.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><polyline></code>:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9994b9ea8ccf4c42951a703489d1bcbe~tplv-k3u1fbpfcp-watermark.image" alt="12-1.svg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><polygon></code>:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f38164fc8844364ae25c8a804f7dbbd~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104838.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><path></code>:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/650e3d165256441790c28c7c1f9c6fdd~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104906.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code><path></code>是最强大的图形工具，可以画任意图形，同时也难以掌握，参数众多，手撸比较痛苦，复杂的图形基本靠UI小姐姐切成SVG然后我们在加特效上去。</p>
<h3 data-id="heading-5">基本属性</h3>
<p>他们通用的属性常用的有:</p>
<pre><code class="copyable">fill，stroke，stroke-dasharray，stroke-dashoffset
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分别代表填充色和轮廓色。</p>
<p>可以直接设置，也可以写成style用CSS来写，以最后的小月亮为例：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>
    <span class="hljs-attr">xmlns:xlink</span>=<span class="hljs-string">"http://www.w3.org/1999/xlink"</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40,20  A30,30 0 0,0 70,70"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"stroke: #cccc00; stroke-width:2; fill:none;"</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40,20  A30,30 0 1,0 70,70"</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">"stroke: #ff0000; stroke-width:2; fill:none;"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两段<code><path></code>都只画了stroke(轮廓)，没有进行填充，两条线弧线拼在一起形成了小月亮，下面给第一个设置为<code>pink</code>:</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>
    <span class="hljs-attr">xmlns:xlink</span>=<span class="hljs-string">"http://www.w3.org/1999/xlink"</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40,20  A30,30 0 0,0 70,70"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"stroke: #cccc00; stroke-width:2; fill:pink;"</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40,20  A30,30 0 1,0 70,70"</span>
        <span class="hljs-attr">style</span>=<span class="hljs-string">"stroke: #ff0000; stroke-width:2; fill:none;"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08ee413328ba4f73b26765b087eeef2b~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729104938.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>就变成了一个小西瓜。</p>
<p>这里要注意<code>fill</code>如果不想要一定要设为<code>none</code>，默认的话是黑色的。</p>
<p><code>stroke-dasharray</code>可以设置一组虚线值：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M40,20  A30,30 0 0,0 70,70"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"stroke: #cccc00; stroke-width:2; fill:pink; stroke-dasharray: 10 5 5 10"</span>/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据你设置的值按照宽度-间隔的模式循环，上面<code>10 5 5 10</code>会有一个10px长度的虚线，5px的间隔，之后会有一个5px的虚线，然后10px的间隔，之后按照此模式循环出现虚线。</p>
<p><code>stroke-dasharray</code>一般会与<code>stroke-dashoffset</code>一起出现，来做一些线段动画，<code>stroke-dashoffset</code>用来设置虚线的起始点。</p>
<p>下面一起来撸一个掘金的logo，并让他一点点绘制起来。</p>
<h1 data-id="heading-6">线段动画</h1>
<p>掘金的logo也是一个svg图形，点开可以看到它是一条<code><path></code>实现的，实际项目里可能会让UI小姐姐切图出来而不会亲自写<code><path></code>，下面我们用其他语义化更强的形状来实现一下。</p>
<p>掘金的logo分为三部分，最上面是个菱形，之后是两个折线，写的时候记得翻手册，我也是翻着手册写的(￣▽￣)／。</p>
<p>菱形我们可以用<code><polyline></code>或者<code><polygon></code>来填充色实现：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polygon</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"165,0 180,15 165,30 150,15"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polygon</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1883d9609a3b4bebb3210fc01787ce2b~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729110903.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里如果用填充色后面是没法用stroke-dasharray来让它动起来的，为了方便我们还是用了填充色。</p>
<p>折线我们需要用<code>polyline</code>设置一下stroke相关属性来实现：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polygon</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"165,0 180,15 165,30 150,15"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polygon</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polyline</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"141,24 165,40 189,24"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"fill:none;stroke-width: 7px;stroke:#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polyline</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polyline</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"130.5,35.5 165,55 199.5,35.5"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"fill:none;stroke-width: 7px;stroke:#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polyline</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里设置fill为none，只设置轮廓颜色来展示两条虚线：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f835c223f4f44589b7039855b132d239~tplv-k3u1fbpfcp-watermark.image" alt="Dingtalk_20210729110913.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还是稍微有点僵硬，这里不继续打磨了，有兴趣可以自行继续~。</p>
<p>上面说到stroke-dasharray可以这是虚线和虚线的间隔，我们可以将虚线设置的与原stroke长度一样间隔也是刚好可以，然后设置stroke-dashoffset将起始点设置也与长度的一样，这样开始时是一个隐藏的，然后慢慢将offset归零实现一个线段动画。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polygon</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"165,0 180,15 165,30 150,15"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polygon</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polyline</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"line"</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"141,24 165,40 189,24"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"fill:none;stroke-width: 7px;stroke:#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polyline</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">polyline</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"line2"</span> <span class="hljs-attr">points</span>=<span class="hljs-string">"130.5,35.5 165,55 199.5,35.5"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"fill:none;stroke-width: 7px;stroke:#1E80FF"</span>></span><span class="hljs-tag"></<span class="hljs-name">polyline</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.line</span> &#123;
            stroke-dasharray: <span class="hljs-number">59</span>;
            stroke-dashoffset: <span class="hljs-number">59</span>;

            <span class="hljs-attribute">animation</span>: show <span class="hljs-number">2s</span> linear infinite;
            <span class="hljs-attribute">animation-fill-mode</span>: forwards;
        &#125;

        <span class="hljs-selector-class">.line2</span> &#123;
            stroke-dasharray: <span class="hljs-number">79</span>;
            stroke-dashoffset: <span class="hljs-number">79</span>;

            <span class="hljs-attribute">animation</span>: show2 <span class="hljs-number">2s</span> linear infinite;
            <span class="hljs-attribute">animation-fill-mode</span>: forwards;
        &#125;

        <span class="hljs-keyword">@keyframes</span> show &#123;
            <span class="hljs-number">0%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">59</span>;
            &#125;

            <span class="hljs-number">100%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">0</span>;
            &#125;
        &#125;

        <span class="hljs-keyword">@keyframes</span> show2 &#123;
            <span class="hljs-number">0%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">79</span>;
            &#125;

            <span class="hljs-number">100%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">0</span>;
            &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4019817d5d544b2cbfffe9ba493732f5~tplv-k3u1fbpfcp-watermark.image" alt="logo-ani.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一切都是熟悉的CSS动画。</p>
<p>我们甚至可以给原logo做一些改进加上这个动画：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05b6b7bc3069421cb13821f7f24fae8a~tplv-k3u1fbpfcp-watermark.image" alt="raw-logo.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哈哈，有点酷酷的，截得gif帧数较低，没法直接贴带动画的SVG，可以复制自浏览器试试。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">path</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span> <span class="hljs-attr">fill-rule</span>=<span class="hljs-string">"evenodd"</span> <span class="hljs-attr">clip-rule</span>=<span class="hljs-string">"evenodd"</span> <span class="hljs-attr">d</span>=<span class="hljs-string">"M15.0737 5.80396H15.0757L18.706 2.91722L15.0757 0.00406298L15.0717 0L11.4475 2.91112L15.0717 5.80193L15.0737 5.80396ZM15.0757 14.9111L15.0778 14.9091L24.4429 7.52057L21.9036 5.48096L15.0778 10.8664L15.0757 10.8685L15.0737 10.8705L8.2479 5.48502L5.71057 7.52463L15.0737 14.9132L15.0757 14.9111ZM15.0716 19.9614L15.0757 19.9593L27.614 10.066L30.1534 12.1056L24.449 16.6053L15.0757 24L0.243779 12.3047L0 12.1117L2.53936 10.0721L15.0716 19.9614Z"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"logo"</span>/></span>

    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-class">.logo</span> &#123;
            fill: none;
            stroke: <span class="hljs-number">#1E80FF</span>;
            stroke-dasharray: <span class="hljs-number">106</span>;
            stroke-dashoffset: <span class="hljs-number">106</span>;
            <span class="hljs-attribute">animation</span>: logo <span class="hljs-number">1.5s</span> linear infinite;
            <span class="hljs-attribute">animation-fill-mode</span>: forwards;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">3</span>);
        &#125;

        <span class="hljs-keyword">@keyframes</span> logo &#123;
            <span class="hljs-number">0%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">106</span>;
            &#125;

            <span class="hljs-number">100%</span> &#123;
                stroke-dashoffset: <span class="hljs-number">0</span>;
            &#125;

        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">微信炸屎</h1>
<p>前几天大火的微信炸屎我们来用SVG来实现一下，相比Canvas不用处理每一帧的状态也不用写复杂的数学函数。</p>
<h2 data-id="heading-8">拆解需求</h2>
<ol>
<li>
<p>我们需要三段不同的图片，炸弹，爆炸效果，粑粑。</p>
</li>
<li>
<p>第一段中我们需要将炸弹丢出去，需要让炸弹沿着抛物线轨迹运动，这个在SVG里可以很轻易的用<code><animateMotion></code>来实现，用CSS则比较困难。</p>
</li>
<li>
<p>第二段爆炸我们直接播放gif即可。</p>
</li>
<li>
<p>第四段粑粑出现与下落是一个Scale增大，transform移动与opacity逐渐透明的过程，其实用CSS也可以轻易实现，不过我们为了SVG的连贯与学习的目的，也用SVG来实现。</p>
</li>
</ol>
<h2 data-id="heading-9">具体实现</h2>
<h3 data-id="heading-10">炸弹</h3>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500px"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"600px"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300px"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"boom"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"30"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"30"</span>
                <span class="hljs-attr">href</span>=<span class="hljs-string">"./zha.svg"</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">animateMotion</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"M 255 79 C 256 79 133 -60 47 33"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span> /></span>
                    <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"op"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0.8s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"0.2s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"freeze"</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">animate</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span>
                    <span class="hljs-attr">type</span>=<span class="hljs-string">"rotate"</span>
                    <span class="hljs-attr">from</span>=<span class="hljs-string">"0 15 15"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"360 15 15"</span>
                    <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1s"</span>
                    <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span>
                    /></span>
                <span class="hljs-tag"></<span class="hljs-name">image</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">g</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#boom"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>defs/g/svg/symbol</code>都可以聚合一组SVG内元素，我们每个都试一下，各个都有点细微的区别，defs只用来定义而不显示出里面的SVG，g只聚合不影响内部显示(除非设置了其他属性)，g相比svg来说可以设置<code>transform</code>，symbol相比g来说多了<code>viewbox</code>和<code>preserveAspectRation</code>属性可以设置。</p>
<p>之后可以用<code>use</code>来索引到上面元素所定义的svg图形。</p>
<p><code>image</code>和<code>img</code>标签类似，来显示图片，内部的我们一共写了三段混合的动画来控制整个过程：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">animateMotion</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"M 255 79 C 256 79 133 -60 47 33"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用来让图片以path定义的路径运动，这个path画出来的话就是一段抛物线，总动运动1秒。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"op"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0.8s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"0.2s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"freeze"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在炸弹快要落地的时候我们要将炸弹隐藏，<code>fill="freeze"</code>可以让这段动画的结果变为最终值，类似<code>animation-fill-mode: forwards</code>，我们让炸弹最终隐藏掉不再显示。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span>
    <span class="hljs-attr">type</span>=<span class="hljs-string">"rotate"</span>
    <span class="hljs-attr">from</span>=<span class="hljs-string">"0 15 15"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"360 15 15"</span>
    <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1s"</span>
    <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span>
/></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后这个混合的动画在抛物线运动一开始执行，让炸弹旋转一圈。</p>
<p>这里要注意一下SVG中旋转与CSS旋转的不同点，CSS中的旋转会以自身中心点开始旋转，SVG则是绕着给定的坐标点旋转，rotate(360, 15, 15)，因为上面我们定义了大小为30x30，自身中心点则是15x15，当然有其他x,y的话还要加上x,y，写的时候注意一下这边。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aa42de6b39a4a399051b322f5c33d48~tplv-k3u1fbpfcp-watermark.image" alt="baozha.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">爆炸</h3>
<p>爆炸我们直接贴个图即可：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">g</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bom"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"200"</span>
        <span class="hljs-attr">opacity</span>=<span class="hljs-string">"0"</span>
        <span class="hljs-attr">href</span>=<span class="hljs-string">"./baozha.gif"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bomStart"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"op.end"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"0.2s"</span> <span class="hljs-attr">repeateCount</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">animate</span>></span>    
        <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"bomEnd"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"bomStart.end"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"0.2s"</span> <span class="hljs-attr">repeateCount</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"freeze"</span>></span><span class="hljs-tag"></<span class="hljs-name">animate</span>></span>    
    <span class="hljs-tag"></<span class="hljs-name">image</span>></span>
<span class="hljs-tag"></<span class="hljs-name">g</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样的思路，根据不同的爆炸gif调整调整时间大小即可。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/835f09ac66a1493fa7aaa653106d1d66~tplv-k3u1fbpfcp-watermark.image" alt="baozha2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">粑粑</h3>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">symbol</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"shit"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">image</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"50%"</span> <span class="hljs-attr">opacity</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./shit.png"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"bomStart.end"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"2.4s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">animate</span>></span> 
        <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"scale"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"scale"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0.5"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"bomStart.end"</span> 
        <span class="hljs-attr">dur</span>=<span class="hljs-string">"0.1s"</span>></span><span class="hljs-tag"></<span class="hljs-name">animateTransform</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">animateTransform</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"transform"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"translate"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0 0"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0, 40"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"scale.end + 0.8s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1.5s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">animateTransform</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"opacity"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"scale.end + 0.8s"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"1.5s"</span> <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"1"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"freeze"</span>></span><span class="hljs-tag"></<span class="hljs-name">animate</span>></span> 
    <span class="hljs-tag"></<span class="hljs-name">image</span>></span>
<span class="hljs-tag"></<span class="hljs-name">symbol</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>粑粑我们初始显示为透明，我们不需要它一开始就显示，需要在爆炸后出现。</p>
<p>第二段动画变化<code>scale</code>，让粑粑从小到大突然出现。</p>
<p>第三段动画则是在粑粑出现后的开始擦屏幕版的向下移动。</p>
<p>最后一段则是一个重新隐藏的过程。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"position:absolute"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500px"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"400px"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"250"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"30"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#shit"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"150"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">transform</span>=<span class="hljs-string">"rotate(-17, 250, 30)"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"30"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#shit"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"120"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"240"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"50"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#shit"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"180"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"250"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#shit"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"180"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"360"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"200"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"160"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#shit"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"90"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"180"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个<code>use</code>就是一个粑粑。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/637be4d3ee1d47848c7c2402331a7862~tplv-k3u1fbpfcp-watermark.image" alt="baozha3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以继续打磨一下，多写几个不同的粑粑效果~。</p>
<h1 data-id="heading-13">红包雨</h1>
<p>每次618，双11活动总能看到淘宝天猫的各类型红包雨，随机出现的红包雨运动曲线让CSS有点难以招架，一般也都会选用Canvas来做，其实也可以用SVG来做。</p>
<p>经过上面的实现我们已经有了SVG动画的知识，我们来简单实现一个下红包雨的效果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdef8dd7e5b241d38d56e858a14bcd7d~tplv-k3u1fbpfcp-watermark.image" alt="rain.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">拆解需求</h2>
<ol>
<li>红包需要倾斜，需要用到transform rotate，也可以直接贴倾斜的红包图。</li>
<li>红包有大有小，可以用transform scale也可以指定width和height。</li>
<li>红包需要从上至下倾斜运动，需要用到animateMotion。</li>
<li>红包尽可能出现在随机位置，需要连续不断的下雨。</li>
</ol>
<h2 data-id="heading-15">具体实现</h2>
<h3 data-id="heading-16">创建单个红包</h3>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">image</span>
    <span class="hljs-attr">href</span>=<span class="hljs-string">"hongbao.png"</span>
    <span class="hljs-attr">width</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">height</span>=<span class="hljs-string">"100px"</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">"transform-box: fill-box; transform-origin: center; cursor: pointer"</span>
    <span class="hljs-attr">transform</span>=<span class="hljs-string">"rotate(25)"</span>
></span>
    <span class="hljs-comment"><!-- 这里也可以分开写animate x y --></span>
    <span class="hljs-tag"><<span class="hljs-name">animateMotion</span>
        <span class="hljs-attr">path</span>=<span class="hljs-string">"M 0 0 L 1000 100"</span>
        <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s"</span>
        <span class="hljs-attr">dur</span>=<span class="hljs-string">"10s"</span>
        <span class="hljs-attr">repeatCount</span>=<span class="hljs-string">"indefinite"</span>
    /></span>
<span class="hljs-tag"></<span class="hljs-name">image</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们用width和height来指定红包大小，继续用rotate来旋转红包，我们通过之前的知识知道SVG中的rotate需要指定具体的x,y值，否则不会按中心点旋转，这对于这种需要旋转但是每一帧的位置都不同的元素来说尤其困难，这里我们可以用<code>transform-box: fill-box; transform-origin: center;</code>来让SVG中的rotate行为与CSS中默认的行为一致。</p>
<p>倾斜运动这里省事直接写了path，一条斜线。</p>
<p>最后的随机出现我们可以给不同的红包设置不同的dur来造成一种伪随机的现象，当然也可以在它end的时候删掉它加一个新的。这样单个红包的运动就做好啦。</p>
<h3 data-id="heading-17">形成红包雨</h3>
<p>我们只需要将单个红包组合即可生成红包雨，用到Vue或者React等框架的话可以直接写属性，这里直接用原生的撸方便无依赖：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"svgboard"</span> <span class="hljs-attr">version</span>=<span class="hljs-string">"1.1"</span> <span class="hljs-attr">xmlns</span>=<span class="hljs-string">"http://www.w3.org/2000/svg"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
</body>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

    <span class="hljs-keyword">const</span> getX = <span class="hljs-function">(<span class="hljs-params">box=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(), config = &#123;&#125;</span>) =></span> &#123;
        <span class="hljs-comment">// box可传引用，也可以return。</span>
        <span class="hljs-keyword">let</span> maxX = <span class="hljs-built_in">document</span>.documentElement.clientWidth

        config = &#123;
            <span class="hljs-attr">num</span>: <span class="hljs-number">15</span>,
            <span class="hljs-attr">minWidth</span>: <span class="hljs-number">104</span>,
            <span class="hljs-attr">maxWidth</span>: <span class="hljs-number">146</span>,
            <span class="hljs-attr">minHeight</span>: <span class="hljs-number">145</span>,
            <span class="hljs-attr">maxHeight</span>: <span class="hljs-number">204</span>,
            <span class="hljs-attr">durBase</span>: <span class="hljs-number">10</span>,
            <span class="hljs-attr">imageLink</span>: <span class="hljs-string">'bg.png'</span>,
            ...config,
        &#125;;
        <span class="hljs-keyword">let</span> &#123; num, minWidth, maxWidth, minHeight, maxHeight, durBase, imageLink &#125; = config;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < num; i++) &#123;
            <span class="hljs-keyword">let</span> height = <span class="hljs-built_in">Math</span>.random() * (maxHeight - minHeight) + minHeight;

            box.push(&#123;
                <span class="hljs-attr">key</span>: +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() + <span class="hljs-built_in">Math</span>.random() + i,
                <span class="hljs-attr">width</span>: <span class="hljs-built_in">Math</span>.random() * (maxWidth - minWidth) + minWidth,
                <span class="hljs-attr">height</span>: height,
                <span class="hljs-attr">x</span>: <span class="hljs-built_in">Math</span>.random() * maxX + <span class="hljs-number">1</span>,
                <span class="hljs-attr">y</span>: <span class="hljs-string">`-<span class="hljs-subst">$&#123;height&#125;</span>`</span>,
                <span class="hljs-attr">dur</span>: <span class="hljs-built_in">Math</span>.random() * durBase + <span class="hljs-number">1</span>,
                <span class="hljs-attr">imageLink</span>: imageLink
            &#125;);
        &#125;

        <span class="hljs-keyword">return</span> box
    &#125;;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSVGElement</span>(<span class="hljs-params">elementName</span>) </span>&#123;
        <span class="hljs-keyword">let</span> node = <span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">'http://www.w3.org/2000/svg'</span>, elementName)

        <span class="hljs-keyword">return</span> node
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setAnimation</span>(<span class="hljs-params">board, lists</span>) </span>&#123;
        <span class="hljs-keyword">let</span> maxY = <span class="hljs-built_in">document</span>.documentElement.clientHeight
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> lists) &#123;
            <span class="hljs-keyword">let</span> image = createSVGElement(<span class="hljs-string">'image'</span>)
            image.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// alert会阻塞住整个渲染进程，但动画好像还在继续。</span>
                <span class="hljs-comment">// 这里最好用Promise直接写一个弹窗。</span>
                alert(<span class="hljs-string">'哦吼，红包1个亿'</span>)
            &#125;)
            image.setAttribute(<span class="hljs-string">'href'</span>, item.imageLink)
            image.setAttribute(<span class="hljs-string">'width'</span>, item.width)
            image.setAttribute(<span class="hljs-string">'height'</span>, item.height)
            image.setAttribute(<span class="hljs-string">'style'</span>, <span class="hljs-string">'transform-box: fill-box; transform-origin: center; cursor: pointer'</span>)
            image.setAttribute(<span class="hljs-string">'transform'</span>, <span class="hljs-string">'rotate(25)'</span>)
            <span class="hljs-keyword">let</span> motion = createSVGElement(<span class="hljs-string">'animateMotion'</span>)
            motion.setAttribute(<span class="hljs-string">'path'</span>, <span class="hljs-string">`M <span class="hljs-subst">$&#123;item.x&#125;</span> <span class="hljs-subst">$&#123;item.y&#125;</span> L <span class="hljs-subst">$&#123;item.x - <span class="hljs-number">500</span>&#125;</span> <span class="hljs-subst">$&#123;maxY + <span class="hljs-number">500</span>&#125;</span>`</span>)
            motion.setAttribute(<span class="hljs-string">'begin'</span>, <span class="hljs-string">'0s'</span>)
            motion.setAttribute(<span class="hljs-string">'dur'</span>, <span class="hljs-string">`<span class="hljs-subst">$&#123;item.dur&#125;</span>s`</span>)
            motion.setAttribute(<span class="hljs-string">'repeatCount'</span>, <span class="hljs-string">'indefinite'</span>)

            image.appendChild(motion)

            board.appendChild(image)
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">insertImage</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">let</span> board = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#svgboard'</span>)
        <span class="hljs-keyword">let</span> bgArguments = getX()
        <span class="hljs-keyword">let</span> starArguments = getX(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(), &#123;<span class="hljs-attr">minWidth</span>: <span class="hljs-number">21</span>, <span class="hljs-attr">maxWidth</span>: <span class="hljs-number">21</span>, <span class="hljs-attr">minHeight</span>: <span class="hljs-number">21</span>, <span class="hljs-attr">maxHeight</span>: <span class="hljs-number">21</span>, <span class="hljs-attr">imageLink</span>: <span class="hljs-string">'star.png'</span>&#125;)
        <span class="hljs-keyword">let</span> lineArguments = getX(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(), &#123; <span class="hljs-attr">num</span>: <span class="hljs-number">13</span>, <span class="hljs-attr">minWidth</span>: <span class="hljs-number">16</span>, <span class="hljs-attr">maxWidth</span>: <span class="hljs-number">16</span>, <span class="hljs-attr">minHeight</span>: <span class="hljs-number">114</span>, <span class="hljs-attr">maxHeight</span>: <span class="hljs-number">114</span>, <span class="hljs-attr">imageLink</span>: <span class="hljs-string">'line.png'</span>&#125;)
        setAnimation(board, bgArguments)
        setAnimation(board, starArguments)
        setAnimation(board, lineArguments)
    &#125;

    insertImage()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4f320bc42384087a8f17f40bc8e3c9c~tplv-k3u1fbpfcp-watermark.image" alt="rain.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>里面的图片可以找其他的替换一下，比起Canvas，这个都是熟悉的配方，熟悉的味道~，用框架的话整体可能不超过20行就可以实现~。</p>
<h1 data-id="heading-18">最后</h1>
<p>上面所有完整的代码可以在我的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FHuberTRoy%2Fmyown%2Ftree%2Fmaster%2F%25E5%25B0%258F%25E5%25B7%25A5%25E5%2585%25B7%2F%25E4%25B8%2580%25E4%25BA%259B%25E6%259C%2589%25E8%25B6%25A3%25E7%259A%2584%25E7%2589%25B9%25E6%2595%2588" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/HuberTRoy/myown/tree/master/%E5%B0%8F%E5%B7%A5%E5%85%B7/%E4%B8%80%E4%BA%9B%E6%9C%89%E8%B6%A3%E7%9A%84%E7%89%B9%E6%95%88" ref="nofollow noopener noreferrer">Github</a>中找到，嘘~，里面还有一个给任意元素添加水波纹效果的SVG。</p>
<p>路过的大哥哥，小姐姐这次一定好不好，想要10个赞抵御台风。😉</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2afbdff2a4fb4ebeb11b6be66843ff54~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            