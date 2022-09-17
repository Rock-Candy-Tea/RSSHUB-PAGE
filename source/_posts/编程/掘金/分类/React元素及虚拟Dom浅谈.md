
---
title: 'React元素及虚拟Dom浅谈'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4771'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 06:17:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=4771'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">什么是元素</h4>
<p>元素是构成React应用的最小计量单位，元素描述的是开发想让用户看到的内容。</p>
<p>组件是由n个元素组成的。</p>
<h4 data-id="heading-1">元素的特性</h4>
<ol>
<li>不可变</li>
</ol>
<p>一旦创建就无法改变其元素或者属性，代表了创建那一时刻的UI。</p>
<ol start="2">
<li>都是通过<code>ReactDOM.render(JSX, DOM)</code>函数进行渲染。</li>
</ol>
<h4 data-id="heading-2">什么是虚拟Dom。</h4>
<p>React只更新它需要更新的部分，这是根据虚拟dom的特性进行指定元素更新的。
虚拟dom实际就是一个对象，用来描述元素的名称方法及属性等：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> virtualDom = &#123;
    <span class="hljs-attr">$$typeof</span>: <span class="hljs-title class_">Symbol</span>(react.<span class="hljs-property">element</span>),
    <span class="hljs-attr">type</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">props</span>: &#123;<span class="hljs-attr">class</span>: <span class="hljs-string">'index'</span>&#125;,
    <span class="hljs-attr">key</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ref</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">_owner</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">children</span>: [
        ...
    ],
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">虚拟Dom的优劣势</h4>
<ol>
<li>虚拟dom比起直接操作dom，多了一步创建对象的步骤</li>
<li>当全量对dom进行操作时，虚拟dom可以实现局部更新速度上会更具优势。</li>
<li>如果只是对dom进行进行局部增量编程，可以不使用虚拟dom，此时因为少一步创建对象步骤，会比虚拟dom快。</li>
<li>基于虚拟dom，React实现了一套跨浏览器、平台的事件机制，模拟了事件冒泡捕获，采取事件代理、批量更新的方法，解决了在不同平台、不同浏览器下的兼容性问题。</li>
</ol>
<p>总结：使用虚拟dom，利用其React Fiber的diff更新机制，可以使我们无需手动对dom操作进行优化，保证了性能下限，并且其提供了跨平台的好处。</p></div>  
</div>
            