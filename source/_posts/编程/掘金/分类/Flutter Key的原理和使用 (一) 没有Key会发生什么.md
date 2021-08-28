
---
title: 'Flutter Key的原理和使用 (一) 没有Key会发生什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/babb9b909ae1424193e7e0802f36a784~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 04:27:35 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/babb9b909ae1424193e7e0802f36a784~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>在flutter中,几乎每个widget都有一个Key,但是我们使用的时候一般不会传Key , 那么这个Key,它到底是干什么用的呢? 几乎每个widget都有,但我们又很少用到它. 那到底什么时候才需要用呢?</p>
<p>接下来,我们看一下,在需要Key的时候不用key,会发生什么情况.</p>
<p>先举个常见的例子:</p>
<pre><code class="hljs language-dart copyable" lang="dart">Column(
  children: [
    Container(width: <span class="hljs-number">100</span>, height: <span class="hljs-number">100</span>,color: Colors.red),
    Container(width: <span class="hljs-number">100</span>, height: <span class="hljs-number">100</span>,color: Colors.blue),
  ]
),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有上面一段代码,那么会显示两个方块,如图:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/babb9b909ae1424193e7e0802f36a784~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果把两个<code>Container</code>调换位置,那么UI上,两个方块也会换位置.这个没什么说的,很容易理解.
那如果是两个稍微复杂的widget呢?</p>
<p>现在创建一个新的Wdiget:</p>
<pre><code class="hljs language-dart copyable" lang="dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Box</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatefulWidget</span> </span>&#123;
  <span class="hljs-keyword">final</span> Color color;

  <span class="hljs-keyword">const</span> Box(<span class="hljs-keyword">this</span>.color, &#123;Key? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  _BoxState createState() => _BoxState();
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_BoxState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">Box</span>> </span>&#123;
  <span class="hljs-built_in">int</span> count = <span class="hljs-number">0</span>;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> Container(
        width: <span class="hljs-number">100</span>,
        height: <span class="hljs-number">100</span>,
        color: widget.color,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(<span class="hljs-string">'<span class="hljs-subst">$count</span>'</span>, style: TextStyle(color: Colors.white)),
            IconButton(
              onPressed: () &#123;
                setState(() &#123;
                  count++;
                &#125;);
              &#125;,
              icon: Icon(Icons.add),
            )
          ],
        ));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个Widget内部包含一个<code>count</code>,由自己管理它的状态,并且有一个方法,可以改变这个值.
代码如下:</p>
<pre><code class="hljs language-dart copyable" lang="dart">Column(
  children: [
    Box(Colors.red),
    Box(Colors.blue),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在用这个Widget替代上面的<code>Container</code>, 然后分别改变它们的值:</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/765c468da2ea446e880b5c22c9ef3e98~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们把两个widget互换位置,看看之后的效果:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c065aa24f1194a1bba41b3888c8e7935~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到,它的颜色虽然换了,但是数字却没有互换,似乎不是我们期望的效果.</p>
<p>我们再尝试改变一下代码</p>
<pre><code class="hljs language-dart copyable" lang="dart">Column(
  children: [
    Box(Colors.red),
    Box(Colors.blue),
    Box(Colors.red),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35a51ca55ef141798668b7ce2fa0be32~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们把第一个box,也就是红色的widget去掉,hotreload一下, 会是什么样呢?</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a86b591dbdac4d79afa82fab5e064ec7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很神奇,红色的确实消失了,但是按理说应该第一个去掉, 而蓝色的2和红色的3留下,然而却留下了前两个,并且数值还是第一个和第二个.</p>
<p>看起来,Flutter已经分不清谁是谁了,可是在我们看来,这里并没有复杂的逻辑.</p>
<p>那我们如果换成3个红色的box呢?
把代码改成这样:</p>
<pre><code class="hljs language-dart copyable" lang="dart">Column(
  children: [
    Box(Colors.red),
    Box(Colors.red),
    Box(Colors.red),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们再删掉第一个,代码就变成了:</p>
<pre><code class="hljs language-dart copyable" lang="dart">Column(
  children: [
    Box(Colors.red),
    Box(Colors.red),
  ],
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果不是自己亲手删除的,根本不知道是哪个不见了.只知道是少了一个.</p>
<p>如果我们依然像之前一样,去调换顺序呢? UI没有改变, 可是调换之后代码并没有变化,这么看 似乎UI不变又不奇怪了. 代码都没有变化,你指望UI有什么变化呢?</p>
<p>好像找到了一点灵感, 是不是说明<code>Flutter</code>不能靠颜色来辨别是哪个<code>widget</code>,或者说颜色不能作为widget的唯一标识. 此时我们需要一个<code>uuid</code>来区分不同的<code>widget</code>, 而这 就是<code>key</code>的作用了.</p>
<p>我们如果给widget分别传入不同的key, 就相当于各自有了一个id, 如果这3个id不同,那么flutter也就不会混淆它们了.</p>
<p>Flutter有几种不同的key,我会在后面为大家介绍.
之前定义box组件的时候,已经定义了一个<code>key</code>的参数, 此时我们分别传入不同的key</p>
<pre><code class="hljs language-dart copyable" lang="dart">Box(Colors.red,key: ValueKey(<span class="hljs-number">1</span>)),
Box(Colors.red,key: ValueKey(<span class="hljs-number">2</span>)),
Box(Colors.red,key: ValueKey(<span class="hljs-number">3</span>)),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为有了key,flutter也就能区分它们了, 现在我们无论是调换还是删除其中的<code>widget</code>, flutter的变化就都会朝着我们预期的方向发展了.</p>
<p>在实际开发中,我们也会遇到不同widget混淆的问题,一般情况下, 加一个<code>ValueKey</code>就可以解决了.</p>
<p>至于有什么情况加<code>ValueKey</code>不能解决,我们后面也会介绍到.</p></div>  
</div>
            