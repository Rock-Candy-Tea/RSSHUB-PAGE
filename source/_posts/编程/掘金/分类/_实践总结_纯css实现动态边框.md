
---
title: '_实践总结_纯css实现动态边框'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bdf6a3d54f24e84b3cd7f7afdfa6f47~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:15:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bdf6a3d54f24e84b3cd7f7afdfa6f47~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<p>这几天工作中遇到一个交互需求，要求实现一个效果，当鼠标移入一个元素的时候，元素出现一个动态的边框，如图：</p>
<p><img alt="动态边框示例" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bdf6a3d54f24e84b3cd7f7afdfa6f47~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>动态边框</p>
<h2 data-id="heading-1">CSS3 Background</h2>
<p>CSS3对于<code>background</code>做了一些修改，最明显的一个就是采用设置多背景，不但添加了4个新属性，并且还对目前的属性进行了调整增强。</p>
<p><strong>1、 多个背景图片</strong></p>
<p>在CSS3里面，你可以在一个标签元素里应用多个背景图片。代码类似与CSS2.0版本的写法，但引用图片之间需用“，”逗号隔开。第一个图片是定位在元素最上面的背景，后面的背景图片依次在它下面显示，如下：</p>
<pre><code class="copyable">background-image: url(image1.jpg), url(image2.jpg), url(image3.jpg);
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2、新属性：Background Clip</strong></p>
<p>background-clip 顾名思义，背景剪切，用来设置元素的背景（背景图片或颜色）是否延伸到边框下面。</p>
<ul>
<li><code>background-clip: border-box;</code> 背景延伸至边框外沿（但是在边框下层）</li>
<li><code>background-clip: padding-box;</code> 背景延伸至内边距（padding）外沿。不会绘制到边框处</li>
<li><code>background-clip: content-box;</code> 背景被裁剪至内容区（content box）外沿</li>
<li><code>background-clip: text;</code> 背景被裁剪成文字的前景色（实验属性，需要加浏览器前缀）</li>
</ul>
<p><strong>3、新属性: Background Origin</strong></p>
<p>此属性需要与<code>background-position</code>配合使用。你可以用<code>background-position</code>计算定位是从border，padding或content boxes内容区域算起。（类似<code>background-clip</code>）</p>
<ul>
<li>
<p>注意：当使用 background-attachment 为fixed时，该属性将被忽略不起作用。</p>
</li>
<li>
<p><code>background-origin：border-box;</code> 从border边框位置算起</p>
</li>
<li>
<p><code>background-origin：padding-box;</code> 从padding位置算起</p>
</li>
<li>
<p><code>background-origin：content-box;</code> 从content-box内容区域位置算起；</p>
</li>
</ul>
<p><strong>4、新属性：Background Size</strong></p>
<p>Background Size属性用来设置背景图片的大小。有几个属性值：</p>
<ul>
<li><code>background-size: contain;</code> 缩小背景图片使其适应标签元素（主要是像素方面的比率）</li>
<li><code>background-size: cover;</code> 让背景图片放大延伸到整个标签元素大小（主要是像素方面的比率）</li>
<li><code>background-size: 100px 100px;</code> 标明背景图片缩放的尺寸大小</li>
<li><code>background-size: 50% 100%;</code> 百分比是根据内容标签元素大小，来缩放图片的尺寸大小</li>
</ul>
<p><strong>5、Background Repeat 调整</strong></p>
<p>CSS2里当设置背景的时候，它经常被标签元素截取而显示不全，CSS3介绍了2个新属性来修复此问题。</p>
<ul>
<li><code>background-repeat: space;</code> 图片以相同的间距平铺且填充整个标签元素</li>
<li><code>background-repeat: round;</code> 图片自动缩放直到适应且填充整个标签元素</li>
</ul>
<p><strong>6、Background Attachment 的调整</strong></p>
<p>Background Attachment有了一个新属性值:<code>local</code>，当标签元素滚动时它才有效(如设置<code>overflow: scroll;</code>)，当<code>background-attachment</code>设置为<code>scroll</code>时，背景图片是不随内容滚条滚动的。现在，有了<code>background-attachment: local</code>，就可以做到让背景随元素内容滚动而滚动了。</p>
<p><strong>7、新增 Background Blend Mode</strong> 背景的混合模式是当背景重叠时计算像素最终色值的方法，每种混合模式采用前景和背景颜色值（分别为顶部颜色和底部颜色），执行其计算并返回颜色值。最终的可见层是对混合层中的每个重叠像素执行混合模式计算的结果。 <code>background-blend-mode: normal | multiply | screen | overlay | darken | lighten | color-dodge | color-burn | hard-light | soft-light | difference | exclusion | hue | saturation | color | luminosity;</code></p>
<p>每种混合效果参见：<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/background-blend-mode" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></p>
<h2 data-id="heading-2">CSS3 多背景模拟元素边框</h2>
<p>我们这里主要使用了<code>background-img</code>、<code>background-size</code> 和 <code>background-position</code> 三个属性。</p>
<pre><code class="copyable">background-image: [background-image], [background-image], [background-image]; 
background-position: [background-position], [background-position], [background-position]; 
background-repeat: [background-repeat], [background-repeat], [background-repeat]; 
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简写形式如下：</p>
<pre><code class="copyable">background: [background-image] [background-position] [background-repeat], 
[background-image] [background-position] [background-repeat], 
[background-image] [background-position] [background-repeat]; 
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们用多背景来模拟一个元素的边框</p>
<pre><code class="copyable">/*CSS*/
.exammple &#123;
    background: linear-gradient(0, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-90deg, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-180deg, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-270deg, #108b96 2px, #108b96 2px) no-repeat;
    background-size: 100% 2px, 2px 100%, 100% 2px, 2px 100%;
    background-position: left top, right top, right bottom, left bottom;
&#125;
复制代码

<div class="exammple"></div>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们用四个渐变的背景来模拟四个边框（为什么我们要用渐变而不是直接的Color呢？这是由于CSS的多背景只能是<code>background-image</code>， <code>background-color</code>不支持多个值,所有即便是纯色的边框，我们也只能使用渐变）。</p>
<p><img alt="输入图片说明" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3784ae874f9c4049b690c757bfa84b15~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>初步效果</p>
<p>接下来我们让边框动起来</p>
<pre><code class="copyable">/*CSS*/
.exammple &#123;
    transition: ease-in .3s;
    background: linear-gradient(0, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-90deg, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-180deg, #108b96 2px, #108b96 2px) no-repeat, 
                linear-gradient(-270deg, #108b96 2px, #108b96 2px) no-repeat;
    background-size: 0 2px, 2px 0, 0 2px, 2px 0;
    background-position: left top, right top, right bottom, left bottom;
&#125;
.exammple:hover &#123;
    background-size: 100% 2px,  2px 100%, 100% 2px, 2px 100%;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们已经按要求实现了交互效果。</p>
<h2 data-id="heading-3">总结</h2>
<p>相比border属性，用background的模拟边框存在以下的优势和劣势</p>
<p>优势</p>
<p>劣势</p>
<p>可以控制宽高，渐变色，运动方向等，灵活多变，能实现很多border不能实现的效果，并且不用添加额外的元素</p>
<p>不能实现border圆角</p>
<p>需要注意的是<strong>background模拟的边框不等同于真正的边框，是不占用边框的宽高的，计算盒子模型时要留心</strong></p>
<h2 data-id="heading-4">最后</h2>
<p>由于CSS3对背景属性的进一步丰富，利用CSS3的多背景可以实现很多以前必须借助js或图片才能实现的效果，比如半透明背景、几何图案背景、条纹背景等，期待和大家一块儿去探索CSS的奥秘。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            