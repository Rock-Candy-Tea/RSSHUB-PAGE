
---
title: '深入了解__before 和 __after 伪元素'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0b3e1cbec56490da9c7a70ee4065bba~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 05:36:58 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0b3e1cbec56490da9c7a70ee4065bba~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAQlBMVEVHcEwlRnqtZBj76q4lRnolRnolRnolRnolRnokRnr/gGtrVUeLXDBKTl+hYSHasW7Ik0zs0JG4dCvUdEE0SW+rYxrLQJfjAAAACnRSTlMA////0H/xUaMi5MCoTwAACfVJREFUeNrtnQl3qygUgJ9GXAqosfL//+pgmgXwXmRNJGdu55xO+6rx8+6I8O9fehmGriN93zdN07bVXdpW/ih/SbpuGP6dXbpOXv7z2i3S9ISck2eQOnAhMHG64VQQbmrAaM4B05GmipaGdB+m6BNQPBXzMYtKR3EPbB/RS5eY4g+lIW9WBqnySCvVMrzRpqqs0g9nwVg5p1KYlHEchRT5bftp+y3n6xlQDjAkABtrKULU9f377ev+4/1/NiT+URRiZRhrcZP6WLa/Gq005BORaqXsdYEuHPIP798ZxSyt6d5sVfxJESRCsvB32lfXwhRjnUBGmKXNoJQe04VIASJqRC/9G7yDsyQMiloYz+0pHYghEoPISAGgpDSvHsCoMwmA0mfjSG5UOsqah2RodkljzMkhZZdamiEDB8+Nsbk9T04yGNljDXGOZZ6u0+Tj9DuvbyNJBuPO0ABtLNPlJtfZJ4CNNCWJoY8gddwxNpm9YrHh9DEkBoeMud4Kma8XRZaYpBJOYvg59U9wOsblMvmGrzQe30dyqFZ1dxPfO0FT5BOdw989THVs4q1TFk+iN4PMu7CaLpd4EJOExNaJLE4d0xQKYpJ0cY5Ozcwwu6WOu2cs9TUYxPB4b4fvLRzTUXbT1HH7y0BnB0j6CAehkPFfFzd1TMsi6sU1/P4VM9NiISHBlYnBMR+kad075sXlmMehj1twnfTUqJH4GJfqIKte7S72emPnHbdiYHIB0e6ATjKq1UoTaFh6wBL2csMIVo9fH/v6QRHAgoxrOHQQxG/36tC1ODmGOeBGBRmXalgcdhDQ1xF1vI6a3DF2d4r7G1enOUgNOshlFq7qUCxrca9ldiCam7ilxRbP6JbOYsYtfLFmkcXEgLG1DN/6eroxHjqh5bh+Uw27e1oWVK7pN+AqwzUcq/UYTPw8nWufLFBHN2zcxLRYlmGPs6rA2Wy0uJe/E7TknbHIa1WH1bLA8DAj3JpxET+FCNCWZ5uNT6jxTPZK/1mXoCBeKlGLRT2lP69XN3XdqqCojKX1ZVda6iD2McjeXSHa0I+AHd2InGAJgjRVM6gOBfygDrarRJnho6eQBbrns+HkcNUCWtYClJa66qFgPbqqZEBTCOAgRqxCOhQBWpZeIC6QBq91hEoI5unTjsMsK9DCFigY9WNn19hgVCrELalrTw6WnYMYzjHhQ2/7G2xTx1HvwpzSe4cVi5ORQQwMW9+72FU5L4gGsa6Yu1RcDeIhs64Qs8izt0vGH+n9/IKaIlYpM2UqkYOrwwq5CgBjWpyGtxaonxe4KaJ3hx+7O0HaqVkxLBPj8FmBVmjNevIUFhUuDmMq5NDV9RwyPe/95IvxAhG7ymqxHGE5sZJL2kPLUhUinkXfrnFwGFwXD99djNLSFh/meXEb2B6Oyiwm0I7BC+OlTlOVPk9K8CIYzu5YHwKDTI6XAo5lz3WEqEXwQRKhh5cyLa6D81P4PXBw984as9YaGXHwx4Ba8rmOldUat/BHt9cQ38AaljnBdCJqs60OcXVDJZP//ZwSWtV9FpHNtgg22KuYx/U2tB5Mcp1TYOiphNhiFjgWeJ3DL2OZpuuUisIoUyzZEJ76I+LmyqWdv8LwnEiwMYczihjxeqtBsuFJSTg2oD1ETQx4v6D1VleSZW1xCwvAfVGWpQ069kgrQksAUW2rReYzsboIjSABuDQX0QJwB9cnZVgWVgE31vrklAJnEmVObykgYCk/VGX5OlpuKb5eiovUAvJ2tMstw0kIkNdpiSA91K6XA6K8CVCyr4PePhTo65q3DyX7OpTbSVk1PB62mhJ9HSpSqtKaESxsFRm0tLBVcvTV+vbBrLRK4hC7aitN9B0ZpX6vNMgjGIt5ZdmMv32KrmprD1afsPd4FEhThK0+WfTl3kpd482AGvG3jQdZK1+t8ireDswhofigRb3fxfI/4jj+xkffUX/1ccxxhEP9qyyBEH9Cx9vhf8TB7eiSpBHjZVSa4whQMJC1TqIR6q8RERtjOr2ID0yx3oYi0oAIvZCPz4eG64p3ObuREeOHUIR3MBVJwq9yll5P7KHdiPBOiOoRa/AjXz21J3k04l+i8OjErj4kaXWQiIVO/EvA+KLRAEnUVomtjPd6SvR3RLoeMT54nKFH1EqtkkEGFaQuTlSQrsxhRiOIt51S/Ho8B11+FUlwRaHnU4utEI38/mgSjRJ8PhWEtN6Z6WcncQOU4efjKoh3zfi7/+DfhPrwOZ9a/iYBiVJJxPlei3CqIDTYEqAPFow5/c71fAdVIwmo4n+cTIGbr2n9NULAE5ifcNNS63hvEOFk0wxYnICBBZ0I9xERBVILF0uggNdxuOkR4S6ngvgPmArzHv4KpMKGQFjQ+Rw6q9dC6R6dgZaJF7RVWIH0BTY9h+fz0ohHOyLuy+He/hN4GUR3/RxcBx2f76izarI9CaXmzRmhNQuSfIgJkva5GzN6HJbhQxCNsDGDSh56plmef6sg2eaXPsYBt5W+H6VE6omG6hOS1w4hiTWiThbJ1YO+RSO1vrpMlomf6nhQGz0m7qT6W04XOUHyzhZ4rkG+0hxL66oDW9mnPWyL3TMmssxyQUwr01CHX7b2OvUIaqS48TnMtAoEQTQixJeAlDfSiGmk/l8jpwIpTyFqOfeNIHWBooC036ERtUQp2tm/CKT5jjySbxTlvUVj2yhjvyWDVL3yfKRojXwLSEWUp7q0PBAKPp7m5YGoT3WH7wAZ1BeOywNZv3Gak/LIqriwxbQ5jaTcsEW1eb+FvoWo+zr5V/IUOvNtsapU2zJXSyj0xVB13sPfq0kkZA7dubIIKXIlJ8Cy7u+BN22RVcr+peOuxHdcBbA04FAVmEoEtO5vX55K4KVZS1QJvBBzU1rgUl8JapBNYIowLoZtD9NWRTWKqqe36L48BSz8QPH9epqqIDehlh2UuqocEmrdV7AvhuRoM74m80yeDIEX3ppreNN235FxV58DNjhswn5K8zK21+5ctjut6NmUIoy9tVvitnHr2VDM3ahtW8KQ/Vbsp9GGiWHfk8skyTSFz9/HdxhHe4uR/RxX/mG1SGXwypcDJNmCMfucZ/C1CuCQUbiBUDYbe7tiRkZX8GIat50d+wqR1fdN7ygGzrHrcN4kGFHK02cil5M6INgQVsvnNz77T5PqUFYJJInYmIBplJfP5On4eiOwYfhuCD44oLyYVs43rI1rk3H7usttzq8Qo3j84vavN9mOkAeuq8dHEd9NtCVKX51Oen+MM6IEYvz5StOehKLpIjD+nKU5AQWJpLizdB+1sb5LQvFRxbSJVGHmSdK/0WWaPguEYmcSJ68aWkK6rAw6jwSSCmrTWVHT96R7HwHANEgqybVJL+E2vE2q7Uu91Gr73SbbNUvZDtiOlCeIv4r/AI+0XUwz1lvcAAAAAElFTkSuQmCC")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<p>本文从最简单的开始，解释如何理解和使用::before和::after。然后再在实际使用场景中去应用它。</p>
<h1 data-id="heading-0">::before和::after是什么?</h1>
<p>::before和::after可以添加到选择器以创建伪元素的关键字。伪元素被插入到与选择器匹配的元素内容之前或之后。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0b3e1cbec56490da9c7a70ee4065bba~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">content属性</h2>
<p>1）::before和::after下特有的content，用于在css渲染中向元素逻辑上的头部或尾部添加内容。</p>
<p>2）::before和::after必须配合content属性来使用，content用来定义插入的内容，content必须有值，至少是空</p>
<p>3）这些添加不会出现在DOM中，不会改变文档内容，不可复制，仅仅是在css渲染层加入。所以不要用:before或:after展示有实际意义的内容，尽量使用它们显示修饰性内容</p>
<p>content可取以下值：</p>
<h3 data-id="heading-2">string</h3>
<p>使用引号包一段字符串，将会向元素内容中添加字符串</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45dc71a669884d6ba306a4234d25c7ce~tplv-k3u1fbpfcp-watermark.image" alt="a.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> p::before&#123;
    content: "《";
    color: #000000;
&#125;
p::after&#123;
    content: "》";
    color:#000000;
&#125;

<p>JavaScript高级程序设计</p>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">attr()</h3>
<p>通过attr()调用当前元素的属性，比如将图片alt提示文字或者链接的href地址显示出来。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d000bcd7bf94e2987c841d04a15441d~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">a::after &#123;
    content: ' → ' attr(href); /* 在 href 前显示一个箭头 */
&#125;

 <a href="https://www.baidu.com/">百度地址</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae67aaa97e3843fbba5d2b1b0a2040b8~tplv-k3u1fbpfcp-watermark.image" alt="b.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> a::after&#123;
    content: "【" attr(href) "】";
&#125;

<a href="https://www.baidu.com/">百度地址</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">url()/uri()</h3>
<p>用于引用媒体文件。比如：“百度”前面给出一张图片，后面给出href属性。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad7da669d042414eb7a7cbff9dbf4a51~tplv-k3u1fbpfcp-watermark.image" alt="c.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">a::before&#123;
    content: url("img/baidu_jgylogo3.gif");
&#125;
a::after&#123;
    content:"("attr(href)")";
&#125;

<a href="https://www.baidu.com/">百度地址</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<p>1）URL不能使用引号。如果你将URL用引号括起来，那么它会变成一个字符串和插入文本“url(image.jpg)”作为其内容，插入的而不是图像本身。</p>
<p>2）content属性，直接使用图片，即使写width,height也无法改变图片大小;</p>
<p><em>解决方案：如果要解决这个问题，可以把content:''写成空，使用background:url()来添加图片</em></p>
<pre><code class="copyable">/*伪元素添加图片：*/
.wrap:after&#123;
    /*内容置为空*/
    content:"";
    /*设置背景图，并拉伸*/
    background:url("img/06.png") no-repeat center;
    /*必须设置此伪元素display*/
    display:inline-block;
    /*必须设置此伪元素大小（不会被图片撑开）*/
    background-size:100%;
    width:100px;
    height:100px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3）苹果端伪元素不生效,img、input和其他的单标签是没有:after和:before伪元素的（在部分浏览器中没有，如:苹果端会发现无效），因为单标签本身不能有子元素。</p>
<p><em>解决方案：给img包一个div可以解决</em></p>
<p>4）想要动态改变伪元素的图片，可以给当前元素添加伪元素图片的基础样式，再动态class来写伪元素的图片。</p>
<h1 data-id="heading-5">::before和::after的应用</h1>
<h2 data-id="heading-6">配合quotes 属性使用</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446acfd7589c4b8bb2280e6d2e59fb78~tplv-k3u1fbpfcp-watermark.image" alt="f.png" loading="lazy" referrerpolicy="no-referrer">
<strong>加括号</strong></p>
<pre><code class="copyable"> h1&#123;
    quotes:"(" ")";  /*利用元素的quotes属性指定文字符号*/
&#125;
h1::before&#123;
    content:open-quote;
&#125;
h1::after&#123;
    content:close-quote;
&#125;

<h1>给标题加括号</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>加引号</strong></p>
<pre><code class="copyable"> h2&#123;
    quotes:"\"" "\"";  /*添加双引号要转义*/
&#125;
h2::before&#123;
    content:open-quote;
&#125;
h2::after&#123;
    content:close-quote;
&#125;

<h2>给标题加引号</h2>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>不指定，默认</strong></p>
<pre><code class="copyable"> h3::before&#123;
    content:open-quote;
&#125;
h3::after&#123;
    content:close-quote;
&#125;

<h3>不设置quotes</h3>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">装饰标题</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d98f5423db24e23869f0fd0c79eb339~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">h1 &#123;
    display: grid;
    grid-template-columns: minmax(50px, 1fr) auto minmax(50px, 1fr);
    align-items: center;
    text-align: center;
    gap: 40px;
&#125;

h1::before, h1::after &#123;
    content: '';
    border-top: 6px double;
&#125;

<h1>标题</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>布局是通过将<code><h1></code>元素变成 3 列来实现的。左列和右列是双线，宽度均为minmax(50px, 1fr)，这意味着它们的匹配宽度始终不小于50px。标题文本整齐地居中居中。</p>
</blockquote>
<h2 data-id="heading-8">彩带标题</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a22daac25757455cbef29573b9e992c8~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"> h1 &#123;
    position: relative;
    margin: 0 auto 20px;
    padding: 10px 40px;
    text-align: center;
    background-color: #875e46;
&#125;

h1::before, h1::after &#123;
    content: '';
    width: 80px;
    height: 100%;
    background-color: #724b34;

    /* 定位彩带两端形状的位置，并且放在最底层 */
    position: absolute;
    z-index: -1;
    top: 20px;

    /* 彩带两端的形状 */
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%, 25% 50%);

    /* 绘制并定位彩带的阴影三角形 */
    background-image: linear-gradient(45deg, transparent 50%, #5d3922 50%);
    background-size: 20px 20px;
    background-repeat: no-repeat;
    background-position: bottom right;
&#125;

h1::before &#123;
    left: -60px;
&#125;

h1::after &#123;
    right: -60px;
    transform: scaleX(-1); /* 水平翻转 */
&#125;
---------------------------
 <h1>标题</h1>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">实现更逼真的阴影</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9cd1ded810f49108067b5ea8ea4ae4f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">.box&#123;margin:10px;width:300px;height:100px;border-radius:10px;background:#ccc&#125;
.shadow&#123;position:relative;max-width:270px;box-shadow:0 1px 4px rgba(0,0,0,.3),0 0 20px rgba(0,0,0,.1) inset&#125;
.shadow::after,.shadow::before&#123;position:absolute;z-index:-1;content:""&#125;
.shadow::after,.shadow::before&#123;position:absolute;bottom:15px;left:10px;z-index:-1;width:50%;height:20%;content:""&#125;
.shadow::after,.shadow::before&#123;position:absolute;bottom:15px;left:10px;z-index:-1;width:50%;height:20%;box-shadow:0 15px 10px rgba(0,0,0,.7);content:"";transform:rotate(-3deg)&#125;
.shadow::after&#123;right:10px;left:auto;transform:rotate(3deg)&#125;


<div class="box shadow"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">替换内容</h2>
<p>有些情况下content可以不使用::before或::after。如果content设置为单个图像，那么你可以直接在元素上使用它来替换该元素的 HTML 内容。</p>
<p>如页面上分别有以下三个内容：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebe83245d5484e9c9f9b0978c4cce0e0~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>加了replace类之后</p>
<pre><code class="copyable">.replace &#123;
    content: url(img/replace.png);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59700ca83c6c4ccaa621add4cd3ccae3~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>1)具有简单文本的元素。它会被取代。<br>2)一个包含<code><img></code>在其中的元素。它也会被取代。<br> 3)<code><img></code>直接一个元素。Firefox不会取代它，但其他浏览器会。</p>
</blockquote>
<h2 data-id="heading-11">清除浮动</h2>
<p>方式一：</p>
<pre><code class="copyable">.classic-clearfix::after &#123;
    content: '';
    display: block;
    clear: both;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方式二：</p>
<pre><code class="copyable">.modern-clearfix &#123;
    display: flow-root;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df227bab5a0d4ce39d2fad89f69aaafc~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">模拟float:center的效果</h2>
<p>float没有center这个取值，但是可以通过伪类来模拟实现。</p>
<p><em>原理：左右通过::before float各自留出一半图片的位置，再把图片绝对定位上去。</em></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01636cd773fd453f88e480105d8f2095~tplv-k3u1fbpfcp-watermark.image" alt="d.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">body &#123; font: 14px/1.8 Georgia, serif;&#125;
#page-wrap &#123; width: 60%; margin: 40px auto; position: relative; &#125;
#logo &#123; position: absolute; top: 0; left: 50%; margin-left: -125px; &#125;
#l, #r &#123; width: 49%; &#125;
#l &#123; float: left; &#125;
#r &#123; float: right; &#125;
#l:before, #r:before &#123; content: ""; width: 125px; height: 250px; &#125;
#l:before &#123; float: right; &#125;
#r:before &#123; float: left; &#125;

<div id="page-wrap">
    <img src="img/cat.jpg" id="logo">
    <div id="l">
        <p>
            Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus
        </p>
    </div>
    <div id="r">
        <p>
            Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus
        </p>
    </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1b03d37581405bb00494a89c1ffd45~tplv-k3u1fbpfcp-watermark.image" alt="e.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>引用参考:</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fcss_selectors.asp" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3school.com.cn/cssref/css_selectors.asp" ref="nofollow noopener noreferrer">W3C官方文档</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodersblock.com%2Fblog%2Fdiving-into-the-before-and-after-pseudo-elements%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://codersblock.com/blog/diving-into-the-before-and-after-pseudo-elements/" ref="nofollow noopener noreferrer">Diving into the ::before and ::after Pseudo-Elements</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcss-tricks.com%2Ffloat-center%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://css-tricks.com/float-center/" ref="nofollow noopener noreferrer">Faking ‘float: center’ with Pseudo Elements</a></p>
<hr>
<p>小可爱看完就点个赞再走吧！🤞🤞🤞</p></div>  
</div>
            