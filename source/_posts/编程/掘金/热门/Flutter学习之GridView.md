
---
title: 'Flutter学习之GridView'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfb6a4ddc70f4e48a2ab9a7df7a3c4cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Sun, 21 Aug 2022 05:54:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfb6a4ddc70f4e48a2ab9a7df7a3c4cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第22天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>本文主要介绍下Flutter中GridView的介绍和使用</p>
</blockquote>
<p><strong>GridView</strong> 是一个可滚动的组件。类似我们iOS中的<code>collectionView</code>，我看下简单的使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:flutter/material.dart'</span>;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">GridViewPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">StatelessWidget</span> &#123;
  <span class="hljs-keyword">const</span> <span class="hljs-title class_">GridViewPage</span>(&#123;<span class="hljs-title class_">Key</span>? key&#125;) : <span class="hljs-variable language_">super</span>(<span class="hljs-attr">key</span>: key);

  @override
  <span class="hljs-title class_">Widget</span> <span class="hljs-title function_">build</span>(<span class="hljs-params">BuildContext context</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Scaffold</span>(
      <span class="hljs-attr">appBar</span>: <span class="hljs-title class_">AppBar</span>(<span class="hljs-attr">title</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'GridView'</span>),),
      <span class="hljs-attr">body</span>: <span class="hljs-title class_">GridView</span>(
        <span class="hljs-attr">gridDelegate</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">SliverGridDelegateWithFixedCrossAxisCount</span>(
          <span class="hljs-attr">crossAxisCount</span>: <span class="hljs-number">3</span>,
        ),
        <span class="hljs-attr">children</span>: [
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">0</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">1</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">2</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">3</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">4</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">5</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">6</span>]),
          <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-title class_">Colors</span>.<span class="hljs-property">primaries</span>[<span class="hljs-number">7</span>]),

        ],
      )

    ,
    );
  &#125;
  <span class="hljs-title function_">_createGridViewItem</span>(<span class="hljs-params">Color color</span>)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">height</span>: <span class="hljs-number">80</span>,
      <span class="hljs-attr">color</span>: color,
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfb6a4ddc70f4e48a2ab9a7df7a3c4cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>或者我们使用GridView.count来指定</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title class_">GridView</span>.<span class="hljs-title function_">count</span>(
  <span class="hljs-attr">primary</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">20</span>),
  <span class="hljs-attr">crossAxisSpacing</span>: <span class="hljs-number">10</span>,
  <span class="hljs-attr">mainAxisSpacing</span>: <span class="hljs-number">10</span>,
  <span class="hljs-attr">crossAxisCount</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">children</span>: <<span class="hljs-title class_">Widget</span>>[
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">100</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">"He'd have you all unravel at the"</span>),
    ),
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">200</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'Heed not the rabble'</span>),
    ),
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">300</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'Sound of screams but the'</span>),
    ),
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">400</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'Who scream'</span>),
    ),
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">500</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'Revolution is coming...'</span>),
    ),
    <span class="hljs-title class_">Container</span>(
      <span class="hljs-attr">padding</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">EdgeInsets</span>.<span class="hljs-title function_">all</span>(<span class="hljs-number">8</span>),
      <span class="hljs-attr">color</span>: <span class="hljs-title class_">Colors</span>.<span class="hljs-property">teal</span>[<span class="hljs-number">600</span>],
      <span class="hljs-attr">child</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">Text</span>(<span class="hljs-string">'Revolution, they...'</span>),
    ),
  ],
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c14925ceaca4afb8fb5bce07a3dd6e4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>gridDelegate</code>参数控制子控件的排列，有2个选择：</p>
<ul>
<li>
<p>SliverGridDelegateWithFixedCrossAxisCount：创建网格布局，创建网格布局与固定数量的item在交叉轴。</p>
</li>
<li>
<p>SliverGridDelegateWithMaxCrossAxisExtent：此委托将为作为的item选择一个交叉轴范围  在以下条件下尽可能大:1.范围均匀地划分网格的横轴范围。2. extent最多为<code>maxCrossAxisExtent</code>。</p>
</li>
</ul>
<p>SliverGridDelegateWithFixedCrossAxisCount有属性介绍如下：</p>
<ul>
<li><code>crossAxisCount</code>：交叉轴方向上个数。</li>
<li><code>mainAxisSpacing</code>：主轴方向上2行之间的间隔。</li>
<li><code>crossAxisSpacing</code>：交叉轴方向上之间的间隔。</li>
<li><code>childAspectRatio</code>：子控件宽高比。</li>
</ul>
<p><code>scrollDirection</code> 表示滚动方向，默认是垂直方向，可以设置为水平方向。</p>
<p><code>reverse</code>表示是否反转滚动方向，比如当前滚动方向是垂直方向，<code>reverse</code>设置为true，滚动方向为从上倒下，设置为false，滚动方向为从下倒上。</p>
<h2 data-id="heading-0">2. 快速构建</h2>
<p>对于类似的item我们使用快速构造方法，<code>itemBuilder</code>是构建子控件，<code>itemCount</code>指定数据个数。</p>
<ul>
<li>GridView.builder</li>
</ul>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-keyword">return</span> GridView.<span class="hljs-title function_ invoke__">builder</span>(
  <span class="hljs-attr">itemCount</span>: <span class="hljs-number">250</span>,
  <span class="hljs-attr">gridDelegate</span>:
  <span class="hljs-keyword">const</span> <span class="hljs-title function_ invoke__">SliverGridDelegateWithFixedCrossAxisCount</span>(<span class="hljs-attr">crossAxisCount</span>: <span class="hljs-number">3</span>,),
  <span class="hljs-attr">itemBuilder</span>: (BuildContext context, <span class="hljs-keyword">int</span> index) => <span class="hljs-title function_ invoke__">buildNetImage</span>(
      <span class="hljs-string">'https://loremflickr.com/100/100/music?lock=$index'</span>,
      <span class="hljs-attr">placeholder</span>: _loader,
      <span class="hljs-attr">errorWidget</span>: _error
      // <span class="hljs-attr">height</span>: <span class="hljs-number">60</span>,
      // <span class="hljs-attr">width</span>: <span class="hljs-number">60</span>
  ),

);

<span class="hljs-comment">/// 加载网络图片</span>
<span class="hljs-title function_ invoke__">buildNetImage</span>(String url,
&#123;BoxFit fit = BoxFit.scaleDown, <span class="hljs-keyword">double</span>? width, <span class="hljs-keyword">double</span>? height, Alignment alignment = Alignment.center, PlaceholderWidgetBuilder? placeholder, LoadingErrorWidgetBuilder? errorWidget&#125;) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-title function_ invoke__">CachedNetworkImage</span>(
    <span class="hljs-attr">imageUrl</span>: url,
    <span class="hljs-attr">placeholder</span>: placeholder ?? _loader,
    <span class="hljs-attr">errorWidget</span>: errorWidget ?? _error,
    <span class="hljs-attr">width</span>: width ,
    <span class="hljs-attr">height</span>: height,
    <span class="hljs-attr">fit</span>: fit,
  );
&#125;


<span class="hljs-comment">/// 加载等待视图</span>
Widget <span class="hljs-title function_ invoke__">_loader</span>(BuildContext context, String url) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">Center</span>(
    child: <span class="hljs-title function_ invoke__">CircularProgressIndicator</span>(),
  );
&#125;
<span class="hljs-comment">/// 加载错误视图</span>
Widget <span class="hljs-title function_ invoke__">_error</span>(BuildContext context, String url, dynamic error) &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">Center</span>(child: <span class="hljs-title function_ invoke__">Icon</span>(Icons.error));
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0595f75502514995a79c6d8ce5f322cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>GridView.custom</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> <span class="hljs-title class_">GridView</span>.<span class="hljs-title function_">custom</span>(
   <span class="hljs-attr">gridDelegate</span>: <span class="hljs-keyword">const</span> <span class="hljs-title class_">SliverGridDelegateWithFixedCrossAxisCount</span>(
     <span class="hljs-attr">crossAxisCount</span>: <span class="hljs-number">3</span>,
   ),
   <span class="hljs-attr">childrenDelegate</span>: <span class="hljs-title class_">SliverChildBuilderDelegate</span>((context, index) &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-title function_">buildNetImage</span>(
         <span class="hljs-string">'https://loremflickr.com/100/100/music?lock=$index'</span>,
         <span class="hljs-attr">placeholder</span>: _loader,
         <span class="hljs-attr">errorWidget</span>: _error
       <span class="hljs-comment">// height: 60,</span>
       <span class="hljs-comment">// width: 60</span>
     );
   &#125;, <span class="hljs-attr">childCount</span>: <span class="hljs-number">10</span>),
 );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af7503c61c654d3abb88d13b72a3ab5a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>GridView.extent</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> <span class="hljs-title class_">GridView</span>.<span class="hljs-title function_">extent</span>(
   <span class="hljs-attr">maxCrossAxisExtent</span>: <span class="hljs-number">100</span>,
   <span class="hljs-attr">children</span>: <span class="hljs-title class_">List</span>.<span class="hljs-title function_">generate</span>(<span class="hljs-number">50</span>, (i) &#123;
     <span class="hljs-keyword">return</span> <span class="hljs-title function_">buildNetImage</span>(
                  <span class="hljs-string">'https://loremflickr.com/100/100/music?lock=$i'</span>,
                  <span class="hljs-attr">placeholder</span>: _loader,
                  <span class="hljs-attr">errorWidget</span>: _error
                <span class="hljs-comment">// height: 60,</span>
                <span class="hljs-comment">// width: 60</span>
              );
   &#125;),
 );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91243b75e1ef4c7696ccd98dd003ce69~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            