
---
title: '小技巧系列 -- 对象、数组、Map、JSON之间的相互转换'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3730'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 01:39:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=3730'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ES5 中 对象 与数组，JSON 之间的相互转换</h2>
<ul>
<li>对象转换为数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 取 keys</span>
<span class="hljs-keyword">const</span> obj1 = &#123;
    <span class="hljs-attr">name1</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">name2</span>: <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">name3</span>: <span class="hljs-literal">undefined</span>,
&#125;
<span class="hljs-keyword">const</span> arr1 = <span class="hljs-built_in">Object</span>.keys(obj)
<span class="hljs-comment">// 取 values</span>
<span class="hljs-keyword">const</span> obj2 = &#123;
    <span class="hljs-attr">name1</span>: <span class="hljs-string">'aaa'</span>,
    <span class="hljs-attr">name2</span>: <span class="hljs-string">'bbb'</span>,
    <span class="hljs-attr">name3</span>: <span class="hljs-string">'ccc'</span>,
&#125;
<span class="hljs-keyword">const</span> arr2 = <span class="hljs-built_in">Object</span>.values(obj)
<span class="hljs-built_in">console</span>.log(arr)
<span class="hljs-comment">// 都取</span>
<span class="hljs-keyword">const</span> obj3 = &#123;
    <span class="hljs-attr">name1</span>: <span class="hljs-string">'aaa'</span>,
    <span class="hljs-attr">name2</span>: <span class="hljs-string">'bbb'</span>,
    <span class="hljs-attr">name3</span>: <span class="hljs-string">'ccc'</span>,
&#125;
<span class="hljs-keyword">const</span> arr3 = <span class="hljs-built_in">Object</span>.keys(obj)
<span class="hljs-built_in">console</span>.log(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组转换为对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 索引为 key 值，数组元素为 value 值</span>
<span class="hljs-keyword">const</span> arr1 = [<span class="hljs-string">'name1'</span>,<span class="hljs-string">'name2'</span>,<span class="hljs-string">'name3'</span>]
<span class="hljs-keyword">const</span> obj1 = &#123;..arr1&#125; <span class="hljs-comment">// &#123; '0': 'name1', '1': 'name2', '2': 'name3' &#125;</span>
<span class="hljs-comment">// 数组元素为 key 值，value 值为 undefined</span>
<span class="hljs-keyword">const</span> arr2 = [<span class="hljs-string">'name1'</span>,<span class="hljs-string">'name2'</span>,<span class="hljs-string">'name3'</span>]
<span class="hljs-keyword">const</span> obj2 = &#123;&#125;
arr2.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>)=></span>&#123; obj2[item] = <span class="hljs-literal">undefined</span> &#125;)
<span class="hljs-built_in">console</span>.log(obj2)<span class="hljs-comment">// &#123; name1: undefined, name2: undefined, name3: undefined &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">ES6 中 Map 与对象、数组，JSON 之间的相互转换</h2>
<p>以下内容来自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fjingtian678%2Farticle%2Fdetails%2F94365296" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/jingtian678/article/details/94365296" ref="nofollow noopener noreferrer">原文</a></p>
<ul>
<li>Map转为数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 保留 key、value，转换成二元数组</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-number">1</span>,<span class="hljs-string">"foo"</span>).set(<span class="hljs-number">2</span>,<span class="hljs-string">"bar"</span>).set(<span class="hljs-number">3</span>,<span class="hljs-string">"baz"</span>);
<span class="hljs-keyword">const</span> arr = [...map]; <span class="hljs-comment">// 法一：[ [ 1, 'foo' ], [ 2, 'bar' ], [ 3, 'baz' ] ]</span>
<span class="hljs-keyword">const</span> arr = <span class="hljs-built_in">Array</span>.from(map); <span class="hljs-comment">// 法二：[ [ 1, 'foo' ], [ 2, 'bar' ], [ 3, 'baz' ] ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组 转为 Map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-string">"foo"</span>,<span class="hljs-string">"bar"</span>,<span class="hljs-string">"baz"</span>];
<span class="hljs-comment">// key 值是索引、value 值是元素</span>
<span class="hljs-keyword">const</span> map1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(arr.map( <span class="hljs-function">(<span class="hljs-params">value,key</span>) =></span> [key,value]));
<span class="hljs-comment">// Map(3) &#123; 0 => 'foo', 1 => 'bar', 2 => 'baz' &#125;</span>

<span class="hljs-comment">// key 值是元素，value 值是 undefined</span>
<span class="hljs-keyword">const</span> map2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(arr.map(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> [value,<span class="hljs-literal">undefined</span>]));
<span class="hljs-comment">// Map(3) &#123; 'foo' => undefined, 'bar' => undefined, 'baz' => undefined &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Map 转为对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-number">1</span>,<span class="hljs-string">"foo"</span>).set(<span class="hljs-number">2</span>,<span class="hljs-string">"bar"</span>).set(<span class="hljs-number">3</span>,<span class="hljs-string">"baz"</span>);
<span class="hljs-keyword">const</span> mapToObj = <span class="hljs-function">(<span class="hljs-params">map</span>) =></span> &#123;
     <span class="hljs-keyword">let</span> obj = &#123;&#125;;
     <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> [k,v] <span class="hljs-keyword">of</span> map) &#123;
         obj[k] = v;
     &#125;
     <span class="hljs-keyword">return</span> obj;
&#125;
<span class="hljs-built_in">console</span>.log(mapToObj(map));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>对象转为 Map</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;
       <span class="hljs-string">"1"</span> : <span class="hljs-string">"foo"</span>,
       <span class="hljs-string">"2"</span>: <span class="hljs-string">"bar"</span>,
      <span class="hljs-string">"3"</span> : <span class="hljs-string">"baz"</span>,
&#125;
<span class="hljs-keyword">const</span> objToMap = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;
           map.set(key,obj[key]);
      &#125;
      <span class="hljs-keyword">return</span> map;
&#125;
<span class="hljs-built_in">console</span>.log(objToMap(obj));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Map 转为 JSON（借助 Map 转 JSON）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-number">1</span>,<span class="hljs-string">"foo"</span>).set(<span class="hljs-number">2</span>,<span class="hljs-string">"bar"</span>).set(<span class="hljs-number">3</span>,<span class="hljs-string">"baz"</span>);
<span class="hljs-keyword">const</span> mapToJson = <span class="hljs-function">(<span class="hljs-params">map</span>) =></span> <span class="hljs-built_in">JSON</span>.stringify(mapToObj(map));
<span class="hljs-built_in">console</span>.log(mapToJson(map));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>JSON 转为 Map（借助对象转 Map）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> json = <span class="hljs-string">'&#123;"1":"foo","2":"bar","3":"baz"&#125;'</span>;
<span class="hljs-keyword">const</span> jsonToMap = <span class="hljs-function">(<span class="hljs-params">json</span>) =></span> objToMap(<span class="hljs-built_in">JSON</span>.parse(json));
<span class="hljs-built_in">console</span>.log(jsonToMap(json));
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            