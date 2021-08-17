
---
title: 'ES6的symbol数据类型'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4661'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 02:00:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=4661'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">symbol数据类型</h2>
<p>js语言中，ES6前有6种数据类型。</p>
<p>ES6新提出symbol数据类型，所以symbol是js的第七种数据类型，表示独一无二的值。是一种类似于字符串的数据类型。</p>
<p><strong>symbol出现的原因</strong></p>
<p>ES5 的对象属性名都是字符串，这容易造成属性名的冲突。比如，你使用了一个他人提供的对象，但又想为这个对象添加新的方法（mixin 模式），新方法的名字就有可能与现有方法产生冲突。如果有一种机制，保证每个属性的名字都是独一无二的就好了，这样就从根本上防止属性名的冲突。这就是 ES6 引入<code>Symbol</code>的原因</p>
<p><strong>Symbol特点</strong></p>
<ol>
<li>
<p>Symbol的值是唯一的，用来解决命名冲突的问题</p>
</li>
<li>
<p>Slymbol 值不能与其他数据进行运算</p>
</li>
<li>
<p>Symbol 定义的对象属性不能使用fr..in 循环遍历，但是可以使用Reflect.ownKeys来获取对象的所有键名</p>
</li>
<li>
<p><code>Symbol</code>函数前不能使用<code>new</code>命令，否则会报错。这是因为生成的 Symbol 是一个原始类型的值，不是对象。也就是说，由于 Symbol 值不是对象，所以不能添加属性。基本上，它是一种类似于字符串的数据类型。</p>
</li>
</ol>
<pre><code class="copyable">//创建Symbol
let s= Symbol();
console.log(s, typeof s);


// 试试创建2个symbol相同
let s2 = Symbol(' 辣鸡rb');
let s3 = Symbol(' 辣鸡rb');
console.log(s2 === s3); //false


//用Symbol.for创建一样的symbol
let s4 = Symbol.for('辣鸡rb');
let s5 = Symbol.for('辣鸡rb');
console.log(s4 === s5); //true


//不能与其他数据进行运算
let result = s + 100;//报错，
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文章结尾回顾一下js的数据类型
引用尚硅谷的一个记忆口诀</p>
<pre><code class="copyable">// USONB =>you are so .niubility 你是如此牛逼

// u=>undefined

// s=>string symbol

// 0=>object

// n=>null number

// b=>boolean
<span class="copy-code-btn">复制代码</span></code></pre>
<p>思考一下，决定再写点，</p>
<h2 data-id="heading-1">symbol的应用</h2>
<h3 data-id="heading-2">在rb对象中添加up和down方法</h3>
<p><strong>方法1</strong></p>
<pre><code class="copyable">let rb = &#123;
    name: '日本战犯',
    age: 500,
&#125;;
// 用symbol处理
// 声明对象，里面包含两个方法，方法用symbol()写
let methods = &#123;
    up: Symbol(),
    down: Symbol()
&#125;;
// 把方法加进去
rb[methods.up] = function () &#123;
    console.log('原谅说的是人');
&#125;;
rb[methods.down] = function () &#123;
    console.log('畜生没脸让中华儿女原谅它');
&#125;;
console.log(rb);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法2</strong></p>
<p>在rb对象中添加sb和dsb方法</p>
<pre><code class="copyable">let rb = &#123;
    name: '日本战犯',
    age: 500,
    [Symbol('sb')]: function () &#123;
        console.log('我喜欢日本动画');
    &#125;,
     [Symbol('dsb')]: function () &#123;
         console.log('但不妨碍我恨他们在华夏大地犯的罪');
     &#125;,
&#125;;

console.log(rb);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            