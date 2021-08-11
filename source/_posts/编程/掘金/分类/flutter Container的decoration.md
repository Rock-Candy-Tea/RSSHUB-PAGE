
---
title: 'flutter Container的decoration'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85b166b5f36c4e33bed8842e5acb5425~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 02:17:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85b166b5f36c4e33bed8842e5acb5425~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">decoration： 背景装饰</h1>
<p>decoration可以设置边框、背景色、背景图片、圆角等属性，非常实用。对于transform这个属性，一般有过其他平台开发经验的，都大致了解，这种变换，一般不是变换的实际位置，而是变换的绘制效果，也就是说它的点击以及尺寸、间距等都是按照未变换前的。
但需要注意的是 deoration和 <code>color： 背景颜色 </code>不能共存，二者同时只能有一个</p>
<p>Decoration共有以下几种：</p>
<ul>
<li>BoxDecoration:实现边框、圆角、阴影、形状、渐变、背景图像</li>
<li>ShapeDecoration: 颜色，阴影，图片</li>
<li>FlutterLogoDecoration: Logo图片</li>
<li>UnderlineTabindicator:下划线</li>
</ul>
<h2 data-id="heading-1">BoxDecoration</h2>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">const</span> BoxDecoration(&#123;
<span class="hljs-keyword">this</span>.color,<span class="hljs-comment">//背景色</span>
<span class="hljs-keyword">this</span>.image,<span class="hljs-comment">//图片</span>
<span class="hljs-keyword">this</span>.border,<span class="hljs-comment">//边框</span>
<span class="hljs-keyword">this</span>.borderRadius,<span class="hljs-comment">//圆角的大小</span>
<span class="hljs-keyword">this</span>.boxShadow,<span class="hljs-comment">//阴影</span>
<span class="hljs-keyword">this</span>.gradient,<span class="hljs-comment">//渐变色</span>
<span class="hljs-keyword">this</span>.backgroundBlendMode,<span class="hljs-comment">//图像的混合模式</span>
<span class="hljs-keyword">this</span>.shape = BoxShape.rectangle,<span class="hljs-comment">//形状,BoxShape.circle和borderRadius不能同时使用</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">boxShadow 阴影</h3>
<ul>
<li>color - 阴影颜色</li>
<li>offset - 阴影相偏移量</li>
<li>blurRadius - 高斯模糊数值</li>
<li>gradient - 渐变，支持2种渐变：LinearGradient线性渐变 和 RadialGradient扫描渐变</li>
</ul>
<h3 data-id="heading-3">LinearGradient</h3>
<ul>
<li>begin - 渐变开始的位置</li>
<li>end - 渐变结束的位置</li>
<li>colors - 渐变颜色,数组</li>
<li>stops - 值列表，范围[0,1]</li>
<li>tileMode - 平铺模式</li>
<li>shape形状</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85b166b5f36c4e33bed8842e5acb5425~tplv-k3u1fbpfcp-watermark.image" alt="效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>example:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-keyword">new</span> Container(
  constraints: <span class="hljs-keyword">new</span> BoxConstraints.expand(
    height:Theme.of(context).textTheme.display1.fontSize * <span class="hljs-number">1.1</span> + <span class="hljs-number">200.0</span>,
  ),
  decoration: <span class="hljs-keyword">new</span> BoxDecoration(
    border: <span class="hljs-keyword">new</span> Border.all(width: <span class="hljs-number">2.0</span>, color: Colors.red),
    color: Colors.grey,
    borderRadius: <span class="hljs-keyword">new</span> BorderRadius.all(<span class="hljs-keyword">new</span> Radius.circular(<span class="hljs-number">20.0</span>)),
    image: <span class="hljs-keyword">new</span> DecorationImage(
      image: <span class="hljs-keyword">new</span> NetworkImage(<span class="hljs-string">'http://h.hiphotos.baidu.com/zhidao/wh%3D450%2C600/sign=0d023672312ac65c67506e77cec29e27/9f2f070828381f30dea167bbad014c086e06f06c.jpg'</span>),
      centerSlice: <span class="hljs-keyword">new</span> Rect.fromLTRB(<span class="hljs-number">270.0</span>, <span class="hljs-number">180.0</span>, <span class="hljs-number">1360.0</span>, <span class="hljs-number">730.0</span>),
    ),
  ),
  padding: <span class="hljs-keyword">const</span> EdgeInsets.all(<span class="hljs-number">8.0</span>),
  alignment: Alignment.center,
  child: <span class="hljs-keyword">new</span> Text(<span class="hljs-string">'Hello World'</span>,
    style: Theme.of(context).textTheme.display1.copyWith(color: Colors.black)),
  transform: <span class="hljs-keyword">new</span> Matrix4.rotationZ(<span class="hljs-number">0.3</span>),
)

 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>tips：
color：用来设置container背景色，如果foregroundDecoration设置的话，可能会遮盖color效果。
decoration：绘制在child后面的装饰，设置了decoration的话，就不能设置color属性，否则会报错，此时应该在decoration中进行颜色的设置。
foregroundDecoration：绘制在child前面的装饰。</p>
<blockquote>
<p>相关参考 ：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu011068702%2Farticle%2Fdetails%2F108475511" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u011068702/article/details/108475511" ref="nofollow noopener noreferrer">blog.csdn.net/u011068702/…</a></p>
</blockquote></div>  
</div>
            