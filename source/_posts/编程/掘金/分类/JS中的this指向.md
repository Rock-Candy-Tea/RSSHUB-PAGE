
---
title: 'JS中的this指向'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1339'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 06:34:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=1339'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><code>this</code>作为Javascript语言中的一个关键字。它代表函数运行时，自动生成的一个内部对象，只能在函数内部使用。简言之，<code>this</code>是用来指向对象。今天就一下几方面学习一下<code>this</code>：</p>
<blockquote>
<p>一般函数 箭头函数 对象 严格模式</p>
</blockquote>
<h2 data-id="heading-0">一般函数</h2>
<p><strong>独立函数调用,<code>this</code>指向全局对象</strong></p>
<pre><code class="copyable">var a = 'foo';
function foo()&#123;
    console.log(this.a);
&#125;
foo();  //foo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里函数<code>foo()</code>中的<code>this</code>指向全局对象。</p>
<p><strong>严格模式,<code>this</code>绑定undefined</strong></p>
<pre><code class="copyable">var a = 'foo';
function foo()&#123;
    'use strict'
    console.log(this.a);
&#125;
foo();  //TypeError: Cannot read property 'a' of undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在严格模式下，<code>foo()</code>中<code>this</code>指向<code>undefined</code>，所以报错。</p>
<h2 data-id="heading-1">箭头函数</h2>
<pre><code class="copyable">var a = 'foo';
var obj = &#123;
    a : 1,
    foo : ()=>&#123;console.log(this.a)&#125;

&#125;;
obj.foo(); //foo (use strict : foo)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数体内的<code>this</code>对象,就是<code>定义该函数时所在的作用域指向的对象</code>,而不是使用时所在的作用域指向的对象.</p>
<blockquote>
<p>不可以当作构造函数,也就是说不可以使用new命令<br>
不可以使用arguments对象,可以使用rest参数代替<br>
不可以使用yield命令,因此不能用作Generator函数</p>
</blockquote>
<h2 data-id="heading-2">对象</h2>
<pre><code class="copyable">function foo()&#123;
console.log(this.a);
&#125;
var obj1 = &#123;
a : 1,
foo : foo
&#125;;
var obj2 = &#123;
a : 2,
obj1 : obj1
&#125;;
obj2.obj1.foo(); //1
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var a = 'foo';
function foo()&#123;
console.log(this.a);
&#125;
var obj = &#123;
a : 2,
foo : foo
&#125;;
var bar = obj.foo;
bar(); //foo
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">var a = 'foo';
function foo()&#123;
console.log(this.a);
&#125;
function doFoo(fn)&#123; //fn = obj.foo  隐式赋值
fn();
&#125;
var obj = &#123;
a : 2,
foo : foo
&#125;;
doFoo(obj.foo);  //foo
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">练习题</h2>
<hr>
<p><strong>题1</strong></p>
<p><strong>严格模式下</strong></p>
<pre><code class="copyable">'use strict'
var a = 10;
function foo()&#123;
    console.log('this1',this);
    console.log(window.a);
    console.log(this.a);
&#125;
console.log(window.foo);
console.log('this2',this);
foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果:</p>
<pre><code class="copyable">f foo()&#123;...&#125;  
this2 Window&#123;...&#125;  
this1 undefined  
10  
TypeError: Cannot read property 'a' of undefined  
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>全局环境中,<code>this</code>会返回顶层对象.但是,node模块和ES6模块中,<code>this</code>返回的是当前模块<br>
函数里面的<code>this</code>,如果函数不是作为对象的方法运行,而是单纯作为函数运行,<code>this</code>会指向顶层对象.但是严格模式下,<code>this</code>会返回<code>undefined</code></p>
</blockquote>
<hr>
<p><strong>题2</strong></p>
<pre><code class="copyable">let a = 10;
const b = 20;

function foo()&#123;
    console.log(this.a); //undefined
    console.log(this.b); //undefined
&#125;
console.log(window.a); //undefined
foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ES5中顶层对象的属性与全局变量是等价的<br>
ES6中,var命令和function命令声明的全局变量,依旧是顶层对象的属性<br>
let、const、class命令声明的全局变量,不属于顶层对象的属性</p>
</blockquote>
<hr>
<p><strong>题3</strong></p>
<pre><code class="copyable">var name = 'windowsName';
function sayName()&#123;
    var name = 'Jake';
    console.log(this.name);  //windowsName  (严格模式下:TypeError)
    console.log(this); //Window
&#125;
sayName(); //window.sayName()
console.log(this); //Window
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>function this</code>对于函数中<code>this</code>:运行时this永远指向最后调用它的那个对象</p>
<hr>
<p><strong>题4</strong></p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.age);
&#125;

var obj1 = &#123;
    age : 23,
    foo : foo
&#125;;

var obj2 = &#123;
    age : 18,
    obj1 : obj1
&#125;;

obj2.obj1.foo(); //23
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后调用foo()的是obj1,所以this指向obj1</p>
<hr>
<p><strong>题5</strong></p>
<p>隐式绑定的隐式丢失问题 第一种:使用另一个变量给函数取别名会发生隐式丢失</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.a)
&#125;;
var obj = &#123; a : 1, foo&#125;;
var a = 2;
var foo2 = obj.foo;

obj.foo(); //1
foo2();  //2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二种:</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.a)
&#125;
var obj = &#123;a:1,foo&#125;;
var obj2 = &#123;a:3, foo2: obj.foo&#125;;
obj2.foo2(); //3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三种:</p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.a)
&#125;
function doFoo(fn)&#123;
    console.log(this);  //window
    fn();
&#125;
var obj = &#123;a:1,foo&#125;
var a = 2;
doFoo(obj.foo);  //2
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>题6</strong></p>
<p>构造函数中的<code>this</code><br>
<code>new</code>的过程</p>
<pre><code class="copyable">var a = new Foo("zhang","jake");

new Foo&#123;
    var obj = &#123;&#125;;
    obj.__proto__ = Foo.prototype;
    var result = Foo.call(obj,"zhang","jake");
    return typeof result === 'obj'?result:obj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>new</code>的过程如下:</p>
<blockquote>
<p>创建新对象obj; 给新对象的内部属性赋值,构造原型链(将新对象的隐式原型指向其构造函数的显示原型); 执行函数Foo,执行过程中内部this指向新创建的对象obj 如果Foo内部显式返回对象类型数据,则返回该数据,执行结束;否则返回新创建的对象obj</p>
</blockquote>
<pre><code class="copyable">var name = 'Jake';
function testThis()&#123;
    this.name = 'jakezhang';
    this.sayName = function ()&#123;
        return this.name;
    &#125;
&#125;
console.log(this.name);  //Jake

new testThis();
console.log(this.nam);  //Jake

var result = new testThis();
console.log(result.name);  //jakezhang
console.log(result.sayName());  //jakezhang

testThis();
console.log(this.name);  //jakezhang
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>题7</strong></p>
<pre><code class="copyable">function foo()&#123;
    console.log(this.a);  //1
    bar.apply(&#123;a:2&#125;,arguments);
&#125;
function bar(b)&#123;
    console.log(this.a + b); //5
&#125;
var a = 1;
foo(3);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>call、apply、bind都可以改变函数的this指向</p>
<hr>
<p><strong>题8</strong></p>
<pre><code class="copyable">var name = 'window'
var obj1 = &#123;
  name: 'obj1',

  foo1: function () &#123;
    console.log(this.name)
    return () => &#123;
      console.log(this.name)
    &#125;
  &#125;,

  foo2: () => &#123;
    console.log(this.name)
    return function () &#123;
      console.log(this.name)
    &#125;
  &#125;
&#125;


var obj2 = &#123;
  name: 'obj2'
&#125;
obj1.foo1.call(obj2)() //2 2
obj1.foo1().call(obj2)  //1 1
obj1.foo2.call(obj2)()  //window window
obj1.foo2().call(obj2)  //window 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数中的<code>this</code></p>
<blockquote>
<p>箭头函数中没有 this 绑定，必须通过查找作用域链来决定其值<br>
箭头函数被非箭头函数包含，则 this 绑定的是最近一层非箭头函数的 this<br>
箭头函数的 this 始终指向函数定义时的 this，而非执行时。</p>
</blockquote></div>  
</div>
            