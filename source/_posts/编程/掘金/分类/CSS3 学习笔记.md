
---
title: 'CSS3 学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448131e4cf57406b8178e0b5e0417553~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 22:21:06 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448131e4cf57406b8178e0b5e0417553~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、CSS3新特性</h3>
<ul>
<li>选择器</li>
<li>盒模型</li>
<li>背景和边框：border-radius、box-shadow、border-image</li>
<li>文字特效：text-shadow、text-overflow、word-wrap、word-break</li>
<li>2D/3D转换：移动、缩放、转动、拉长或拉伸（transform）</li>
<li>动画：@keyframes</li>
<li>多列布局：olumn-count（分割列数）column-gap（列与列间隙）column-rule（列边框样式，同border）column-width（列宽度）</li>
<li>用户界面：resize:both（由用户去调整大小）box-sizing、outline-offset</li>
</ul>
<h3 data-id="heading-1">二、具体属性</h3>
<h4 data-id="heading-2">1、background</h4>
<ul>
<li>background-image：背景图片，不同的背景图像用逗号隔开，所有的图片中显示在最顶端的为第一张；</li>
<li>background-size：背景图像相对于父元素的宽度和高度的百分比的大小；</li>
<li>background-origin：背景图像的位置区域；（content-box | padding-box | border-box）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/448131e4cf57406b8178e0b5e0417553~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>background-clip：背景剪裁，从指定位置开始绘制，同background-origin</li>
</ul>
<h4 data-id="heading-3">2、边框</h4>
<p>box-shadow: h-shadow v-shadow blur spread color inset（同text-shadow的使用）</p>

































<table><thead><tr><th>值</th><th>说明</th></tr></thead><tbody><tr><td>h-shadow</td><td>必需，水平阴影的位置，允许负值</td></tr><tr><td>v-shadow</td><td>必需，垂直阴影的位置，允许负值</td></tr><tr><td>blur</td><td>可选，模糊距离</td></tr><tr><td>spread</td><td>可选，阴影的大小</td></tr><tr><td>color</td><td>可选，阴影的颜色。</td></tr><tr><td>inset</td><td>可选，从外层的阴影（开始时）改变阴影内侧阴影</td></tr></tbody></table>
<p>border-radius</p>
<ul>
<li>四个值: 第一个值为左上角，第二个值为右上角，第三个值为右下角，第四个值为左下角。</li>
<li>三个值: 第一个值为左上角, 第二个值为右上角和左下角，第三个值为右下角</li>
<li>两个值: 第一个值为左上角与右下角，第二个值为右上角与左下角</li>
<li>一个值： 四个圆角值相同</li>
</ul>
<h4 data-id="heading-4">3、文字特效</h4>
<ul>
<li>text-overflow：文本溢出属性，指定应向用户如何显示溢出内容（clip剪切 | ellipsis省略号）</li>
<li>word-wrap：自动换行（break-word）</li>
<li>word-break：单词拆分换行（keep-all整个单词换行 | break-all单词被拆分）</li>
</ul>
<h4 data-id="heading-5">4、渐变</h4>
<ul>
<li>线性渐变（linear-gradient）- 向下/向上/向左/向右/对角方向</li>
<li>径向渐变（radial-gradient）- 由它们的中心定义</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/*direction为方向，如to right */</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(direction, color-stop1, color-stop2, ...);
<span class="hljs-comment">/*angle为水平线和渐变线之间的角度，如90deg*/</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(angle, color-stop1, color-stop2);
<span class="hljs-comment">/*重复渐变repeating-linear-gradient*/</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">repeating-linear-gradient</span>(red, yellow <span class="hljs-number">10%</span>, green <span class="hljs-number">20%</span>);

<span class="hljs-comment">/*shape为形状，circle | ellipse（椭圆形，默认）*/</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">radial-gradient</span>(shape size at position, start-color, ..., last-color);
<span class="hljs-comment">/*重复渐变repeating-radial-gradient*/</span>
<span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">repeating-radial-gradient</span>(red, yellow <span class="hljs-number">10%</span>, green <span class="hljs-number">15%</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>颜色可以使用多个，支持透明度</strong></p>
<h4 data-id="heading-6">5、转换</h4>
<p>2D 转换</p>
<ul>
<li>translate()：根据左(X轴)和顶部(Y轴)位置给定的参数，从当前元素位置移动</li>
<li>rotate()：给定度数顺时针旋转，负值是允许的，这样是元素逆时针旋转</li>
<li>scale()：增加或减少的大小，取决于宽度（X轴）和高度（Y轴）的参数</li>
<li>skew()：分别表示X轴和Y轴倾斜的角度</li>
</ul>
<p>3D 转换</p>
<ul>
<li>translate3d(x,y,z)：3D 转化</li>
<li>scale3d(x,y,z)：3D 缩放转换</li>
<li>rotate3d(x,y,z,angle)：3D 旋转</li>
<li>perspective(n)：3D 转换元素的透视视图</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c6c19d88f64bae96b21ae3393aefba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">6、过渡</h4>
<p>元素从一种样式逐渐改变为另一种的效果</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: red;
    <span class="hljs-attribute">transition</span>: width <span class="hljs-number">2s</span>;
    -webkit-<span class="hljs-attribute">transition</span>: width <span class="hljs-number">2s</span>;
&#125;
<span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">300px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>要添加多个样式的变换效果，添加的属性由逗号分隔</strong></p>
<h4 data-id="heading-8">7、动画</h4>
<p>@keyframes 规则内指定一个 CSS 样式和动画将逐步从目前的样式更改为新的样式。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@keyframes</span> myfirst &#123;
    <span class="hljs-selector-tag">from</span> &#123;<span class="hljs-attribute">background</span>: red;&#125;
    <span class="hljs-selector-tag">to</span> &#123;<span class="hljs-attribute">background</span>: yellow;&#125;
&#125;
<span class="hljs-keyword">@-webkit-keyframes</span> myfirst&#123;
    <span class="hljs-selector-tag">from</span> &#123;<span class="hljs-attribute">background</span>: red;&#125;
    <span class="hljs-selector-tag">to</span> &#123;<span class="hljs-attribute">background</span>: yellow;&#125;
&#125;

<span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">animation</span>: myfirst <span class="hljs-number">5s</span>;
    -webkit-<span class="hljs-attribute">animation</span>: myfirst <span class="hljs-number">5s</span>;
&#125;

<span class="hljs-comment">/*可以改变任意多的样式任意多的次数,用百分比来规定变化发生的时间*/</span>
<span class="hljs-keyword">@keyframes</span> myfirst&#123;
    <span class="hljs-number">0%</span>   &#123;<span class="hljs-attribute">background</span>: red;&#125;
    <span class="hljs-number">25%</span>  &#123;<span class="hljs-attribute">background</span>: yellow;&#125;
    <span class="hljs-number">50%</span>  &#123;<span class="hljs-attribute">background</span>: blue;&#125;
    <span class="hljs-number">100%</span> &#123;<span class="hljs-attribute">background</span>: green;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">三、其他使用</h3>
<h4 data-id="heading-10">1、盒模型</h4>
<p>width(宽) + padding(内边距) + border(边框) = 元素实际宽度</p>
<p>height(高) + padding(内边距) + border(边框) = 元素实际高度</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a50f006498a34bb7a641051bdd43f317~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>box-sizing 属性可以设置 width 和 height 属性中是否包含了 padding(内边距) 和 border(边框)，默认为不包含。</p>
<ul>
<li>box-sizing: border-box; padding(内边距) 和 border(边框) 也包含在 width 和 height 中</li>
<li>box-sizing: content-box；padding(内边距) 和 border(边框) 不包含在 width 和 height 中</li>
</ul>
<h4 data-id="heading-11">2、弹性盒子</h4>
<p>一种当页面需要适应不同的屏幕大小以及设备类型时确保元素拥有恰当的行为的布局方式。引入弹性盒布局模型的目的是提供一种更加有效的方式来对一个容器中的子元素进行排列、对齐和分配空白空间。</p>
<p>弹性盒子由弹性容器(Flex container)和弹性子元素(Flex item)组成，设置 display=flex |  inline-flex将其定义为弹性容器。</p>
<p><a href="https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html" target="_blank" rel="nofollow noopener noreferrer">Flex 布局</a></p>
<h4 data-id="heading-12">3、多媒体查询</h4>
<p>根据设置自适应显示，媒体查询可用于检测很多事情，例如：</p>
<ul>
<li>viewport(视窗) 的宽度与高度</li>
<li>设备的宽度与高度</li>
<li>朝向 (智能手机横屏，竖屏) 。</li>
<li>分辨率</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">480px</span>) &#123;
    <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">background-color</span>: lightgreen;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            