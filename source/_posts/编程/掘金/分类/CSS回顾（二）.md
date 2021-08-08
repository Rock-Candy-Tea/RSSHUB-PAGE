
---
title: 'CSS回顾（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3163c067adb64716827e6433caf0ae41~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 07:23:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3163c067adb64716827e6433caf0ae41~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">CSS知识回顾（二）</h1>
<p>css动画，css3操作及进阶内容</p>
<h3 data-id="heading-1">css过渡实现动画</h3>
<p>过渡transition:属性（all） 花费时间  运动曲线  何时开始。</p>
<p>搭配:hover使用。谁要发生动画效果就给谁加。</p>
<p>转换transform:与过渡一起使用，达到动画效果。</p>
<ul>
<li>translate:移动效果。</li>
<li>rotate:旋转效果。</li>
<li>scale:缩放。</li>
</ul>
<h3 data-id="heading-2">css关键帧动画</h3>
<p>animation:相比于过渡，动画可以实现更多的动态效果</p>
<pre><code class="copyable">//定义动画
@keyframs 动画名&#123;
    0%&#123;//开始状态
        转换操作
    &#125;,
    ....//可以在中间添加任意多的关键帧没实现复杂的动画
    100%&#123;//结束状态
        转换操作
    &#125;
&#125;
//使用动画
.类&#123;
    animation:名字 持续时间 运动曲线 何时开始 步长  播放次数 是否逆向。。。。
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">css的3d动画</h3>
<p>3d动画通过‘近大远小’的视觉规律来实现3d效果
perspective写在父盒子中，才会有3d效果</p>
<ul>
<li>3d位移：translateZ向远离眼睛和靠近眼睛移动</li>
<li>3d旋转：rotateX，Y，Z()和rotate3D(x,y,z)</li>
<li>tranform-style:preserve-3d;是否开启立体空间。</li>
</ul>
<h3 data-id="heading-4">position定位</h3>
<h4 data-id="heading-5">固定定位fixed：</h4>
<p>元素的位置相对于浏览器窗口是固定位置，即使窗口是滚动的它也不会移动。Fixed定位使元素的位置与文档流无关，因此不占据空间。 Fixed定位的元素和其他元素重叠。</p>
<p>通常可以用来做一些<em>吸顶</em>，<em>广告窗口</em>的操作</p>
<h4 data-id="heading-6">相对定位relative：</h4>
<p>如果对一个元素进行相对定位，它将出现在它所在的位置上。然后，可以通过设置垂直或水平位置，让这个元素“相对于”它的起点进行移动。 在使用相对定位时，无论是否进行移动，元素仍然占据原来的空间。因此，移动元素会导致它覆盖其它框。</p>
<h4 data-id="heading-7">绝对定位absolute：</h4>
<p>绝对定位的元素的位置相对于最近的已定位父元素，如果元素没有已定位的父元素，那么它的位置相对于<code><body></code>。 absolute 定位使元素的位置与文档流无关，因此不占据空间。 absolute 定位的元素和其他元素重叠。</p>
<h4 data-id="heading-8">粘性定位sticky：</h4>
<p>元素先按照普通文档流定位，然后相对于该元素在流中的flow root（BFC）和 containing block（最近的块级祖先元素）定位。而后，元素定位表现为在跨越特定阈值前为相对定位，之后为固定定位。</p>
<h4 data-id="heading-9">固定定位Static：</h4>
<p>默认值。没有定位，元素出现在正常的流中（忽略top, bottom, left, right 或者 z-index 声明）。</p>
<h3 data-id="heading-10">浏览器的重绘和重排</h3>
<p>DOM的变化影响到了预算内宿的几何属性比如宽高，浏览器重新计算元素的几何属性，其他元素的几何属性也会受到影响，浏览器需要重新构造渲染书，这个过程称之为重排。</p>
<p>浏览器将受到影响的部分重新绘制在屏幕上 的过程称为重绘。</p>
<h4 data-id="heading-11">引起重排重绘的原因有：</h4>
<ul>
<li>添加或者删除可见的DOM元素。</li>
<li>元素尺寸位置的改变。</li>
<li>浏览器页面初始化。</li>
<li>浏览器窗口大小发生改变，重排一定导致重绘，重绘不一定导致重排。</li>
</ul>
<h4 data-id="heading-12">减少重绘重排的方法有：</h4>
<ul>
<li>不在布局信息改变时做DOM查询。</li>
<li>使用csstext,className一次性改变属性。</li>
<li>使用fragment文档片段。<code>createDocunmentFragment</code></li>
<li>对于多次重排的元素，比如说动画。使用绝对定位脱离文档流，使其不影响其他元素</li>
</ul>
<blockquote>
<p>当然，我们所用框架后的V-Dom会帮我们很好的减少重绘重排提升性能</p>
</blockquote>
<h3 data-id="heading-13">用户界面样式优化</h3>
<h4 data-id="heading-14">表单轮廓线</h4>
<p>通过outline:none;取消表单轮廓线。</p>
<h4 data-id="heading-15">文本域大小固定</h4>
<p>通过reszie:none;防止文本域大小拖拽改变</p>
<h4 data-id="heading-16">鼠标样式</h4>
<p>通过cursor的属性决定鼠标在元素上时显示的样式。</p>
<pre><code class="copyable">pointer 手     move移动标     text文本    not-allowed禁止 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">网页元素的显示与隐藏</h3>
<ol>
<li>我们可以使用display:none;来将元素隐藏，这样的方法会使元素在页面中消失，不再占有原来的位置。想要恢复元素，则修改display:block;就会显示消失的元素。这种操作可以用来制作弹出窗口。</li>
<li>我们也可以用visibility:hidden;来隐藏元素。与display：none不同的是，这种方式隐藏的元素不会空出原来位置，会继续占有位置。也不会触发绑定的事件。</li>
<li>还有opacity=0，该元素隐藏起来了，但不会改变页面布局，并且，如果该元素已经绑定一些事件，如click事件，那么点击该区域，也能触发点击事件。</li>
<li>对装不下的内容隐藏也是实际操作中经常遇到的场景，使用overflow:hidden;来隐藏超出区域外的内容。这样的方法通常搭配white-space:nowarp;和text-overflow:ellipsis;来达到溢出文字省略号的效果。</li>
</ol>
<p>text-overflow还有另外两个属性可以选择，scroll和auto，可以为溢出部分显示一个滚动条。</p>
<p>把高度或宽度调整为0有时也能隐藏隐藏掉元素，同时在flex布局中会有特殊的作用</p>
<h3 data-id="heading-18">溢出文字省略号效果：</h3>
<pre><code class="copyable">write-space:nowarp;
overflow:hidden;
text-overflow:ellipsis;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">css三角</h3>
<p>当我们把box的宽高置为0，再设置边框时就会形成四个三角形，为他们设置不同颜色可以看到四个三角形。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3163c067adb64716827e6433caf0ae41~tplv-k3u1fbpfcp-watermark.image" alt="css三角" loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置其中一个有颜色，另外三个透明就可以得到css三角
代码如下：</p>
<pre><code class="copyable">   div &#123;
            height: 0;
            width: 0;
            border: 100px solid transparent;
            border-left-color: pink;
            /* border-top: 10px solid blue;
            border-bottom: 10px solid red;
            border-right: 10px solid yellow; */
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">遮罩，滤镜，渐变</h3>
<ul>
<li>mask:遮罩</li>
<li>filter：滤镜，搭配blur模糊使用</li>
<li>linear-gradient：线性渐变</li>
<li>radial-gradient：径向渐变</li>
</ul>
<h3 data-id="heading-21">shdow</h3>
<p>阴影不仅可以提升立体感获得阴影效果，还可以实现光晕效果。</p>
<h3 data-id="heading-22">line-height的继承</h3>
<p>要注意的是，整数可以继承，但是百分数不行
如果是百分数，就会乘上高度再继承下去，如200%*15px=30px，然后继承这个30px</p>
<h3 data-id="heading-23">scoped</h3>
<p>在style标签内加属性‘scoped’可以建立一个css作用域，让该style下的css样式不影响其余文件，增强代码可维护性。</p>
<h3 data-id="heading-24">Scss，Less和PostCSS</h3>
<p>Scss和Less都是css预处理器，用更简洁高效的语法写css。需配合插件使用。</p>
<p>PostCSS是“后处理器”，打包编译css。</p></div>  
</div>
            