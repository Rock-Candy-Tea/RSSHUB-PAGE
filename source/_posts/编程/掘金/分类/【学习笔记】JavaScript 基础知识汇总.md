
---
title: '【学习笔记】JavaScript 基础知识汇总'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9075'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:30:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=9075'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>本章内容为JavaScript基础（变量、数据类型、运算符、流程语句、数组、函数、字符串函数、正则表达式、DOM基本操作、Window 对象、JS对象、JSON、Cookie），博主自己以前整理的学习笔记，如有整理不对的地方，请各位大大指点出来</p>
<h1 data-id="heading-0">简介</h1>
<h2 data-id="heading-1">0. 简介</h2>
<p>JavaScript 对网页行为进行编程</p>
<p>javascript 是脚本语言，是一种轻量级的编程语言</p>
<p>JavaScript 是动态类型语言，而 Java 是静态类型语言</p>
<p>JavaScript 是弱类型的，Java 属于强类型</p>
<h2 data-id="heading-2">1. 命名规范</h2>
<ul>
<li>
<p>区分大小写</p>
</li>
<li>
<p>第一个字符必须是一个字母、下划线（_）或一个美元符号（$）;其他字符可以是字母、下划线、美元符号或数字</p>
</li>
<li>
<p>不能含有空格和其他标点符号。</p>
</li>
<li>
<p>不能以关键字或保留字命名</p>
</li>
</ul>
<h2 data-id="heading-3">2.书写规范</h2>
<ol>
<li>
<p>缩进的最小单位是4个空格</p>
</li>
<li>
<p>所有的变量应该在使用前声明</p>
</li>
<li>
<p>命名应该由26个大小写字母(A .. Z, a .. z)，10个数字(0 .. 9)和_(下划线)组成。不要在名字里使用$(美元符号)或(反斜线符号)。</p>
</li>
</ol>
<h2 data-id="heading-4">3. 使用</h2>
<p>1、JavaScript 代码必须位于 < script > 与 </ script > 标签之间。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"demo"</span>).innerHTML = <span class="hljs-string">"我的第一段 JavaScript"</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、JavaScript 文件放置外部脚本引用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"myScript.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>外部 JavaScript 的优势:</p>
<blockquote>
<p>1、分离了 HTML 和代码<br>
2、使 HTML 和 JavaScript 更易于阅读和维护<br>
3、已缓存的 JavaScript 文件可加速页面加载</p>
</blockquote>
</blockquote>
<h2 data-id="heading-5">4. 注释</h2>
<blockquote>
<p>//单行注释 <br>
/*   */多行注释</p>
</blockquote>
<h2 data-id="heading-6">5. 输出</h2>
<h3 data-id="heading-7">输出</h3>
<p>代码|详解
-|-|-
window.alert()|【弹出警告框】
document.write()|【将内容写到HTML文档中】
innerHTML|【写入到HTML中】
console.log()|【写入到浏览器控制台】</p>
<blockquote>
<p>附（PS：console有很多有意思的玩法） <br>
console.log('文字信息'); <br>
console.info('提示信息'); <br>
console.warn('警告信息'); <br>
console.error('错误信息');</p>
</blockquote>
<h3 data-id="heading-8">语句标识符（关键词）</h3>
<p>关键词|详解
-|-|-
break|用于跳出循环。
catch|语句块，在 try 语句块执行出错时执行 catch 语句块。
continue|跳过循环中的一个迭代。
do ... while|执行一个语句块，在条件语句为 true 时继续执行该语句块。
for|在条件语句为 true 时，可以将代码块执行指定的次数。
for ... in|用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。
function|定义一个函数
if ... else|用于基于不同的条件来执行不同的动作。
return|退出函数
switch|用于基于不同的条件来执行不同的动作。
throw|抛出（生成）错误 。
try|实现错误处理，与 catch 一同使用。
var|声明一个变量。
while|当条件语句为 true 时，执行语句块。</p>
<h1 data-id="heading-9">变量</h1>
<h2 data-id="heading-10">1. 变量</h2>
<p>变量是用于存储某种/某些数值的存储器。</p>
<h2 data-id="heading-11">2. 命名方法</h2>
<h3 data-id="heading-12">2.1 匈牙利命名法</h3>
<p>变量名 = 类型 + 对象描述</p>









































<table><thead><tr><th>命名类型</th><th align="center">命名前缀</th></tr></thead><tbody><tr><td>array 数组</td><td align="center">a</td></tr><tr><td>boolean 布尔值</td><td align="center">b</td></tr><tr><td>float 浮点数</td><td align="center">l</td></tr><tr><td>function 函数</td><td align="center">fn</td></tr><tr><td>int 整型</td><td align="center">i</td></tr><tr><td>object 对象</td><td align="center">o</td></tr><tr><td>regular 正则</td><td align="center">r</td></tr><tr><td>string 字符串</td><td align="center">s</td></tr></tbody></table>
<blockquote>
<p>举例：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> s_webname = <span class="hljs-string">'hello world'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.2 驼峰式命名法</h3>
<p>当标识符由一个或多个单词连接在一起，第一个单词的首字母小写，后面的单词首字母大写，其它字母全部小写。</p>
<blockquote>
<p>举例：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> webName = <span class="hljs-string">'hello world'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.3 帕斯卡命名法</h3>
<p>与骆驼式命名法类似，不过第一个单词首字母也大写</p>
<blockquote>
<p>举例：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> WebName = <span class="hljs-string">'hello world'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">3.变量声明</h2>
<p>var - 声明全局变量</p>
<p>let - 声明块级变量，即局部变量。(即：所声明的变量，只在let命令所在的代码块内有效。)</p>
<p>const - 用于声明常量，也具有块级作用域 ，也可声明块级。(const声明的变量不得改变值，
这意味着，const一旦声明变量，就必须立即初始化，不能留到以后赋值。不可重复声明。)</p>
<h2 data-id="heading-16">4.变量类型</h2>
<p>此处不作介绍，详情可看 <a href="https://juejin.cn/basics/b/b_datatype.html#_1-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B">2.数据类型</a> →</p>
<h2 data-id="heading-17">5.变量作用域</h2>
<p>在 JavaScript 中, 作用域是可访问变量的集合。</p>
<p>JavaScript 函数作用域: 作用域在函数内修改。</p>
<p>一个变量的作用域（scope)是程序源代码中定义这个变量的区域。</p>
<blockquote>
<p>JavaScript 变量生命周期在它声明时初始化。<br></p>
<blockquote>
<p>局部变量在函数执行完毕后销毁。<br>
全局变量在页面关闭后销毁。</p>
</blockquote>
</blockquote>
<h3 data-id="heading-18">5.1 全局变量</h3>
<p>变量在函数外定义，即为全局变量。</p>
<p>全局变量有 全局作用域: 网页中所有脚本和函数均可使用。</p>
<h3 data-id="heading-19">5.2 局部变量</h3>
<p>变量在函数内声明，变量为局部作用域。</p>
<p>局部变量的优先级高于同名的全局变量</p>
<p>局部变量在函数开始执行时创建，函数执行完后局部变量会自动销毁。</p>
<h1 data-id="heading-20">数据类型</h1>
<h2 data-id="heading-21">1. 数据类型</h2>
<p>JavaScript 的数据类型，共有 <strong>七</strong> 种（其中 Symbol 是ES6新增），分为“基本类型”和“引用类型”</p>
<p><strong>基本类型：</strong> 字符串(String)、数字(Number)、布尔(Boolean)、数组(Array)、空(Null)、未定义(Undefined)</p>
<p><strong>引用类型：</strong> 对象(Object)</p>
<p><strong>原始类型：</strong> 符号(Symbol)</p>
<p>null 和 undefined 通常被认为是特殊值，这两种类型的值唯一，就是其本身。</p>
<p>数据类型|说明
--|:--:|--:
字符串（String）|使用双引号 " 或单引号 ' 括起来的一个或多个字符
数字(Number)|包括整数和浮点数（包含小数点的数或科学记数法的数）
布尔(Boolean)|表示 true 或 false 这两种状态
空（Null）|变量或内容值为空（null），可以通过给一个变量赋 null 值来清除变量的内容
未定义（Undefined）|变量被创建后，未给该变量赋值，该类型只有一个取值：undefined
数组(Array)|var cars=new Array();
对象(Object)|JavaScript 操作的对象
符号(Symbol)|Symbol 值通过Symbol函数生成。凡是属性名属于 Symbol 类型，就都是独一无二的，可以保证不会与其他属性名产生冲突。（PS：Symbol函数前不能使用new命令，否则会报错。）</p>
<h2 data-id="heading-22">2. js弱类型语言</h2>
<p><strong>JavaScript 拥有动态类型，这意味着相同的变量可用作不同的类型</strong></p>
<p><strong>js是弱类型语言</strong>，不重视类型的定义，但js会根据为变量赋值的情况自定判断该变量是何种类型。</p>
<h2 data-id="heading-23">3. 数据类型转换</h2>
<p>JavaScript 拥有动态类型，可以不需要指定数据类型，在执行时会自动转换</p>
<p>JavaScript 变量可以转换为新变量或其他数据类型：</p>
<ul>
<li>通过使用 JavaScript 函数</li>
<li>通过 JavaScript 自身自动转换</li>
</ul>
<p>Number() 转换为数字， String() 转换为字符串， Boolean() 转化为布尔值。</p>
<h2 data-id="heading-24">4.数据类型判断</h2>
<h3 data-id="heading-25">4.1 typeof 操作符</h3>
<p>typeof 操作符用来检测变量的数据类型。</p>
<ol>
<li>写法</li>
</ol>
<ul>
<li>
<p>typeof() 括号</p>
</li>
<li>
<p>typeof object 中间加空格</p>
</li>
</ul>
<ol start="2">
<li>返回的数据类型</li>
</ol>
<ul>
<li>number</li>
<li>string</li>
<li>boolean</li>
<li>object</li>
<li>undefined</li>
<li>function</li>
<li>Symbols</li>
</ul>
<h3 data-id="heading-26">4.2 instanceof</h3>
<p>instanceof 其实适合用于判断自定义的类实例对象, 而不是用来判断原生的数据类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">judgeType2</span> (<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (obj === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">"null"</span>;
  <span class="hljs-keyword">if</span> (obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)  <span class="hljs-keyword">return</span> <span class="hljs-string">"array"</span>;
  <span class="hljs-keyword">return</span> (<span class="hljs-keyword">typeof</span> obj);
&#125; 
judgeType2(<span class="hljs-string">"123"</span>)   <span class="hljs-comment">// "string"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">4.3 Object.prototype.toString.call()</h3>
<p>使用 Object.prototype.toString.call() 方法, 可以获取到变量的准确的类型.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.prototype.toString.call(<span class="hljs-string">'asd'</span>));  <span class="hljs-comment">// [object String]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-28">5. null、undefined、NaN</h2>
<p><strong>1. null</strong></p>
<p>null 表示“空值”，代表一个空对象指针，使用typeof运算得到 “object”，所以你可以认为它是一个特殊的对象值。</p>
<p><strong>2. undefined</strong></p>
<p>undefined 表示“未定义”，可以把undefined看作是空的变量。</p>
<p><strong>3. NaN</strong></p>
<p>NaN，即非数字值，是一个特殊的数值，属于Number类型。</p>
<p><strong>NaN的特点:</strong></p>
<ol>
<li>任何设计NaN的操作都会返回NaN，这个特点在多步计算中有可能导致问题。</li>
<li>NaN与任何值都不相等，包括其本身。</li>
</ol>
<blockquote>
<p>ps：针对NaN的这两个特点，ECMAScript定义了isNaN() 函数。</p>
</blockquote>
<h1 data-id="heading-29">运算符</h1>
<h2 data-id="heading-30">1. 算数运算符</h2>
<p>+（加法）、-（减法）、*（乘法）、/（除法）、%（取余）、++（自加）、--（自减）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// +（加法）</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">1</span> + <span class="hljs-number">1</span>) <span class="hljs-comment">// 2</span>

<span class="hljs-comment">// -（减法）</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">2</span> - <span class="hljs-number">1</span>) <span class="hljs-comment">// 1</span>

<span class="hljs-comment">// *（乘法）</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">2</span> * <span class="hljs-number">2</span>) <span class="hljs-comment">// 4</span>

<span class="hljs-comment">// /（除法）</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">4</span> / <span class="hljs-number">2</span>) <span class="hljs-comment">// 2</span>

<span class="hljs-comment">// %（取余）</span>
<span class="hljs-built_in">console</span>.log( <span class="hljs-number">5</span> % <span class="hljs-number">2</span>) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">2. 赋值运算符</h2>
<p>=（等于）、+=、-=、*=、/=、%=</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// =（等于）</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// 10</span>

<span class="hljs-comment">// +=</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a+=<span class="hljs-number">1</span>) <span class="hljs-comment">// 11</span>

<span class="hljs-comment">// -=</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a-=<span class="hljs-number">1</span>) <span class="hljs-comment">// 9</span>

<span class="hljs-comment">// *=</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a*=<span class="hljs-number">2</span>) <span class="hljs-comment">// 20</span>

<span class="hljs-comment">// /=</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a/=<span class="hljs-number">2</span>) <span class="hljs-comment">// 5</span>

<span class="hljs-comment">// %=</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span> 
<span class="hljs-built_in">console</span>.log(a%=<span class="hljs-number">3</span>) <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-32">3. 字符串运算符</h2>
<p>+、+=</p>
<p>+ 运算符也可用于对字符串进行相加</p>
<p>+= 赋值运算符也可用于相加（级联）字符串</p>
<h2 data-id="heading-33">4. 关系(比较)运算符</h2>
<p>（大于）、<（小于）、>=（大于等于）、<=（小于等于）、!=（不等于）、==（等于）、===（全等）、！===（真不等）</p>
<blockquote>
<p>PS：==只比较数值不比较类型   ===比较包括类型</p>
</blockquote>
<h2 data-id="heading-34">5. 逻辑运算符</h2>
<p>&&（逻辑与/并且）：当两边表达式均为真运算结果才为真，否则为假</p>
<p>||（逻辑或/或者）：当两边有一个表达式为真则结果即为真</p>
<p>！（逻辑非/取反）：取反</p>
<h2 data-id="heading-35">6. 位运算符</h2>

































<table><thead><tr><th>运算符</th><th>描述</th></tr></thead><tbody><tr><td>&</td><td>和</td></tr><tr><td>|</td><td>或</td></tr><tr><td>~</td><td>取反</td></tr><tr><td>^</td><td>异或</td></tr><tr><td><<</td><td>左移</td></tr><tr><td>>></td><td>右移</td></tr></tbody></table>
<h2 data-id="heading-36">7. 其他运算符</h2>
<h3 data-id="heading-37">7.1 三元运算符( ? : )</h3>
<p>条件？条件成立执行：条件不成立执行；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">2</span>><span class="hljs-number">1</span>?<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"true"</span>):<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"false"</span>)  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-38">7.2 typeof</h3>
<p><a href="https://juejin.cn/pages/ecc503/#_4-1-typeof-%E6%93%8D%E4%BD%9C%E7%AC%A6">数据类型中已写过，点此跳转到对应位置</a></p>
<h3 data-id="heading-39">7.3 逗号(,)</h3>
<p>逗号运算符的作用是将若干表达式连接起来。它的优先级别在所有运算符中是最低的，结合方向是"自左至右"的。 （即：逗号运算符：是按顺序执行表达式，并且获得右边表达式的值。）</p>
<p>逗号表达式的一般形式是：表达式1，表达式2，表达式3……表达式n</p>
<pre><code class="hljs language-js copyable" lang="js">x=<span class="hljs-number">2</span>*<span class="hljs-number">2</span>,x*<span class="hljs-number">2</span>;
<span class="hljs-built_in">console</span>.log(x)  <span class="hljs-comment">// 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-40">7.4 void</h3>
<p>void 运算符对任何值返回 undefined。该运算符通常用于避免输出不应该输出的值</p>
<p>作用一：返回undefined</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">tan</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">33</span>;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">void</span> tan());  <span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>作用二:防止不必要的行为。在页面中有个a标签，但是该a标签又不是为了指向跳转页面的话，这个时候void运算符就派上大大的用场了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'javascript:void(0)'</span>></span>点我将不会执行任何行为<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-41">流程语句</h1>
<h2 data-id="heading-42">1. 循环语句</h2>
<h3 data-id="heading-43">1.1 while</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span>(条件表达式)&#123;
  循环执行的代码块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>流程：</strong></li>
</ol>
<ul>
<li>当指定的条件为 true 时循环指定的代码块</li>
<li>当指定的条件为 false 时退出循环体</li>
</ul>
<ol start="3">
<li><strong>特性：</strong></li>
</ol>
<ul>
<li>先检查条件，再执行循环，条件不满足则循环一次也不执行</li>
</ul>
<ol start="4">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">while</span>(i < <span class="hljs-number">2</span>)&#123;
  <span class="hljs-built_in">console</span>.log(i)
  i++;
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">1.2 do...while</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">do</span>&#123;
  循环执行的代码块
&#125;<span class="hljs-keyword">while</span>(条件表达式);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>流程：</strong></li>
</ol>
<ul>
<li>先执行循环体内代码块再进行判断</li>
<li>如果表达式的值为 true ，循环执行代码块</li>
<li>如果表达式的值为 false ，退出循环体</li>
</ul>
<ol start="3">
<li><strong>特性：</strong></li>
</ol>
<ul>
<li>先执行循环体，再进行条件判断，循环体内代码至少执行一次</li>
</ul>
<ol start="4">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;
<span class="hljs-keyword">do</span>&#123;
  <span class="hljs-built_in">console</span>.log(i)
  i++;
&#125;<span class="hljs-keyword">while</span>(i < <span class="hljs-number">2</span>)
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-45">1.3 for</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(循环变量=初值;循环条件;递增/递减计数器)&#123;
  循环执行的代码块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>流程：</strong></li>
</ol>
<ul>
<li>用循环变量初始值与循环条件相比较，确定返回值</li>
<li>如果返回值为 true ，执行循环体</li>
<li>执行完后进行递增/递减云算</li>
<li>将运算结果与循环条件相比较</li>
<li>如果返回值为 true 则继续执行，为 false 则退出循环</li>
</ul>
<ol start="3">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;i < <span class="hljs-number">2</span>;i++)&#123;
  <span class="hljs-built_in">console</span>.log(i)
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-46">1.4 for...in</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(声明变量 <span class="hljs-keyword">in</span> 对象)&#123;
  代码块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>循环输出的属性顺序不可预知，对象的值不能是 null 或 undefined</p>
</blockquote>
<ol start="2">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr= [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>];
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> x <span class="hljs-keyword">in</span> arr )&#123;
  <span class="hljs-built_in">console</span>.log(arr[x]);
&#125;
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">2.跳转语句</h2>
<h3 data-id="heading-48">2.1 return</h3>
<p>终止循环体的运行，并返回一个值</p>
<h3 data-id="heading-49">2.2 break</h3>
<p>终止整个循环，不再进行判断，只能用在循环或 switch 中。</p>
<h3 data-id="heading-50">2.3 continue</h3>
<p>continue 语句中断循环中的迭代，如果出现了指定的条件，然后继续循环中的下一个迭代。(即：结束本次循环，接着去判断是否执行下次循环)</p>
<h2 data-id="heading-51">3.条件判断语句</h2>
<h3 data-id="heading-52">3.1 if</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(条件表达式<span class="hljs-number">1</span>)&#123;
  代码块 <span class="hljs-number">1</span>
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(条件表达式<span class="hljs-number">2</span>)&#123;
  代码块 <span class="hljs-number">2</span>
&#125;<span class="hljs-keyword">else</span>&#123;
  代码块 <span class="hljs-number">3</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>流程：</strong></li>
</ol>
<ul>
<li>判断条件1，如果返回值为 true ，执行代码块1</li>
<li>判断条件1的返回值为 false 则跳过语句块并检测条件表达式2</li>
<li>如果所有表达式的值均为 false 则执行 else 后面的语句</li>
</ul>
<ol start="3">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="hljs-keyword">var</span> b = <span class="hljs-number">2</span>
<span class="hljs-keyword">if</span>(a > b)&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"true"</span>)
&#125;<span class="hljs-keyword">else</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"false"</span>)
&#125;
<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-53">3.2 switch</h3>
<ol>
<li><strong>语法：</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">switch</span>(条件表达式)&#123;
  <span class="hljs-keyword">case</span> 标签<span class="hljs-number">1</span> ：
    代码块 <span class="hljs-number">1</span>;
    <span class="hljs-keyword">break</span>;
    …… ……
  <span class="hljs-attr">default</span>:
    代码块n;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>流程：</strong></li>
</ol>
<ul>
<li>计算表达式的值，并与各标签比较</li>
<li>若找到与之匹配的标签，则执行其后的代码块</li>
<li>若没有找到与之匹配的标签，则直接执行 default 之后的代码块</li>
</ul>
<ol start="3">
<li><strong>例子</strong></li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> day;
<span class="hljs-keyword">switch</span> (<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getDay()) &#123;
  <span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:
    day = <span class="hljs-string">"周日"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">1</span>:
    day = <span class="hljs-string">"周一"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:
    day = <span class="hljs-string">"周二"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">3</span>:
    day = <span class="hljs-string">"周三"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
    day = <span class="hljs-string">"周四"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span> <span class="hljs-number">5</span>:
    day = <span class="hljs-string">"周五"</span>;
    <span class="hljs-keyword">break</span>;
  <span class="hljs-keyword">case</span>  <span class="hljs-number">6</span>:
    day = <span class="hljs-string">"周六"</span>;
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"今天是"</span> + day)

<span class="hljs-comment">//假设 new Date().getDay() 得到的值是5 那么最后输出是</span>
<span class="hljs-comment">//今天是周五</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-54">4.异常处理语句</h2>
<h3 data-id="heading-55">4.1 throw</h3>
<p>主动抛出异常</p>
<h3 data-id="heading-56">4.2 try</h3>
<p>指明需要处理的代码块</p>
<h3 data-id="heading-57">4.3 catch</h3>
<p>捕获异常</p>
<h3 data-id="heading-58">4.4 finally</h3>
<p>后期处理</p>
<h1 data-id="heading-59">数组</h1>
<h2 data-id="heading-60">1. 创建方法</h2>
<blockquote>
<p>数组长度是弹性的，可自由伸缩；
数组下标从0开始
数组元素可添加到对象中</p>
</blockquote>
<p><strong>1. 空数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 指定长度数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>( Size );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. 指定元素数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>( 元素<span class="hljs-number">1</span>,元素<span class="hljs-number">2</span>,元素<span class="hljs-number">3</span>,...,元素N );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4. 单维数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Obj = [元素<span class="hljs-number">1</span>,元素<span class="hljs-number">2</span>,元素<span class="hljs-number">3</span>,...,元素N];
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>5. 多维数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>( [数组序列<span class="hljs-number">1</span>],[数组序列<span class="hljs-number">2</span>],[数组序列<span class="hljs-number">3</span>],...,[数组序列N] );
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-61">2. 数组属性</h2>
<h3 data-id="heading-62">2.1 constructor</h3>
<p>constructor 属性返回对象的构造函数</p>
<h3 data-id="heading-63">2.2 length</h3>
<p>length 返回数组的长度</p>
<h3 data-id="heading-64">2.3 prototype</h3>
<p>prototype 通过增加属性和方法扩展数组定义</p>
<h2 data-id="heading-65">3. 遍历数组</h2>
<h3 data-id="heading-66">3.1 使用 for 循环</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>;i < <span class="hljs-number">5</span>;i++)&#123;
  <span class="hljs-built_in">console</span>.log(i)
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>
<span class="hljs-comment">// 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-67">3.2 使用 for...in</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>];
<span class="hljs-keyword">for</span>(i <span class="hljs-keyword">in</span> arr)&#123;
  <span class="hljs-built_in">console</span>.log(arr[i])
&#125;
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-68">3.3 使用 forEach</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> arr = [<span class="hljs-string">'a'</span>,<span class="hljs-string">'b'</span>,<span class="hljs-string">'c'</span>];
arr.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;);
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// c</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-69">4. 数组方法</h2>

































































<table><thead><tr><th>方法</th><th align="center">描述</th></tr></thead><tbody><tr><td>concat()</td><td align="center">连接两个或更多的数组，并返回结果。</td></tr><tr><td>join()</td><td align="center">把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。</td></tr><tr><td>pop()</td><td align="center">删除并返回数组的最后一个元素</td></tr><tr><td>push()</td><td align="center">向数组的末尾添加一个或更多元素，并返回新的长度。</td></tr><tr><td>reverse()</td><td align="center">颠倒数组中元素的顺序。</td></tr><tr><td>shift()</td><td align="center">删除并返回数组的第一个元素</td></tr><tr><td>slice()</td><td align="center">从某个已有的数组返回选定的元素</td></tr><tr><td>sort()</td><td align="center">对数组的元素进行排序</td></tr><tr><td>splice()</td><td align="center">删除元素，并向数组添加新元素。</td></tr><tr><td>toSource()</td><td align="center">返回该对象的源代码。</td></tr><tr><td>toString()</td><td align="center">把数组转换为字符串，并返回结果。</td></tr><tr><td>toLocaleString()</td><td align="center">把数组转换为本地数组，并返回结果。</td></tr><tr><td>unshift()</td><td align="center">向数组的开头添加一个或更多元素，并返回新的长度。</td></tr><tr><td>valueOf()</td><td align="center">返回数组对象的原始值</td></tr></tbody></table>
<h3 data-id="heading-70">4.1 concat()</h3>
<p>连接两个或更多的数组，并返回结果。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.concat(arrayX,arrayX,......,arrayX)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.concat(<span class="hljs-number">4</span>,<span class="hljs-number">5</span>)
<span class="hljs-built_in">console</span>.log(b)
<span class="hljs-comment">// [1,2,3,4,5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-71">4.2 join()</h3>
<p>把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.join(separator)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.join(<span class="hljs-string">","</span>)
<span class="hljs-built_in">console</span>.log(b)
<span class="hljs-comment">// 1,2,3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">4.3 pop()</h3>
<p>删除并返回数组的最后一个元素</p>
<p>pop() 方法将删除 arrayObject 的最后一个元素，把数组长度减 1，并且返回它删除的元素的值。如果数组已经为空，则 pop() 不改变数组，并返回 undefined 值。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.pop()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.pop()
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">//[1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-73">4.4 push()</h3>
<p>向数组的末尾添加一个或更多元素，并返回新的长度。</p>
<p>push() 方法可把它的参数顺序添加到 arrayObject 的尾部。它直接修改 arrayObject，而不是创建一个新的数组。push() 方法和 pop() 方法使用数组提供的先进后出栈的功能。</p>
<blockquote>
<p>PS：该方法会改变数组的长度。</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.push(newelement1,newelement2,....,newelementX)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.push(<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 4</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">//[1,2,3,4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-74">4.5 reverse()</h3>
<p>颠倒数组中元素的顺序。</p>
<blockquote>
<p>PS：该方法会改变原来的数组，而不会创建新的数组。</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.reverse()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.reverse()
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 3,2,1</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// 3,2,1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-75">4.6 shift()</h3>
<p>删除并返回数组的第一个元素</p>
<p>如果数组是空的，那么 shift() 方法将不进行任何操作，返回 undefined 值。请注意，该方法不创建新数组，而是直接修改原有的 arrayObject。</p>
<blockquote>
<p>PS：该方法会改变数组的长度。</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.shift()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.shift()
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-76">4.7 slice()</h3>
<p>从某个已有的数组返回选定的元素</p>
<blockquote>
<p>PS：该方法并不会修改数组，而是返回一个子数组。如果想删除数组中的一段元素，应该使用方法 Array.splice()。<br>
您可使用负值从数组的尾部选取元素。<br>
如果 end 未被规定，那么 slice() 方法会选取从 start 到数组结尾的所有元素。</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.slice(start,end)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.slice(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// [2]</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-77">4.8 sort()</h3>
<p>对数组的元素进行排序</p>
<p>如果调用该方法时没有使用参数，将按字母顺序对数组中的元素进行排序，说得更精确点，是按照字符编码的顺序进行排序。要实现这一点，首先应把数组的元素都转换成字符串（如有必要），以便进行比较。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.sort(sortby)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-string">'c'</span>,<span class="hljs-string">'d'</span>,<span class="hljs-string">'a'</span>,<span class="hljs-string">'f'</span>];
a.sort()
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// ["a", "c", "d", "f"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-78">4.9 splice()</h3>
<p>删除元素，并向数组添加新元素。</p>
<p>splice() 方法可删除从 index 处开始的零个或多个元素，并且用参数列表中声明的一个或多个值来替换那些被删除的元素。</p>
<p>如果从 arrayObject 中删除了元素，则返回的是含有被删除的元素的数组。</p>
<blockquote>
<p>PS：请注意，splice() 方法与 slice() 方法的作用是不同的，splice() 方法会直接对数组进行修改。</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.splice(index,howmany,item1,.....,itemX)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.splice(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// [2,3]</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-79">4.10 toSource()</h3>
<p>返回该对象的源代码。</p>
<p>该原始值由 Array 对象派生的所有对象继承。</p>
<p>toSource() 方法通常由 JavaScript 在后台自动调用，并不显式地出现在代码中。</p>
<p><strong>语法</strong></p>
<p><code>object.toSource()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">employee</span>(<span class="hljs-params">name,sex,born</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.name=name;
  <span class="hljs-built_in">this</span>.sex=sex;
  <span class="hljs-built_in">this</span>.born=born;
&#125;
<span class="hljs-keyword">var</span> bill = <span class="hljs-keyword">new</span> employee(<span class="hljs-string">"miluluyo"</span>,<span class="hljs-string">"girl"</span>,<span class="hljs-number">1997</span>);
<span class="hljs-built_in">document</span>.write(bill.toSource());
<span class="hljs-comment">//(&#123;name:"miluluyo", sex:"girl", born:1997&#125;) </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-80">4.11 toString()</h3>
<p>把数组转换为字符串，并返回结果。</p>
<p>当数组用于字符串环境时，JavaScript 会调用这一方法将数组自动转换成字符串。但是在某些情况下，需要显式地调用该方法。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.toString()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.toString()
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 1,2,3</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-81">4.12 toLocaleString()</h3>
<p>把数组转换为本地数组，并返回结果。</p>
<p>首先调用每个数组元素的 toLocaleString() 方法，然后使用地区特定的分隔符把生成的字符串连接起来，形成一个字符串。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.toLocaleString()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.toLocaleString()
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 1,2,3</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-82">4.13 unshift()</h3>
<p>向数组的开头添加一个或更多元素，并返回新的长度。</p>
<p>unshift() 方法将把它的参数插入 arrayObject 的头部，并将已经存在的元素顺次地移到较高的下标处，以便留出空间。该方法的第一个参数将成为数组的新元素 0，如果还有第二个参数，它将成为新的元素 1，以此类推。</p>
<blockquote>
<p>unshift() 方法不创建新的创建，而是直接修改原有的数组。<br>
unshift() 方法无法在 Internet Explorer 中正确地工作！</p>
</blockquote>
<p><strong>语法</strong></p>
<p><code>arrayObject.unshift(newelement1,newelement2,....,newelementX)</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">var</span> b = a.unshift(<span class="hljs-number">0</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>)
<span class="hljs-built_in">console</span>.log(b)  <span class="hljs-comment">// 6</span>
<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// [0,4,5,1,2,3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-83">4.14 valueOf()</h3>
<p>返回数组对象的原始值</p>
<p>该原始值由 Array 对象派生的所有对象继承。</p>
<p>valueOf() 方法通常由 JavaScript 在后台自动调用，并不显式地出现在代码中。</p>
<p><strong>语法</strong></p>
<p><code>arrayObject.valueOf()</code></p>
<p><strong>例子</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> boo = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">false</span>)
<span class="hljs-built_in">document</span>.write(boo.valueOf())
<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-84">函数</h1>
<h2 data-id="heading-85">1. 定义方法</h2>
<p><strong>1. 静态方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> 函数名(<span class="hljs-params">[虚参列表]</span>)</span>&#123;
  函数体;
  [<span class="hljs-keyword">return</span>[函数返回值;]]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 动态匿名方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> 函数名 = <span class="hljs-keyword">new</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">[<span class="hljs-string">"虚参列表"</span>],<span class="hljs-string">"函数体"</span></span>)
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3. 直接量方法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">函数名 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">[虚参列表]</span>)</span>&#123;函数体;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-86">2. 调用方法</h2>
<p><strong>2.1 直接调用</strong></p>
<pre><code class="hljs language-js copyable" lang="js">函数名(实参列表)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.2 链接中调用</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"javascript:函数名()"</span>></span>a标签<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.3 在事件中调用</strong></p>
<pre><code class="hljs language-js copyable" lang="js">事件类型 = <span class="hljs-string">"函数名()"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2.4 递归调用</strong></p>
<p>在函数体内部调用函数自身</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> 函数名(<span class="hljs-params"></span>)</span>&#123;
  代码
  函数名();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-87">3.方法</h2>
<h3 data-id="heading-88">apply</h3>
<p>将函数作为对象的方法来调用，将参数以数组形式传递给该方法</p>
<p><strong>语法</strong></p>
<p><code>function.apply(thisObj,[arg1,arg2,....argN])</code></p>
<h3 data-id="heading-89">call</h3>
<p>将函数作为对象的方法来调用，将指定参数传递给该方法</p>
<p><strong>语法</strong></p>
<p><code>function.call(thisObj, arg1,arg2,...argN)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> foo = &#123;
  <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>
&#125;;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.value);
&#125;
bar.call(foo); <span class="hljs-comment">// 1</span>
<span class="hljs-comment">//call 改变了 this 的指向，指向到 foo</span>
<span class="hljs-comment">//bar 函数执行了</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-90">toString</h3>
<p>返回函数的字符串表示</p>
<h2 data-id="heading-91">4. arguments 对象</h2>
<p>arguments是一个对应于传递给函数的参数的类数组对象。</p>
<p>arguments对象是所有（非箭头）函数中都可用的局部变量。</p>
<p><strong>属性</strong></p>
<p><strong>4.1 length</strong></p>
<p>获取函数实参的长度</p>
<p><strong>4.2 arguments.callee</strong></p>
<p>返回当前正在指向的函数</p>
<blockquote>
<p>严格模式下，无法使用。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">arguments</span>.callee) 
&#125;
test();  <span class="hljs-comment">//fn test</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>4.3 caler</strong></p>
<p>返回调用当前正在执行函数的函数名</p>
<h2 data-id="heading-92">5. 函数参数</h2>
<p><strong>参数类型</strong></p>
<p><strong>5.1 形参</strong></p>
<p>定义函数时使用的参数，接收调用该函数时传递的参数</p>
<p><strong>5.2 实参</strong></p>
<p>调用函数时传递给函数的实际参数</p>
<p><strong>特性</strong></p>
<ol>
<li>参数个数没有限制；</li>
</ol>
<p><strong>实参 < 形参：</strong> 多余形参 = undefined</p>
<p><strong>实参 > 形参：</strong> 多余形参被忽略</p>
<ol start="2">
<li>
<p>参数的数据类型没有限制；</p>
</li>
<li>
<p>通过 arguments 对象访问参数数组</p>
</li>
<li>
<p>参数始终按值传递</p>
</li>
</ol>
<p>**基本类型：**传值</p>
<p>**引用类型：**传址</p>
<h2 data-id="heading-93">6. 指针标识</h2>
<h3 data-id="heading-94">6.1 this</h3>
<p>指向当前操作对象</p>
<h3 data-id="heading-95">6.2 callee</h3>
<p>指向参数集合所属函数</p>
<h3 data-id="heading-96">6.3 prototype</h3>
<p>指向函数附带的原型对象</p>
<h3 data-id="heading-97">6.4 constructor</h3>
<p>指向创建该对象的构造函数</p>
<h2 data-id="heading-98">7. 箭头函数 （ES6）</h2>
<p><strong>和普通函数的区别</strong></p>
<ol>
<li>不绑定this,arguments</li>
<li>更简化的代码语法。</li>
</ol>
<blockquote>
<p>不绑定this</p>
<blockquote>
<p>箭头函数的 this 始终未定义的 this</p>
</blockquote>
</blockquote>
<blockquote>
<p>不绑定arguments</p>
<blockquote>
<p>如果你在箭头函数中使用arguments参数不能得到想要的内容。</p>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>)
&#125;
<span class="hljs-comment">//写成箭头函数后如下：</span>
()=> conosle.log(<span class="hljs-string">'hello'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-99">8. 闭包</h2>
<p>JavaScript 变量属于本地或全局作用域。</p>
<p>全局变量能够通过闭包实现局部（私有）。</p>
<p>闭包是一种保护私有变量的机制，在函数执行时形成私有的作用域，保护里面的私有变量不受外界干扰。</p>
<p>直观的说就是形成一个不销毁的栈环境。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> add = (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> counter = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-keyword">return</span> counter += <span class="hljs-number">1</span>;&#125;
&#125;)();

<span class="hljs-built_in">console</span>.log(add());  <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(add());  <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(add());  <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>变量 add 的赋值是自调用函数的返回值。</p>
<p>这个自调用函数只运行一次。它设置计数器为零（0），并返回函数表达式。</p>
<p>这样 add 成为了函数。最“精彩的”部分是它能够访问父作用域中的计数器。</p>
<p>这被称为 JavaScript 闭包。它使函数拥有“私有”变量成为可能。</p>
<p>计数器被这个匿名函数的作用域保护，并且只能使用 add 函数来修改。</p>
<p>闭包指的是有权访问父作用域的函数，即使在父函数关闭之后。</p>
<h1 data-id="heading-100">字符串函数</h1>
<h2 data-id="heading-101">1. 查找方法</h2>
<h3 data-id="heading-102">1.1 字符串方法</h3>
<p><strong>chartAt()</strong></p>
<p>chartAt() 返回字符串中第N个字符</p>
<p><strong>chartCodeAt()</strong></p>
<p>chartCodeAt() 返回字符串中第N个字符的代码</p>
<p><strong>fromCharCode()</strong></p>
<p>fromCharCode() 根据字符编码创建字符串</p>
<blockquote>
<p><strong>关系</strong><br></p>
</blockquote>
<blockquote>
<blockquote>
<p>charAt与charCodeAt共性：根据下标查找指定字符<br>
charCodeAt与fromCharCode:互为反向操作</p>
</blockquote>
</blockquote>
<h3 data-id="heading-103">1.2 位置方法</h3>
<p><strong>indexOf()</strong></p>
<p>indexOf() 从前向后检索字符串，看其是否含有指定字符串</p>
<p><strong>lastIndexOf()</strong></p>
<p>从后向前检索字符串，看其是否含有指定字符串</p>
<h3 data-id="heading-104">1.3 匹配方法</h3>
<p><strong>match()</strong></p>
<p>match()找到一个或多个正则表达式的匹配</p>
<p><strong>search()</strong></p>
<p>search()检索字符串中与正则表达式匹配的字符串</p>
<p><strong>replace()</strong></p>
<p>replace()替换一个与正则表达式匹配的字符串</p>
<p><strong>split()</strong></p>
<p>split()根据指定分隔符将字符串分割成多个字符串，并返回数组</p>
<h2 data-id="heading-105">2. 操作方法</h2>
<h3 data-id="heading-106">2.1 拼接方法</h3>
<p><strong>concat()</strong></p>
<p>将指定字符串连接到此字符串的结尾</p>
<p><strong>语法</strong></p>
<p><code>string.concat(value..)</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span> str = <span class="hljs-string">"abc"</span>;
str = str.concat(<span class="hljs-string">"123"</span>);
System.out.println(str);<span class="hljs-comment">//abc123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-107">2.2 获取方法</h3>
<blockquote>
<p><strong>根据下标截取字符串</strong></p>
<blockquote>
<p><strong>slice()</strong></p>
<p>slice()与字符长度相加</p>
<p><strong>substring()</strong></p>
<p>substring()转换为0</p>
</blockquote>
<p><strong>根据长度截取字符串</strong></p>
<blockquote>
<p><strong>substr()</strong>
substr()返回字符的个数</p>
</blockquote>
</blockquote>
<h3 data-id="heading-108">2.3 空格处理</h3>
<p><strong>trim</strong> 清除前置及后缀空格</p>
<p><strong>timLeft</strong> 清除前置空格</p>
<p><strong>trimRight</strong> 清除后缀空格</p>
<h3 data-id="heading-109">2.4 比较方法</h3>
<p>localCompare() 用本地特定顺序比较两个字符串</p>
<h2 data-id="heading-110">3. 编码方法</h2>
<p><strong>字符串常规编码与解码</strong>
escape()、unescape()</p>
<p><strong>URI字符串编码与解码</strong>
encodeURI()、decodeURI()</p>
<h2 data-id="heading-111">4. 转换方法</h2>
<h3 data-id="heading-112">4.1 大小写转换</h3>
<p><strong>转为大写</strong>
toUpperCase()、toLocaleUpperCase()</p>
<p><strong>转为小写</strong>
toLowerCase()、toLocaleLowerCase()</p>
<p><strong>URI组件编码与解码</strong>
encodeURIComponent()、decodeURIComponent()</p>
<h1 data-id="heading-113">正则表达式</h1>
<h2 data-id="heading-114">0. 正则表达式</h2>
<p>正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp或RE）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串搜索模式。</p>
<h2 data-id="heading-115">1. 方式：</h2>
<p><strong>字面量</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> 变量名 = <span class="hljs-regexp">/表达式/</span>模式修饰符
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>构造函数</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> 变量名 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(<span class="hljs-string">"表达式"</span>,<span class="hljs-string">"模式修饰符"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-116">2. 表达式</h2>
<h3 data-id="heading-117">单个字符与数字</h3>





































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>.</td><td>匹配除换行符之外的任意字符</td></tr><tr><td>[a-z0-9]</td><td>匹配方括号中的任意字符</td></tr><tr><td>[^a-z0-9]</td><td>匹配不在方括号中的任意字符</td></tr><tr><td>\d</td><td>匹配数字</td></tr><tr><td>\D</td><td>匹配非数字</td></tr><tr><td>\w</td><td>匹配字母</td></tr><tr><td>\W</td><td>匹配非字母</td></tr></tbody></table>
<h3 data-id="heading-118">空白字符</h3>









































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>\0</td><td>匹配 null 字符</td></tr><tr><td>\b</td><td>匹配空格字符</td></tr><tr><td>\f</td><td>匹配进纸符</td></tr><tr><td>\n</td><td>匹配换行符</td></tr><tr><td>\r</td><td>匹配回车符</td></tr><tr><td>\s</td><td>匹配空白字符、空格、制表符或换行符</td></tr><tr><td>\S</td><td>匹配非空白字符</td></tr><tr><td>\t</td><td>匹配制表符</td></tr></tbody></table>
<h3 data-id="heading-119">定位符</h3>









































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>^</td><td>行首匹配</td></tr><tr><td>$</td><td>行尾匹配</td></tr><tr><td>\A</td><td>只匹配字符串的开始处</td></tr><tr><td>\b</td><td>匹配单词边界，词在[]内无效</td></tr><tr><td>\B</td><td>匹配非单词边界</td></tr><tr><td>\G</td><td>匹配当前搜索的开始位置</td></tr><tr><td>\Z</td><td>匹配字符串结束处或行尾</td></tr><tr><td>\z</td><td>只匹配字符串结束处</td></tr></tbody></table>
<h3 data-id="heading-120">限定符</h3>

























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>x?</td><td>匹配0个或1个x</td></tr><tr><td>x*</td><td>匹配0个或任意多个x</td></tr><tr><td>x+</td><td>匹配至少1个x</td></tr><tr><td>x&#123;m,n&#125;</td><td>匹配最少m个，最多n个x</td></tr></tbody></table>
<h3 data-id="heading-121">分组</h3>





















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>(?:x)</td><td>匹配x但不记录匹配结果</td></tr><tr><td>x(?=y)</td><td>当x后接y时匹配x</td></tr><tr><td>x(?!y)</td><td>当x后不是y时匹配x</td></tr></tbody></table>
<h3 data-id="heading-122">引用</h3>













<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>\1…\9</td><td><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>…</mo></mrow><annotation encoding="application/x-tex">1…</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.64444em;vertical-align:0em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="minner">…</span></span></span></span></span>9 返回九个在模式匹配期间找到的、最近保存的部分</td></tr></tbody></table>
<h3 data-id="heading-123">或迷失</h3>













<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>x`</td><td>y</td></tr></tbody></table>
<h2 data-id="heading-124">3. 模式修饰符</h2>





















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>g</td><td>全局模式，应用于所有字符串</td></tr><tr><td>i</td><td>区分大小写模式</td></tr><tr><td>m</td><td>多行匹配模式</td></tr></tbody></table>
<h2 data-id="heading-125">4. 属性</h2>
<h3 data-id="heading-126">实例属性</h3>

































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>global</td><td>检测是否设置g标记</td></tr><tr><td>ignoreCase</td><td>检测是否设置i标记</td></tr><tr><td>multiline</td><td>检测是否设置了m标记</td></tr><tr><td>lastIndex</td><td>开始检索下一个匹配项的字符位置</td></tr><tr><td>source</td><td>返回正则表达式的字符串表示</td></tr><tr><td>lastIndex</td><td>返回被查找字符串中下一次成功匹配的开始位置</td></tr></tbody></table>
<h3 data-id="heading-127">构造函数属性</h3>








































<table><thead><tr><th>编码</th><th>代码</th><th>详解</th></tr></thead><tbody><tr><td>$_</td><td>input</td><td>返回最近一次匹配的字符串</td></tr><tr><td>$&</td><td>lastMatch</td><td>返回最近一次的匹配项</td></tr><tr><td>$+</td><td>lastParen</td><td>返回最近一次匹配的捕获组</td></tr><tr><td>$`</td><td>leftContext</td><td>返回被查找的字符串中从字符串开始位置到最后匹配之前的位置之间的字符</td></tr><tr><td>$'</td><td>rightContext</td><td>返回被搜索的字符串中从最后一个匹配位置开始到字符串结尾之间的字符</td></tr><tr><td>$*</td><td>multiline</td><td>检测表达式是否采用多行模式匹配m</td></tr></tbody></table>
<h2 data-id="heading-128">5. 方法</h2>
<h3 data-id="heading-129">实例方法</h3>
<p><strong>exec</strong></p>
<p>exec 在字符串中执行匹配检索，返回结果数组</p>
<blockquote>
<p>派生属性</p>
<blockquote>
<p>index 匹配项在字符串中的位置
input 应用正则表达式的字符串
length 返回数组元素个数</p>
</blockquote>
</blockquote>
<p><strong>test</strong></p>
<p>test 在字符串中测试模式匹配，返回true或false</p>
<h3 data-id="heading-130">字符串方法</h3>

























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>match</td><td>找到一个或多个正则表达式的匹配</td></tr><tr><td>replace</td><td>替换与正则表达式匹配的子串</td></tr><tr><td>search</td><td>检索与正则表达式相匹配的值</td></tr><tr><td>split</td><td>把字符串分割为字符串数组</td></tr></tbody></table>
<h1 data-id="heading-131">DOM 基本操作</h1>
<h2 data-id="heading-132">0. DOM</h2>
<p>通过 HTML DOM，可访问 JavaScript HTML 文档的所有元素。</p>
<p>HTML DOM (文档对象模型)
当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。</p>
<h2 data-id="heading-133">1. 获取节点</h2>
<h3 data-id="heading-134">document</h3>





















<table><thead><tr><th>编码</th><th>语法</th></tr></thead><tbody><tr><td>getElementById</td><td>document.getElementById(元素ID)</td></tr><tr><td>getElementByName</td><td>document.getElementByName(元素name)</td></tr><tr><td>getElementByTagName</td><td>document.getElementByTagName(元素标签)</td></tr></tbody></table>
<h3 data-id="heading-135">节点指针</h3>








































<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>firstChild</td><td>父节点.firstChild</td><td>获取元素的首个子节点</td></tr><tr><td>lastChild</td><td>父节点.lastChild</td><td>获取元素的最后一个子节点</td></tr><tr><td>childNodes</td><td>父节点.childNodes</td><td>获取元素的子节点列表</td></tr><tr><td>previousSibling</td><td>兄弟节点.previousSibling</td><td>获取已知节点的前一个节点</td></tr><tr><td>nextSibling</td><td>兄弟节点.nextSibling</td><td>获取已知节点的后一个节点</td></tr><tr><td>parentNode</td><td>子节点.parentNode</td><td>获取已知节点的父节点</td></tr></tbody></table>
<h2 data-id="heading-136">2. 节点操作</h2>
<h3 data-id="heading-137">创建节点</h3>

























<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>createElement</td><td>document.createElement(元素标签)</td><td>创建元素节点</td></tr><tr><td>createAttribute</td><td>document.createAttribute(元素属性)</td><td>创建属性节点</td></tr><tr><td>createTextNode</td><td>document.createTextNode(文本内容)</td><td>创建文本节点</td></tr></tbody></table>
<h3 data-id="heading-138">插入节点</h3>




















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>appendChild</td><td>appendChild(所添加的新节点)</td><td>向节点的子节点列表的末尾添加新的子节点</td></tr><tr><td>insertBefore</td><td>insertBefore(所要添加的新节点，已知子节点)</td><td>在已知的子节点前插入一个新的子节点</td></tr></tbody></table>
<h3 data-id="heading-139">替换节点</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>replaceChild</td><td>replaceChild(要插入的新元素，将被替换的老元素)</td><td>将某个子节点替换为另一个</td></tr></tbody></table>
<h3 data-id="heading-140">复制节点</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>choneNode</td><td>需要被复制的节点.cloneNode(true/false)</td><td>创建指定节点的副本</td></tr></tbody></table>
<blockquote>
<p>true ：复制当前节点及其所有子节点<br>
false：仅复制当前节点</p>
</blockquote>
<h3 data-id="heading-141">删除节点</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>removeChild</td><td>removeChild(要删除的节点)</td><td>删除指定的节点</td></tr></tbody></table>
<h2 data-id="heading-142">3. 属性操作</h2>
<h3 data-id="heading-143">获取属性</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>getAttribute</td><td>元素节点.getAttribute(元素属性名)</td><td>获取元素节点中指定属性的属性值</td></tr></tbody></table>
<h3 data-id="heading-144">设置属性</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>setAttribute</td><td>元素节点.setAttribute(属性名,属性值)</td><td>创建或改变元素节点的属性</td></tr></tbody></table>
<h3 data-id="heading-145">删除属性</h3>















<table><thead><tr><th>编码</th><th>语法</th><th>功能</th></tr></thead><tbody><tr><td>removeAttribute</td><td>元素节点.removeAttribute(属性名)</td><td>删除元素中的指定属性</td></tr></tbody></table>
<h2 data-id="heading-146">4. 文本操作</h2>

































<table><thead><tr><th>编码</th><th>功能</th></tr></thead><tbody><tr><td>insertData(offset,String)</td><td>从offset指定的位置插入string</td></tr><tr><td>appendData(string)</td><td>将string插入到文本节点的末尾处</td></tr><tr><td>deleteDate(offset,count)</td><td>从offset起删除count个字符</td></tr><tr><td>replaceData(off,count,string)</td><td>从off将count个字符用string替代</td></tr><tr><td>splitData(offset)</td><td>从offset起将文本节点分成两个节点</td></tr><tr><td>substring(offset,count)</td><td>返回由offset起的count个节点</td></tr></tbody></table>
<h1 data-id="heading-147">Window 对象</h1>
<h2 data-id="heading-148">1. navigator 导航器对象</h2>

































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>appCodeName</td><td>返回浏览器的代码名</td></tr><tr><td>appName</td><td>返回浏览器的名称</td></tr><tr><td>appVersion</td><td>返回浏览器的平台和版本信息</td></tr><tr><td>cookieEnabled</td><td>返回指明浏览器中是否启用cookie的布尔值</td></tr><tr><td>platform</td><td>返回运行浏览器的操作系统平台</td></tr><tr><td>userAgent</td><td>返回由客户机发送服务器的user-agent头部的值</td></tr></tbody></table>
<h2 data-id="heading-149">2. screen 显示器对象</h2>





























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>availHeight</td><td>返回显示屏幕的可用高度</td></tr><tr><td>availWidth</td><td>返回显示屏幕的可用宽度</td></tr><tr><td>height</td><td>返回屏幕的像素高度</td></tr><tr><td>width</td><td>返回屏幕的像素宽度</td></tr><tr><td>colorDepth</td><td>返回屏幕颜色的位数</td></tr></tbody></table>
<h2 data-id="heading-150">3. history 历史对象</h2>





















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>back()</td><td>返回前一个URL</td></tr><tr><td>forward()</td><td>返回下一个URL</td></tr><tr><td>go()</td><td>返回某个具体页面</td></tr></tbody></table>
<h2 data-id="heading-151">4. location 位置对象</h2>
<p><strong>属性</strong></p>









































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>hash</td><td>设置或返回从井号(#)开始的URL</td></tr><tr><td>host</td><td>设置或返回主机名和当前URL的端口号</td></tr><tr><td>hostname</td><td>设置或返回当前URL的主机名</td></tr><tr><td>href</td><td>设置或返回完整的URL</td></tr><tr><td>pathname</td><td>设置或返回当前URL的路径部分</td></tr><tr><td>port</td><td>设置或返回当前URL的端口号</td></tr><tr><td>protocol</td><td>设置或返回当前URL的协议</td></tr><tr><td>search</td><td>设置或返回从问号(?)开始的URL</td></tr></tbody></table>
<p><strong>方法</strong></p>





















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>assign(URL)</td><td>加载新的文档</td></tr><tr><td>reload()</td><td>重新加载当前页面</td></tr><tr><td>replace(newURL)</td><td>用新的文档替换当前文档</td></tr></tbody></table>
<h2 data-id="heading-152">5. document 文档对象</h2>
<p><strong>集合</strong></p>

























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>anchors[]</td><td>描点对象数组</td></tr><tr><td>images[]</td><td>图片对象数组</td></tr><tr><td>links[]</td><td>连接对象数组</td></tr><tr><td>forms[]</td><td>表单对象数组</td></tr></tbody></table>
<p><strong>属性</strong></p>





























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>cookie</td><td>设置或返回与当前文档有关的所有cookie</td></tr><tr><td>domain</td><td>返回当前文档的域名</td></tr><tr><td>referrer</td><td>返回载入当前文档的文档的URL</td></tr><tr><td>title</td><td>返回当前文档的标题</td></tr><tr><td>URL</td><td>返回当前文档的URL</td></tr></tbody></table>
<p><strong>方法</strong></p>

























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>open()</td><td>打开一个新的文档，并擦除旧文档内容</td></tr><tr><td>close()</td><td>关闭文档输出流</td></tr><tr><td>write()</td><td>向当前文档追加写入文本</td></tr><tr><td>writeIn()</td><td>与write()相同，在<code><pre></code>中会追加换行</td></tr></tbody></table>
<h2 data-id="heading-153">6. 窗口控制</h2>








































<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>moveBy</td><td>moveBy(水平位移量,垂直位移量)</td><td>按照给定像素参数移动指定窗口</td></tr><tr><td>moveTo</td><td>moveTo(x,y)</td><td>将窗口移动到指定的指定坐标(x,y)处</td></tr><tr><td>resizeBy</td><td>resizeBy(水平,垂直)</td><td>将当前窗口改变指定的大小(x,y)<br>当x、y的值大于0时为扩大<br>当x、y的值小于0时为缩小</td></tr><tr><td>resizeTo</td><td>resizeTo(水平宽度,垂直宽度)</td><td>将当前窗口改成(x,y)大小，x、y分别为宽度和高度</td></tr><tr><td>scrollBy</td><td>scrollBy(水平位移量,垂直位移量)</td><td>将窗口中的内容按给定的位移量滚动<br>参数为整数时，正向滚动，否则反向滚动</td></tr><tr><td>scrollTo</td><td>scrollTo(x,y)</td><td>将窗口中的内容滚动到指定位置</td></tr></tbody></table>
<h2 data-id="heading-154">7. 焦点控制</h2>

















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>focus</td><td>得到焦点</td></tr><tr><td>blur</td><td>移出焦点</td></tr></tbody></table>
<h2 data-id="heading-155">8. 打开关闭窗口</h2>
<p><strong>open</strong></p>















<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>open</td><td>open("URL","窗口名称","窗口风格")</td><td>打开一个新的窗口，并在窗口中装载指定URL地址的网页</td></tr></tbody></table>
<blockquote>
<p>窗口风格</p>
<blockquote>








































<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>location</td><td>yes/no</td><td>是否显示地址栏</td></tr><tr><td>menubar</td><td>yes/no</td><td>是否显示菜单栏</td></tr><tr><td>resizable</td><td>yes/no</td><td>是否可以改变窗口大小</td></tr><tr><td>scrollbars</td><td>yes/no</td><td>是否允许出现滚动条</td></tr><tr><td>status</td><td>yes/no</td><td>是否显示状态栏</td></tr><tr><td>toolbar</td><td>yes/no</td><td>是否显示工具栏</td></tr></tbody></table>
</blockquote>
</blockquote>
<p><strong>close</strong></p>















<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>close</td><td>close()</td><td>自动关闭浏览器窗口</td></tr></tbody></table>
<h2 data-id="heading-156">9. 定时器</h2>






























<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>setTimeout</td><td>setTimeout(执行代码,毫秒数)</td><td>当到了指定多的毫秒数后，自动执行功能代码</td></tr><tr><td>clearTimeout</td><td>clearTimeout(定时器)</td><td>取消由setTimeout()设置的定时器</td></tr><tr><td>setInterval</td><td>setInterval(重复执行的代码,毫秒数)</td><td>按指定周期重复执行功能代码</td></tr><tr><td>clerInterval</td><td>clearInterval(时间间隔器)</td><td>取消由setInterval()设置的时间间隔器</td></tr></tbody></table>
<h2 data-id="heading-157">10. 对话框</h2>

























<table><thead><tr><th>编码</th><th>语法</th><th>详解</th></tr></thead><tbody><tr><td>alert</td><td>alert("提示字符串")</td><td>弹出警告框，在警告框内显示提示字符串文本</td></tr><tr><td>confirm</td><td>confirm("确认字符串")</td><td>显示一个确认框，在确认框内显示提示字符串<br>当用户单击“确认”按钮时该方法返回true,单击“取消”返回false</td></tr><tr><td>prompt</td><td>prompt("提示字符串","缺省文本")</td><td>显示一个输入框，在输入框内显示提示字符串<br>在输入文本框显示缺省文本，并等待用户输入<br>当用户单击“确认”按钮时，返回输入的字符串，点击“取消”时返回null</td></tr></tbody></table>
<h2 data-id="heading-158">11. 属性</h2>
<p><strong>状态栏</strong></p>

















<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>defaultStatus</td><td>改变浏览器状态栏的默认显示</td></tr><tr><td>status</td><td>临时改变浏览器状态栏的显示</td></tr></tbody></table>
<p><strong>窗口位置</strong></p>
<blockquote>
<p>IE</p>
<blockquote>
<p>screenLeft 声明窗口的左上角的X坐标 <br>
screeTop 声明窗口的左上角的Y坐标 <br>
document.body.scrollLeft 声明当前文档向右滚动过的像素数 <br>
document.body.scrollTop 声明当前文档向下滚动过的像素数</p>
</blockquote>
</blockquote>
<blockquote>
<p>!IE</p>
<blockquote>
<p>screenX 声明窗口的左上角的X坐标 <br>
screenY 声明窗口的左上角的Y坐标 <br>
pageXOffset 声明当前文档向右滚动过的像素数 <br>
pageYOffset 声明当前文档向下滚动过的像素数</p>
</blockquote>
</blockquote>
<blockquote>
<p>FF</p>
<blockquote>
<p>innerHeight 返回窗口的文档显示区的高度 <br>
innerWidth 返回窗口的文档显示区的宽度 <br>
outerHeight 返回窗口的外部高度 <br>
outerWidth 返回窗口的外部宽度</p>
</blockquote>
</blockquote>
<p><strong>其他属性</strong></p>

























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>opener</td><td>可以实现同域名下跨窗体之间的通讯<br>一个窗体要包含另一个窗体的opener</td></tr><tr><td>closed</td><td>当前窗口关闭时返回true</td></tr><tr><td>name</td><td>设置或返回窗口的名称</td></tr><tr><td>self</td><td>返回对当前窗口的引用</td></tr></tbody></table>
<h1 data-id="heading-159">JS 对象</h1>
<h2 data-id="heading-160">1. javascript 对象</h2>
<p>JavaScript 中的所有事物都是对象：字符串、数字、数组、日期，等等。</p>
<p>在 JavaScript 中，对象是数据（变量），拥有属性和方法。</p>
<blockquote>
<p>属性和方法</p>
<blockquote>
<p>属性是与对象相关的值。方法是能够在对象上执行的动作。<br>
在面向对象的语言中，属性和方法常被称为对象的成员。</p>
</blockquote>
</blockquote>
<h2 data-id="heading-161">2. 创建 javascript 对象</h2>
<p><strong>方法一：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Person = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>(); <span class="hljs-comment">// 声明一个空对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法二：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Person = &#123;&#125;;   <span class="hljs-comment">// 声明一个空对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-162">3. 对象属性及对象方法</h2>
<p><strong>JavaScript 属性</strong>
属性指的是与 JavaScript 对象相关的值。</p>
<p>JavaScript 对象是无序属性的集合。</p>
<p>属性通常可以被修改、添加和删除，但是某些属性是只读的。</p>
<p><strong>访问语法</strong>
<code>objectName.propertyName</code></p>
<p><strong>JavaScript 方法</strong></p>
<p>方法是存储为对象属性的函数。</p>
<p><strong>访问语法</strong>
<code>objectName.methodName()</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> Person = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
Person.name = <span class="hljs-string">"麋鹿鲁哟"</span>  <span class="hljs-comment">//设置对象属性</span>
Person.age = <span class="hljs-number">22</span>
Person.getDate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;  <span class="hljs-comment">//设置对象方法</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>();
&#125;

<span class="hljs-built_in">console</span>.log(Person) <span class="hljs-comment">// &#123;name: "麋鹿鲁哟", age: "22"&#125;</span>

<span class="hljs-built_in">console</span>.log(Person.name)  <span class="hljs-comment">// 麋鹿鲁哟      //访问对象属性</span>
<span class="hljs-built_in">console</span>.log(Person.getDate()) <span class="hljs-comment">//输出当前时间   //访问对象方法</span>

<span class="hljs-keyword">delete</span> Person.age  <span class="hljs-comment">// delete 关键词从对象中删除属性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>PS:对象的名称，对大小写敏感。</p>
</blockquote>
<h2 data-id="heading-163">4. 对象访问器(get、set)</h2>
<p><strong>为什么使用 Getter 和 Setter？</strong></p>
<ul>
<li>它提供了更简洁的语法</li>
<li>它允许属性和方法的语法相同</li>
<li>它可以确保更好的数据质量</li>
<li>有利于后台工作</li>
</ul>
<p><strong>JavaScript Getter（get 关键词）</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"麋鹿鲁哟"</span>,
  <span class="hljs-attr">age</span> : <span class="hljs-number">22</span>,
  <span class="hljs-keyword">get</span> <span class="hljs-title">lang</span>() &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.age;
  &#125;
&#125;;
<span class="hljs-built_in">console</span>.log(Person.lang)  <span class="hljs-comment">// 22 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>JavaScript Setter（set 关键词）</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> Person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"麋鹿鲁哟"</span>,
  <span class="hljs-attr">age</span> : <span class="hljs-number">22</span>,
  <span class="hljs-keyword">set</span> <span class="hljs-title">lang</span>(<span class="hljs-params">lang</span>) &#123;
    <span class="hljs-built_in">this</span>.age = lang;
  &#125;
&#125;;
<span class="hljs-comment">// 使用 setter 来设置对象属性：</span>
Person.lang = <span class="hljs-number">3</span>
<span class="hljs-built_in">console</span>.log(Person.age)  <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-164">5. 对象构造器</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.age = age;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数 Person() 就是对象构造器函数。</p>
<p>通过 new 关键词调用构造器函数可以创建相同类型的对象：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> me = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"麋鹿鲁哟"</span>,<span class="hljs-number">22</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>this 关键词</strong></p>
<p>在 JavaScript 中，被称为 this 的事物是代码的“拥有者”。</p>
<p>this 的值，在对象中使用时，就是对象本身。</p>
<p>在构造器函数中，this 是没有值的。它是新对象的替代物。 当一个新对象被创建时，this 的值会成为这个新对象。</p>
<p>请注意 this 并不是变量。它是关键词。您无法改变 this 的值。</p>
<h2 data-id="heading-165">6. JavaScript 对象原型</h2>
<p><strong>原型继承</strong></p>
<p>所有 JavaScript 对象都从原型继承属性和方法。</p>
<ul>
<li>日期对象继承自 Date.prototype。</li>
<li>数组对象继承自 Array.prototype。</li>
<li>Person 对象继承自 Person.prototype。</li>
<li>Object.prototype 位于原型继承链的顶端：</li>
<li>日期对象、数组对象和 Person 对象都继承自 Object.prototype。</li>
</ul>
<p><strong>prototype 属性</strong></p>
<p>JavaScript prototype 属性允许您为对象构造器添加新属性、方法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name,age</span>)</span>&#123;
  <span class="hljs-built_in">this</span>.name = name;
  <span class="hljs-built_in">this</span>.age = age;
&#125;
Person.prototype.github = <span class="hljs-string">"https://github.com/miluluyo"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-166">7. ES5 对象方法</h2>

























































<table><thead><tr><th>代码</th><th>详解</th></tr></thead><tbody><tr><td>Object.defineProperty(object, property, descriptor)</td><td>添加或更改对象属性</td></tr><tr><td>Object.defineProperties(object, descriptors)</td><td>添加或更改多个对象属性</td></tr><tr><td>Object.getOwnPropertyDescriptor(object, property)</td><td>访问属性</td></tr><tr><td>Object.getOwnPropertyNames(object)</td><td>以数组返回所有属性</td></tr><tr><td>Object.keys(object)</td><td>以数组返回所有可枚举的属性</td></tr><tr><td>Object.getPrototypeOf(object)</td><td>访问原型</td></tr><tr><td>Object.preventExtensions(object)</td><td>阻止向对象添加属性</td></tr><tr><td>Object.isExtensible(object)</td><td>如果可将属性添加到对象，则返回 true</td></tr><tr><td>Object.seal(object)</td><td>防止更改对象属性（而不是值）</td></tr><tr><td>Object.isSealed(object)</td><td>如果对象被密封，则返回 true</td></tr><tr><td>Object.freeze(object)</td><td>防止对对象进行任何更改</td></tr><tr><td>Object.isFrozen(object)</td><td>如果对象被冻结，则返回 true</td></tr></tbody></table>
<h2 data-id="heading-167">7. prototype 继承</h2>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">子类.prototype = <span class="hljs-keyword">new</span> 父类()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有的 JavaScript 对象都会从一个 prototype（原型对象）中继承属性和方法。</p>
<p>指向了一个对象，这个对象正式调用该构造函数而创建的实例的原型</p>
<p><strong><strong>proto</strong></strong></p>
<p>__proto__这是每一个 javascript 对象( null 除外)都具有的属性，这个属性会指向该对象的原型</p>
<h2 data-id="heading-168">8. Number 对象</h2>





























<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>toExponential()</td><td>可把对象的值转换成指数计数法。</td></tr><tr><td>toFixed()</td><td>可把 Number 四舍五入为指定小数位数的数字。</td></tr><tr><td>toPrecision()</td><td>方法可在对象的值超出指定位数时将其转换为指数计数法。</td></tr><tr><td>toString()</td><td>可把一个逻辑值转换为字符串，并返回结果。</td></tr><tr><td>valueOf()</td><td>可返回 Boolean 对象的原始值。</td></tr></tbody></table>
<h2 data-id="heading-169">9. Math (算数) 对象</h2>
<p>执行常见的算数任务。</p>

















































































<table><thead><tr><th>编码</th><th>详解</th></tr></thead><tbody><tr><td>abs(x)</td><td>返回 x 的绝对值。</td></tr><tr><td>acos(x)</td><td>返回 x 的反余弦值。</td></tr><tr><td>asin(x)</td><td>返回 x 的反正弦值。</td></tr><tr><td>atan(x)</td><td>以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。</td></tr><tr><td>atan2(y,x)</td><td>返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。</td></tr><tr><td>ceil(x)</td><td>对数进行上舍入。</td></tr><tr><td>cos(x)</td><td>返回数的余弦。</td></tr><tr><td>exp(x)</td><td>返回 Ex 的指数。</td></tr><tr><td>floor(x)</td><td>对 x 进行下舍入。</td></tr><tr><td>log(x)</td><td>返回数的自然对数（底为e）。</td></tr><tr><td>max(x,y,z,...,n)</td><td>返回 x,y,z,...,n 中的最高值。</td></tr><tr><td>min(x,y,z,...,n)</td><td>返回 x,y,z,...,n中的最低值。</td></tr><tr><td>pow(x,y)</td><td>返回 x 的 y 次幂。</td></tr><tr><td>random()</td><td>返回 0 ~ 1 之间的随机数。</td></tr><tr><td>round(x)</td><td>四舍五入。</td></tr><tr><td>sin(x)</td><td>返回数的正弦。</td></tr><tr><td>sqrt(x)</td><td>返回数的平方根。</td></tr><tr><td>tan(x)</td><td>返回角的正切。</td></tr></tbody></table>
<h1 data-id="heading-170">JSON</h1>
<h2 data-id="heading-171">1. JSON</h2>
<ul>
<li>JSON 指的是 JavaScript 对象标记法（JavaScript Object Notation）</li>
<li>JSON 是一种轻量级的数据交换格式</li>
<li>JSON 具有自我描述性且易于理解</li>
<li>JSON 独立于语言*</li>
</ul>
<p>JSON 是存储和传输数据的格式。</p>
<p>JSON 经常在数据从服务器发送到网页时使用</p>
<p><strong>交换数据</strong></p>
<p>当数据在浏览器与服务器之间进行交换时，这些数据只能是文本。</p>
<p>JSON 属于文本，并且我们能够把任何 JavaScript 对象转换为 JSON，然后将 JSON 发送到服务器。</p>
<p>我们也能把从服务器接收到的任何 JSON 转换为 JavaScript 对象。</p>
<p>以这样的方式，我们能够把数据作为 JavaScript 对象来处理，无需复杂的解析和转译。</p>
<h3 data-id="heading-172">JSON.parse()</h3>
<p>JSON 格式写的字符串转换为原生 JavaScript 对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">JSON</span>.parse()  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-173">JSON.stringify()</h3>
<p>JSON.stringify() 把 JavaScript 对象转换为字符串。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123; <span class="hljs-attr">name</span>:<span class="hljs-string">"麋鹿鲁哟"</span>, <span class="hljs-attr">age</span>:<span class="hljs-number">22</span>&#125;;
<span class="hljs-built_in">JSON</span>.stringify(obj)  
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-174">2. JSONP</h2>
<p>JSONP 是一种无需考虑跨域问题即可传送 JSON 数据的方法。</p>
<p>JSONP 不使用 XMLHttpRequest 对象。</p>
<p>JSONP 使用 <code><script></code> 标签取而代之。</p>
<p><strong>简介</strong>
JSONP 指的是 JSON with Padding。</p>
<p>从另一个域请求文件会引起问题，由于跨域政策。</p>
<p>从另一个域请求外部脚本没有这个问题。</p>
<p>JSONP 利用了这个优势，并使用 script 标签替代 XMLHttpRequest 对象。</p>
<p>就是利用script标签绕过同源策略，获得一个类似这样的数据，jsonpcallback是页面存在的回调方法，参数就是想得到的json。</p>
<blockquote>
<p>它只支持GET请求而不支持POST等其它类型的HTTP请求；它只支持跨域HTTP请求这种情况，不能解决不同域的两个页面之间如何进行JavaScript调用的问题</p>
</blockquote>
<h1 data-id="heading-175">Cookie</h1>
<h2 data-id="heading-176">1. Cookie</h2>
<p>Cookie实际上是一小段的文本信息，客户端请求服务器，如果服务器需要记录该用户状态，就使用 response 向客户端浏览器颁发一个Cookie。客户端会把Cookie存起来，当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器，服务器检查该Cookie，以此来辨认用户状态，服务器也可根据需求修改Cookie的内容</p>
<h2 data-id="heading-177">2. 优点</h2>
<ol>
<li>极高的扩展性和可用性</li>
</ol>
<p>可以控制保存在cookie中的session对象的大小；</p>
<p>通过加密和安全传输技术（SSL），减少Cookie被破解的可能性；</p>
<p>只在Cookie中存放不敏感数据，被盗不会有重大损失；</p>
<p>控制Cookie的生命期，使之不会永远有效，偷盗者可能会拿到一个过期的Cookie；</p>
<p>基于文本轻量结构；</p>
<p>Cookie存储在客户端并在发送后由服务器读取；</p>
<h2 data-id="heading-178">3. 缺点</h2>
<ol>
<li>Cookie 数量和长度的限制</li>
</ol>
<p>每个domain最多只能有20条cookie，每个cookie的长度不能超过4KB，否则被截掉；</p>
<ol start="2">
<li>安全性</li>
</ol>
<p>Cookie可能被拦截、篡改。如果Cookie被人拦截了，那人就可以取得所有的session信息</p>
<ol start="3">
<li>有些状态不可能保存在客户端</li>
</ol>
<p>例：防止重复提交表单，在服务端保存计数器，如果将此计数器保存在客户端，无用。</p>
<h2 data-id="heading-179">4. 延伸</h2>
<p><strong>Cookie 和 session 的区别</strong></p>
<ol>
<li>
<p>cookie数据 ==》 客户的浏览器     session数据 ==》 服务器</p>
</li>
<li>
<p>Cookie不是很安全，别人可以分析存放在本地的Cookie并进行Cookie欺骗，考虑到安全应当使用session</p>
</li>
<li>
<p>session会在一定时间内保存在服务器上，当访问增多，会比较占用服务器的性能，考虑到减轻服务器性能方面，应当使用Cookie</p>
</li>
<li>
<p>单个Cookie数据不能超过4K，很多浏览器都限制一个站点最多保存20个Cookie</p>
</li>
</ol>
<blockquote>
<p>建议：</p>
<blockquote>
<ul>
<li>登录信息等重要信息存放session</li>
<li>其他信息如果要保留，可以放在Cookie</li>
</ul>
</blockquote>
</blockquote></div>  
</div>
            