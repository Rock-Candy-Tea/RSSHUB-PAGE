
---
title: 'JavaScript数据结构（六）散列表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f3fe0a98614e30993516a6d26f9b74~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 23:07:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f3fe0a98614e30993516a6d26f9b74~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 定义</h3>
<p>HashTable、HashMap，是Dictionary类的一种散列表实现方式</p>
<p>散列算法：尽可能快地在数据结构中找到一个值</p>
<p>散列函数：给定一个键值，然后返回值在表中的地址</p>
<blockquote>
<p>应用：</p>
<p>关系型数据库：创建新的表时，同时创建一个索引来更快地查询到记录的key</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3f3fe0a98614e30993516a6d26f9b74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2. 具体操作</h3>
<p><strong>创建</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HaspTable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">toStrFn = defaultToString</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.toStrFn = toStrFn;
        <span class="hljs-built_in">this</span>.table = &#123;&#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建散列函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">loseloseHashCode</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> key === <span class="hljs-string">'number'</span>) &#123;
        <span class="hljs-keyword">return</span> key;
    &#125;
    <span class="hljs-keyword">const</span> tableKey = <span class="hljs-built_in">this</span>.toStrFn(key);
    <span class="hljs-keyword">let</span> hash = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < tableKey.length; i++) &#123;
        has += tableKey.charCodeAt(i);  <span class="hljs-comment">//转换为ASII码值</span>
    &#125;
    <span class="hljs-keyword">return</span> hash % <span class="hljs-number">37</span>;  <span class="hljs-comment">//规避操作数超过数值变量最大表示范围的风险</span>
&#125;

<span class="hljs-function"><span class="hljs-title">hashCode</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.loseloeseHashCode(key);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法</strong></p>
<ul>
<li>
<p>put(key,value)：向散列表增加一个新的项（也能更新散列表）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">key, value</span>)</span> &#123;
    <span class="hljs-keyword">if</span>(key != <span class="hljs-literal">null</span> && value ! <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
        <span class="hljs-built_in">this</span>.table[position] = <span class="hljs-keyword">new</span> ValuePair(key, value);
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>remove(key)：根据键值从散列表中移除值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> hash = <span class="hljs-built_in">this</span>.hashCode(key);
    <span class="hljs-keyword">const</span> valuePair = <span class="hljs-built_in">this</span>.table[hash];
    <span class="hljs-keyword">if</span>(valuePair != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[hash];
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>get(key)：返回根据键值检索到的特定的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> valuePair = <span class="hljs-built_in">this</span>.table[<span class="hljs-built_in">this</span>.hashCode(key)];
    <span class="hljs-keyword">return</span> valuePair == <span class="hljs-literal">null</span> ? <span class="hljs-literal">undefined</span> : valuePair.value;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">3. 使用</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> hash = <span class="hljs-keyword">new</span> HashTable();

hash.put(<span class="hljs-string">'Gandalf'</span>, <span class="hljs-string">'gandalf@email.com'</span>);
hash.put(<span class="hljs-string">'John'</span>, <span class="hljs-string">'johnsnow@email.com'</span>);
hash.put(<span class="hljs-string">'Tyrion'</span>, <span class="hljs-string">'tyrion@email.com'</span>);

<span class="hljs-built_in">console</span>.log(hash.hashCode(<span class="hljs-string">'Gandalf'</span>) + <span class="hljs-string">' - Gandalf'</span>); <span class="hljs-comment">// 19 - Gandalf</span>
<span class="hljs-built_in">console</span>.log(hash.hashCode(<span class="hljs-string">'John'</span>) + <span class="hljs-string">' - John'</span>);  <span class="hljs-comment">// 29 - John</span>
<span class="hljs-built_in">console</span>.log(hash.hashCode(<span class="hljs-string">'Tyrion'</span>) + <span class="hljs-string">' - Tyrion'</span>);  <span class="hljs-comment">// 16 - Tyrion</span>
<span class="hljs-built_in">console</span>.log(hash.get(<span class="hljs-string">'Gandalf'</span>)); <span class="hljs-comment">// gandalf@email.com</span>
<span class="hljs-built_in">console</span>.log(hash.get(<span class="hljs-string">'Loiane'</span>)); <span class="hljs-comment">// undefined</span>

hash.remove(<span class="hljs-string">'Gandalf'</span>);
<span class="hljs-built_in">console</span>.log(hash.get(<span class="hljs-string">'Gandalf'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>散列表和散列集合</strong></p>
<p>类似</p>
<p>散列集合由一个集合构成，插入、移除或获取元素时，使用的是hashCode函数</p>
<blockquote>
<p>不同之处： 不需要添加键值对，只插入值而没有键</p>
</blockquote>
<h3 data-id="heading-3">4. 处理散列表的冲突</h3>
<p>当键有相同的散列值时，不同的值在散列表中对应着相同的位置，后面添加的值会覆盖前面的，称为冲突。</p>
<p><strong>处理冲突的几种方法： 分离链接、线性探查和双散列法</strong></p>
<h4 data-id="heading-4">1. 分离链接</h4>
<p>解决冲突的最简单的方法</p>
<p>分离链接法包括为散列表的每一个位置创建一个链表并将元素存储在里面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bec423ba9ea4fb2942f3631136ea6c0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>创建</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashTableSeparateChaining</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">toStrFn = defaultString</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.toStrFn = toStrFn;<span class="hljs-number">2</span>
        <span class="hljs-built_in">this</span>.table = &#123;&#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法</strong></p>
<ul>
<li>
<p>put(key,value)：向散列表增加一个新的项（也能更新散列表）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">key, value</span>)</span> &#123;
    <span class="hljs-keyword">if</span>(key != <span class="hljs-literal">null</span> && value != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.table[position] == <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-built_in">this</span>.table[position] = <span class="hljs-keyword">new</span> LinkedList();
        &#125;
        <span class="hljs-built_in">this</span>.table[position].push(<span class="hljs-keyword">new</span> ValuePair(key, value));
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>remove(key)：根据键值从散列表中移除值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
    <span class="hljs-keyword">const</span> linkedList = <span class="hljs-built_in">this</span>.table[position];
    <span class="hljs-keyword">if</span> (linkedList != <span class="hljs-literal">null</span> && !linkedList.isEmpty()) &#123;
        <span class="hljs-keyword">let</span> current = linkedList.getHead();
        <span class="hljs-keyword">while</span> (current != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">if</span> (current.element.key === key)&#123;
                linkedList.remove(current.element);
                <span class="hljs-keyword">if</span> (linkedList.isEmpty()) &#123;
                    <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[position];
                &#125;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
            &#125;
            current = current.next;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>get(key)：返回根据键值检索到的特定的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
    <span class="hljs-keyword">const</span> linkedList = <span class="hljs-built_in">this</span>.table[position];
    <span class="hljs-keyword">if</span>(linkedList != <span class="hljs-literal">null</span> && !linkedList.isEmpty()) &#123;
        <span class="hljs-keyword">let</span> current = linkedList.getHead();
        <span class="hljs-keyword">while</span>(current != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">if</span>(current.element.key === key)&#123;
                <span class="hljs-keyword">return</span> current.element.value;
            &#125;
            current = current.next;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-5">2. 线性探查</h4>
<p>将元素直接存储到表中</p>
<p>当想向表中添加一个新元素的时候，如果索引为position的位置被占据，以此寻找position+1、position+2……直到有空的位置</p>
<p><strong>删除键值对</strong>：</p>
<ol>
<li>
<p>软删除： 使用特殊的值（标记）来表示键值对被删除，并不是真的删除</p>
<blockquote>
<p>会降低散列表的效率，因为搜索键值会随时间变慢</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5222109c6c540a9a65a4c45fb0321bb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>检验是否有必要将一个或多个元素移动到之前的位置。当搜索一个键的时候，这种方法可以避免找到一个空位置</p>
<blockquote>
<p>需要移动元素，挪动键值对</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d96e69e665948fbbf9335d5d975d010~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
<p><strong>方法</strong></p>
<ul>
<li>
<p>put(key,value)：向散列表增加一个新的项（也能更新散列表）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">key, value</span>)</span> &#123;
    <span class="hljs-keyword">if</span>(key != <span class="hljs-literal">null</span> && value != <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.table[position] == <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-built_in">this</span>.table[position] = <span class="hljs-keyword">new</span> ValuePair(key, value);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">let</span> index = position + <span class="hljs-number">1</span>;
            <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.table[position] != <span class="hljs-literal">null</span>) &#123;  <span class="hljs-comment">//如果位置被占了，就找下一位</span>
                index++;
            &#125;
            <span class="hljs-built_in">this</span>.table[index] = <span class="hljs-keyword">new</span> ValuePair(key, value);
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>remove(key)：根据键值从散列表中移除值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.table[position] != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.table[position].key === key) &#123;
            <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[position];
            <span class="hljs-built_in">this</span>.varifyRemoveSideEffect(key, position);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
        <span class="hljs-keyword">let</span> index = position + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.table[index] != <span class="hljs-literal">null</span> && <span class="hljs-built_in">this</span>.table[index].key !== key) &#123;
            index++;
        &#125;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.table[index] != <span class="hljs-literal">null</span> && <span class="hljs-built_in">this</span>.table[index].key === key) &#123;
            <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[index];
            <span class="hljs-built_in">this</span>.verifyRemoveSideEffect(key, index);
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;

<span class="hljs-function"><span class="hljs-title">verifyRemoveSideEffect</span>(<span class="hljs-params">key, removedPosition</span>)</span> &#123;
    <span class="hljs-keyword">const</span> hash = <span class="hljs-built_in">this</span>.hashCode(key); 
    <span class="hljs-keyword">let</span> index = removedPosition + <span class="hljs-number">1</span>; 
    <span class="hljs-keyword">while</span> (<span class="hljs-built_in">this</span>.table[index] != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-keyword">const</span> posHash = <span class="hljs-built_in">this</span>.hashCode(<span class="hljs-built_in">this</span>.table[index].key);
        <span class="hljs-keyword">if</span> (posHash <= hash || posHash <= removedPosition) &#123; 
            <span class="hljs-built_in">this</span>.table[removedPosition] = <span class="hljs-built_in">this</span>.table[index];
            <span class="hljs-keyword">delete</span> <span class="hljs-built_in">this</span>.table[index];  removedPosition = index; 
        &#125; 
        index++; 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>get(key)：返回根据键值检索到的特定的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> position = <span class="hljs-built_in">this</span>.hashCode(key);
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.table[position] != <span class="hljs-literal">null</span>)&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.table[position].key === key) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.table[position].value;
        &#125;
        <span class="hljs-keyword">let</span> index = position + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.table[index] != <span class="hljs-literal">null</span> && <span class="hljs-built_in">this</span>.table[index].key !== key) &#123;
            index++;
        &#125;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.table[index] != <span class="hljs-literal">null</span> && <span class="hljs-built_in">this</span>.table[index].key === key) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.table[position].value;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6">5. ES2015Map类</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'Gandalf'</span>, <span class="hljs-string">'gandalf@email.com'</span>);
map.set(<span class="hljs-string">'John'</span>, <span class="hljs-string">'johnsnow@email.com'</span>);
map.set(<span class="hljs-string">'Tyrion'</span>, <span class="hljs-string">'tyrion@email.com'</span>);
<span class="hljs-built_in">console</span>.log(map.has(<span class="hljs-string">'Gandalf'</span>)); <span class="hljs-comment">// true console.log(map.size);</span>
<span class="hljs-built_in">console</span>.log(map.keys()); <span class="hljs-comment">// 输出&#123;"Gandalf", "John", "Tyrion"&#125; </span>
<span class="hljs-built_in">console</span>.log(map.values()); <span class="hljs-comment">// 输出&#123;"gandalf@email.com", "johnsnow@email.com", "tyrion@email.com"&#125;</span>
<span class="hljs-built_in">console</span>.log(map.get(<span class="hljs-string">'Tyrion'</span>)); <span class="hljs-comment">// tyrion@email.com</span>
map.delete(<span class="hljs-string">'John'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6. ES2105 WeakMap类和WeakSet类</h3>
<p>除了Set和Map这两种新的数据结构，ES2015还增加了它们的弱化版本，WeakSet和WeakMap</p>
<p><strong>区别</strong>：</p>
<ul>
<li>WeakSet或WeakMap类没有entries、keys和values等方法</li>
<li>只能用对象作为键</li>
</ul>
<p>创建和使用这两个类主要是为了<strong>性能</strong>，WeakSet和WeakMap是弱化的（用对象作为键），没有强引用的键。这使得JavaScript的垃圾回收器可以从中清除整个入口。</p>
<p>必须用键才可以取出值。这些类没有entries、keys和values等迭代器方法，因此，除非你知道键，否则没有办法取出值。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">const</span> ob1 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Gandalf'</span> &#125;; 
<span class="hljs-keyword">const</span> ob2 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'John'</span> &#125;;
<span class="hljs-keyword">const</span> ob3 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Tyrion'</span> &#125;;
map.set(ob1, <span class="hljs-string">'gandalf@email.com'</span>);
map.set(ob2, <span class="hljs-string">'johnsnow@email.com'</span>);
map.set(ob3, <span class="hljs-string">'tyrion@email.com'</span>);
<span class="hljs-built_in">console</span>.log(map.has(ob1)); 
<span class="hljs-built_in">console</span>.log(map.get(ob3)); <span class="hljs-comment">// tyrion@email.com &#123;4&#125; map.delete(ob2);</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            