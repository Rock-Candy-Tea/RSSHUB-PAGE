
---
title: 'js中的 _ 操作符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3252'
author: 掘金
comments: false
date: Fri, 09 Sep 2022 00:10:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=3252'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">三目运算符 ?</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> z = <span class="hljs-number">0</span>, x = <span class="hljs-number">10</span>, y = <span class="hljs-number">20</span>;
<span class="hljs-comment">// if 逻辑判断</span>
<span class="hljs-keyword">if</span> (x > y) &#123;
    z = <span class="hljs-number">30</span>
&#125; <span class="hljs-keyword">else</span> &#123;
    z = <span class="hljs-number">30</span>
&#125;

<span class="hljs-comment">// 三目运算简化 if</span>
z = x > y ? <span class="hljs-number">20</span> : <span class="hljs-number">30</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>非常简单也非常的常见，如果你还不知道，该赶紧补习一下啦；</p>
<h4 data-id="heading-1">可选链操作符 ?.</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'掘进好友'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">30</span> &#125;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'昵称'</span>, obj.<span class="hljs-property">nickName</span>.<span class="hljs-title function_">toString</span>())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们在执行上面的代码时，因为<code>obj</code>对象上并不存在<code>nickName</code>属性，所以当读取<code>obj.nickName</code>时，得到的将会是<code> undefined</code>，而<code>undefined</code>是没有<code>toString()</code>方法的，所以这个时候程序就会报错了。</p>
<p>以前我们的解决方案是加一层判断，确保访问的对象不为<code>undefined</code>或者<code> null</code>，我们才做后续操作，具体代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'掘进好友'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">30</span> &#125;
<span class="hljs-keyword">if</span>(obj.<span class="hljs-property">nickName</span>)&#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'昵称'</span>, obj.<span class="hljs-property">nickName</span>.<span class="hljs-title function_">toString</span>())
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写代码虽然解决了问题，但是写起来太繁琐，不够优雅，所以新版 JS 增加了可选链操作符来简化这一过程。上面的代码用可选链操作符简化如下</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'掘进好友'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">30</span> &#125;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'昵称'</span>, obj.<span class="hljs-property">nickName</span>?.<span class="hljs-title function_">toString</span>())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以<code>?.</code>可选链操作符的作用就是，如果<code>obj</code>对象的<code>nickName</code>属性值不为<code>null</code>或 <code>undefined </code>则调用其<code>toString()</code>方法，如果不存在则不调用，实际效果与<code>if</code>判断是等价的。</p>
<p>可选链操作符在深层嵌套时，优势就更明显了，简便的不是一点半点，举个例子，看如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> demo = &#123;
    <span class="hljs-attr">setp1</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'步骤一'</span>,
        <span class="hljs-attr">step2</span>: &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">'步骤二'</span>
        &#125;
    &#125;
&#125;

<span class="hljs-comment">// 如果我们想访问【步骤二】的 name 属性，即</span>
demo.<span class="hljs-property">step1</span>.<span class="hljs-property">step2</span>.<span class="hljs-property">name</span>

<span class="hljs-comment">// 我们为了确保安全性，过去我们可能要写如下代码</span>
<span class="hljs-keyword">if</span> (demo && demo.<span class="hljs-property">step1</span> && demo.<span class="hljs-property">step1</span>.<span class="hljs-property">step2</span> && demo.<span class="hljs-property">step1</span>.<span class="hljs-property">step2</span>.<span class="hljs-property">name</span>) &#123;
    demo.<span class="hljs-property">step1</span>.<span class="hljs-property">step2</span>.<span class="hljs-property">name</span>.<span class="hljs-title function_">toString</span>()
&#125;

<span class="hljs-comment">// 用可选链的话</span>
demo?.<span class="hljs-property">step1</span>?.<span class="hljs-property">step2</span>?.<span class="hljs-property">name</span>?.<span class="hljs-title function_">toString</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">空值合并操作符 ??</h4>
<p>这是一个逻辑操作符，与<code>||</code>操作符十分相似，但是它们并不是等价的，具体的区别如下:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-string">''</span>
<span class="hljs-keyword">let</span> c = <span class="hljs-literal">null</span>
<span class="hljs-keyword">let</span> d = <span class="hljs-literal">undefined</span>

<span class="hljs-keyword">let</span> x = a ?? <span class="hljs-number">100</span> <span class="hljs-comment">// x 等于 0</span>
<span class="hljs-keyword">let</span> y = b ?? <span class="hljs-number">100</span> <span class="hljs-comment">// y 等于 ''</span>
<span class="hljs-keyword">let</span> z = c ?? <span class="hljs-number">100</span> <span class="hljs-comment">// z 等于 100</span>
<span class="hljs-keyword">let</span> k = d ?? <span class="hljs-number">100</span> <span class="hljs-comment">// k 等于 100</span>

<span class="hljs-keyword">let</span> o = a || <span class="hljs-number">100</span>  <span class="hljs-comment">// o 等于 100</span>
<span class="hljs-keyword">let</span> p = b || <span class="hljs-number">100</span>  <span class="hljs-comment">// p 等于 100</span>
<span class="hljs-keyword">let</span> q = c || <span class="hljs-number">100</span>  <span class="hljs-comment">// q 等于 100</span>
<span class="hljs-keyword">let</span> r = d || <span class="hljs-number">100</span>  <span class="hljs-comment">// r 等于 100</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>?? </code>只有当操作符左侧表达式的值为<code>undefined</code>或者<code>null</code>时，才会返回右侧的值。</p>
<p><code>|| </code>只要操作符左侧表达式的值为<code> false</code> 时，那么就会返回右侧的值。左侧的表达式会自动做布尔运算，因为<code>0</code>和 空字符串<code>''</code>做布尔运算，其值为<code> false</code>，所以<code>o</code>和<code> p</code> 的值等于<code> 100</code>。</p>
<p>通过上面的比较可以发现，<code>?? </code>操作符的出现，是为了更准确的做空值判断，只有<code>null</code>和<code>undefined</code>才会被判定为空值，<code> 0</code> 和<code>''</code>不会被判定为空值。</p>
<h4 data-id="heading-3">空值赋值操作符 ??=</h4>
<p>只有当<code>??=</code>左侧的值为<code>null</code>或者 <code>undefined</code> 的时候，才会将右侧变量的值赋值给左侧变量，其他所有值都不会进行赋值，在某些场景下可以省略很多代码。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-literal">null</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-literal">undefined</span>
<span class="hljs-keyword">let</span> c = <span class="hljs-number">100</span>
<span class="hljs-keyword">let</span> d = <span class="hljs-number">200</span>

<span class="hljs-comment">// 因为 a 的值为 null，所以会将 c 的值赋值给 a , 所以最终 a = 100</span>
a ??= c

<span class="hljs-comment">// 因为 b 的值为 undefined，所以会将 d 的值赋值给 b , 所以最终 b = 200</span>
b ??= d
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            