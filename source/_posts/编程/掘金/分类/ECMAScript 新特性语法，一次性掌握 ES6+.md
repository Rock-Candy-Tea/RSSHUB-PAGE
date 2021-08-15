
---
title: 'ECMAScript 新特性语法，一次性掌握 ES6+'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4021'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 22:58:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4021'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1 ECMAScript 和 JavaScript 概述</h2>
<pre><code class="copyable">浏览器端JavaScript: ECMAScript、BOM、DOM
node端的JavaScript：ECMAScript、nodeAPI

ECMA： 欧洲计算机标准协会
ECMAScript： 一套语法标准

ECMAScript是JavaScript的规格
JavaScript是ECMAScript的实现

ECMAScript的实现： JavaScript、JScript、ActionScript(flash)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">1.1 ECMAScript的重要版本</h3>
<pre><code class="copyable">ECMAScript3.0  简称ES3   
ES5.0 / ES5.1  新增一些扩展
ES6 2015年6月  又叫ES2015 (之后每年6月份出一个新的版本)
ES7 ES2016
ES8 ES2017
ES9 ES2018
ES10 ES2019
ES11 ES2020
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ECMA 参考文档 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://es6.ruanyifeng.com/" ref="nofollow noopener noreferrer">es6.ruanyifeng.com/</a></p>
</blockquote>
<h2 data-id="heading-2">2 关键字扩展</h2>
<h3 data-id="heading-3">2.1 let 关键字</h3>
<pre><code class="copyable">用于声明变量，类似于var
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">特点：
    ① 不能重复声明
    ② let声明的变量不会提升
    ③ let声明的变量可以具有块级作用域
    ④ let声明的全局变量不再是顶层对象的属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.2 let 与块级作用域</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 给三个按钮绑定单击事件，点击输出索引号</span>
<span class="hljs-keyword">let</span> btn = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'button'</span>)

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < btn.length; i++) &#123;
    btn[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 3 3 3</span>
    &#125;;
  &#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < btn.length; i++) &#123;
    btn[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">// 0 1 2</span>
    &#125;;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.3 const 关键字</h3>
<pre><code class="copyable">常量不可改变的量，用途：程序的配置信息习惯用常量定义
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">特点：
    ① 值不能修改，更不能重复声明
    ② 不会变量提升
    ③ 具有全局、局部、块级作用域
    ④ 全局的常量不是window的属性
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3 对象的简写</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> name = <span class="hljs-string">'小明'</span>
<span class="hljs-keyword">const</span> age = <span class="hljs-string">'18'</span>

<span class="hljs-comment">// 属性同名可简写</span>
<span class="hljs-keyword">const</span> obj = &#123;
  name
  age
  <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;   <span class="hljs-comment">//方法简写 </span>

  &#125;,
&#125;

<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123; name: '小明', age: '18' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">4 解构赋值</h2>
<h3 data-id="heading-8">4.1 数组解构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 解构声明</span>
<span class="hljs-keyword">const</span> [a, b, c] = [value1, value2, value3]

<span class="hljs-comment">// 2. 修改变量的值</span>
[a, b, c] = [value1, value2, value3]

<span class="hljs-comment">// 3 复杂数组 （保证两边的数组形式一致）</span>
<span class="hljs-keyword">const</span> [a, [b], [c, [d,e]]] = [<span class="hljs-number">100</span>, [<span class="hljs-number">200</span>], [<span class="hljs-number">300</span>, [<span class="hljs-number">400</span>, <span class="hljs-number">500</span>]]]

<span class="hljs-comment">// 4. 声明变量的时候可以有默认值 （与函数传参类似）</span>
<span class="hljs-keyword">const</span> [a, b, c, d = <span class="hljs-number">5</span>] = arr 
<span class="hljs-built_in">console</span>.log(d) <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">4.2 对象解构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 简写形式</span>
&#123;name, age&#125; = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>&#125; <span class="hljs-comment">//张三 ，18</span>

<span class="hljs-comment">// 对象形式</span>
<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'小明'</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
  <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>,
  <span class="hljs-attr">love</span>: &#123;
    <span class="hljs-attr">eat</span>: <span class="hljs-string">'吃饭'</span>,
    <span class="hljs-attr">sleep</span>: <span class="hljs-string">'睡觉'</span>,
    <span class="hljs-attr">peas</span>: <span class="hljs-string">'打豆豆'</span>,
  &#125;
&#125;

<span class="hljs-keyword">const</span> &#123; name, age, sex &#125; = obj
<span class="hljs-built_in">console</span>.log(name, age, sex) <span class="hljs-comment">// 小明 18 男</span>

<span class="hljs-comment">// 解构重名</span>
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">name</span>: myname &#125; = obj
<span class="hljs-built_in">console</span>.log(myname) <span class="hljs-comment">// 小明</span>

<span class="hljs-comment">// 嵌套解构</span>
<span class="hljs-keyword">const</span> &#123; <span class="hljs-attr">love</span>: &#123; sleep &#125; &#125; = obj
<span class="hljs-built_in">console</span>.log(sleep) <span class="hljs-comment">// 睡觉</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">5 字符串扩展</h2>
<h3 data-id="heading-11">5.1 模板字符串</h3>
<pre><code class="hljs language-js copyable" lang="js">两个反引号 <span class="hljs-string">``</span>
特点：
$&#123;变量&#125; 直接解析
$&#123;表达式&#125; 得到表达式的结果
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">5.2 字符串对象新增的方法</h3>
<h4 data-id="heading-13">① ES5</h4>
<pre><code class="copyable">trim() 去除两边的空格
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">② ES6+</h4>
<pre><code class="hljs language-js copyable" lang="js">startsWith() 返回布尔值 
endsWith()   返回布尔值
includes()   返回布尔值
repeat()
padStart()   ES8   补全  <span class="hljs-comment">//message.padStart(100, '#')</span>
padEnd()     ES8   补全  <span class="hljs-comment">//message.padEnd(100, '#')</span>
matchAll()   ES10  message.matchAll(<span class="hljs-regexp">/\w/</span>) <span class="hljs-comment">//返回迭代器（是所有匹配到的结果）</span>
trimStart()  ES10
trimEnd()    ES10
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">6 数值的扩展</h2>
<h3 data-id="heading-16">6.1 指数运算符 (**) ES7</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">2</span> ** <span class="hljs-number">4</span>;  <span class="hljs-comment">// 计算2的4次方</span>
<span class="hljs-number">2</span> ** <span class="hljs-number">2</span> ** <span class="hljs-number">3</span>； <span class="hljs-comment">// 运算顺序，先算右边的</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">6.2 二进制和八进制的表示</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 二进制</span>
<span class="hljs-number">0b101010</span>

<span class="hljs-comment">// 八进制</span>
<span class="hljs-number">0o17</span>

<span class="hljs-comment">// 比以前的八进制表示方式语法更合理，在严格模式可用（0开头表示八进制，严格模式不可用）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">6.3 Math对象新增的方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Math</span>.trunc()  去掉小数部分
<span class="hljs-built_in">Math</span>.sign()   判断一个数字是正数、负数、还是<span class="hljs-number">0</span>
<span class="hljs-built_in">Math</span>.cbrt()   求立方根
<span class="hljs-built_in">Math</span>.hypot()  求所有参数的平方和的平方根（用于勾股定理计算斜边长度）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">7 函数扩展</h2>
<h3 data-id="heading-20">7.1 参数默认值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ES6的写法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a,b=默认值</span>) </span>&#123;
    
&#125;

<span class="hljs-comment">// ES6之前的写法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">a,b</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (b === <span class="hljs-literal">undefined</span>) &#123;
        b = 默认值
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">7.2 rest参数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1、arguments获取实参</span>
<span class="hljs-comment">// function fn() &#123;</span>
<span class="hljs-comment">//    console.log(arguments);</span>
<span class="hljs-comment">// &#125;</span>

<span class="hljs-comment">// 2、rest参数获取</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">...numbers</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(numbers); <span class="hljs-comment">//得到一个数组，里面是所有的实参； numbers的名字只要符合标识名命名规范即可</span>
&#125;

与<span class="hljs-built_in">arguments</span>类似
rest参数得到是数组，<span class="hljs-built_in">arguments</span>得到是伪数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">7.3 箭头函数</h3>
<h4 data-id="heading-23">① 语法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以前定义函数的方式 （表达式方式）</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 箭头函数写法</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function">() =></span> &#123;&#125;

<span class="hljs-comment">// 箭头函数简写，如果参数只有一个，可以省略括号</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;&#125;

<span class="hljs-comment">// 只有一个参数，且只有一条返回语句</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function"><span class="hljs-params">num</span> =></span> num * num

<span class="hljs-comment">// 如果返回的是对象</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function"><span class="hljs-params">name</span> =></span> (&#123; <span class="hljs-attr">name</span>: name &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">② 特点</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> <span class="hljs-built_in">this</span>指向。 与谁调用了箭头函数无关,与声明箭头函数位置有关
   看声明箭头函数的地方，是不是嵌套在函数内，如果嵌套在了函数内，看外层函数的<span class="hljs-built_in">this</span>指向；如果没有被函数嵌套，指向<span class="hljs-built_in">window</span>
   
<span class="hljs-number">2.</span> 箭头函数内无法获取aruguments，可以使用rest参数

<span class="hljs-number">3.</span> 箭头函数不能作为构造函数

<span class="hljs-number">4.</span> 箭头函数不能作为生成器
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">③ 适用场景</h4>
<pre><code class="copyable">使用场景：
    作为回调函数
    
不适合的场景：
    给对象添加方法（this指向）
    构造函数
    生成器函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">7.4 函数对象新增属性</h3>
<pre><code class="copyable">name  返回函数名（声明函数时给的名字）
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">8 数组扩展</h2>
<h3 data-id="heading-28">8.1 扩展运算符</h3>
<h4 data-id="heading-29">① 定义</h4>
<pre><code class="copyable">rest参数的逆运算 把数组转为用逗号分隔的参数序列
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">② 应用</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> nums = [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>, <span class="hljs-number">250</span>];
<span class="hljs-built_in">console</span>.log(...nums); <span class="hljs-comment">// 100 200 300 250</span>

<span class="hljs-comment">// 1. call 数组传参</span>
fn.call(&#123;&#125;, ...nums);
fn.apply(&#123;&#125;, nums);

<span class="hljs-comment">// 2. 计算数组中最大的元素</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.max(...nums));

<span class="hljs-comment">// 3. 把一个数组的成员 追加到另一个数组的尾部</span>
<span class="hljs-keyword">const</span> names = [<span class="hljs-string">'曹操'</span>, <span class="hljs-string">'张仁'</span>, <span class="hljs-string">'刘备'</span>];
nums.push(...names); <span class="hljs-comment">// nums, push('曹操', '张仁', '刘备')</span>
<span class="hljs-built_in">console</span>.log(nums);   <span class="hljs-comment">//[100, 200, 300, 250, "曹操", "张仁", "刘备"]</span>

<span class="hljs-comment">// 4. 克隆数组</span>
<span class="hljs-comment">// const nums1 = nums;  //引用类型</span>
<span class="hljs-keyword">const</span> nums1 = [...nums];  <span class="hljs-comment">//克隆版</span>
nums1[<span class="hljs-number">2</span>]= <span class="hljs-string">'啦啦啦'</span>;
<span class="hljs-built_in">console</span>.log(nums1); <span class="hljs-comment">//[100, 200, "啦啦啦", 250, "曹操", "张仁", "刘备"]</span>
<span class="hljs-built_in">console</span>.log(nums);  <span class="hljs-comment">//[100, 200, 300, 250, "曹操", "张仁", "刘备"]</span>

<span class="hljs-comment">// 5. 合并数组</span>
<span class="hljs-keyword">const</span> newArr = [...nums, ...nums1, ...names];
<span class="hljs-built_in">console</span>.log(newArr);

<span class="hljs-comment">// 6. 把字符串和类数组对象转为数组</span>
<span class="hljs-comment">// 字符串转换为数组</span>
<span class="hljs-keyword">const</span> newArr1 = [...<span class="hljs-string">'hello'</span>];
<span class="hljs-built_in">console</span>.log(newArr1); <span class="hljs-comment">// ["h", "e", "l", "l", "o"]</span>

<span class="hljs-comment">// 7. 类数组对象转为数组</span>
<span class="hljs-keyword">const</span> btns = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'button'</span>);
<span class="hljs-built_in">console</span>.log(btns); 
<span class="hljs-built_in">console</span>.log([...btns]); 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">③ 解构赋值版的rest参数</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 与解构赋值一起使用 （解构赋值版的rest参数）</span>
<span class="hljs-keyword">const</span> [a, ...b] = [<span class="hljs-number">10</span>,<span class="hljs-number">20</span>,<span class="hljs-number">30</span>,<span class="hljs-number">40</span>,<span class="hljs-number">50</span>,<span class="hljs-number">50</span>,<span class="hljs-number">60</span>];
<span class="hljs-built_in">console</span>.log(a, b);  <span class="hljs-comment">// a是10， b是数组[20, 30, 40, 50, 50, 60]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">8.2 Array函数新增方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.from()   把类数组/字符串转为纯数组
<span class="hljs-built_in">Array</span>.of()     创建数组，参数是数组的成员（任意个数的参数）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">8.3 Array实例新增的方法</h3>
<pre><code class="copyable">find()          参数是回调函数，返回第一个满足条件的元素
findIndex()参数是回调函数，返回第一个满足条件的元素的索引
fill()填充数组，覆盖数组中所有的元素；适合填充 new Array（20）创建的数组
includes()      判断数组中是否包含某个元素，返回布尔值； ES7新增的
flat()          把数组拉平（多维数组变为一维数组），参数默认是1（只拉1层）， 可设置Infinity，不论维位数租  ES10新增
flatMap()参数是回调函数，相当于map和flat的结合 ES10新增
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-34">9 对象的扩展</h2>
<h3 data-id="heading-35">9.1 属性名表达式</h3>
<pre><code class="copyable">&#123;
    [表达式]:值,
     属性名: 值
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-36">9.2 super 关键字</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> <span class="hljs-built_in">super</span>指向调用该函数的实例的原型 
<span class="hljs-number">2.</span> 只有对象的方法中才有<span class="hljs-built_in">super</span>关键字，且简写形式定义的方法
&#123;
    <span class="hljs-function"><span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">super</span>; <span class="hljs-comment">//得到super</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">9.3 对象的扩展运算符 ... (ES9新增)</h3>
<pre><code class="copyable">定义：把对象转为用逗号分隔的键值对序列

作用：对象的解构赋值,对象操作（对象合并、对象克隆）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定义对象</span>
 <span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'曹操'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">100</span>,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'My Name is '</span> + <span class="hljs-built_in">this</span>.name);
    &#125;,
  &#125;;

<span class="hljs-built_in">console</span>.log(&#123; ...obj &#125;);
<span class="hljs-comment">// 相当于</span>
<span class="hljs-built_in">console</span>.log(name:<span class="hljs-string">'曹操'</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">100</span>, <span class="hljs-attr">say</span>:fn);

<span class="hljs-comment">// 对象克隆 (浅克隆)</span>
<span class="hljs-keyword">const</span> obj2 = &#123; ...obj &#125;;
obj2.name = <span class="hljs-string">'刘备'</span>;
<span class="hljs-built_in">console</span>.log(obj2);<span class="hljs-comment">// &#123;name: "刘备", age: 100, say: ƒ&#125;</span>
<span class="hljs-built_in">console</span>.log(obj); <span class="hljs-comment">// &#123;name: "曹操", age: 100, say: ƒ&#125;</span>

<span class="hljs-comment">// 对象合并 如果有重名属性，后面覆盖前面的</span>
<span class="hljs-keyword">const</span> obj3 = &#123; <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">height</span>: <span class="hljs-number">200</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'孙权'</span> &#125;;
<span class="hljs-keyword">const</span> obj4 = &#123; ...obj, ...obj3 &#125;;
<span class="hljs-built_in">console</span>.log(obj4); <span class="hljs-comment">// &#123;name: "孙权", age: 100, width: 100, height: 200, say: ƒ&#125;</span>

<span class="hljs-comment">// 用于对象的解构赋值</span>
<span class="hljs-keyword">const</span> &#123; age, ...b &#125; = obj;
<span class="hljs-built_in">console</span>.log(age); <span class="hljs-comment">// 100</span>
<span class="hljs-built_in">console</span>.log(b);   <span class="hljs-comment">// &#123;name: "曹操", say: ƒ&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">9.4 Object函数新增的方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.is()  用于比较两个数据是否相等，返回布尔值； 类似于全等，不同点<span class="hljs-literal">NaN</span>和Nan相等、+<span class="hljs-number">0</span>和-<span class="hljs-number">0</span>不相等
<span class="hljs-built_in">Object</span>.assign()  合并对象
<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptor()    获取某个自身属性的描述信息
<span class="hljs-built_in">Object</span>.getOwnProppertyDescriptors()  获取对象所有自身属性的描述信息  ES8新增
<span class="hljs-built_in">Object</span>.getPrototypeOf()     获取对象的原型
<span class="hljs-built_in">Object</span>.setPrototypeOf()     给对象设置原型
<span class="hljs-built_in">Object</span>.keys()     返回数组，由对象的属性名组成。
<span class="hljs-built_in">Object</span>.values()   返回数组，由对象的属性值组成。 ES8新增
<span class="hljs-built_in">Object</span>.entries()  返回二维数组，由属性名和属性值 组成  ES8新增
<span class="hljs-built_in">Object</span>.getOwnPropertyNames()   返回数组，有对象的属性名组成
<span class="hljs-built_in">Object</span>.formEntries()   <span class="hljs-built_in">Object</span>.entries（）的逆运算  ES8新增
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-39">10 Class语法</h2>
<h3 data-id="heading-40">10.1 定义类(构造函数)</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">// 定义类</span>
  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    <span class="hljs-comment">// 属性，会添加到实例上</span>
    <span class="hljs-comment">// 把所有的属性在这里声明</span>
    name = <span class="hljs-literal">null</span>;
    age = <span class="hljs-literal">null</span>;

    <span class="hljs-comment">// 定义构造方法 实例化的时候自动执行</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name, age = <span class="hljs-number">10</span></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.name = name;
      <span class="hljs-built_in">this</span>.age = age;
    &#125;

    <span class="hljs-comment">// 方法，添加到原型上</span>
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'MY Name is '</span> + <span class="hljs-built_in">this</span>.name);
    &#125;
    <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'My age is '</span> + <span class="hljs-built_in">this</span>.age);
    &#125;

    <span class="hljs-comment">// 静态方法 没有添加到实例上,构造函数本身的方法</span>
    <span class="hljs-comment">// static getClassName() &#123;</span>
    <span class="hljs-comment">//   console.log('类名是 Person 构造函数本身的方法');</span>
    <span class="hljs-comment">// &#125;</span>
  &#125;
  <span class="hljs-comment">//   Person.getClassName(); // 相当于 Person.getClassName = function()&#123;&#125;</span>

  <span class="hljs-built_in">console</span>.log(Person); <span class="hljs-comment">//输出整个函数</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> Person); <span class="hljs-comment">// Function</span>
  <span class="hljs-built_in">console</span>.log(Person.name); <span class="hljs-comment">// Person ===> name指的是这个对象的名字</span>

  <span class="hljs-comment">// 不能调用</span>
  <span class="hljs-comment">// Person();</span>

  <span class="hljs-comment">// 实例化</span>
  <span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'曹操'</span>, <span class="hljs-number">19</span>);
  <span class="hljs-built_in">console</span>.log(p); <span class="hljs-comment">// Person &#123;name: "曹操", age: 19&#125;</span>
  p.say(); <span class="hljs-comment">// MY Name is 曹操</span>

  <span class="hljs-keyword">var</span> p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'吕布'</span>, <span class="hljs-number">21</span>);
  <span class="hljs-built_in">console</span>.log(p1); <span class="hljs-comment">// Person &#123;name: "吕布", age: 21&#125;</span>
  p1.say(); <span class="hljs-comment">// MY Name is 吕布</span>

  <span class="hljs-keyword">var</span> p2 = <span class="hljs-keyword">new</span> Person();
  <span class="hljs-built_in">console</span>.log(p2); <span class="hljs-comment">// Person &#123;name: undefined, age: 10&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong></p>
<p>class定义的类 本质还是个函数，但是不能被调用，只能被实例化</p>
<p>typeof 类名 === 'funciton'</p>
</blockquote>
<h3 data-id="heading-41">10.2 实例化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> 类名;
<span class="hljs-keyword">new</span> 类名(构造方法的参数);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>注意：</strong></p>
<p>① 类中定义的属性会添加到实例上</p>
<p>② 类中定义的方法会添加到原型上</p>
</blockquote>
<h3 data-id="heading-42">10.3 静态方法</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span></span>&#123;
    <span class="hljs-keyword">static</span> 方法名() &#123;
    
    &#125;
&#125;

Person.方法名()

<span class="hljs-comment">// 静态方法没有添加给实例，添加给构造函数（类）本身</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-43">10.4 getter 和 setter</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
    firstName = <span class="hljs-string">'东方'</span>;
    lastName = <span class="hljs-string">'不败'</span>;

    <span class="hljs-keyword">get</span> <span class="hljs-title">fullName</span>() &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.firstName + <span class="hljs-string">'_'</span> + <span class="hljs-built_in">this</span>.lastName;
    &#125;

    <span class="hljs-keyword">set</span> <span class="hljs-title">fullName</span>(<span class="hljs-params">val</span>) &#123;
      <span class="hljs-keyword">const</span> name = val.split(<span class="hljs-string">'_'</span>);
      <span class="hljs-built_in">this</span>.firstName = name[<span class="hljs-number">0</span>];
      <span class="hljs-built_in">this</span>.lastName = name[<span class="hljs-number">1</span>];
    &#125;
  &#125;

  <span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person();
  <span class="hljs-built_in">console</span>.log(p); <span class="hljs-comment">//Person &#123;firstName: "东方", lastName: "不败"&#125;</span>

  <span class="hljs-built_in">console</span>.log(p.fullName); <span class="hljs-comment">//可读可写 东方_不败</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">10.5 继承</h3>
<pre><code class="copyable">1. 使用 extends 来继承
2. 继承之后：
    子类的实例的原型指向父类的一个实例
    子类自己的原型指向父类 (静态方法也可以继承)
3. 可以在子类上添加属性和方法
4. 在子类上重写父类的方法，子类重写的方法必须调用super()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> 子类 <span class="hljs-keyword">extends</span> 父类 </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-45">11 新增的数据类型（原始类型）</h2>
<h3 data-id="heading-46">11.1 Symbol</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 创建一<span class="hljs-built_in">Symbol</span>数据(只能调用，不能实例化)
    <span class="hljs-built_in">Symbol</span>()
    
<span class="hljs-number">2.</span> symbol数据特点：
    ① 每创建一个symbol类型的数据，都是唯一的。
    ② symbol类型的数据可以作为属性名，同字符串一样
    
<span class="hljs-number">3.</span> 应用：
    给对象添加属性（不会被覆盖）
    
<span class="hljs-number">4.</span> 注意：(可以作为对象的属性名，（字符串）symbol创建的都是唯一的)
    <span class="hljs-keyword">for</span>...in、<span class="hljs-built_in">Object</span>.keys()、<span class="hljs-built_in">Object</span>.values()、<span class="hljs-built_in">Object</span>.entries()、<span class="hljs-built_in">Object</span>.getOwnPropertyNames()  这些方法都取不到属性名时<span class="hljs-built_in">Symbol</span>类型的属性
    <span class="hljs-built_in">Object</span>.getOwnPropertySymbols()  获取类型是symbol的属性名
    <span class="hljs-built_in">Reflect</span>.ownKeys(obj)  获取对象自身所有的属性（不论属性名时什么类型）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-47">11.2 BigInt （ES10）</h3>
<h4 data-id="heading-48">① 安全数</h4>
<pre><code class="hljs language-js copyable" lang="js">通过 <span class="hljs-built_in">Number</span>.MAX_SAFE_INTEGER 和 <span class="hljs-built_in">Number</span>.MIN_SAFE_INTEGER  两个属性获得
如果整数超过了这个范围，无法按照整型的方式存储，计算会造成不精确
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-49">② BigInt类型</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1. 字面量</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">100n</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a); <span class="hljs-comment">//bigint</span>

<span class="hljs-comment">// 2 转换函数</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-built_in">BigInt</span>(<span class="hljs-number">1000</span>)
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">//1000n</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">bigInt类型的数据适合比较大的数字运算
bigInt类型的数据只能和<span class="hljs-built_in">BigInt</span>类型的数据运算,不能和number类型数据 相互运算
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-50">12 Set 和 Map</h2>
<h3 data-id="heading-51">12.1 Set</h3>
<h4 data-id="heading-52">① 描述</h4>
<pre><code class="copyable">无序且不重复的多个值的 集合
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">② 创建一个Set类型的数据</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(); <span class="hljs-comment">//创建的是空的Set</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(数组); <span class="hljs-comment">//把数组变为Set，去掉重复的值</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(类数组)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-54">③ Set实例的方法</h4>
<pre><code class="copyable">add(value)      添加一个值
delete(value)   删除一个值
has(value)      判断是否存在某个值
clear()         删除所有的值
keys()          返回遍历器
values()        返回遍历器
entries()       返回遍历器
forEach()       用于遍历
size 属性  获取Set成员的个数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-55">④ Set应用</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 实现数组去重
<span class="hljs-keyword">const</span> arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">100</span>, <span class="hljs-number">200</span>, <span class="hljs-number">300</span>, <span class="hljs-number">400</span>, <span class="hljs-number">300</span>, <span class="hljs-number">500</span>, <span class="hljs-number">500</span>, <span class="hljs-number">500</span>]);
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//Set(5) &#123;100, 200, 300, 400, 500&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-56">12.2 Map</h3>
<h4 data-id="heading-57">① 描述</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>对象是一种键值对(key-value)的集合，属性名就是键（key）,属性值就是值（value） 
<span class="hljs-built_in">Map</span>类似于对象，也是键值对的集合，对象的Key只能是字符串和<span class="hljs-built_in">Symbol</span>类型，<span class="hljs-built_in">Map</span>的Key可以是任意类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-58">② 创建Map</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建空的</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-comment">// 创建的时候，指定初始值</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
    [key,value],
    [key,value]
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">③ Map实例的方法</h4>
<pre><code class="copyable">get(key)        获取指定key的值
set(key,value)  设置或添加某个key的值
delete(key)     删除指定的某个key和他值
clear()         清空所有
has(key)        判断某个key是否存在
keys()          返回遍历器，所有key的集合
values()        返回遍历器，所有值的集合
entries()       返回遍历器，所有key-value的集合（二维）
forEach()       用于遍历
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-60">13.2 iterable 可遍历对象</h3>
<h4 data-id="heading-61">① 什么是 iterable 可遍历对象</h4>
<pre><code class="hljs language-js copyable" lang="js">把部署了 iterator 接口的数据结构，称之为<span class="hljs-string">'iterable'</span>（可遍历对象）
可以使用 <span class="hljs-keyword">for</span>...of 遍历 iterable对象

iterator接口部署在了数据结构的<span class="hljs-built_in">Symbol</span>.iterator属性上
一个对象，只有具有<span class="hljs-built_in">Symbol</span>.iterator属性，且该属性指向一个返回遍历器的函数，该对象就是
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-62">② 原生实现了iterator接口的数据结构 （可遍历对象）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>
<span class="hljs-built_in">Set</span>
<span class="hljs-built_in">Map</span>
<span class="hljs-built_in">String</span>
Arguments
NodeList
HTMLcollection
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-63">14 generator 生成器</h2>
<h3 data-id="heading-64">14.1 什么是生成器</h3>
<pre><code class="copyable">生成器就是生成遍历器的函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-65">14.2 定义生成器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>* 生成器名(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">yield</span> 值;
     <span class="hljs-keyword">yield</span> 值;
     <span class="hljs-keyword">yield</span> 值;
     <span class="hljs-keyword">yield</span> 值;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-66">14.3 yield 关键字</h3>
<pre><code class="hljs language-js copyable" lang="js">yeild关键返回一个值， 遍历的时候每次得到就是<span class="hljs-keyword">yield</span>的值
调用next(),执行到<span class="hljs-keyword">yield</span>就会停止； 下一次调用next(),执行到下一个<span class="hljs-keyword">yield</span>停止
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>调用生成器函数的时候，函数内不会执行</p>
<p>当调用next()的时候，才开始执行生成器函数内的代码； 执行到yield停止</p>
</blockquote>
<h3 data-id="heading-67">14.4 使用生成器函数给对象部署iterator接口</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'曹操'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
    <span class="hljs-attr">score</span>: <span class="hljs-number">80</span>,
    <span class="hljs-attr">height</span>: <span class="hljs-number">170</span>
&#125;;

<span class="hljs-comment">// 把obj变为一个 iterable</span>
<span class="hljs-comment">// 部署iterator接口</span>
obj[<span class="hljs-built_in">Symbol</span>.iterator] = <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> obj) &#123;
        <span class="hljs-keyword">yield</span> [i, obj[i]];
    &#125;
&#125;;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> obj) &#123;
    <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">//可遍历对象</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-68">15 模块</h2>
<h3 data-id="heading-69">15.1 模块中导出数据</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 模块内部</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">say</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eat</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-keyword">export</span> &#123;
    say,
    eat
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-70">15.2 导入模块</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;say, eat&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'模块文件路径'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-71">16 总结</h2>
<h3 data-id="heading-72">16.1 ECMAScript中数据类型</h3>
<pre><code class="hljs language-js copyable" lang="js">原始类型（值类型）： string、number、boolean、<span class="hljs-literal">null</span>、<span class="hljs-literal">undefined</span>、symbol、bigint
对象类型（引用类型）： array、object、regexp、set、map......
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">16.2 ECMAScript中声明变量的方式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1</span>、 <span class="hljs-keyword">var</span>
<span class="hljs-number">2</span>、 <span class="hljs-function"><span class="hljs-keyword">function</span>
3、 <span class="hljs-title">let</span>
4、 <span class="hljs-title">const</span> (<span class="hljs-params">常量</span>)
5、 <span class="hljs-title">class</span>
6、 <span class="hljs-title">import</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-74">16.3 实现数组扁平化的方式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [[<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>],[<span class="hljs-number">10</span>, [<span class="hljs-number">100</span>, <span class="hljs-number">200</span>]],[[<span class="hljs-string">'A'</span>, <span class="hljs-string">'B'</span>],[<span class="hljs-string">'一'</span>, <span class="hljs-string">'二'</span>],],<span class="hljs-number">1000</span>,];

  <span class="hljs-comment">//方式一</span>
  <span class="hljs-comment">//console.log(arr.flat(Infinity)); //["a", "b", 10, 100, 200, "A", "B", "一", "二", 1000]</span>

  <span class="hljs-comment">//方式二 利用字符串的join方法  缺点：数组的元素都会变为字符串类型</span>
  <span class="hljs-comment">//const arr2 = arr.join().split(',');</span>
  <span class="hljs-comment">//console.log(arr2); //["a", "b", "10", "100", "200", "A", "B", "一", "二", "1000"]</span>

  <span class="hljs-comment">//方式三： 递归</span>
  <span class="hljs-built_in">console</span>.log(flatArray(arr));

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatArray</span>(<span class="hljs-params">array</span>) </span>&#123;
    <span class="hljs-comment">//创建一个空数组</span>
    <span class="hljs-keyword">let</span> res = [];
    <span class="hljs-comment">// 遍历传进来的数组</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
      <span class="hljs-comment">//判断数组的元素还是不是数组</span>
      <span class="hljs-keyword">if</span> (array[i] <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) &#123;
        res = res.concat(flatArray(array[i])); <span class="hljs-comment">//继续调用把返回值拼起来，然后再赋值给res</span>
        <span class="hljs-comment">// res = [...res, ...flatArray(arr[i])];</span>
        <span class="hljs-comment">// res = res.concat(arguments.callee(arr[i]));</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.push(array[i]); <span class="hljs-comment">//添加一个数组</span>
      &#125;
    &#125;
    <span class="hljs-comment">//返回新数组</span>
    <span class="hljs-keyword">return</span> res;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-75">16.4 实现数组对象拷贝（克隆）的方式 （浅拷贝）</h3>
<pre><code class="hljs language-js copyable" lang="js">数组<span class="hljs-built_in">Array</span>:
<span class="hljs-number">1.</span> [...arr]
<span class="hljs-number">2.</span> arr.concat()  不写参数 数组合并方式
<span class="hljs-number">3.</span> arr.splice(<span class="hljs-number">0</span>) / arr.substring(<span class="hljs-number">0</span>) / arr.substr(<span class="hljs-number">0</span>)  数组截取方式

对象<span class="hljs-built_in">Object</span>:
<span class="hljs-number">1.</span> &#123;...obj&#125;
<span class="hljs-number">2.</span> <span class="hljs-built_in">Object</span>.assign(obj)   对象合并方式
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-76">16.5 实现对象的深度克隆（深拷贝）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sons = [<span class="hljs-string">'曹丕'</span>, <span class="hljs-string">'曹植'</span>, <span class="hljs-string">'曹冲'</span>];
<span class="hljs-keyword">let</span> sister = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'曹芹'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;

  <span class="hljs-keyword">const</span> obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'曹操'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">100</span>,
    sons,
    sister,
    <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
    <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;&#125;,
  &#125;;
  <span class="hljs-comment">// 1. 借助于JSON，无法拷贝方法，适合于纯数据对象</span>
  <span class="hljs-comment">// JSON.parse(JSON.stringify(obj));</span>

  <span class="hljs-comment">// 2. 使用递归函数 实现深度克隆</span>
  <span class="hljs-keyword">let</span> obj1 = deepClone(obj);
  obj1.sister.name = <span class="hljs-string">'曹雪芹'</span>;
  <span class="hljs-built_in">console</span>.log(obj);
  <span class="hljs-built_in">console</span>.log(obj1);

  <span class="hljs-comment">//定义函数 获取对象的构造函数（类）名</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getObjectClass</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(obj).slice(<span class="hljs-number">8</span>, -<span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-comment">//深拷贝的函数</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepClone</span>(<span class="hljs-params">obj</span>) </span>&#123;
    <span class="hljs-comment">//判断obj是对象是数组还是其他</span>
    <span class="hljs-keyword">if</span> (getObjectClass(obj) === <span class="hljs-string">'Object'</span>) &#123;
      <span class="hljs-keyword">var</span> res = &#123;&#125;; <span class="hljs-comment">//创建空的对象</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (getObjectClass(obj) === <span class="hljs-string">'Array'</span>) &#123;
      <span class="hljs-keyword">var</span> res = []; <span class="hljs-comment">//创建空数组</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> obj;
    &#125;

    <span class="hljs-comment">//对传入的对象(遍历)进行遍历</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> obj) &#123;
      res[i] = deepClone(obj[i]);
    &#125;
    <span class="hljs-comment">//返回新数组或对象</span>
    <span class="hljs-keyword">return</span> res;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-77">16.6 遍历对象属性的方式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> <span class="hljs-keyword">for</span> ... <span class="hljs-keyword">in</span>  遍历自身以及原型上可以被遍历的属性,属性名是symbol类型不可以
<span class="hljs-number">2.</span> <span class="hljs-built_in">Object</span>.keys()、<span class="hljs-built_in">Object</span>.value()、<span class="hljs-built_in">Object</span>.entries()    自身的属性，属性名是symbol类型不可以
<span class="hljs-number">3.</span> <span class="hljs-built_in">Object</span>.getOwnPropertyNames()     自身属性名的集合， 属性名是symbol类型不可以
<span class="hljs-number">4.</span> <span class="hljs-built_in">Object</span>.getOwnPropertySymbols()   自身属性名时symbol类型的属性名的集合
<span class="hljs-number">5.</span> Reflec.ownKeys()                 自身所有的属性名的集合 （字符串和symbol都可以）
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-78">16.7 Promise 对象</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// promise对象状态：成功 -> 触发then的第一个回调</span>
<span class="hljs-comment">// promise对象状态：失败 -> 触发then的第二个回调</span>

<span class="hljs-comment">// then(onFulfilled, onRejected)</span>
<span class="hljs-comment">// 传了两个函数，这两个仅会执行一个</span>

<span class="hljs-comment">// then方法默认返回值 成功状态promise对象</span>
<span class="hljs-comment">// 什么时候会返回失败状态promise对象呢？</span>
<span class="hljs-comment">//     1. 方法中函数的返回值是一个失败状态的promise对象</span>
<span class="hljs-comment">//     2. 方法报错</span>
<span class="hljs-comment">//   除了以上两个方式，默认就是成功promise</span>

<span class="hljs-keyword">const</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-comment">// 同步调用</span>
  resolve();
  <span class="hljs-comment">// reject();</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">111</span>);
&#125;);

promise
  .then(
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">222</span>);
    &#125;,
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">333</span>);
      <span class="hljs-comment">// 返回一个失败状态promise对象</span>
      <span class="hljs-comment">// return Promise.reject();</span>
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        reject();
      &#125;);
      <span class="hljs-comment">// 报错</span>
      <span class="hljs-comment">// 抛异常（立即产生一个错误）</span>
      <span class="hljs-comment">// throw 'error';</span>
    &#125; <span class="hljs-comment">// 默认返回成功状态promise对象</span>
  )
  <span class="hljs-comment">// 下一个then触发哪个？看上一个then的返回值promise状态</span>
  .then(
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">444</span>);
    &#125;,
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">555</span>);
    &#125;
  );

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">666</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-79">16.8 Promise 对象其它状态</h3>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-comment">//   Promise 一个异步编程的解决方案</span>
  <span class="hljs-comment">//   作用：用来解决异步回调地狱问题（消除回调函数，以同步方式表达异步代码）</span>

  <span class="hljs-comment">//   特点：</span>
  <span class="hljs-comment">//     状态：</span>
  <span class="hljs-comment">//       1. pending 初始化状态</span>
  <span class="hljs-comment">//       2. resolved / fulfilled 成功状态</span>
  <span class="hljs-comment">//       3. rejected 失败状态</span>

  <span class="hljs-comment">//       注意：</span>
  <span class="hljs-comment">//         同一时间，只能是一个状态</span>
  <span class="hljs-comment">//         只能由初始化状态变成成功/失败状态</span>
  <span class="hljs-comment">//         不能由成功变成失败，也不能由失败变成成功</span>
  <span class="hljs-comment">//         （状态初始化为pending，只能改变一次，要么成功，要么失败）</span>
  <span class="hljs-comment">//       怎么判断promise对象的状态？</span>
  <span class="hljs-comment">//         then() / catch()</span>

  <span class="hljs-comment">//     结果值：内部的结果值(value/reason)</span>
  <span class="hljs-comment">//       resolve(value)</span>
  <span class="hljs-comment">//       reject(reason)</span>
  <span class="hljs-comment">//       怎么得到promise对象内部的结果值？</span>
  <span class="hljs-comment">//         then((value) => &#123;&#125;) / await</span>
  <span class="hljs-comment">//         catch((reason) => &#123;&#125;)</span>

  <span class="hljs-comment">//     怎么创建promise对象？</span>
  <span class="hljs-comment">//       new Promise()  默认是pending</span>
  <span class="hljs-comment">//       Promise.resolve() 默认是resolved</span>
  <span class="hljs-comment">//       Promise.reject() 默认是rejected</span>

  <span class="hljs-comment">//     其他方法：</span>
  <span class="hljs-comment">//       Promise.all([promise1, promise2...])</span>
  <span class="hljs-comment">//         返回值是一个新的promise对象，新promise对象状态看传入的promise</span>
  <span class="hljs-comment">//           如果传入的promise状态都是成功的状态，新promise也成功</span>
  <span class="hljs-comment">//           如果传入的promise状态有一个失败，新promise立即失败</span>
  
  <span class="hljs-comment">//       Promise.race([promise1, promise2...])</span>
  <span class="hljs-comment">//         返回值是一个新的promise对象，新promise对象状态看传入的promise</span>
  <span class="hljs-comment">//           只看传入的n个promise，哪一个传入promise状态先发生变化</span>
  <span class="hljs-comment">//           新promise和先发生变化promise的状态一致</span>
  
  <span class="hljs-comment">//       Promise.allSettled([promise1, promise2...])  源自ES11/ES2020</span>
  <span class="hljs-comment">//         返回值是一个新的promise对象，一定是成功状态</span>
  <span class="hljs-comment">//           promise对象内部状态值，包含传入的n个promise对象的状态值</span>

  <span class="hljs-keyword">const</span> promise11 = <span class="hljs-built_in">Promise</span>.resolve();
  <span class="hljs-keyword">const</span> promise22 = <span class="hljs-built_in">Promise</span>.reject();

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功状态'</span>, promise11); <span class="hljs-comment">//成功状态 Promise &#123;<fulfilled>: undefined&#125;</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'失败状态'</span>, promise22); <span class="hljs-comment">//失败状态 Promise &#123;<rejected>: undefined&#125;</span>

  <span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      reject(<span class="hljs-number">111</span>);
    &#125;, <span class="hljs-number">1000</span>);
  &#125;);

  <span class="hljs-keyword">const</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      reject(<span class="hljs-number">222</span>);
    &#125;, <span class="hljs-number">2000</span>);
  &#125;);

  <span class="hljs-keyword">const</span> promise3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      reject(<span class="hljs-number">333</span>);
    &#125;, <span class="hljs-number">3000</span>);
  &#125;);

  <span class="hljs-comment">// 只有全部成功才成功，只要有一个失败即失败</span>
  <span class="hljs-comment">//  Promise.all([promise1, promise2, promise3])</span>
  <span class="hljs-comment">//   .then(value => &#123;</span>
  <span class="hljs-comment">//     console.log("成功了", value);</span>
  <span class="hljs-comment">//   &#125;)</span>
  <span class="hljs-comment">//   .catch(reason => &#123;</span>
  <span class="hljs-comment">//     console.log("失败了", reason);</span>
  <span class="hljs-comment">//   &#125;);</span>

  <span class="hljs-comment">// 只看执行最快那个，结果和先发生变化promise的状态一致，无论成功或失败</span>
  <span class="hljs-comment">//  Promise.race([promise2, promise1, promise3])</span>
  <span class="hljs-comment">//   .then(value => &#123;</span>
  <span class="hljs-comment">//     console.log("成功了", value);</span>
  <span class="hljs-comment">//   &#125;)</span>
  <span class="hljs-comment">//   .catch(reason => &#123;</span>
  <span class="hljs-comment">//     console.log("失败了", reason);</span>
  <span class="hljs-comment">//   &#125;);</span>

  <span class="hljs-comment">// 等所有promise都执行完，返回成功状态</span>
  <span class="hljs-built_in">Promise</span>.allSettled([promise1, promise2, promise3])
    .then(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'成功了'</span>, value);
    &#125;)
    .catch(<span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'失败了'</span>, reason);
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>牛人不是培养出来的，都是自己努力拼搏出来的，靠谁都不如靠自己，自己都不想主动多学习，只期望用一把锤子，就能搞定所有钉子，那你还不如想想怎么买彩票中500万吧，还更实际些，喜欢收藏，不喜勿喷，谢谢 ^_^</p>
</blockquote></div>  
</div>
            