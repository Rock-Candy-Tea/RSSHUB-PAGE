
---
title: 'ES5 ES6 ES7'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12afe75501294eeeab61c85333a8f130~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Apr 2021 19:14:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12afe75501294eeeab61c85333a8f130~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ES6 语法</h2>
<h3 data-id="heading-1">es5 和 es6 声明变量的方式对比</h3>
<p>ES5中声明变量的方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1.通过var声明</span>
<span class="hljs-keyword">var</span> num;

<span class="hljs-comment">//2.函数方式声明</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">num</span>)</span>&#123; <span class="hljs-keyword">return</span> num; &#125;
fn(<span class="hljs-number">10</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6中声明变量的方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1.使用let声明</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>;
<span class="hljs-comment">//2.使用const声明</span>
<span class="hljs-keyword">const</span> name = <span class="hljs-string">"小红"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">var、let、const 的区别</h3>
<ol>
<li>不存在变量提升
<ul>
<li>var 命令会发生 变量提升 现象，即变量可以在声明之前使用，值为undefined</li>
<li>let 和 const 则没有变量声明提升的功能，必须要先声明才能使用</li>
</ul>
</li>
<li>不允许重复声明
<ul>
<li>var命令能重复声明，后者覆盖前者</li>
<li>let 和 const不允许在相同作用域内，重复声明同一个变量</li>
</ul>
</li>
<li>作用域
<ul>
<li>var 的作用域是以函数为界限</li>
<li>let 和 const 的作用域是块作用域，块级作用域指 &#123; &#125; 内的范围</li>
<li>var 可以定义全局变量和局部变量，let 和 const 只能定义局部变量</li>
<li>const 的声明的常量不能被修改，但对于引用类型来说，堆内存中的值是可以被改变的。</li>
</ul>
</li>
<li>变量作为全局属性
<ul>
<li>var定义的变量会作为window对象的属性，而let不会</li>
</ul>
</li>
</ol>
<p>**
<strong>常量定义的引用类型可以修改</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1.使用常量定义数组</span>
        <span class="hljs-keyword">const</span> arr = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>];
        <span class="hljs-built_in">console</span>.log(arr);
        arr[<span class="hljs-number">0</span>] = <span class="hljs-string">"hello"</span>;
        <span class="hljs-built_in">console</span>.log(arr);   <span class="hljs-comment">//['hello', 200, 300]</span>
        <span class="hljs-comment">//2.使用常量来定义对象</span>
        <span class="hljs-keyword">const</span> obj = &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"Jack"</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>,
            <span class="hljs-attr">no</span>: <span class="hljs-string">"001"</span>
        &#125;
        <span class="hljs-built_in">console</span>.log(obj);
        obj.age = <span class="hljs-number">100</span>;
        <span class="hljs-built_in">console</span>.log(obj);   <span class="hljs-comment">//&#123;name: "Jack", age: 100,  no: "001"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>暂时性死区</strong>
定义：块级作用域内存在let命令时，所声明的变量就“绑定”这个区域，不再受外部的影响</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-comment">//let a 之前的区域成为暂时性死区，调用a 会报错</span>
    <span class="hljs-keyword">let</span> a = <span class="hljs-string">"hello"</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">for循环中的作用域问题</h3>
<pre><code class="copyable">//设置循环变量的部分是父级作用域，而循环体内部是一个单独的子作用域。
//ES6 中引用变量采用就近原则
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">变量的解构</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript">本质：模式匹配
   <span class="hljs-number">1.</span> 完全解构：模式完全匹配
   <span class="hljs-number">2.</span> 不完全解构：模式不完全匹配
     - 为解构变量设置默认值，不会出现 <span class="hljs-literal">undefined</span> 的现象
     - 解构成功时，解构变量的默认值会被覆盖
     - 解构不成功时，解构变量的值为默认值
   
  对象的解构注意：
    <span class="hljs-number">1.</span>对象在解构时，变量名要与属性名一致
    <span class="hljs-number">2.</span>对象解构的解构变量不考虑顺序
    <span class="hljs-number">3.</span>对象在解构时，为对象属性重命名，可以方便程序的编写。注：重命名不会更改对象的属性
    <span class="hljs-number">4.</span>和解构数组一样，解析对象时可以设置默认值 outLookURL:url = <span class="hljs-number">111</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>函数添加参数的默认值</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span> 利用解构传参，参数设置默认值   <span class="hljs-comment">//show(&#123; name = 'lucy', age = 22 &#125; = &#123;&#125;)  </span>
                            <span class="hljs-comment">//show([a = 0, b = 0])</span>

<span class="hljs-number">2.</span> ES6 直接为参数添加默认值     <span class="hljs-comment">//show(a = 0, b = 0)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>rest参数</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">rest 参数： 接收不定参
--
<span class="hljs-number">1.</span> rest 参数是一种方式(形参)，rest参数可以重命名为其他参数 ...a
<span class="hljs-number">2.</span> rest 参数只能作为最后一个参数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">es6 对于对象的扩展**</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1.对象的属性简写: 当对象的属性名和属性值（变量）名称一致，可省略赋值</span>

<span class="hljs-comment">//2.对象的方法简写：</span>
    <span class="hljs-keyword">let</span> name = <span class="hljs-string">"jack"</span>;
    <span class="hljs-keyword">let</span> age = <span class="hljs-number">22</span>;
    <span class="hljs-keyword">let</span> obj = &#123;
        name,
        age,
        <span class="hljs-attr">walk</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">" is walk"</span>);
        &#125;,
        <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name + <span class="hljs-string">` say`</span>);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">es6 中箭头函数</h3>
<p><strong>ES5 中的两种函数定义方法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-number">1.</span> 函数式       <span class="hljs-comment">//var fn = function()&#123;&#125;</span>
<span class="hljs-number">2.</span> 声明式       <span class="hljs-comment">//function show()&#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES6 中函数式声明方式被箭头函数( => )取代</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">箭头函数：使用 => 定义函数
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>当函数没有参数时，（）不能省略</li>
<li>当函数只有一个参数，且函数体是一句代码，且是返回语句, 参数的（）可省略、函数体 &#123;&#125; 可省略、return 可省略、中间使用 => 连接</li>
<li>若函数体只有一句，且不是return 语句， 不能省略 &#123;&#125;</li>
<li>若函数体有多条语句，不能省略 &#123;&#125;</li>
<li>若函数有多个参数，不能省略()</li>
<li>若函数的返回值为对象，此时不能省略return</li>
</ol>
<p><strong>使用箭头函数注意</strong></p>
<ol>
<li>箭头函数不适用于声明函数</li>
<li>箭头函数不适用于DOM事件</li>
<li>箭头函数不能作为构造函数（迭代器）</li>
<li>箭头函数内不能使用arguments</li>
<li>不能使用yield命令</li>
</ol>
<h5 data-id="heading-7">箭头函数this指向</h5>
<ol>
<li>箭头函数没有this，this是父级的</li>
<li>定义时候绑定，就是this是继承自父执行上下文中的this</li>
<li>ES5中的this指调用者，ES6中的this指定义时候绑定</li>
</ol>
<h3 data-id="heading-8">字符串遍历</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> str = <span class="hljs-string">"hello"</span>;
    <span class="hljs-comment">//1.for遍历</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < str.length; i++) &#123;
        <span class="hljs-built_in">console</span>.log(i, str[i]);     <span class="hljs-comment">//i 索引    数值类型</span>
    &#125;
    
    <span class="hljs-comment">//2.数组->for->for in</span>
    <span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> arr) &#123;
        <span class="hljs-built_in">console</span>.log(i, arr[i]);     <span class="hljs-comment">//i 索引    字符串类型</span>
    &#125;
    
    <span class="hljs-comment">//3.for... of</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> str)&#123;
        <span class="hljs-built_in">console</span>.log(i);     <span class="hljs-comment">//数据</span>
    &#125;
    
    <span class="hljs-comment">//4.解构</span>
    <span class="hljs-keyword">let</span> [a, b, c, d ,e] = str;
    <span class="hljs-built_in">console</span>.log(a, b, c, d ,e);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES6 新增字符串方法</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//字符串新增方法：</span>
方法                返回值          作用
includes(<span class="hljs-string">'str'</span>)     boolean         判断字符串中包含子串
endWith(<span class="hljs-string">'str'</span>)      boolean         判断字符串以<span class="hljs-string">"str"</span>结尾
startWith(<span class="hljs-string">'str'</span>)    boolean         判断字符串以<span class="hljs-string">"str"</span>开头
repeat(n)           重复拼接自身      重复n次输出字符串 repeat + repeat

<span class="hljs-comment">//补全字符串长度的方法 </span>
padStart(length, s);        字符串开头补全
endStart(length, s);        字符串末尾补全
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">es6 模板字符串</h3>
<p>es6的模板字符串为反引号<code> </code></p>
<ul>
<li>支持换行</li>
<li>模板中传变量$&#123;变量&#125;</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'jack'</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">20</span>
    &#125;;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`名称：<span class="hljs-subst">$&#123;obj.name&#125;</span>,年龄：<span class="hljs-subst">$&#123;obj.age&#125;</span>`</span>);  <span class="hljs-comment">//名称：jack,年龄：20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">es6 的Set结构</h3>
<p>set结构 <strong>此结构中元素是唯一的，不能重复</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">使用<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()实例化

方法：返回值是set可以连缀
  add(val)           加元素
  <span class="hljs-keyword">delete</span>(val)        删元素
  has(val)           判断是否包含元素     boolean
  clear()            删除所有数据
    
    
属性：
  size    元素个数
    

set结构的遍历:
  <span class="hljs-number">1.</span> <span class="hljs-keyword">for</span>  <span class="hljs-keyword">of</span>  遍历set
  <span class="hljs-number">2.</span> <span class="hljs-keyword">for</span>  <span class="hljs-keyword">of</span>  遍历keys()
  <span class="hljs-number">3.</span> <span class="hljs-keyword">for</span>  <span class="hljs-keyword">of</span>  遍历values()
  <span class="hljs-number">4.</span> <span class="hljs-keyword">for</span>  <span class="hljs-keyword">of</span>  遍历对象实体 entries
  <span class="hljs-number">5.</span> forEach遍历 set
  <span class="hljs-number">6.</span> 使用扩展运算符 和 解构  将set结构转为数组
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// for of 遍历数据</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set) &#123;
        <span class="hljs-built_in">console</span>.log(i);     <span class="hljs-comment">//1  2  5  3</span>
    &#125;
   
    <span class="hljs-comment">// 遍历 keys    等于遍历set</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set.keys()) &#123;
        <span class="hljs-built_in">console</span>.log(i);
    &#125;
    <span class="hljs-comment">//遍历values</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set.values()) &#123;
        <span class="hljs-built_in">console</span>.log(i);
    &#125;
    <span class="hljs-comment">//遍历对象实体 entries</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> set.entries()) &#123;
        <span class="hljs-built_in">console</span>.log(i[<span class="hljs-number">0</span>]);
    &#125;
    
    <span class="hljs-comment">//解构的方式遍历对象实体</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k, v] <span class="hljs-keyword">of</span> set.entries()) &#123;
        <span class="hljs-built_in">console</span>.log(k, v);
    &#125;
    <span class="hljs-comment">// for  each遍历 set</span>
    set.forEach(<span class="hljs-function"><span class="hljs-params">i</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(i);
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">es6 Map结构</h3>
<p>Map 结构 由于对象的属性只能接受字符串类型，所有产生了Map结构，优化对象结构, <strong>Map的Key能为任何属性</strong></p>
<pre><code class="hljs language-c copyable" lang="c">使用<span class="hljs-keyword">new</span> Map()实例化

方法：返回值是Map实例可以连缀
    <span class="hljs-built_in">set</span>(key,val)        加元素
    get(key)            取元素
    has(key)            判断是否包含元素     boolean
    clear()             删除所有数据
    
    <span class="hljs-comment">// 1.添加数据 set()</span>
    <span class="hljs-built_in">map</span>.<span class="hljs-built_in">set</span>(<span class="hljs-string">'name'</span>, <span class="hljs-string">'jack'</span>).<span class="hljs-built_in">set</span>(<span class="hljs-string">'age'</span>, <span class="hljs-number">22</span>).<span class="hljs-built_in">set</span>(<span class="hljs-number">0</span>,<span class="hljs-number">100</span>);
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>);
    <span class="hljs-comment">// 2.获取数据 get()</span>
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>.get(<span class="hljs-number">0</span>));        <span class="hljs-comment">//100</span>
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>.get(<span class="hljs-string">'name'</span>))    <span class="hljs-comment">//jack</span>
    <span class="hljs-comment">// 3.判断存在数据 has()</span>
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>.has(<span class="hljs-number">0</span>));        <span class="hljs-comment">//true</span>
    <span class="hljs-comment">// 4.删除数据 delete()</span>
    <span class="hljs-built_in">map</span>.<span class="hljs-keyword">delete</span>(<span class="hljs-number">0</span>);
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>);       <span class="hljs-comment">//Map(2) &#123;"name" => "jack", "age" => 22&#125;</span>
    <span class="hljs-comment">// 5.清空数据 clear()</span>
    <span class="hljs-built_in">map</span>.clear();
    console.<span class="hljs-built_in">log</span>(<span class="hljs-built_in">map</span>);       <span class="hljs-comment">//Map(0) &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Map结构规则</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1. map 支持数组作为构造函数的参数,但必须是二维数组</span>
<span class="hljs-comment">// let arr = [1, 2, 3, 4, 5];  //Iterator value 1 is not an entry object</span>
<span class="hljs-keyword">let</span> arr = [[<span class="hljs-string">'name'</span>, <span class="hljs-string">'jack'</span>], [<span class="hljs-string">'age'</span>, <span class="hljs-number">23</span>]];
<span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(arr);
<span class="hljs-built_in">console</span>.log(map);   <span class="hljs-comment">//Map(4) &#123;"name" => "jack", "age" => 23&#125;</span>

<span class="hljs-comment">// 2.key 不能重复，val可以重复, key如果重复会将原来的值覆盖</span>
map.set(<span class="hljs-string">'name'</span>,<span class="hljs-string">'tom'</span>);
map.set(<span class="hljs-string">'hob'</span>,<span class="hljs-string">'sing'</span>);
<span class="hljs-built_in">console</span>.log(map);   <span class="hljs-comment">//Map(5) &#123;"name" => "tom", "age" => 23, "hob" => "sing"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Map的遍历</strong></p>
<ul>
<li>let of 遍历map</li>
<li>forEach 遍历 map</li>
<li>let of 遍历map.keys</li>
<li>let of 遍历map.values</li>
<li>let of 遍历map.entries</li>
<li>let of 遍历 map.entries + 解构</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1.let of 遍历map</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> map) &#123;
        <span class="hljs-built_in">console</span>.log(i[<span class="hljs-number">0</span>], i[<span class="hljs-number">1</span>]);
    &#125;
   
    <span class="hljs-comment">// 2.foreach 遍历 map</span>
    map.forEach(<span class="hljs-function">(<span class="hljs-params">v, k</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(k, v);
    &#125;)
  
    <span class="hljs-comment">// 3.let of 遍历map.keys</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">of</span> map.keys()) &#123;
        <span class="hljs-built_in">console</span>.log(k, map.get(k));
    &#125;
    
    <span class="hljs-comment">// 4.let of 遍历map.values</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> v <span class="hljs-keyword">of</span> map.values()) &#123;
        <span class="hljs-built_in">console</span>.log(v);
    &#125;
    
    <span class="hljs-comment">// 5.let of 遍历map.entries</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> map.entries()) &#123;
        <span class="hljs-built_in">console</span>.log(i[<span class="hljs-number">0</span>], i[<span class="hljs-number">1</span>]);
    &#125;
    
    <span class="hljs-comment">// 6.let of 遍历 map.entries + 解构</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k, v] <span class="hljs-keyword">of</span> map.entries()) &#123;
        <span class="hljs-built_in">console</span>.log(k, v);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">es6 set与map类型转换</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Set</span> 和 数组
    <span class="hljs-number">1.</span>set -> 数组
        方式<span class="hljs-number">1.</span> <span class="hljs-built_in">Array</span>.from();
        方式<span class="hljs-number">2.</span> 遍历set然后push
        方式<span class="hljs-number">3.</span> 扩展运算符
    <span class="hljs-number">2.</span>数组 -> set
        方式<span class="hljs-number">1.</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr);
    


<span class="hljs-built_in">Map</span>  对象  string
    <span class="hljs-number">1.</span>map -> 对象 -> <span class="hljs-built_in">String</span>
        方式<span class="hljs-number">1.</span> forEach遍历<span class="hljs-built_in">Map</span> -> 对象 -> <span class="hljs-built_in">JSON</span>.stringify
    <span class="hljs-number">2.</span><span class="hljs-built_in">String</span> -> 对象 -> map
        方式<span class="hljs-number">1.</span> <span class="hljs-built_in">JSON</span>.parse -> 对象 -> <span class="hljs-keyword">for</span>...in 遍历对象 -> <span class="hljs-built_in">Map</span>.add()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Set 和 数组之间</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
set.add(<span class="hljs-number">1</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">3</span>).add(<span class="hljs-number">2</span>);
<span class="hljs-comment">// 1.Array.from();</span>
<span class="hljs-keyword">var</span> arr = <span class="hljs-built_in">Array</span>.from(set);
<span class="hljs-built_in">console</span>.log(arr);

<span class="hljs-comment">// 2.遍历set然后push</span>
<span class="hljs-keyword">var</span> arr  = [];
set.forEach(<span class="hljs-function"><span class="hljs-params">i</span>=></span>&#123;
    arr.push(i);
&#125;);
<span class="hljs-built_in">console</span>.log(arr);

<span class="hljs-comment">// 3.扩展运算符</span>
<span class="hljs-keyword">var</span> arr = [...set];
<span class="hljs-built_in">console</span>.log(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>map、对象和字符串之间</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'name'</span>, <span class="hljs-string">'jack'</span>).set(<span class="hljs-string">'age'</span>, <span class="hljs-number">22</span>).set(<span class="hljs-string">'tel'</span>, <span class="hljs-number">151</span>);

<span class="hljs-comment">// 1.map -> 对象 -> String</span>
<span class="hljs-keyword">var</span> obj = &#123;&#125;;
map.forEach(<span class="hljs-function">(<span class="hljs-params">v,k</span>)=></span>&#123;
    obj[k] = v;
&#125;)
<span class="hljs-built_in">console</span>.log(obj);
<span class="hljs-keyword">var</span> str = <span class="hljs-built_in">JSON</span>.stringify(obj);
<span class="hljs-built_in">console</span>.log(str);

<span class="hljs-comment">// 2.String -> 对象 -> map</span>
<span class="hljs-keyword">var</span> obj1 = <span class="hljs-built_in">JSON</span>.parse(str);
<span class="hljs-keyword">var</span> map1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> obj1)&#123;
    map1.set(i,obj1[i]);
&#125;
<span class="hljs-built_in">console</span>.log(map1);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">rest 和 扩展运算符区别</h3>
<p>rest参数，出现在函数参数位置
离散数据 -> 数组</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">...rest</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(rest);
&#125;
fn(<span class="hljs-number">100</span>, <span class="hljs-number">110</span>, <span class="hljs-number">120</span>);    <span class="hljs-comment">//(3) [100, 110, 120]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>⚠️**注意: **... 扩展 运算符出现在非参数位置
**</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-built_in">console</span>.log(...arr);    <span class="hljs-comment">//1 2 3 4 5  </span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>);     <span class="hljs-comment">//Arguments(3) [2, 3, 4]</span>
    <span class="hljs-built_in">console</span>.log(...arguments);  <span class="hljs-comment">//2 3 4</span>
&#125;
fn1(<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组 -> 离散的数据</li>
<li>拆分伪数组： NodeList  HTMLCollection  arguments...</li>
</ul>
<h3 data-id="heading-14">ES6 面向对象</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> 类、模板
1. 构造器：当类被实例化时，自动执行构造器
2. 每个类必须至少一个构造器，若没有，系统自动添加一个无参构造器
3. 构造函数，不能主动调用


<span class="hljs-title">set</span> 和 <span class="hljs-title">get</span> 设置和获取属性
1. <span class="hljs-title">get</span> 不能传递参数
2. 只有当有<span class="hljs-title">set</span>方法时才可以写<span class="hljs-title">get</span>方法，同时出现


静态方法：
1. 类自身的方法，不用实例化即可调用
2. 不会被实例继承,直接通过类来调用


静态属性：
1. 类名.属性名 </span>= 值;


<span class="hljs-keyword">extends</span> 实现继承
<span class="hljs-number">1.</span> 继承是单向的
<span class="hljs-number">2.</span> 被继承的类属于父类，基类，也称超类
<span class="hljs-number">3.</span> 静态方法可以被子类继承
<span class="hljs-number">4.</span> 继承属性<span class="hljs-built_in">super</span>()必须放在构造器第一句
<span class="hljs-number">5.</span> 一个父类可以有多个子类，一个子类只有一个父类


注意：
<span class="hljs-number">1.</span> 父类可调用自己的成员方法
<span class="hljs-number">2.</span> 父类可以调自己的静态方法
<span class="hljs-number">3.</span> 父类不能调子类的成员方法
<span class="hljs-number">4.</span> 子类的实例可以调父类成员方法
<span class="hljs-number">5.</span> 子类的实例不能调父类静态方法
<span class="hljs-number">6.</span> 子类可以调父类静态方法
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-keyword">static</span> name = <span class="hljs-string">"Ken"</span>;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">uname, uage</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.uname = uname;
    <span class="hljs-built_in">this</span>.uage = uage;
  &#125;

  <span class="hljs-comment">//成员方法</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.uname&#125;</span>正在奔跑！`</span>);
  &#125;

  <span class="hljs-comment">// 静态方法:类自身的方法</span>
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">cry</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'人生下来就会哭！'</span>);
  &#125;
&#125;

<span class="hljs-comment">// 静态属性</span>
Person.living = <span class="hljs-string">'earth'</span>;


<span class="hljs-comment">//学生类继承Person类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Student</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">sname, sage, sno</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(sname, sage);  <span class="hljs-comment">//此句必须在构造器第一句</span>
    <span class="hljs-built_in">this</span>.sno = sno;
  &#125;
  <span class="hljs-comment">// 成员方法</span>
  <span class="hljs-function"><span class="hljs-title">study</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.sname&#125;</span>在学习呢！`</span>);
  &#125;

  <span class="hljs-comment">//set 访问器 控制属性的设置</span>
  <span class="hljs-keyword">set</span> <span class="hljs-title">sage</span>(<span class="hljs-params">age</span>) &#123; <span class="hljs-built_in">this</span>._age=age&#125;
  <span class="hljs-comment">// get 访问器，获取属性</span>
  <span class="hljs-keyword">get</span> <span class="hljs-title">sage</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._age &#125;
&#125;
<span class="hljs-comment">//创建类的实例   类的实例化</span>
<span class="hljs-keyword">var</span> stu = <span class="hljs-keyword">new</span> Student(<span class="hljs-string">'王飒'</span>, <span class="hljs-number">23</span>, <span class="hljs-string">'001'</span>);
stu.sage = <span class="hljs-number">25</span>
<span class="hljs-built_in">console</span>.log(stu.sage);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">JS中的异常处理</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">try</span>..catch
<span class="hljs-keyword">try</span>..finally
<span class="hljs-keyword">try</span>...catch..finally
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">ES6 Promise 解决回调地狱</h3>
<p><strong>promise:为了解决异步编程中的回调地狱而产生</strong>
Promise的实例需要接收一个函数作为参数
该函数又需要接收两个函数数作为参数
resolve     函数
reject      函数</p>
<p><strong>promise 的三种状态</strong>
pending    进行中
fullfilled    已成功        resolved    成功    执行resolve函数
rejected    已失败      rejected    失败    执行reject函数</p>
<p><strong>then方法</strong>
参数一：是resolve函数的实现
参数二：是reject函数的实现</p>
<p><strong>then方法返回值的是一个新的Promise实例</strong>
<strong>⚠️注意</strong>，不是原来那个Promise实例
若前一个回调函数返回的是一个Promise对象（即有异步操作）时
后一个回调函数，会等待该Promise对象的状态发生变化，才会被调用</p>
<p><strong>promise的异常处理</strong></p>
<ol>
<li>建议总是使用catch方法。</li>
<li>Promise 对象的错误具有“冒泡”性质，会一直向后传递，直到被捕获为止。</li>
<li>Promise 的状态一旦改变，就永久保持该状态，不会再变了。</li>
<li>catch方法返回的还是一个 Promise 对象</li>
<li>catch和reject同时出现时，只执行reject</li>
</ol>
<p><strong>多个异步操作</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 加载图片函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadPic</span>(<span class="hljs-params">id, src, sec</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> oImg = <span class="hljs-keyword">new</span> Image();
        oImg.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            resolve(oImg);
        &#125;
        oImg.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            reject(<span class="hljs-string">`编号为<span class="hljs-subst">$&#123;id&#125;</span>的任务失败`</span>);
        &#125;
        <span class="hljs-comment">// oImg.src = src;</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            oImg.src = src;
        &#125;, sec);   <span class="hljs-comment">//延迟加载函数</span>
    &#125;)
&#125;
<span class="hljs-keyword">let</span> s1 = <span class="hljs-string">"远程图片"</span>;
<span class="hljs-keyword">let</span> s2 = <span class="hljs-string">"远程图片"</span>;
<span class="hljs-keyword">let</span> p1 = loadPic(<span class="hljs-string">'001'</span>, s1, <span class="hljs-number">1000</span>);
<span class="hljs-keyword">let</span> p2 = loadPic(<span class="hljs-string">'002'</span>, s2, <span class="hljs-number">100</span>);
<span class="hljs-comment">// Promise.all 方法</span>
<span class="hljs-comment">// 当所有图片都加载完在执行后续动作，有一张失败都不执行then</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-built_in">Promise</span>.all([p1, p2]);  <span class="hljs-comment">//all返回新的promise对象</span>
p.then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(data,<span class="hljs-string">'加载成功'</span>);
    <span class="hljs-built_in">document</span>.body.append(data[<span class="hljs-number">0</span>],data[<span class="hljs-number">1</span>]);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;).finally(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'不论成功与否，我都执行'</span>);
&#125;); 
<span class="hljs-comment">// Promise.race 方法</span>
<span class="hljs-comment">// 注：</span>
<span class="hljs-comment">//  1.只要有一张图片加载完成，就执行then的resolve实现</span>
<span class="hljs-comment">//  2.如果先加载的图片有失败的情况，后续图片就不加载，直接执行catch 或 reject</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-built_in">Promise</span>.race([p1, p2]);
p.then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data);      <span class="hljs-comment">//只返回最先加载成功的那个</span>
    <span class="hljs-built_in">document</span>.body.append(data);    <span class="hljs-comment">//由于设置了延迟，所以第二个先加载完成</span>
&#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">ES模块导入规则</h3>
<p><strong>容易出错的地方</strong></p>
<ol>
<li>页面不基于服务器运行，会出现跨域的错误</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">origin <span class="hljs-string">'null'</span> has been blocked by CORS policy: Cross origin requests are only
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用模块化时，页面不加type = "module" 会出现语法错误</li>
</ol>
<p>app.js:1 Uncaught SyntaxError: Unexpected token &#123;</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script src=<span class="hljs-string">"./module/app.js"</span> type=<span class="hljs-string">"module"</span>></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>import导入模块时不添加 .js 的后缀名会报找不到module错误</li>
</ol>
<p><em>GET xxx net::ERR_ABORTED 404 (Not Found)</em></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Student &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./Student.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>导出方式</strong></p>
<ul>
<li>定义时导出</li>
<li>批量导出</li>
<li>导出重命名（不建议）</li>
<li>默认导出</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 1.定义时导出</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">let</span> uname = <span class="hljs-string">'李四'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showStudentName</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(uname);
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SomeAnimalInfo</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">type, age</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.type = type;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;
  <span class="hljs-function"><span class="hljs-title">showInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`物种:<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.type&#125;</span>,年龄：<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>);
  &#125;
&#125;



<span class="hljs-comment">// 2.批量导出</span>
<span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415926</span>;
<span class="hljs-keyword">const</span> DBNAME = <span class="hljs-string">'Local'</span>;
    ... ...

<span class="hljs-keyword">export</span> &#123; PI, DBNAME &#125;;



<span class="hljs-comment">// 3.默认导出 - 工具类</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> </span>&#123;
  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">log</span>(<span class="hljs-params">msg</span>)</span> &#123;
    <span class="hljs-keyword">let</span> now = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;now.toLocaleString()&#125;</span>    <span class="hljs-subst">$&#123;msg&#125;</span>`</span>);
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">setCookie</span>(<span class="hljs-params"></span>)</span> &#123;

  &#125;
        ... ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>导入方式</strong></p>
<ul>
<li>导入重命名</li>
<li>导入整个模块</li>
<li>导入默认模块</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1.导入重命名  as语法</span>
<span class="hljs-keyword">import</span> &#123; num, showStudentName <span class="hljs-keyword">as</span> showName &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./all.js'</span>;

<span class="hljs-comment">// 2.导入整个模块   需要使用as重命名，接收的是一个对象</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> cons <span class="hljs-keyword">from</span> <span class="hljs-string">'./const.js'</span>;

<span class="hljs-comment">// 3.导入默认模块   需要起名，名字包含导出内容</span>
<span class="hljs-keyword">import</span> Tool <span class="hljs-keyword">from</span> <span class="hljs-string">'./tools.js'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">es7 语法</h2>
<h3 data-id="heading-19">async await转化es5</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncFN</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> getSyncFnResult = <span class="hljs-keyword">await</span> syncFn()
  <span class="hljs-built_in">console</span>.log(getSyncFnResult);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">syncFn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"这是syncFn()的结果"</span>;
&#125;

asyncFN()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转成es5后的代码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncGeneratorStep</span>(<span class="hljs-params">gen, resolve, reject, _next, _throw, key, arg</span>) </span>&#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">var</span> info = gen[key](arg); <span class="hljs-comment">//相当于 步骤标点1-fn['next']("这是syncFn()的结果")</span>
    <span class="hljs-keyword">var</span> value = info.value;
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    reject(error);
    <span class="hljs-keyword">return</span>;
  &#125;
  <span class="hljs-keyword">if</span> (info.done) &#123;
    resolve(value);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">Promise</span>.resolve(value).then(_next, _throw);
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_asyncToGenerator</span>(<span class="hljs-params">fn</span>) </span>&#123;
  <span class="hljs-comment">//其实步骤标点1-fn=function* () &#123;</span>
  <span class="hljs-comment">//   var getSyncFnResult = yield syncFn();</span>
  <span class="hljs-comment">//   console.log(getSyncFnResult);</span>
  <span class="hljs-comment">// &#125;</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> self = <span class="hljs-built_in">this</span>,
      args = <span class="hljs-built_in">arguments</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
      <span class="hljs-keyword">var</span> gen = fn.apply(self, args);
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_next</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"value"</span>, value);

        asyncGeneratorStep(gen, resolve, reject, _next, _throw, <span class="hljs-string">"next"</span>, value);
      &#125;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_throw</span>(<span class="hljs-params">err</span>) </span>&#123;
        asyncGeneratorStep(gen, resolve, reject, _next, _throw, <span class="hljs-string">"throw"</span>, err);
      &#125;
      _next(<span class="hljs-literal">undefined</span>);
    &#125;);
  &#125;;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">asyncFN</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> _asyncFN.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_asyncFN</span>(<span class="hljs-params"></span>) </span>&#123;
  _asyncFN = _asyncToGenerator(<span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> getSyncFnResult = <span class="hljs-keyword">yield</span> <span class="hljs-string">"这是syncFn()的结果"</span>;
    <span class="hljs-comment">// var getSyncFnResult = yield syncFn();</span>
    <span class="hljs-built_in">console</span>.log(getSyncFnResult);
  &#125;);

  <span class="hljs-keyword">return</span> _asyncFN.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
&#125;

<span class="hljs-comment">// function syncFn() &#123;</span>
<span class="hljs-comment">//   return "这是syncFn()的结果";</span>
<span class="hljs-comment">// &#125;</span>

asyncFN();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12afe75501294eeeab61c85333a8f130~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">参考文献</h2></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            