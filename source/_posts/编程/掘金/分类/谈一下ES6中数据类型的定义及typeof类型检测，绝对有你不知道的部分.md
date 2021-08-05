
---
title: '谈一下ES6中数据类型的定义及typeof类型检测，绝对有你不知道的部分'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba6d7cf92ab44f0aba1686df3312177a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 17:25:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba6d7cf92ab44f0aba1686df3312177a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天</strong></p>
<h3 data-id="heading-0">js中的数据类型</h3>
<h4 data-id="heading-1"> 原始值类型</h4>
<ul>
<li> 1. number:NaN[不是一个有效数字]、Infinity[无穷大的值]</li>
<li> 2. string</li>
<li>3. boolean</li>
<li> 4. null</li>
<li> 5. undefined</li>
<li> 6. symbol</li>
<li> 7. bigint</li>
</ul>
<h4 data-id="heading-2">对象类型</h4>
<ul>
<li> 标准普通对象 object</li>
<li>标准特殊对象 Array/Regexp/Date/Error/Math/ArrayBuffer/DataView/Set/Map。。。</li>
<li> 非标准特殊对象 Number/Sring/Boolean/Symbol/Bigint</li>
<li> 可调用对象 【实现了call方法】function</li>
</ul>
<h3 data-id="heading-3">symbol类型</h3>
<h4 data-id="heading-4">1.对象的唯一属性</h4>
<p> 如果想要拿到Symbol()的值</p>
<h5 data-id="heading-5">方法1</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> key = <span class="hljs-built_in">Symbol</span>()
<span class="hljs-keyword">let</span> obj = &#123;
    [key]: <span class="hljs-number">100</span>
&#125;
<span class="hljs-built_in">console</span>.log(obj[key]) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">方法2</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj) <span class="hljs-comment">//获得当前对象所有的Symbol属性</span>
arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(obj[item])
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.宏观管理标识：保证标志的唯一性（vuex/redux）</h4>
<h4 data-id="heading-8">3.底层原理</h4>
<ul>
<li>Symbol.hasInstance</li>
<li>Symbol.iterator</li>
<li>Symbol.toPrimitive</li>
<li>Symbol.toStringTag</li>
<li>......</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba6d7cf92ab44f0aba1686df3312177a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">typeof的语法</h3>
<p><strong>typeof是一个运算符，有2种使用方式：typeof(表达式)和typeof 变量名，第一种是对表达式做运算，第二种是对变量做运算。</strong></p>
<h4 data-id="heading-10">数据类型检测</h4>
<ul>
<li> 1. typeof 运算符</li>
<li> 2. instanceof [本意：检测实例是否属于某类]</li>
<li> 3. constructor [本意：获取构造函数]</li>
<li> 4. Object.prototype.toString.call([value]) 检测数据类型</li>
<li> 5. Array.isArray([value]) 检测一个值是否为数组</li>
</ul>
<h4 data-id="heading-11">typeof[value]</h4>
<ul>
<li>1. 返回[value]所属类型的字符串 例如'Number'/'String'...</li>
<li>2. 不能检测null typeod null -> 'Object'</li>
<li>3. 除可调用对象[函数]会返回'function' [不论是箭头函数、构造函数、生成器函数、普通函数都返回'function'] 其余的对象数据值返回的都是'Object'</li>
<li> 4. 检测一个未被申明的变量不会报错，返回undefined</li>
</ul>
<h6 data-id="heading-12">GetValue(val) [浏览器内部提供的方法C++]，按照值存储的二进制进行检测</h6>
<ul>
<li>  + 对象 000 -> 函数实现了call，则返回'function' 没实现call返回'object'</li>
<li>  + null 000000 -> 没实现call返回'object'</li>
<li>  + undefined -2^30</li>
<li>  + 数字 -> 整数1 浮点数010</li>
<li>  + 字符串 -> 100</li>
<li>  + 布尔 -> 110</li>
</ul>
<h6 data-id="heading-13">typeof 检测数据类型还是很快的，检测原始值类型[除了null，还是很准确的]</h6>
<h6 data-id="heading-14"></h6>
<p>字面量:原始值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> n = <span class="hljs-number">10</span>
<span class="hljs-comment">// 构造函数</span>
<span class="hljs-keyword">let</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Number</span>(<span class="hljs-number">10</span>);
<span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Object</span>(<span class="hljs-number">10</span>);
<span class="hljs-comment">// 不允许被new的</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Symbol</span>()  <span class="hljs-comment">// Uncaught TypeError: Symbol is not a constructor</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">BigInt</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">最大安全数字：9007199254740991 超过这个数字进行运算就不准确了</h6>
<h6 data-id="heading-16">console.log(Number.MAX_SAFE_INTEGER,Number.MIN_SAFE_INTEGER)</h6>
<h6 data-id="heading-17">问题：服务器中有longInt 长整型这种值，如果把这样的值返回客户端，则客户端无法进行有效的处理</h6>
<h6 data-id="heading-18">[一般服务器都是以字符串的形式返回，但是字符串进行计算还是需要转换为数字才可以，还是不准确]</h6>
<p>9007199254740991n-1n 数字后面加n就是bigint类型
9007199254741000n.toString() =>返给服务器</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f1069f0122d448e97824c22858eba11~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em><strong>前端路漫漫其修远兮，吾将上下而求索，一起加油，学习前端吧!</strong></em></p></div>  
</div>
            