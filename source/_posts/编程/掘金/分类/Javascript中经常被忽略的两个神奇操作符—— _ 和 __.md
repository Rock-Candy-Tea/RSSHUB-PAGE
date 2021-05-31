
---
title: 'Javascript中经常被忽略的两个神奇操作符—— _. 和 __'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2394'
author: 掘金
comments: false
date: Thu, 27 May 2021 08:24:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=2394'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>?.</code>和<code>??</code>估计是Javascript两个最为有用并且最经常被忽略的操作符了。这两个操作符最大的作用，就是对于<code>undefined</code>和<code>null</code>的应对，在没有lodash等库的情况下，直接桶过Javascript自身的机制就可以很大的程度上提高程序的健壮性。</p>
<p><code>?.</code>主要用于在多层的object/array进行取值和函数调用，而<code>??</code>则比较类似于<code>||</code>，但是专门作用于<code>undefined</code>和<code>null</code>。</p>
<p>下面我们会通过一些例子来说明<code>?.</code>和<code>??</code>，并且和lodash的一些用法做一些比较。首先准备一个测试数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> data = &#123;
  <span class="hljs-attr">layer1</span>: &#123;
    <span class="hljs-attr">layer2</span>: [
      &#123;
        <span class="hljs-attr">layer4</span>: <span class="hljs-string">"layer 4 value"</span>,
        <span class="hljs-attr">func</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>) </span>&#123;
          <span class="hljs-keyword">return</span> <span class="hljs-string">`in layer 4 func <span class="hljs-subst">$&#123;x&#125;</span>`</span>;
        &#125;
      &#125;,
      <span class="hljs-string">"layer 3 value"</span>
    ]
  &#125;,
  <span class="hljs-attr">x</span>: <span class="hljs-string">"layer 1 value"</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先比较一下<code>?.</code>和<code>lodash</code>：</p>








































<table><thead><tr><th><code>?.</code></th><th>lodash</th><th>结果</th></tr></thead><tbody><tr><td><code>data?.x</code></td><td><code>_.get(data, "x")</code></td><td><code>"layer 1 value"</code></td></tr><tr><td><code>data?.layer1?.layer2?.[1]</code></td><td><code>_.get(data, "layer1.layer2[1]")</code></td><td><code>"layer 3 value"</code></td></tr><tr><td><code>data?.layer1?.layer2?.[0]?.layer4</code></td><td><code>_.get(data, "layer1.layer2[0].layer4")</code></td><td><code>"layer 4 value"</code></td></tr><tr><td><code>data?.layer1?.layer2?.[2]</code></td><td><code>_.get(data, "layer1.layer2[2]")</code></td><td><code>undefined</code></td></tr><tr><td><code>data?.layer1?.layer2?.[0]?.func(0)</code></td><td><code>_.get(data, "layer1.layer2[0].func")(0)</code></td><td><code>"in layer 4 func 0"</code></td></tr><tr><td><code>data?.layer1?.layer2?.[0]?.func_not_existed?.(0)</code></td><td><code>_.get(data, "layer1.layer2[0].func_not_existed", () => undefined)(0)</code></td><td><code>undefined</code></td></tr></tbody></table>
<p>然后比较一下<code>??</code>和一些相关的操作符：</p>













































<table><thead><tr><th>使用<code>??</code>操作符</th><th>使用其他操作符</th></tr></thead><tbody><tr><td><code>undefined??true // true</code></td><td><code>undefined || true // true</code></td></tr><tr><td><code>undefined??false // false</code></td><td><code>undefined || false // false</code></td></tr><tr><td><code>null??false // false</code></td><td><code> null || false // false</code></td></tr><tr><td><code>null??true // true</code></td><td><code>null || false // false</code></td></tr><tr><td><code>false??true // false</code></td><td><code>false || true // true</code></td></tr><tr><td><code>false??'' // false</code></td><td><code>false || "" // ""</code></td></tr><tr><td><code>""??true // ""</code></td><td><code>"" || true // true</code></td></tr><tr><td><code>""??false // ""</code></td><td><code>"" || false // false</code></td></tr><tr><td><code>""??null // ""</code></td><td><code>"" || null // null</code></td></tr></tbody></table>
<p>在使用<code>??</code>操作符的时候，需要注意的正是根据<code>??</code>的定义，注意到它只能作用于<code>undefined</code>和<code>null</code>。而结合<code>?.</code>和<code>??</code>使用最常见的例子就是，通过<code>?.</code>来获取嵌套在对象内部的值，并且通过在最后放一个<code>??</code>来给出一个表达式的默认值。</p></div>  
</div>
            