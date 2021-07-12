
---
title: 'Set和Map数据结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9354'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 08:05:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=9354'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、Set</h2>
<h3 data-id="heading-1">1、概述：</h3>
<ul>
<li>
<p>ES6提供新的数据结构Set，类似于数组，但是成员的值是唯一的，没有重复值。也就是说Set是不重复的值的集合</p>
</li>
<li>
<p>没有键名，只有键值，或说键名和键值是同一个值，两个值永远是相等的</p>
</li>
<li>
<p>接受一个数组作为参数，用来初始化</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>]);
consle.log(set);<span class="hljs-comment">//[1,2,3,4]</span>
<span class="hljs-built_in">console</span>.log([...set]);<span class="hljs-comment">//[1,2,3,4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2、属性和方法</h3>
<h4 data-id="heading-3">操作方法：</h4>
<ul>
<li>
<p>.add( ) 添加某一个值，返回的是Set结构本身</p>
</li>
<li>
<p>.delete( ) 删除某个值，返回一个布尔值，表示删除是否成功</p>
</li>
<li>
<p>.has( ) 返回一个布尔值，表示该值是否为Set的成员</p>
</li>
<li>
<p>.clear( ) 清除所有成员，没有返回值</p>
</li>
</ul>
<h4 data-id="heading-4">遍历方法：</h4>
<ul>
<li>.keys( ) 返回键名</li>
<li>.values( ) 返回键值</li>
</ul>
<p>​        因为Set没有键名只有键值，或说键名和键值是同一个值，所以.values( )和.keys()行为一致</p>
<p>​        Set结构的实例默认可遍历，所以可以省略.values方法；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>]);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set.keys()) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"set.keys:"</span>, i);
&#125;

<span class="hljs-keyword">let</span> set2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>]);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set2.values()) &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"set.values:"</span>, i);
&#125;

<span class="hljs-keyword">let</span> set4 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"red"</span>, <span class="hljs-string">"green"</span>, <span class="hljs-string">"blue"</span>]);
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set4) &#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Set结构的实例默认可遍历："</span>, i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>.entries( ) 返回键值对</li>
<li>.forEach( )</li>
</ul>
<h3 data-id="heading-5">3、Set结构如何转为数组：使用Array.from</h3>
<p><strong>Array.from****方法可以将 Set 结构转为数组</strong></p>
<h3 data-id="heading-6">4、使用场景：</h3>
<h4 data-id="heading-7">（1）去除数组重复成员</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//实例1</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">4</span>]);
<span class="hljs-built_in">console</span>.log(set);<span class="hljs-comment">//[1,2,3,4]</span>

<span class="hljs-comment">//实例2</span>
<span class="hljs-keyword">const</span> items = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">6</span>]);
<span class="hljs-keyword">const</span> array = <span class="hljs-built_in">Array</span>.from(items);<span class="hljs-comment">//[1,2,3,4,5,6]</span>

<span class="hljs-comment">//实例3</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dedupe</span>(<span class="hljs-params">array</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(array));<span class="hljs-comment">//Array.from方法可以将Set结构转为数组</span>
&#125;

dedupe([<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]);<span class="hljs-comment">//[1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">（2）去除字符串重复字符</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">"ascddsdfg"</span>;
<span class="hljs-keyword">const</span> DEPLICATE_STR = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(str);
<span class="hljs-built_in">console</span>.log([...DEPLICATE_STR].join(<span class="hljs-string">''</span>));<span class="hljs-comment">//ascdfg</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>join( )将数组中的所有元素转换成一个字符串;</strong></p>
<h4 data-id="heading-9">（3）求并集/交集/差集</h4>
<p>数组的map和filter方法可以间接用于Set，Set本身没有map和filter方法的哦~</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">4</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>]);

<span class="hljs-keyword">let</span> union = [...new <span class="hljs-built_in">Set</span>([...a, ...b])];
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"并集="</span>, union); <span class="hljs-comment">//[1,2,3,4]</span>

<span class="hljs-keyword">let</span> intersect = [...new <span class="hljs-built_in">Set</span>([...a].filter(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> b.has(x)))];
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"交集="</span>, intersect); <span class="hljs-comment">//[2,3]</span>

<span class="hljs-keyword">let</span> difference = <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...a].filter(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> !b.has(x))));
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"差集="</span>, difference); <span class="hljs-comment">//[1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5、WeakSet和Set的区别：</h3>
<p>WeakSet和Set的区别：</p>
<ul>
<li>
<p>都是不可重复值的集合</p>
</li>
<li>
<p>成员只能是对象</p>
</li>
<li>
<p>没有size属性，不可遍历</p>
</li>
</ul>
<p>用处：</p>
<p>WeakSet的一个用处，是储存DOM节点，而不担心这些节点从文档移除时，会引发内存泄漏；</p>
<h2 data-id="heading-11">二、Map</h2>
<h3 data-id="heading-12">1、概述</h3>
<ul>
<li>
<p>本质上是健值对的集合，类似集合;</p>
</li>
<li>
<p>传统键值对都是“字符串-值”的对应，有所限制，所以Map结构提供了“值-值”的对应；</p>
</li>
<li>
<p>可以遍历，可以跟各种数据格式转换</p>
</li>
<li>
<p>接受一个数组作为参数，数组成员是一个个表示键值对的数组；</p>
</li>
<li>
<p>Set和Map都可以生成新的Map;</p>
</li>
<li>
<p>只有对同一个对象的引用，Map 结构才将其视为同一个键;</p>
</li>
</ul>
<p>​       Map 的键实际上是跟内存地址绑定的，只要内存地址不一样，就视为两个键。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set([<span class="hljs-string">'aaa'</span>,<span class="hljs-number">5</span>]);
<span class="hljs-built_in">console</span>.log(map.get([<span class="hljs-string">'aaa'</span>]));<span class="hljs-comment">//undefined</span>

<span class="hljs-comment">//只有对同一个对象的引用，Map 结构才将其视为同一个键;所以必须要指向同一个对象，将其存为一个对象；</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">const</span> k1 = [<span class="hljs-string">'aaa'</span>];
map.set(k1,<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(map.get(k1));<span class="hljs-comment">//5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2、属性和方法</h3>
<h4 data-id="heading-14">操作方法：</h4>
<ul>
<li>
<p>.set( )</p>
</li>
<li>
<p>.get( )</p>
</li>
<li>
<p>.delete( )</p>
</li>
<li>
<p>.has( )</p>
</li>
<li>
<p>.clear( )</p>
</li>
</ul>
<h4 data-id="heading-15">遍历方法：</h4>
<ul>
<li>
<p>.keys( ) 返回键名的遍历器</p>
</li>
<li>
<p>.values( ) 返回键值的遍历器</p>
</li>
<li>
<p>.entries( ) 返回所有成员的遍历器</p>
</li>
<li>
<p>forEach( ) 遍历Map的所有成员</p>
</li>
</ul>
<p>Map的遍历顺序就是插入的顺序</p>
<h3 data-id="heading-16">3、与其他数据结构的互相转换</h3>
<h3 data-id="heading-17">（1）Map转数组： 使用扩展运算符</h3>
<h3 data-id="heading-18">（2）数组转Map</h3>
<h3 data-id="heading-19">（3）Map转对象：Object.create( )</h3>
<h3 data-id="heading-20">（4）对象转Map：Object.entries( )</h3>
<h3 data-id="heading-21">（5）Map转JSON</h3>
<h3 data-id="heading-22">（6）JSON转Map</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1、Map转数组</span>
<span class="hljs-keyword">const</span> map0 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>().set(<span class="hljs-number">1</span>,<span class="hljs-string">'a'</span>).set(<span class="hljs-number">2</span>,<span class="hljs-string">'b'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"："</span>,[...map0]);<span class="hljs-comment">//[&#123;1,'a'&#125;,&#123;2,b&#125;]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Map转数组："</span>,[...map0].keys());<span class="hljs-comment">//[1,2]</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Map转数组："</span>,[...map0].values());<span class="hljs-comment">//['a','b']</span>

<span class="hljs-comment">//2、数组转Map,将数组直接传入Map构造函数</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
[<span class="hljs-literal">true</span>,<span class="hljs-number">7</span>],
[&#123;<span class="hljs-attr">foo</span>:<span class="hljs-number">3</span>&#125;,[<span class="hljs-string">'abc]]
])
 
//3、Map转对象
 const map1 = new Map().set(1,'</span>a<span class="hljs-string">').set(2,'</span>b<span class="hljs-string">');
 function strMapToObj(strMap)&#123;
   let obj = Object.create(null);//创建一个空对象，这样创建的对象干净，除了自身属性之外没有其他属性和方法
   for(let [k,v] of strMap)&#123;
     obj[k] = v;
   &#125;
   return obj
 &#125;
 strMapToObj(map1);

//4、对象转数组
const obj1 = &#123;1:'</span>a<span class="hljs-string">',2:'</span>b<span class="hljs-string">'&#125;
let map2 = new Map(Object.entries(obj))//Object.entries()返回一个给定对象自身可枚举属性的键值对数组[['</span><span class="hljs-number">1</span><span class="hljs-string">','</span>a<span class="hljs-string">'],['</span><span class="hljs-number">2</span><span class="hljs-string">','</span>b<span class="hljs-string">']]
 
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">4、使用场景：</h3>
<p>可以使用数组的map和filter方法,Map本身是没有map和filter方法的</p>
<h4 data-id="heading-24">（1）实现Map的过滤和遍历</h4>
<pre><code class="copyable">const map0 = new Map().set(1,'a).set(2,'b).set(3,'c');

const map1 = new Map([...map0].filter(([k,v])=>k < 3));
const map2 = new Map([...map0].map(([k,v])=>[k*2,'_'+v])) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">5、WeakMap和Map的区别</h3>
<ul>
<li>只接受对象作为键名（null除外）；</li>
<li>WeakMap的键名所指的对象，是弱引用，即不会被计入垃圾回收机制；</li>
</ul>
<p>​       （也就是说一旦不需要了，WeakMap里面的键名对象和所对应的键值对就会自动消失，不用手动删除）</p>
<p>​       （注意：弱引用的只是键名，而不是键值，键值依然是正常引用）</p>
<ul>
<li>
<p>WeakMap的专用场合：</p>
</li>
<li>
<p>它的键所对应的对象，可能会在未来消失。</p>
</li>
<li>
<p>WeakMap结构有助于防止内存泄漏。</p>
</li>
</ul>
<p>在API上的区别：</p>
<ul>
<li>
<p>没有遍历操作，即没有keys()、values()、entries()方法，也没有size属性；</p>
</li>
<li>
<p>无法清空，即不支持clear()方法，因此WeakMap只有set( )、get( )、has( )、delete( )方法；</p>
</li>
</ul>
<p>学习资料：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fset-map" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/set-map" ref="nofollow noopener noreferrer">ECMAScript 6 入门-Set 和 Map 数据结构</a></p></div>  
</div>
            