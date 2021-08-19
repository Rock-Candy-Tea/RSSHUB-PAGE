
---
title: 'JavaScript语言基础（七）函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9757'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 19:48:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=9757'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>函数实际上是对象，每个函数都是Function的实例，而Function也有属性和方法，和其他引用类型一样。</p>
<h1 data-id="heading-0">函数定义方式</h1>
<p>函数名就是指向函数对象的指针，而且不一定与函数本身紧密绑定。</p>
<h2 data-id="heading-1">函数声明方式【通常】</h2>
<pre><code class="copyable">function sum(num1, num2)&#123;
return num1+num2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>函数定义最后没有分号。</strong></p>
<h2 data-id="heading-2">函数表达式</h2>
<pre><code class="copyable">let sum = function(num1, num2)&#123;
return num1+num2;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时function关键字后面没有名称，这个函数通过sum变量来引用。这里函数末尾是有分号的，与任何变量初始化语句一样。</strong></p>
<h2 data-id="heading-3">“箭头函数”方式</h2>
<pre><code class="copyable">let sum = (num1, num2) => &#123;
return num1+num2;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">使用Function构造函数【不推荐使用】</h2>
<pre><code class="copyable">let sum = new Funtion("num1", "num2", "return num1+num2");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可接收多个参数，最后一个函数始终是函数体，之前的参数都是函数的参数。</p>
<h1 data-id="heading-5">箭头函数</h1>
<p>ES6新增使用胖箭头（=>）语法定义函数表达式的能力。<strong>任何使用函数表达式的地方，都可以使用箭头函数。</strong></p>
<p>非常适合嵌入函数的场景</p>
<pre><code class="copyable">let ints = [1,2,3];

console.log(ints.map(function(i)&#123; return i+1; &#125;));// [2,3,4]
console.log(ints.map((i) => &#123; return i+1; &#125;));// [2,3,4]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若只有一个参数，可以不用括号。如果<strong>没有参数或多个参数，则需使用括号</strong>。</p>
<p>箭头函数不能使用arguments、super和new.target，也不能用作构造函数，也没有prototype属性。</p>
<h1 data-id="heading-6">函数名</h1>
<p>一个函数可以有多个名称，因为函数名就是指向函数的指针，所以它们跟其它包含对象指针的变量具有相同的行为。</p>
<pre><code class="copyable">function sum(num1, num2)&#123;
return num1+num2;
&#125;
console.log(sum(10, 10));// 20

let anothor = sum;
console.log(another(10, 10));// 20

sum = null;
console.log(sum(10, 10));// 20
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用不带括号的函数名会访问函数指针，而不会执行函数。</strong>
把sum设置为null之后，就切断了它与函数之间的关联，而another（）还是可以照常调用。</p>
<p>ES6的所有函数对象都暴露了一个只读的name属性，多数情况下，保存的是一个函数标识符，或者是一个字符串化的变量名。即使函数没有名称，也会如实显示成空字符串。
如果它使用Function构造函数创建的，则会标识成”anonymous“。</p>
<pre><code class="copyable">function f1() &#123;&#125;
let f2 = function()&#123;&#125;；
let f3 = () => &#123;&#125;;

console.log(f1.name);// f1
console.log(f2.name);// f2
console.log(f3.name);// f3
console.log((() => &#123;&#125;).name);// (空字符串)
console.log((new Function()).name);// anonymous
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果函数是一个设置函数、获取函数，或者使用bind（）实例化，则标识符前面会添加前缀：</p>
<pre><code class="copyable">function foo()&#123;&#125;
console.log(foo.bind(null).name);// bound foo

let dog = &#123;
years : 1,
get age()&#123;
return this.years;
&#125;,
set age(newAge)&#123;
this.years = newAge;
&#125;
&#125;
let pd = Object.getOwnPropertyDescriptor(dog, 'age');
console.log(pd.get.name);// get age
console.log(pd.set.name);// set age
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">理解参数</h1>
<p>ES函数的参数与大多数其它语言不同，既不关心传入参数的个数，也不关心这个参数的数据类型。</p>
<p>主要因为ES函数的参数在内部表现为一个数组。事实上，在使用function定义（非箭头）函数时，可以在函数内部访问arguments对象，从中取得传进来的每个参数值。</p>
<p>arguments对象是一个类数组对象（但不是Array的实例），可以使用中括号来访问其中的元素（如第一个参数为arguments[0]），若要确定传进来参数的个数，可以访问arguments.length属性。</p>
<p>把函数重写成不声明参数也可以：</p>
<pre><code class="copyable">function sayHi()&#123;
console.log("Hello "+ arguments[0] +","+ argments[1]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES函数的参数并不是必须写出来的。</strong>
与其他语言不同，在ES中的命名参数不会创建让之后的调用必须匹配的函数签名，因为根本不存在验证命名参数的机制。</p>
<p><strong>arguments对象可以跟命名参数一起使用：</strong></p>
<pre><code class="copyable">function doAdd(num1, num2)&#123;
if(arguments.length === 1)&#123;
console.log(num1 + 10);// 命名参数num1保存着与arguments[0]一样的值，使用谁都无所谓。
&#125;else if(arguments.length === 2)&#123;
console.log(arguments[0] + num2);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>arguments对象的值会与对应的命名参数同步。</strong></p>
<pre><code class="copyable">function doAdd(num1, num2)&#123;
arguments[1] = 10;
console.log(arguments[0] + num2);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子，修改了arguments[1]也会修改num2的值。并不意味着访问同一个内存地址，它们在内存中还是分开的，只不过是保持同步而已。</p>
<p>若只传一个参数，然后设置arguments[1]为某个值，则这个值不会反映到第二个命名参数，因为arguments对象的长度是传入的参数个数，而不是定义函数时的命名参数个数确定的。</p>
<p>对于命名参数而言，若调用函数时没有传这个参数，则这个值为undefined。
严格模式下，若给arguments[1]赋值，不会影响到num2的值。在函数中尝试重写arguments对象会导致语法错误。（代码也不会执行）</p>
<p>箭头函数中的参数
不能使用arguments关键字访问，而<strong>只能通过定义的命名参数访问</strong>。</p>
<p>可以在包装函数中把它提供给箭头函数：</p>
<pre><code class="copyable">function foo()&#123;
let bar = () =>&#123;
console.log(arguments[0]);// 5
&#125;;
bar();
&#125;
foo(5);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES中的所有参数都按值传递的。不可能按引用传递参数。如果把对象作为参数传递，则传递的值就是这个对象的引用。</strong></p>
<h1 data-id="heading-8">没有重载</h1>
<p>ES函数没有签名，因为参数是由包含0或多个值的数组表示的。没有函数签名，自然也没有重载。</p>
<p>若ES中定义了<strong>两个同名函数</strong> ，则后面定义的会<strong>覆盖</strong>先定义的。
把函数名当作指针有助于理解为什么ES没有函数重载。</p>
<pre><code class="copyable">let addNum = function(num)&#123;
return num+100;
&#125;;
addNum = function(num)&#123;
return num-100;
&#125;;
let result = addNum(200);// 100
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">默认参数值</h1>
<p>在ES5.1及之前，实现默认参数的一种常用方式就是检测某个参数是否等于undefined。
如果是则意味着没有传这个参数，则给它赋一个值。</p>
<p>ES6之后，支持显式定义默认参数。只要在函数定义中的参数后面用=就可以为参数赋一个默认值。</p>
<pre><code class="copyable">function makeKing(name = 'Henry')&#123;
return 'King $(name) VIII';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给参数传undefined相当于没有传值，不过这样可以利用多个独立的默认值。</p>
<p>在使用默认参数时，<strong>arguments对象的值</strong>不反映参数的默认值，<strong>只反映传给函数的参数</strong>。
与ES5严格模式一样，修改命名参数也不会影响arguments对象，始终以调用函数时传入的值为准。</p>
<pre><code class="copyable">function makeKing(name = 'Henry')&#123;
name = 'CLN';
return 'King $(arguments[0])';
&#125;
console.log(makeKing());// 'King undefined'
console.log(makeKing('JK'));// 'King JK'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认参数值并不限于原始值或对象类型，也可以使用调用函数返回的值。</p>
<pre><code class="copyable">function makeKing(name = 'Henry', numerals = getNumerals())&#123;
return 'King $(name) $(numerals)';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数的默认参数只有在函数被调用时才会求值，不会在函数定义时求值。计算默认值的函数只有在调用函数但未传相应参数时才会被调用。</p>
<p>箭头函数同样也可使用默认参数，只不过在只有一个参数时，必须使用括号。</p>
<blockquote>
<p>let makeKing = (name = 'jk') => 'return $(name)';</p>
</blockquote>
<p>参数初始化顺序遵循”暂时性死区“规则，即前面定义的参数不能引用后面定义的。
参数也存在于自己的作用域中，它们不能引用函数体的作用域。</p>
<pre><code class="copyable">// 调用时不传第二个参数会报错
function makeKing(name = 'cln', numerals = defaultNum)&#123;
let defaultNum = 'ffzf';
return 'King $(name) $(numerals)';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">参数扩展与收集</h1>
<p>ES6新增了扩展操作符，既可以用于调用函数时传参，也可以用于定义函数参数。</p>
<h2 data-id="heading-11">扩展参数</h2>
<p>使用扩展操作符可以将数组直接传给函数：</p>
<pre><code class="copyable">getSum(...values);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为数组长度已知，可以在扩展操作符的前面或后面再传递其它参数：</p>
<pre><code class="copyable">countArg(-1, ...values);
countArg(-1, ...values, 5);
countArg(-1, ...values, ...[5,8,1]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>arguments对象只是消费扩展操作符的一种方式，在普通函数和箭头函数中，也可以将扩展操作符用于命名参数，或者使用默认参数。</p>
<h2 data-id="heading-12">收集参数</h2>
<p>可以使用扩展操作符把不同长度的独立参数组合成一个数组。</p>
<p>收集参数的前面如果还有命名参数，则只会收集其余的参数。若没有就会得到空数组。因为收集参数的结果可变，所以<strong>只能把收集参数作为最后一个参数</strong>。</p>
<pre><code class="copyable">function collect(firstValue, ...values)&#123;
console.log(values);
&#125;
collect();// []
collect(1);// []
collect(1,2);// [2]
collect(1,2,3);// [2,3]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>箭头函数支持收集参数的定义方式。</p>
<pre><code class="copyable">let getSum = (..values) => &#123;
return values.reduce((x,y) => x+y, 0);
&#125;
console.log(getSum(1,2,3));// 6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用收集参数并不影响arguments对象，仍然反映调用时传给函数的参数。</p>
<pre><code class="copyable">function getSum(...values)&#123;
console.log(arguments.length);// 3
console.log(arguments);// [1,2,3]
console.log(values);// [1,2,3]
&#125;
console.log(getSum(1,2,3));
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">函数声明与函数表达式</h1>
<p>事实上，JavaScript引擎在加载数据时对它们是区别对待的。
JavaScript引擎在任何代码执行之前，会先读取函数声明，并在执行上下文中生成函数定义。</p>
<pre><code class="copyable">console.log(sum(10,10));// 20
function sum (num1, num2)&#123;
return num1+num2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数声明会在任何代码执行之前先被读取并添加到执行上下文，这个过程叫做函数声明提升。</p>
<p>而函数表达式必须等到代码执行到它那一行，才会在执行上下文中生成函数定义。</p>
<pre><code class="copyable">console.log(sum(10,10));// 会报错
let sum =function(num1, num2)&#123;
return num1+num2;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码出错，是因为这个函数定义包含在一个变量初始化语句中，而不是函数声明中。如果没有执行到这个语句，则执行上下文中没有函数的定义。
使用var关键字也会碰到同样的问题。</p>
<h1 data-id="heading-14">函数作为值</h1>
<p>因为函数名在ES中就是变量，所以函数可以用在任何可以使用变量的地方。
意味着可以把函数作为参数传给另一个函数，而且还可以在一个函数中返回另一个函数。</p>
<pre><code class="copyable">function callFunc(someFunc, someArg)&#123;
return somFunc(someArg);
&#125;
function add10(num)&#123;
return num+10;
&#125;
let result = callFunc(add10, 10);
console.log(result);// 20
<span class="copy-code-btn">复制代码</span></code></pre>
<p>callFunc函数是通用的，第一个参数传入的是任何函数，始终返回调用作为第一个参数传入的函数的结果。
<strong>如果是访问函数而不是调用函数，就必须不带括号。</strong>
因此传给callFunc()必须是add10，而不是它的执行结果。</p>
<p>从一个函数中返回另一个函数也是可以的。</p>
<pre><code class="copyable">function compareFunc(propertyName)&#123;
return function(obj1, obj2)&#123;
let value1 = obj1[propertyName];
let value2 = obj2[propertyName];

if(value1 > value2)&#123;
return -1;
&#125;else if(value1 < value2)&#123;
return 1;
&#125;else&#123;
return 0;
&#125;
&#125;;
&#125;

let data = &#123;
&#123;name : "jk", age : 24&#125;,
&#123;name : "cln", age : 21&#125;
&#125;;
data.sort(compareFunc("name"));
console.log(data[0].name);// cln
data.sort(compareFunc("age"));
console.log(data[0].name);// cln
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">函数内部</h1>
<p>在ES5中，函数内部存在两个特殊的对象：arguments和this。ES6又新增了new.target属性。</p>
<h2 data-id="heading-16">arguments</h2>
<p>是一个<strong>类数组对象</strong>，包含调用参数时传入的所有参数。这个对象只有以function关键字定义函数（相对于使用箭头语法创建函数）时才会有。
还有一个属性callee，是一个指向arguments对象所在函数的指针。</p>
<pre><code class="copyable">// 经典阶乘函数
function factorial(num)&#123;
if(num <= 1)&#123;
return 1;
&#125;else&#123;
// return num * factorial(num-1)；// 紧密耦合
return num * arguments.callee(num-1);// 可以让函数逻辑与函数名解耦
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>已经用arguments.callee代替了之前硬编码的factorial。无论函数叫什么名称，都可以正确引用函数。</p>
<pre><code class="copyable">let trueFactoral = factorial;
factorial = function()&#123;
return 0;
&#125;;
console.log(trueFactorial(5));// 120
console.log(factorial(5));// 0
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">this</h2>
<p>它在标准函数和箭头函数中有不同的行为。</p>
<p>在标准函数中，this引用的是<strong>把函数当成方法调用的上下文对象</strong>，通常称其为this值（在网页的全局上下文中调用函数时，this指向windows）。</p>
<pre><code class="copyable">window.color = "red";
let o = &#123; color : "blue" &#125;;
function sayColor()&#123;
console.log(this.color);
&#125;
sayColor();// 'red',在全局上下文中调用，this指向window

o.sayColor = sayColor;
o.sayColor();// 'blue'，this指向o
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在箭头函数中，this引用的是<strong>定义箭头函数的上下文</strong>。</p>
<pre><code class="copyable">window.color = "red";
let o = &#123; color : "blue" &#125;;
let sayColor = () => console.log(this.color);

sayColor();// 'red'

o.sayColor = sayColor;
o.sayColor();// 'red'，,在window上下文中定义的箭头函数，this指向window
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在事件回调或定时回调中调用某个函数时，this值指向的并没想要的对象。此时可以将回调函数写成箭头函数可以解决问题，因为箭头函数中的this会保留定义该函数时的上下文。</p>
<pre><code class="copyable">function King()&#123;
this.royaltyName = 'Henry';
// this 引用King的实例
setTimeout(() => console.log(this.royaltyName), 1000);
&#125;
new King();// Henry
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>函数名只是保存指针的变量，因此全局定义的sayColor()函数和o.sayColor()是同一个函数，，只不过执行的上下文不同。</strong></p>
<h2 data-id="heading-18">caller</h2>
<p>ES5也会给函数对象上添加一个属性: caller，引用的是调用当前函数的函数，或者如果是全局作用域中调用的则为null。</p>
<pre><code class="copyable">function outer()&#123;
inner();
&#125;
function inner()&#123;
// console.log(inner.caller);// inner.caller指向outer()
console.log(arguments.callee.caller);// 降低耦合度
&#125;
outer();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在严格模式下访问arguments.callee会报错。</p>
<p>ES5也定义了arguments.caller，严格模式下访问报错，同时不能给函数的caller属性赋值，否则会导致错误；非严格模式下始终是undefined。</p>
<h2 data-id="heading-19">new.target</h2>
<p>ES6新增了<strong>检测函数是否使用new关键字调用</strong>的new.target属性。</p>
<p>如果函数是正常调用，则new.target的值为undefined；</p>
<p>若是使用new关键字调用的，则new.target将引用被调用的构造函数。</p>
<pre><code class="copyable">function King()&#123;
if(!new.target)&#123;
throw 'King must be instantiated using "new"';
&#125;else&#123;
console.log('King instantiated using "new"');
&#125;
&#125;
new King();// King instantiated using "new"
King();// Error : King must be instantiated using "new"
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">函数属性与方法</h1>
<p>每个函数都有两个属性：length和prototype，length属性保存函数定义的命名参数的个数。</p>
<p>prototype是保存引用类型所有实例的地方，在ES5中，prototype属性是不可枚举的，因此使用for-in循环不会返回这个属性。</p>
<p>函数有两个方法：apply（）和call（），都会以指定的this值来调用函数，即会设置调用函数时函数体内this对象的值。</p>
<p>apply（）接收两个参数：函数体内this值和一个参数数组，第二个参数可以是Array的实例，或者arguments对象。</p>
<pre><code class="copyable">sum.apply(this, arguments);
sum.apply(this, [num1, num2]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在严格模式下，调用函数时如果没有指定上下文对象，则this值不会指向window。除非
使用apply（）或call（）把函数指定给一个对象，否则this值会变成undefined。</strong></p>
<p>call（）与apply（）作用一样，只是传参方式不同。第一个参数和apply（）一样，即this值，而剩下的要传给被调用函数的参数是<strong>逐个传递的</strong>。</p>
<blockquote>
<p>sum.call(this, num1, num2);</p>
</blockquote>
<p>两种方法真正强大的地方，是控制函数调用上下文，即函数体内this值的能力。</p>
<pre><code class="copyable">window.color = 'red';
let o = &#123; color : 'blue' &#125;;
function sayColor()&#123;
console.log(this.color);
&#125;
sayColor();// red,在全局上下文中调用，this指向window

sayColor(this);// red
sayColor(window);// red
sayColor(o);// blue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用apply（）或call（）的好处是可以将任意对象设置为任意函数的作用域。
前面的例子，为切换上下文需要先把sayColor()直接赋值为o的属性，然后再调用。
而在修改后的版本中，就不需要这一步操作了。</p>
<p>ES5定义bind（），会创建一个新的函数实例，其this值会被<strong>绑定</strong>到传给bing（）的对象。</p>
<pre><code class="copyable">window.color = 'red';
let o = &#123; color : 'blue' &#125;;
function sayColor()&#123;
console.log(this.color);
&#125;
let objSayColor = sayColor.bind(o);
objSayColor();// blue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对函数而言，继承的方法toLocaleString（）和toString（）始终返回函数的代码，而valueof（）返回函数本身。</p>
<h1 data-id="heading-21">函数表达式</h1>
<blockquote>
<p>let functionName = function(arg0, arg1, arg2) &#123; 函数体 &#125;;</p>
</blockquote>
<p>创建一个函数再把它赋值给一个变量，这样创建的函数叫做<strong>匿名函数</strong>（又称兰姆达函数），因为function关键字后面没有标识符。</p>
<p>理解函数声明与函数表达式的区别，关键是理解提升。</p>
<pre><code class="copyable">if(condition)&#123;
function sayHi()&#123;
console.log('Hi!');
&#125;
&#125;else&#123;
function sayHi()&#123;
console.log('Yo!');
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上这段代码看起来正常，但是这种写法在ES并不是有效的写法，JS引擎会尝试将其纠正为适当的声明。
但是有些浏览器纠正这个问题的方式不一致。因此这种写法很危险，不要使用。</p>
<pre><code class="copyable">let sayHi():
if(condition)&#123;
sayHi = function()&#123;
console.log('Hi!');
&#125;
&#125;else&#123;
sayHi = function()&#123;
console.log('Yo!');
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用函数表达式写法，如预期一样，根据condition的值为变量sayHi赋予相应的函数。</p>
<h1 data-id="heading-22">递归</h1>
<p>在编写递归函数时，arguments.callee是引用当前函数的首选。</p>
<pre><code class="copyable">function factorial(num)&#123;
if(num <= 1)&#123;
return 1;
&#125;else&#123;
return num * arguments.callee(num-1);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在严格模式下运行的代码，是不能访问arguments.callee，因为访问会出错。</strong>
此时，可以使用命名函数表达式达到目的。</p>
<pre><code class="copyable">const factorial = (function f(num) &#123;
if(num <= 1)&#123;
return 1;
&#125;else&#123;
return num * f(num-1);
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即使把函数赋值给另一个变量，函数表达式的名称f也不变，因此递归调用不会有问题，这个模式在严格模式和非严格模式下都可以使用。</p>
<h1 data-id="heading-23">尾调用优化</h1>
<p>ES6规范新增一项内存管理优化机制，让JS引擎在满足条件时可以重用栈帧。
这项优化非常适合“尾调用”，即外部函数的返回值是一个内部函数的返回值。</p>
<h2 data-id="heading-24">尾调用优化的条件</h2>
<ol>
<li>代码在严格模式下执行；</li>
<li>外部函数的返回值是对尾调用函数的调用；</li>
<li>尾调用函数返回后不需要执行额外的逻辑；</li>
<li>尾调用函数不是引用外部函数作用域中自由变量的闭包。</li>
</ol>
<p>以下符合尾调用优化条件的例子：</p>
<pre><code class="copyable">"use strict";

// 有优化：栈帧销毁前执行参数计算
function otherFunc(a,b)&#123;
return innerFunc(a+b);
&#125;

// 有优化：初次返回值不涉及栈帧
function otherFunc(a,b)&#123;
if(a<b)&#123;
return a;
&#125;
return innerFunc(a+b);
&#125;

// 有优化：两个内部函数都在尾部
function otherFunc(condition)&#123;
return condition? innerFuncA() : innerFuncB();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">尾调用优化的代码</h2>
<p>使用两个嵌套的函数，外部函数作为基础框架，内部函数执行递归：</p>
<pre><code class="copyable">"use strict"

// 基础框架，计算斐波那契数列的函数
function fib(n)&#123;
return fibImpl(0,1,n);
&#125;

// 执行递归
function fibImpl(a,b,n)&#123;
if(n === 0)&#123;
return a;
&#125;
return fibImpl(b, a+b, n-1);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码重构之后，满足尾调用优化条件，再调用fib(1000)就不会对浏览器造成威胁了。</p>
<h1 data-id="heading-26">闭包</h1>
<p>是指那些引用了另一个函数作用域中变量的函数，通常是在嵌套函数中实现的。</p>
<pre><code class="copyable">// 前面举例的比较函数CompareFunc（propertyName）中
let value1= obj1[propertyName];
let value2= obj2[propertyName];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用一个函数时，会为这个函数调用创建一个执行上下文，并创建一个作用域链。然后用
arguments和其它命名参数来初始化这个函数的活动对象。外部函数的活动对象是内部函数
作用域链上的第二个对象。这个作用域链一直向外串起了所有包含函数的活动对象，直到全局
执行上下文才终止。</p>
<pre><code class="copyable">function compare(value1, value2)&#123;
if(value1 < value2)&#123;
return -1;
&#125;else if(value1 > value2)&#123;
return 1;
&#125;else&#123;
return 0;
&#125;
&#125;
let result = compare(5,10);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>compare（）是在全局上下文中调用的，第一次调用此函数时，会为它创建一个包含arguments、value1和
value2的活动对象，是其作用域链的第一个对象。而全局上下文的变量对象则是compare（）作用域链上的第二个对象，其中包含
this、result和compare。</p>
<p>函数执行时，每个执行上下文中都会有一个包含其中变量的对象。全局上下文中的叫做变量对象，会在代码执行期间始终存在。
而函数局部上下文中的叫做活动对象，只在函数执行期间存在。作用链其实是一个包含指针的列表，每个指针分别指向一个变量对象，但
物理上并不会包含相应的对象。</p>
<p>闭包的作用域链中包含自己的一个变量对象，然后是包含函数的变量对象，直到全局上下文的变量对象。</p>
<p><strong>建议在使用闭包时要谨慎，仅在十分必要时使用。因为闭包会保留它们包含韩素华的作用域，所以比其他函数更占用内存。</strong></p>
<p>通常，函数作用域及其中的所有变量在函数执行完毕后都会被销毁。闭包在被函数返回之后，其作用域会一直保存在内存中，直到闭包被销毁。</p>
<h2 data-id="heading-27">this对象</h2>
<p>如果在全局函数中调用，则this在非严格模式下等于window，在严格模式等于undefined。</p>
<pre><code class="copyable">window.identity = 'The Window';
let obj = &#123;
identity : 'My Obj',
getIdentity()&#123;
let that = this;
return function()&#123;
that.identity;
&#125;;
&#125;
&#125;;
console.log(obj.getIdentity()());// 'My Obj'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>this和arguments都是不能直接在内部函数中访问的，如果想访问包含作用域中的arguments，则同样需要将其引用先保存
到闭包能访问的另一个变量中。</strong></p>
<h2 data-id="heading-28">立即调用的函数表达式</h2>
<p>立即调用的匿名函数，又称为立即调用的函数表达式。如果不在包含作用域中，将返回值赋给一个变量，则其包含的所有变量都会被销毁。</p>
<pre><code class="copyable">(function()&#123;
// 块级作用域
&#125;) ();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用ES块级作用域变量，让每次点击<div>都显示正确的索引。</p>
<pre><code class="copyable">let divs = document.querySelectorAll('div');

for(let i = 0; i< divs.length;++i)&#123;
        divs[i].addEventListener('click',function()&#123;
console.log(i);
&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在ES6中，若对for循环使用块级作用域变量关键字，在这里就是let，则循环会为每个循环创建
独立的变量，从而让每个点击处理程序都能引用特定的索引。</p>
<h1 data-id="heading-29">私有变量</h1>
<p>任何定义在函数或块中的变量，都可以认为是私有的。</p>
<p>私有变量包括函数参数、局部变量，以及函数内部定义的其它函数。</p>
<p><strong>特权方法</strong>是能够访问函数私有变量（及私有函数）的公有方法。在对象上两种方式创建特权方法：</p>
<ol>
<li>在构造函数中实现</li>
</ol>
<pre><code class="copyable">function MyObj()&#123;
let privateVariable = 30;
function privateFunc()&#123;
return false;
&#125;

// 特权方法,其实是一个闭包，具有访问构造函数中定义的所有变量和函数的能力
this.privateMethod = function()&#123;
privateVariable++;
return privateFunc();  
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-30">静态私有变量</h2>
<ol start="2">
<li>通过私有作用域定义私有变量和函数来实现，即使用原型模式通过自定义类型中实现</li>
</ol>
<pre><code class="copyable">(function()&#123;
let privateVariable = 10;
function privateFunc()&#123;
return false;
&#125;

MyObj = function()&#123;&#125;;// 构造函数
MyObj.prototype.publicMethod = function()&#123;// 公有和特权方法，定义在原型上
privateVariable++;
return privateFunc();  
&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不使用关键字声明的变量，会创建在全局作用域中，MyObj变成了全局变量，<strong>注意在严格模式下给未声明的变量赋值会导致错误</strong>。</p>
<p>使用闭包和私有变量会导致作用域链变长，作用域链越长，则查找变量所需时间也越多。</p>
<h2 data-id="heading-31">模块模式</h2>
<p>在一个单例对象上实现了相同的隔离和封装。单例对象就是只有一个实例的对象，JS通过对象字面量来创建单例对象的：</p>
<pre><code class="copyable">let singleton = &#123;
name : value,
method()&#123;
// 方法代码
&#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模块模式是在单例对象基础上加以扩展，使其通过作用域链来关联私有变量和特权方法。其样板代码如下：</p>
<pre><code class="copyable">let singleton = &#123;
let privateVariable = 10;
function privateFunc()&#123;
return false;
&#125;

// 特权/公有方法和属性， 对象字面量
return&#123;
publicProperty : true,

publicMethod()&#123;
privateVariable++;
return privateFunc();  
&#125;
&#125;;
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本质上，对象字面量定义了单例对象的公共接口。如果单例对象需要进行某种初始化，并且需要访问私有变量时，可以采取这种模式：</p>
<pre><code class="copyable">let application = function()&#123;
let components = new Array();// 私有变量和私有函数
components.push(new BaseComponent());// 初始化

// 公共接口，对象字面量
return&#123;
getComponentCount()&#123;
return components.length;
&#125;,
registerComponent(component)&#123;
if(typeof component == 'object')&#123;
components.push(component);
&#125;
&#125;
&#125;;
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在模块模式中，单例对象作为一个模块，经过初始化可以包含某些私有数据，而这些数据可以通过其暴露的公共方法来访问。<br>
以这种方式创建的每个单例对象都是Object的实例，因为最终单例都由一个对象字面量来表示。</p>
<h2 data-id="heading-32">模块增强模式</h2>
<p>在返回对象之前先对其进行增强。适合单例对象需要是某种特定类型的实例，但又必须给它添加额外属性或方法的场景。</p>
<pre><code class="copyable">let singleton = function()&#123;
let privateVariable = 10;
function privateFunc()&#123;
return false;
&#125;

let obj = new CustomType();// 创建对象
obj.publicProperty = true;// 添加特权/公有属性和方法
obj.publicMethod = function()&#123;
privateVariable++;
return privateFunc();  
&#125;;
return obj;// 返回对象
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若前一节的application对象必须是BaseComponent的实例，则可以使用以下代码创建它：</p>
<pre><code class="copyable">let application = function()&#123;
let components = new Array();// 私有变量和私有函数
components.push(new BaseComponent());// 初始化

let app = new BasComponent();

// 公共接口
app.getComponentCount()&#123;
return components.length;
&#125;;
app.registerComponent(component)&#123;
if(typeof component == 'object')&#123;
components.push(component);
&#125;
&#125;;
return app;// 返回实例
&#125;();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            