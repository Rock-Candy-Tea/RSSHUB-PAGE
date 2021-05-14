
---
title: '如何使用Javascript渲染一颗二叉树'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f4778e1b084b4dbf48f7e43a31af66~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 02:35:05 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f4778e1b084b4dbf48f7e43a31af66~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>​树形数据结构的图形表示更加直观, 因此想简单的实现一个渲染二叉树的<code>js</code>类库.</p>
<ul>
<li>为了进行测试, 编写了随机的二叉树生成方法</li>
<li>为了复现测试时的问题, 使用了二叉树序列化与反序列化的方法</li>
<li>为了使用不同的渲染方式, 解耦布局与渲染过程</li>
</ul>
<h3 data-id="heading-1">数据结构</h3>
<ul>
<li>
<p>数据结构定义</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TreeNode</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.val = value;
        <span class="hljs-built_in">this</span>.left = <span class="hljs-built_in">this</span>.right = <span class="hljs-literal">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在定义好树结构之后, 如果想要验证实现的正确性,就必须构造一棵树, 如果纯手工构造....</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(<span class="hljs-number">0</span>);
root.left = <span class="hljs-keyword">new</span> TreeNode(<span class="hljs-number">1</span>);
root.left.left = ...
root.left.left.left.left.......= ...
<span class="hljs-comment">// fffu...</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以需要实现数据生成的方法</p>
</li>
</ul>
<h3 data-id="heading-2">数据生成方法</h3>
<ul>
<li>随机生成一颗n个节点的二叉树</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">randomTree</span>(<span class="hljs-params">count</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">random</span>(<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(index++);
        <span class="hljs-keyword">let</span> leftNum = randomInt(n - <span class="hljs-number">1</span>);
        root.left = random(leftNum);
        root.right = random(n - leftNum - <span class="hljs-number">1</span>);
        <span class="hljs-keyword">return</span> root;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>生成一颗n层的满二叉树</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fullBinaryTree</span>(<span class="hljs-params">level</span>) </span>&#123;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fullTree</span>(<span class="hljs-params">n</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(n);
        <span class="hljs-keyword">if</span> (n === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(index++);
        root.left = fullTree((n - <span class="hljs-number">1</span>)/<span class="hljs-number">2</span>);
        root.right = fullTree((n - <span class="hljs-number">1</span>)/<span class="hljs-number">2</span>);
        <span class="hljs-keyword">return</span> root;
    &#125;
    <span class="hljs-keyword">return</span> fullTree(<span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, level) - <span class="hljs-number">1</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">二叉树序列化与反序列化</h3>
<p>​如果随机生成一颗树之后, 在测试的过程中发现绘制出现了问题, 如何对问题进行复现?</p>
<ul>
<li>
<p>可以把每次生成的数据在控制台打印, 但是如果直接打印, 输出的是object对象,无法直接使用</p>
<ul>
<li>偷懒的方式, 使用<code>JSON.stringify()</code>序列化, <code>JSON.parse()</code>反序列化;</li>
<li>优雅的方式, 利用树的前序遍历序列实现树的序列化与反序列化</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> serialize = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span>  &#123;
    <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span> <span class="hljs-string">'x'</span>;
    <span class="hljs-keyword">let</span> left = serialize(root.left);
    <span class="hljs-keyword">let</span> right = serialize(root.right);
    <span class="hljs-keyword">return</span> root.val + <span class="hljs-string">","</span> + left + <span class="hljs-string">","</span> + right;
&#125;

<span class="hljs-keyword">const</span> deserialize = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> list = data.split(<span class="hljs-string">','</span>);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildTree</span>(<span class="hljs-params">list</span>) </span>&#123;
        <span class="hljs-keyword">let</span> v = list.shift();
        <span class="hljs-keyword">if</span> (v === <span class="hljs-string">'x'</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        <span class="hljs-keyword">let</span> root = <span class="hljs-keyword">new</span> TreeNode(v);
        root.left = buildTree(list);
        root.right = buildTree(list);
        <span class="hljs-keyword">return</span> root;
    &#125;
    <span class="hljs-keyword">return</span> buildTree(list);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>​到这一步为止, 已经实现的基本的准备工作, 接下来就可以开始实现树的绘制了.</p>
<h3 data-id="heading-4">代码结构</h3>
<p>​首先需要计算树的实际宽度, 可以采取递归的方式计算</p>
<p>​递归首先需要终止条件, 那就是空节点的宽度为0.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 递归计算节点宽度</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computeWidth</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-comment">// 终止条件, 空节点宽度为0</span>
    <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
    <span class="hljs-comment">// 没有子节点, 宽度为预设的节点宽度</span>
    <span class="hljs-keyword">if</span> (!(root.left || root.right)) &#123;
        root.width = nodeW;
        <span class="hljs-keyword">return</span> root.width;
    &#125;
    <span class="hljs-comment">// 否则为左右节点加间距, 间距为一个节点宽度</span>
    root.width = computeWidth(root.left) + computeWidth(root.right) + nodeW;
    <span class="hljs-keyword">return</span> root.width;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​计算完节点的宽度之后, 就可以计算每个节点的位置信息了, 同样也是递归的计算, 为了避免子树节点发生交叉, 所以为每颗子树增加左右边界信息(因为节点保存的是绝对宽度, 所以需要边界信息).</p>
<p>​通过一张图可以看出递归的原理</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f4778e1b084b4dbf48f7e43a31af66~tplv-k3u1fbpfcp-watermark.image" alt="example.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>​将左子树画到左边的框中, 右子树画到右边的框中, 然后依次递归. 需要将当前节点放到左右子树的中间, 然后分别设置左右子树的边界,递归的进行渲染. 这样就不会产生左右子树交叉的问题. 同时也不需要按照满二叉树的空间进行渲染.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 递归计算节点的位置信息</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computePosition</span>(<span class="hljs-params">root, left, right, curY = nodeH</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">let</span> x;
    <span class="hljs-keyword">if</span> (root.left) &#123;
        x = left + root.left.width + nodeW;
    &#125; <span class="hljs-keyword">else</span> &#123;
        x = left + nodeW;
    &#125;
    root.position = [x, curY];
    computePosition(root.left, left, x, curY + nodeH);
    computePosition(root.right, x, right, curY + nodeH);

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>整体架构, 简单的分为布局层和渲染层, 通过分层的设计, 只要渲染器实现了对应的接口,就可以将二叉树渲染到不同的目标上</p>
</li>
<li>
<p>布局层(layout)</p>
<ul>
<li>计算节点的位置, 并且保存到节点中</li>
</ul>
</li>
<li>
<p>渲染层(render)</p>
<ul>
<li>实现渲染器接口, 需要用到的渲染方法有:
<ul>
<li><code>renderCircle(x, y, r)</code>: 以(x, y) 为中心, r为半径画圆</li>
<li><code>renderLine(x1, y1, x2, y2)</code>: 绘制从(x1, y1) 到(x2, y2)的直线</li>
<li><code>renderText(x, y, text)</code>: 在(x, y) 点绘制文本</li>
</ul>
</li>
<li>可以实现<code>svg-render</code>, <code>div-render</code>, <code>canvas-render</code></li>
</ul>
<p><code>canvasRender</code>实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CanvasRender</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">container</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.canvas = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>);
        <span class="hljs-built_in">this</span>.container = container;
        <span class="hljs-built_in">this</span>.ctx = <span class="hljs-built_in">this</span>.canvas.getContext(<span class="hljs-string">'2d'</span>);
    &#125;

    <span class="hljs-function"><span class="hljs-title">initSize</span>(<span class="hljs-params">w, h</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.canvas.width = w;
        <span class="hljs-built_in">this</span>.canvas.height = h;
        <span class="hljs-built_in">this</span>.container.appendChild(<span class="hljs-built_in">this</span>.canvas)
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderCircle</span>(<span class="hljs-params">x, y, r</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.ctx.beginPath();
        <span class="hljs-built_in">this</span>.ctx.arc(x, y, r, <span class="hljs-number">0</span>, <span class="hljs-built_in">Math</span>.PI*<span class="hljs-number">2</span>);
        <span class="hljs-built_in">this</span>.ctx.stroke();
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderLine</span>(<span class="hljs-params">x1, y1, x2, y2</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.ctx.moveTo(x1, y1);
        <span class="hljs-built_in">this</span>.ctx.lineTo(x2, y2);
        <span class="hljs-built_in">this</span>.ctx.stroke();
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderText</span>(<span class="hljs-params">x, y, text</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.ctx.font = <span class="hljs-string">"20px serif"</span>;
        <span class="hljs-built_in">this</span>.ctx.textAlign = <span class="hljs-string">"center"</span>;
        <span class="hljs-built_in">this</span>.ctx.textBaseline = <span class="hljs-string">"middle"</span>;
        <span class="hljs-built_in">this</span>.ctx.fillText(text, x, y);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>svgRender</code>实现, 文字不是居中的....,对于<code>svg</code>不熟悉</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SvgRender</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">container</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.svg =  <span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">"http://www.w3.org/2000/svg"</span>, <span class="hljs-string">"svg"</span>);
        <span class="hljs-built_in">this</span>.container = container;
    &#125;
    <span class="hljs-function"><span class="hljs-title">initSize</span>(<span class="hljs-params">w, h</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.svg.setAttribute(<span class="hljs-string">'width'</span>, w);
        <span class="hljs-built_in">this</span>.svg.setAttribute(<span class="hljs-string">'height'</span>, h);
        <span class="hljs-built_in">this</span>.container.appendChild(<span class="hljs-built_in">this</span>.svg);
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderCircle</span>(<span class="hljs-params">x, y, r</span>)</span> &#123;
        <span class="hljs-keyword">let</span> c = <span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">'http://www.w3.org/2000/svg'</span>,<span class="hljs-string">'circle'</span>);
        c.setAttribute(<span class="hljs-string">'cx'</span>, x);
        c.setAttribute(<span class="hljs-string">'cy'</span>, y);
        c.r.baseVal.value = r;
        c.setAttribute(<span class="hljs-string">'stroke'</span>, <span class="hljs-string">'black'</span>);
        c.setAttribute(<span class="hljs-string">'fill'</span>, <span class="hljs-string">'none'</span>);
        <span class="hljs-built_in">this</span>.svg.appendChild(c)
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderLine</span>(<span class="hljs-params">x1, y1, x2, y2</span>)</span> &#123;
        <span class="hljs-keyword">let</span> p = <span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">'http://www.w3.org/2000/svg'</span>,<span class="hljs-string">'path'</span>);
        p.setAttribute(<span class="hljs-string">'d'</span>, <span class="hljs-string">`M <span class="hljs-subst">$&#123;x1&#125;</span> <span class="hljs-subst">$&#123;y1&#125;</span> L <span class="hljs-subst">$&#123;x2&#125;</span> <span class="hljs-subst">$&#123;y2&#125;</span> Z`</span>);
        p.setAttribute(<span class="hljs-string">'stroke'</span>, <span class="hljs-string">'black'</span>);
        <span class="hljs-built_in">this</span>.svg.appendChild(p);
    &#125;

    <span class="hljs-function"><span class="hljs-title">renderText</span>(<span class="hljs-params">x, y, text</span>)</span> &#123;
        <span class="hljs-keyword">let</span> t = <span class="hljs-built_in">document</span>.createElementNS(<span class="hljs-string">'http://www.w3.org/2000/svg'</span>,<span class="hljs-string">'text'</span>);
        t.setAttribute(<span class="hljs-string">'x'</span>, x - <span class="hljs-number">5</span>);
        t.setAttribute(<span class="hljs-string">'y'</span>, y + <span class="hljs-number">5</span>);
        t.style.textAlign = <span class="hljs-string">'center'</span>;
        t.style.fontSize = <span class="hljs-number">20</span>;
        t.style.verticalAlign = <span class="hljs-string">'middle'</span>;
        t.innerHTML = text;
        <span class="hljs-built_in">this</span>.svg.appendChild(t);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>闲着没事也可以实现<code>divRender</code>...</p>
</li>
</ul>
<h3 data-id="heading-5">渲染方式</h3>
<p>​在计算出布局信息之后, 渲染就变得简单了, 任意使用一种树的遍历方式依次渲染即可.</p>
<ul>
<li>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TreeDrawer</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">render</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.render = render;
    &#125;
    <span class="hljs-function"><span class="hljs-title">layout</span>(<span class="hljs-params">root, nodeW, nodeH</span>)</span> &#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computeWidth</span>(<span class="hljs-params">root</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
            <span class="hljs-keyword">if</span> (!(root.left || root.right)) &#123;
                root.width = nodeW;
                <span class="hljs-keyword">return</span> root.width;
            &#125;
            root.width = computeWidth(root.left) + computeWidth(root.right) + nodeW;
            <span class="hljs-keyword">return</span> root.width;
        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">computePosition</span>(<span class="hljs-params">root, left, right, curY = nodeH</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span>;
            <span class="hljs-keyword">let</span> x;
            <span class="hljs-keyword">if</span> (root.left) &#123;
                x = left + root.left.width + nodeW;
            &#125; <span class="hljs-keyword">else</span> &#123;
                x = left + nodeW;
            &#125;
            root.position = [x, curY];
            computePosition(root.left, left, x, curY + nodeH);
            computePosition(root.right, x, right, curY + nodeH);

        &#125;

        computeWidth(root);
        computePosition(root, <span class="hljs-number">0</span>, root.width);
        <span class="hljs-keyword">return</span> root.width;
    &#125;

    <span class="hljs-function"><span class="hljs-title">draw</span>(<span class="hljs-params">root, nodeW=<span class="hljs-number">40</span>, nodeH=<span class="hljs-number">40</span></span>)</span> &#123;
        <span class="hljs-keyword">let</span> height = getHeight(root);
        <span class="hljs-keyword">let</span> width = <span class="hljs-built_in">this</span>.layout(root, nodeW, nodeH);
        height = height * nodeH + nodeH;
        <span class="hljs-built_in">this</span>.render.initSize(width + nodeW, height);

        <span class="hljs-comment">// (x, y) ===> (x1, y1)</span>
        <span class="hljs-comment">// 求出一个向量的单位向量, 方便连线时从圆的边缘开始</span>
        <span class="hljs-keyword">const</span> getVector = <span class="hljs-function">(<span class="hljs-params">x, y, x1, y1</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> dis = <span class="hljs-built_in">Math</span>.sqrt((x - x1) ** <span class="hljs-number">2</span> + (y - y1) ** <span class="hljs-number">2</span>);
            <span class="hljs-keyword">return</span> [
                (x1 - x)/dis,
                (y1 - y)/dis
            ]
        &#125;
        <span class="hljs-keyword">const</span> linkNode = <span class="hljs-function">(<span class="hljs-params">root, child</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> [px, py] = root.position;
            <span class="hljs-keyword">let</span> [cx, cy] = child.position;
            <span class="hljs-keyword">let</span> [dx, dy] = getVector(px, py, cx, cy);
            <span class="hljs-built_in">this</span>.render.renderLine(px + (nodeW/<span class="hljs-number">2</span>)*dx, py + (nodeW/<span class="hljs-number">2</span>)*dy,
                                   cx - (nodeW/<span class="hljs-number">2</span>)*dx, cy - (nodeW/<span class="hljs-number">2</span>)*dy)
        &#125;

        <span class="hljs-keyword">const</span> drawNode = <span class="hljs-function">(<span class="hljs-params">root</span>) =></span> &#123;
            <span class="hljs-keyword">let</span> [x, y] = root.position;
            <span class="hljs-built_in">this</span>.render.renderText(x, y, root.val);
            <span class="hljs-built_in">this</span>.render.renderCircle(x, y, nodeW/<span class="hljs-number">2</span>);
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">draw</span>(<span class="hljs-params">root</span>) </span>&#123;
            <span class="hljs-keyword">if</span> (!root) <span class="hljs-keyword">return</span>;
            drawNode(root);
            <span class="hljs-keyword">if</span> (root.left) linkNode(root, root.left);
            <span class="hljs-keyword">if</span> (root.right) linkNode(root, root.right);
            draw(root.left);
            draw(root.right);
        &#125;
        draw(root);
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            