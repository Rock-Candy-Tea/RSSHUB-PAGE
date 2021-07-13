
---
title: 'JavaScript数据结构（五）字典'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232bb73c9fa744d7bee16e7c43f9e66c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 23:07:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232bb73c9fa744d7bee16e7c43f9e66c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 定义</h3>
<p>字典是以**[键，值]**的形式来存储元素。字典也称作映射、符号表或关联数组。</p>
<p>es6中有字典Map</p>
<p>常用操作：键值对的增删改查</p>
<h3 data-id="heading-1">2. 具体操作</h3>
<p><strong>创建</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; defaultToString &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../util'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dictionary</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">toStrFn = defaultToString</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.toStrFn = toStrFn;
        <span class="hljs-built_in">this</span>.table = &#123;&#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在字典中，理想的情况是用字符串作为键名，值可以是任何类型。但是，由于JavaScript 不是强类型的语言，我们<strong>不能保证键一定是字符串</strong>。我们需要把所有作为键名传入的对象转化为字符串，使得从Dictionary 类中搜索和获取值更简单。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ValuePair</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">key, value</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.key = key;
        <span class="hljs-built_in">this</span>.value = value;
    &#125;
    <span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">`[#<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.key&#125;</span>: <span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.value&#125;</span>]`</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用</strong></p>
<ul>
<li>
<p>set(key,value)：向字典中添加新元素</p>
<p>如果key 已经存在，那么已存在的 value 会被新的值覆盖</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">key, value</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (key != <span class="hljs-literal">null</span> && value != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> tableKey = <span class="hljs-built_in">this</span>.toStrFn(key);  <span class="hljs-comment">//获取表示key的字符串</span>
        <span class="hljs-comment">//创建一个新的键值对，并赋值给table对象上的key属性</span>
        <span class="hljs-built_in">this</span>.table[tableKey] = <span class="hljs-keyword">new</span> ValuePair(key, value);  
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>remove(key)：通过使用键值作为参数来从字典中移除键值对应的数据值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hasKey(key)) &#123;
        <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[<span class="hljs-built_in">this</span>.toStrFn(key)];
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>hasKey(key)：如果某个键值存在于该字典中，返回true，否则返回false。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">hasKey</span>(<span class="hljs-params">key</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.table[<span class="hljs-built_in">this</span>.toStrFn(key)] != <span class="hljs-literal">null</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>get(key)：通过以键值作为参数查找特定的数值并返回。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> valuePair = <span class="hljs-built_in">this</span>.table[<span class="hljs-built_in">this</span>.toStrFn(key)]; 
    <span class="hljs-keyword">return</span> valuePair == <span class="hljs-literal">null</span> ? <span class="hljs-literal">undefined</span> : valuePair.value; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hasKey(key)) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.table[<span class="hljs-built_in">this</span>.toStrFn(key)];
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>clear()：删除该字典中的所有值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.table = &#123;&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>size()：返回字典所包含值的数量。与数组的length 属性类似。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.table).length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>isEmpty()：在size 等于零的时候返回true，否则返回false。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">isEmpty</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.size() === <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>keys()：将字典所包含的所有键名以数组形式返回。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">keys</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.keyValues().map(<span class="hljs-function"><span class="hljs-params">valuePair</span> =></span> valuePair.key);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> keys = [];
<span class="hljs-keyword">const</span> valuePairs = <span class="hljs-built_in">this</span>.keyValues();
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < valuePairs.length; i++) &#123;
keys.push(valuePairs[i].key);
&#125;
<span class="hljs-keyword">return</span> keys;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>values()：将字典所包含的所有数值以数组形式返回。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">values</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.keyValues().map(<span class="hljs-function"><span class="hljs-params">valuePair</span> =></span> valuePair.value);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>keyValues()：将字典中所有[键，值]对返回。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">keyValues</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.values(<span class="hljs-built_in">this</span>.table); <span class="hljs-comment">//Object.values()为ECMAScript 2017</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">keyValues</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> valuePairs = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> k <span class="hljs-keyword">in</span> <span class="hljs-built_in">this</span>.table) &#123; 
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.hasKey(k)) &#123;
        valuePairs.push(<span class="hljs-built_in">this</span>.table[k]);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> valuePairs;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>forEach(callbackFn)：迭代字典中所有的键值对。callbackFn 有两个参数：key 和value。该方法可以在回调函数返回false 时被中止（和Array 类中的every 方法相似）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">forEach</span>(<span class="hljs-params">callbackFn</span>)</span> &#123;
    <span class="hljs-keyword">const</span> valuePairs = <span class="hljs-built_in">this</span>.keyValues(); <span class="hljs-comment">// &#123;1&#125;</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < valuePairs.length; i++) &#123; <span class="hljs-comment">// &#123;2&#125;</span>
        <span class="hljs-keyword">const</span> result = callbackFn(valuePairs[i].key, valuePairs[i].value); <span class="hljs-comment">// &#123;3&#125;</span>
        <span class="hljs-keyword">if</span> (result === <span class="hljs-literal">false</span>) &#123;
        <span class="hljs-keyword">break</span>; <span class="hljs-comment">// &#123;4&#125;</span>
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>toString()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">toString</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isEmpty()) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
    &#125;
    <span class="hljs-keyword">const</span> valuePairs = <span class="hljs-built_in">this</span>.keyValues();
    <span class="hljs-keyword">let</span> objString = <span class="hljs-string">`<span class="hljs-subst">$&#123;valuePairs[<span class="hljs-number">0</span>].toString()&#125;</span>`</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < valuePairs.length; i++) &#123;
    objString = <span class="hljs-string">`<span class="hljs-subst">$&#123;objString&#125;</span>,<span class="hljs-subst">$&#123;valuePairs[i].toString()&#125;</span>`</span>;
    &#125;
    <span class="hljs-keyword">return</span> objString;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">3. 使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> dictionary = <span class="hljs-keyword">new</span> Dictionary();
dictionary.set(<span class="hljs-string">'Gandalf'</span>, <span class="hljs-string">'gandalf@email.com'</span>);
dictionary.set(<span class="hljs-string">'John'</span>, <span class="hljs-string">'johnsnow@email.com'</span>);
dictionary.set(<span class="hljs-string">'Tyrion'</span>, <span class="hljs-string">'tyrion@email.com'</span>);

<span class="hljs-built_in">console</span>.log(dictionary.hasKey(<span class="hljs-string">'Gandalf'</span>)) <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(dictionary.size());  <span class="hljs-comment">//3</span>
<span class="hljs-built_in">console</span>.log(dictionary.keys());  <span class="hljs-comment">//["Gandalf", "John", "Tyrion"]</span>
<span class="hljs-built_in">console</span>.log(dictionary.values()); <span class="hljs-comment">//["gandalf@email.com", "johnsnow@email.com", "tyrion@email.com"]</span>
<span class="hljs-built_in">console</span>.log(dictionary.get(<span class="hljs-string">'Tyrion'</span>));  <span class="hljs-comment">//tyrion@email.com</span>

dictionary.remove(<span class="hljs-string">'John'</span>);

dictionary.forEach(<span class="hljs-function">(<span class="hljs-params">k, v</span>) =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'forEach: '</span>, <span class="hljs-string">`key: <span class="hljs-subst">$&#123;k&#125;</span>, value: <span class="hljs-subst">$&#123;v&#125;</span>`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. LeetCode</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/232bb73c9fa744d7bee16e7c43f9e66c~tplv-k3u1fbpfcp-zoom-1.image" alt="LeetCode349" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums1</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> <span class="hljs-variable">nums2</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[]&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> intersection = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums1, nums2</span>) </span>&#123;
    <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
    nums1.forEach(<span class="hljs-function"><span class="hljs-params">n</span> =></span> &#123;
        map.set(n,<span class="hljs-literal">true</span>);
    &#125;);
    <span class="hljs-keyword">const</span> res = [];
    nums2.forEach(<span class="hljs-function"><span class="hljs-params">n</span> =></span> &#123;
        <span class="hljs-keyword">if</span>(map.get(n))&#123;
            res.push(n);
            map.delete(n);
        &#125;
    &#125;);
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将nums1的每个值以key的形式存在字典里，值设置为true</p>
<p>遍历nums2，如果在字典里找到有对应的值，则添加到res里，并在字典里删除这个值</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7b01c878d7e422cb1cdd46ace9c58be~tplv-k3u1fbpfcp-zoom-1.image" alt="LeetCode2" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> isValid = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(s.length % <span class="hljs-number">2</span> === <span class="hljs-number">1</span>) &#123; <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; &#125;
    <span class="hljs-keyword">const</span> stack = [];       <span class="hljs-comment">//栈</span>
    <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();  <span class="hljs-comment">//字典</span>
    map.set(<span class="hljs-string">'('</span>,<span class="hljs-string">')'</span>);
    map.set(<span class="hljs-string">'['</span>,<span class="hljs-string">']'</span>);
    map.set(<span class="hljs-string">'&#123;'</span>,<span class="hljs-string">'&#125;'</span>);
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < s.length; i++) &#123;
        <span class="hljs-keyword">const</span> c = s[i];
        <span class="hljs-keyword">if</span>(map.has(c)) &#123;  <span class="hljs-comment">//如果这个值和map匹配上，则向栈中添加</span>
            stack.push(c);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">const</span> t = stack[stack.length - <span class="hljs-number">1</span>]; <span class="hljs-comment">//栈顶元素</span>
            <span class="hljs-keyword">if</span>(map.get(t) === c) &#123;  <span class="hljs-comment">//键对匹配上，删除栈内的元素</span>
                stack.pop();
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> stack.length === <span class="hljs-number">0</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用栈和字典这两个数据结构</p>
<p>栈：后进先出</p>
<p>字典：键对匹配</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23bd9c852e6b4d19ac2d014791cffba2~tplv-k3u1fbpfcp-zoom-1.image" alt="LeetCode1" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> twoSum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums, target</span>) </span>&#123;
    <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;i<nums.length; i += <span class="hljs-number">1</span>)&#123;
        <span class="hljs-keyword">const</span> n = nums[i];
        <span class="hljs-keyword">const</span> n2 = target - n;
        <span class="hljs-keyword">if</span>(map.has(n2)) &#123;  <span class="hljs-comment">//在map中寻找是否有能匹配上的值</span>
            <span class="hljs-keyword">return</span> [map.get(n2), i];
        &#125;<span class="hljs-keyword">else</span>&#123;
            map.set(n, i);
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内存消耗大，执行时间快</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83d5a0aa903747f9957a98c1b1c6129a~tplv-k3u1fbpfcp-zoom-1.image" alt="LeetCode" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> lengthOfLongestSubstring = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> res = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>; r < s.length; r++) &#123;
        <span class="hljs-keyword">if</span>(map.has(s[r]) && map.get(s[r])>= l)&#123;
            l = map.get(s[r]) + <span class="hljs-number">1</span>;
        &#125;
        res = <span class="hljs-built_in">Math</span>.max(res, r - l + <span class="hljs-number">1</span>);
        map.set(s[r], r);
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用滑动窗口，如果map里有这个元素且在窗口内，则左指针向右移动</p>
<p>直到不满足条件，取窗口大小与res进行比较，res存储较大的那个数，并将右指针与指向的数字以键对的形式存储到map里</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84f99a5176d14a5fa67bce3886ecddba~tplv-k3u1fbpfcp-zoom-1.image" alt="LeetCode76" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">s</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> <span class="hljs-variable">t</span></span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;string&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> minWindow = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">s, t</span>) </span>&#123;
    <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">let</span> r = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">const</span> need = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> c <span class="hljs-keyword">of</span> t)&#123;
        need.set(c, need.has(c)? need.get(c) + <span class="hljs-number">1</span> : <span class="hljs-number">1</span>);
    &#125;  <span class="hljs-comment">//need存储t各个字符所需要的个数</span>
    <span class="hljs-keyword">let</span> needType = need.size;  <span class="hljs-comment">// 不同字符种类数</span>
    <span class="hljs-keyword">let</span> res = <span class="hljs-string">''</span>;
    <span class="hljs-keyword">while</span>(r < s.length) &#123; <span class="hljs-comment">//右指针移动</span>
        <span class="hljs-keyword">const</span> c = s[r];
        <span class="hljs-keyword">if</span>(need.has(c)) &#123;  <span class="hljs-comment">//找到need里有对应的值，则减少该字符想要的个数</span>
            need.set(c, need.get(c) - <span class="hljs-number">1</span>);
            <span class="hljs-keyword">if</span>(need.get(c) === <span class="hljs-number">0</span>) needType--;  <span class="hljs-comment">//当该字符变为0个，直接needType-1</span>
        &#125;
        <span class="hljs-keyword">while</span>(needType === <span class="hljs-number">0</span>) &#123;  <span class="hljs-comment">//当所有值都找到时，进行</span>
            <span class="hljs-keyword">const</span> newRes = s.substring(l, r + <span class="hljs-number">1</span>);  <span class="hljs-comment">//截取字符</span>
            <span class="hljs-keyword">if</span>(!res || newRes.length < res.length) res = newRes;
            <span class="hljs-keyword">const</span> c2 = s[l];  <span class="hljs-comment">//c2存放左指针对应的值</span>
            <span class="hljs-keyword">if</span>(need.has(c2)) &#123;  <span class="hljs-comment">//如果左指针对应的值是need的</span>
                need.set(c2,need.get(c2) + <span class="hljs-number">1</span>);  <span class="hljs-comment">//因为移动，会将这个值移出窗口，会使得need里c2需要的个数+1</span>
                <span class="hljs-keyword">if</span>(need.get(c2) === <span class="hljs-number">1</span>) needType++; <span class="hljs-comment">//如果刚好为1个，即需要多增加一个type</span>
            &#125;
            l++;  <span class="hljs-comment">//当窗口里找到所有t，左指针移动</span>
        &#125;
        r++;  <span class="hljs-comment">//当need不为0，右指针移动，继续寻找对应</span>
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用滑动窗口，并使用map进行键对匹配</p></div>  
</div>
            