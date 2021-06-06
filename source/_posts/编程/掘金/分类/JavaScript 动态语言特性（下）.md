
---
title: 'JavaScript 动态语言特性（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6907'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 18:10:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=6907'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<p>上一章我们聊了variables, types和 object，接下来聊一下string, array, function, eval, conditions。</p>
<h2 data-id="heading-0">string</h2>
<h3 data-id="heading-1">string</h3>
<pre><code class="copyable">// 不要尝试这种做法
1 < 'a'; // false
1 > 'a'; // false
1 == 'a'; // false

//总之，语句结束无比加分号！！
var a = 1;
var b= 2;
var foo = function () &#123;
    console.log(arguments);
&#125;
`$&#123;a&#125; + $&#123;b&#125; = $&#123;a+b&#125;` // [[",'+','=',"],1,2,3]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>特性</em> ：</p>
<ul>
<li>Immutable</li>
</ul>
<p><em>陷阱</em> ：</p>
<ul>
<li>不存在char类型</li>
<li>小心模板字符串潜在的语法问题</li>
<li>字符串与数字比较时，总是转成数字</li>
</ul>
<h3 data-id="heading-2">string-模式</h3>
<p>1、 字符串拼接、多行字符串尽可能采用模板字符串的语法</p>
<p>2、更复杂的字符串拼接场景使用模板引擎</p>
<p>3、禁止把字符串当成代码直接运行</p>
<p>4、显示在页面上的字符串必须转义</p>
<p>5、使用字面量定义字符串</p>
<h2 data-id="heading-3">array</h2>
<h3 data-id="heading-4">array-动态特性</h3>
<pre><code class="copyable">// 避免对数组设置属性值
const arr = [1,2,3];
arr.name = 'some thing';

// 禁止对数组使用for...in遍历
for(let key in arr) &#123;
    console.log(key);
&#125;

// 禁止直接操作数组长度
arr.length = 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>特性</em> ：</p>
<ul>
<li>基于对象</li>
<li>允许混合类型（ES6新增typed array）</li>
<li>数组长度动态分配</li>
<li>支持稀疏数组</li>
</ul>
<h3 data-id="heading-5">array-遍历</h3>
<p><em>特性</em> ：</p>
<ul>
<li>支持大量遍历方法</li>
<li>for...of</li>
<li>展开操作符</li>
</ul>
<h3 data-id="heading-6">array-类数组对象</h3>
<pre><code class="copyable">// 借用数组原型方法
const arrayLike = &#123;length: 1, '1': 1 &#125;;
const array = [].slice.call(arrayLike, 0&#125;;

//转换
const arr = Array.from(arrayLike);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>特性</em> ：</p>
<ul>
<li>duck typing</li>
<li>Array.from</li>
</ul>
<h3 data-id="heading-7">array-模式</h3>
<p>1、不适用for...in 遍历数组</p>
<p>2、使用字面量定义数组</p>
<p>3、不操作数组长度</p>
<p>4、注意mutator可能引发的负作用</p>
<p>5、不在遍历方法中操作原数组</p>
<p>6、尽量不给数组添加非正整数的key</p>
<h2 data-id="heading-8">function</h2>
<h3 data-id="heading-9">function-动态特性</h3>
<pre><code class="copyable">// 古老的做法
let makeTeam = function (leader) &#123;
  const members = [].slice.call(arguments, 1);
  return Team.regester(&#123;
    leader,
    members
  &#125;);
&#125;;

// better
let makeTeam = function (...args) &#123;
  const [leader, ...members] = args;
  return Team.regester(&#123;
    leader,
    members
  &#125;);
&#125;;

// (伪)多返回值
function foo() &#123;
  return &#123;name: 'Jack', age: 18&#125;;
&#125;
const &#123;name, age&#125; = foo();

// 获取函数定义
function add(a, b) &#123; return a + b; &#125;
console.log(add.toString());

// 'function add(a, b) &#123; return a + b; &#125;'
const addTwo = (function () &#123;
const increase = 2;
  return function (a) &#123; return add(a, increase); &#125;;
&#125;)();
console.log(addTwo.toString());
// 'function (a) &#123; return add(a, increase); &#125;'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>特性</em> :</p>
<ul>
<li>动态参数列表</li>
<li>基于解构的多返回值</li>
<li>caller/callee</li>
<li>动态this</li>
<li>获取函数定义</li>
</ul>
<h3 data-id="heading-10">function-一等公民</h3>
<pre><code class="copyable">// 函数可以作为其他函数的参数或返回值
function once(func) &#123;
  let invoked = false;
  return function () &#123;
    if (!invoked) &#123;
      invoked = true;
      return func();
    &#125;
  &#125;
&#125;

function log() &#123;
  console.log('logged');
&#125;

const logOnce = once(log);

// 函数表达式
const half = function (a) &#123;
  return a / 2;
&#125;;

// oops...
const double = function (arr) &#123;
  return [...arr, ...arr];
&#125;
([1, 2, 3]).forEach(item => console.log(item));
// 1, 2, 3, 1, 2, 3

// IIFE
const tds = document.querySelectorAll('td');
  for (let i = 0; i < tds.length; i++) &#123;
    tds[i].onclick = (function (i) &#123;
    return function () &#123;
      alert(i);
    &#125;
  &#125;)(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>特性</em> ：</p>
<ul>
<li>高阶函数</li>
<li>闭包</li>
<li>函数式编程</li>
<li>函数定义与函数表达式</li>
<li>立即执行函数表达式（IIFE）</li>
</ul>
<h3 data-id="heading-11">function-模式</h3>
<p>1、尽量使用函数定义，而非函数表达式</p>
<p>2、禁止使用Function构造函数</p>
<p>3、避免使用arguments，而应该使用rest操作符及解构</p>
<p>4、尽可能编写纯函数</p>
<p>5、尽可能不修改（mutate）函数参数的内容</p>
<p>6、多采用箭头函数</p>
<h2 data-id="heading-12">eval</h2>
<p>1、禁止使用eval</p>
<p>2、禁止使用Function构造函数</p>
<p>3、使用setTimeout/ setInterval时，第一个参数禁止使用代码字符串</p>
<h2 data-id="heading-13">conditions</h2>
<p>1、禁止不同类型的数据进行比较</p>
<p>2、禁止使用==和!=，需使用===和!==</p>
<p>3、仅可对number和string进行大小比较</p>
<p>4、避免复杂逻辑运算，如果有必要，请加括号</p>
</div>  
</div>
            