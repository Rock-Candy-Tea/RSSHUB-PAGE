
---
title: 'ECMAScript新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/679a5253ebc34e4c92763f90d6ccb6c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:33:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/679a5253ebc34e4c92763f90d6ccb6c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">ECMAScript</h4>
<ul>
<li>通常将 ECMAScript 看作是 JavaScript 的标准规范</li>
<li>实际上 JavaScript 是 ECMAScript 的扩展语言</li>
<li>ECMAScript 只是提供了最基本的语法</li>
<li>JavaScript 在语言基础上进行了扩展</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/679a5253ebc34e4c92763f90d6ccb6c5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad4ac816b61c44e9af1e1f6da3d863fd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript 语言本身指的就是 ECMAScript</p>
<p>2015 年开始 ES 保持每年一个版本的迭代</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99f8368b1b574b0bb6b675e415305363~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>ES2015 开始按照年份开始命名</p>
<p>很多人习惯将 ES2015 称之为 ES6</p>
<h4 data-id="heading-1">ECMAScript 2015</h4>
<p>最新 ECMAScript 标准的代表版本</p>
<p>用 ES6 来泛指所有的新标准</p>
<p>注意分辨用 ES6 是特指还是泛指</p>
<p>参考网址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fwww.ecma-international.org%2Fecma-262%2F6.0%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.zhihu.com/?target=http%3A//www.ecma-international.org/ecma-262/6.0/" ref="nofollow noopener noreferrer">www.ecma-international.org/ecma-262/6.…</a></p>
<p>重点了解在 ES5.1 基础之上的变化</p>
<ul>
<li>解决原有语法上的一些问题或者缺陷</li>
<li>对原有语法进行增强</li>
<li>全新的对象、全新的方法、全新的功能</li>
<li>全新的数据类型和数据结构</li>
</ul>
<h4 data-id="heading-2">准备工作</h4>
<p>任何一个支持 ES2015 的环境都可以</p>
<p>在 VScode 软件中使用 Chrome 调试</p>
<p>安装插件：</p>
<ul>
<li>Debugger for Chrome</li>
<li>Live Server</li>
<li>Browser Preview</li>
</ul>
<p>调试步骤：</p>
<ul>
<li>安装上面的插件</li>
<li>点击菜单栏的运行——启动调试——选择环境：Chrome——修改调试的 url 地址：8080改为5500（要与临时服务器的端口号保持一致）——保存</li>
<li>配置文件设置好后就可以调试了</li>
<li>在使用时，再次点击菜单栏的运行——启动调试——就可以选择文件实时查看变化过程</li>
<li>同时在vscode里也可以在"查看"打开调试控制台，也可以实时记录当前代码的变化过程</li>
</ul>
<h4 data-id="heading-3">let 与 块级作用域</h4>
<p>作用域 - 某个成员能够起作用的范围</p>
<p>在 ES2015 之前，ES 只有前两种作用域</p>
<ul>
<li>全局作用域</li>
<li>函数作用域</li>
<li>块级作用域</li>
</ul>
<p>块，就是 &#123;&#125; 包裹起来的一个范围</p>
<p>以前的块是没有作用域的</p>
<pre><code class="copyable">if (true) &#123;
    var foo = 1;
&#125;
console.log(foo); // 1

if (true) &#123;
    let foo = 1; 
&#125;
console.log(foo); // 报错
// 可以通过新的关键字 let 定义块内部的变量
// let 定义的变量在块级作用域内部能够被访问
// 非常适合设置在 for 循环中的循环变量
// 使用 var 时，内层循环变量与外层循环变量处于同一个作用域之内，相同的变量名会发生覆盖
// 第一次进入内部循环后，等内部循环完 i 的值就变为3了，再进行下一次外部循环时 i = 3 已经进不去内部循环了
for (var i = 0; i < 3; i++) &#123;
  for (var i = 0; i < 3; i++) &#123;
    console.log(i); // 0 1 2
  &#125;
&#125;

// 通过 let 定义变量，只在自己的循环中生效
// 实际工作中尽量不要在循环内外用同样的变量名进行定义
for (let i = 0; i < 3; i++) &#123;
  for (let i = 0; i < 3; i++) &#123;
    console.log(i); // 0 1 2 0 1 2 0 1 2
  &#125;
&#125;
// 通过循环批量添加事件
// 通过 let 定义变量，只能在块级内部被调用
// 会封闭自己的作用域，i 就是局部变量，局部变量在调用时会去自己原来的作用域访问原来的值
var eles = [&#123;&#125;, &#123;&#125;, &#123;&#125;];
for (var i = 0; i < eles.length; i++) &#123;
  eles[i].onclick = function () &#123;
    console.log(i);
  &#125;;
&#125;
eles[0].onclick(); // 0
eles[1].onclick(); // 1
eles[2].onclick(); // 2
// 若for循环使用 var 定义变量时，不管点击哪个，都会输出3。由于受到闭包的影响， 定义的事件函数本身相当于定义在全局作用域里，记录的 i 变量也是全局变量，在调用时会去找到全局变量里当前最新的值，跳出循环后 i 变成 3，所以在调用时结果都是3
// 循环 实际上有两层作用域
// 第一层是 for 循环作用域，也就是整体作用域，还有一层是每一次大括号内部的块级作用域，块级作用域里每次定义一个 i ,每次 i 都是单独作用域里面的变量，在进行调用时结果是10次 foo
for (let i = 0; i < 10; i++) &#123;
  let i = "foo";
  console.log(i); // 10次foo
&#125;
// 把 for 循环进行拆分书写
let i = 0;
if (i < 10) &#123;
  let i = "foo"; // 块级作用域里的变量
  console.log(i); // 在块级作用域里调用，自己内部定义了 i ，直接调用
&#125;
i++; // 执行的是外部的 for 循环的作用域，而不是内部的块级作用域
// let 除了产生作用域的限制外，还和 var 有另外一个区别
// let 不会进行变量提升，必须先声明，再使用
console.log(a); // undefined
var a = 1;

console.log(a); // 报错，变量引用错误，不能在初始化之前接收变量 a
let a = 2;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">const</h4>
<ul>
<li>const 只读的常量/恒量</li>
<li>在let基础上多了【只读】特性，变量声明过后不能再被修改</li>
<li>变量在声明值时，必须设置一个 <strong>初始值</strong></li>
<li>const声明成员的不能被修改，已经分配了一块内存地址，如果给该成员赋值，会改变该成员的内存指向；但可以修改恒量成员中的属性值</li>
<li>最佳实践： 不用var， 主用const, 配合let</li>
</ul>
<pre><code class="copyable">const obj = &#123;&#125;
obj.name = 'test' OK //这里修改的是成员属性的值，没有重新分配一块内存空间
obj = &#123;&#125; // error 赋值被改变obj的指向
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">ES2015 数组的解构</h4>
<blockquote>
<p><strong>数组的解构</strong> : 以前只能通过索引来获取数组中的值，数据的解构可以快速的获取数组中的值</p>
</blockquote>
<p>现在定义一个数组：const arr = [100, 200,300]</p>
<ul>
<li>传统方法</li>
</ul>
<pre><code class="copyable">const foo = arr[0]
const bar = arr[1]
const baz = arr[3]
console.log(foo, bar, baz)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>[] 提取出来的数据所存放的变量名</li>
</ul>
<pre><code class="copyable">const [, , baz] = arr
console.log(baz) // 300
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>获取其他某个位置其后的成员</li>
</ul>
<pre><code class="copyable">// 获取其他某个位置的成员,但需要保留解构所在的逗号，
// 保证解构数组的格式与原来数组格式是一致的；
// ...： ...rest 只能放在解构位置最后一个成员上去使用
const [foo, ...rest] = arr
console.log(rest) // 200， 300
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解构成员的个数小于数组长度，按照从前到后的顺序去提取，多出来的成员不会被提取</li>
</ul>
<pre><code class="copyable">const [foo, bar , baz, more] = arr
console.log(foo) //100
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解构成员的个数大于数组长度，提取的数据是 undefined</li>
</ul>
<pre><code class="copyable">const [foo, bar , baz, more] = arr
console.log(more) // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>给提取的成员设置默认值，在解构位置的变量名赋值,如果解构到对应的值，那么就会得到默认值</li>
</ul>
<pre><code class="copyable">const [foo, bar , baz = 123, more = 'defalut value'] = arr
console.log(baz, more) // 123, defalut value'
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>场景一：拆分字符串</li>
</ul>
<pre><code class="copyable">// 传统方式
const path = '/foo/bar/baz'
const tmp = path.split('/')
const rootdir = tmp[1] 
console.log(tmp,rootdir) // foo
//解构方式
const [, rootdir] = path.split('/')
console.log(rootdir) // foo
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">对象的解构：</h4>
<blockquote>
<p>对象解构：需要根据 <strong>属性名</strong> 去匹配提取，而不是根据位置；因为数组中元素是有下标的，有顺序规则的；而对象里面的成员 <strong>没有一个固定的次序</strong>，所以不能按照位置去提取</p>
</blockquote>
<pre><code class="copyable">// 对象的解构
const obj = &#123;name: 'zce', age: 18&#125;

// 使用 &#123;&#125; 存储从对象提取的变量名，变量名去匹配对象的属性值
const &#123; name &#125; = obj
console.log( name )

// 解构的变量名同时去匹配被解构对象当中的属性名，就会产生冲突,使用重命名 objName
const name = 'tom'
const &#123; name: objName &#125; = obj
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">模版字符串字面量</h4>
<ul>
<li>传统定义字符串需要用单引号或者双引号表示, 不支持换行符</li>
</ul>
<pre><code class="copyable">const str = 'hello es2015'
console.log(str)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>模板定义字符串使用</li>
</ul>
<pre><code class="copyable">const str = `hello es2015`
// 支持插值表达式$&#123;name&#125;
const name = 'tom'
const msg = `hello, $&#123;name&#125; --- $&#123;1+2&#125;`
console.log(msg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>带标签函数的模板字符串：分割成数组</li>
</ul>
<pre><code class="copyable">const name = 'tom'
const gender = true
function myTagFunc(strings ,naem , gender) &#123;
    console.log(strings, name , gender)
    return strings[0] + name + strings[1] + gender + strings[2]
&#125;
// 打印出就是模版字符串内容中分割过后的结果，因为模版字符串当中可能由嵌入的表达式，
//所以这个数组是按照表达式分割过后的静态内容， 模版中可以接受所有的值
const result = myTagFunc`hey,$&#123;name&#125; is a $&#123;gender&#125;`
console.log(result)
//场景： 1.文本多语言话；2.检查模版字符串当中存在不安全的字符串；3.小型模版引擎
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">字符串的扩展方法</h4>
<p>判断指定字符串当中是否包含所需的内容</p>
<ul>
<li>.includes()</li>
<li>.startsWith() ：</li>
<li>.endsWith()</li>
</ul>
<pre><code class="copyable">const message = 'Error: foo is not edfined'

console.log(
    //是否以Error开头
    message.startsWith('Error') , // true:
    //是否以.结尾
    message.endsWith('.'),
    // 是否包含 is
    message.includes('is')
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">Proxy：为对象设置代理器，监听某个对象属性的读写get(),set()等等</h4>
<p>想像成门卫，也就说进去拿东西还是放东西，都需要门卫去拿；</p>
<ul>
<li>Proxy 和Object.defineProtperty的区别
<ul>
<li>defineProperty只能监视属性的读写，Proxy能够监视到更多对象操作：delete属性等等</li>
<li>Proxy 更好的支持数组对象的监视（重写数组的操作方法），通过自定义方法覆盖原型方法</li>
<li>Proxy是以非侵入的方式监管了对象的读写（也就是说： 一个已经定好的对象，不需要对对象本身做操作，就可以监视到该对象属性）</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90b47dd40c1141d2be8d074d4dfb8141~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">Reflect</h4>
<p>它是一个 <strong>静态类</strong> ，不能实例化new Reflect，只能够调用静态类的方法Reflect.get()；Reflect呢不封装了一系列对对象的底层操作；Reflect成员方法就是 <strong>Proxy处理对象的默认实现</strong>。统一提供一套用于操作对象的API;</p>
<h4 data-id="heading-11">静态方法</h4>
<ul>
<li>通过函数名本身去调用；</li>
<li>静态方法挂在类型上面的，静态方法内部的this不会指向某一个实例对象，而是指向当前类型</li>
</ul>
<h4 data-id="heading-12">类的继承</h4>
<ul>
<li>可以抽象出来相似的地方；</li>
<li>子类型可以继承父类型所有的成员属性</li>
<li>用supper（）访问父对象的方法</li>
</ul>
<h4 data-id="heading-13">Set数据结构：</h4>
<ul>
<li>可以理解成集合，根传统的数组类似</li>
<li>Set的内部成员是不能重复的，每个值都是唯一的；</li>
<li>通过Set的size属性可以获取数组长度</li>
<li>has判断集合当中是否存在某个值</li>
<li>delete删除集合中某个制定的值</li>
<li>clear 清除集合的全部集合</li>
<li>使用Array.from转换为数组</li>
<li>常见的应用场景： 1.为数组去重；</li>
</ul>
<pre><code class="copyable">const s = new Set()
// 因为返回集合可以链式调用
s.add(1).add(2).add(3)
s.size
s.has(100)
s.delete(3)
s.clear()
// 去重
const arr = [1,2,3,4,1,3]
方法一：
const result = [...new Ser(arr)]
方法二：
const result = Array.from(new Set(arr))
console.log(result)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">Map 数据结构</h4>
<ul>
<li>与对象非常类似;本质上都是键值对集合，但是对象的键只能是 <strong>字符串类型</strong>；</li>
<li>Map才能算是键值对集合，用来映射两个 任意类型数据 之间的关系（ <strong>任意数据类型作为键</strong>）</li>
</ul>
<pre><code class="copyable">// 对象方式
const obj = &#123;&#125;
// 如果给我们对象添加的对象是布尔、数值、对象类型最终都会转换为 字符串类型
obj[true] = 'value' // ['ture']
obj[123] = 'value'
obj[&#123;a:1&#125;] = 'value'
//利用对象存储学生的成绩
//Map 方式
const m = new Map()
cosnt tom = &#123;name: 'tom'&#125;
m.set(tom, 90)
console.log(m)
console.log(.get(tom)) // 获取某个值
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">Symbol</h4>
<ul>
<li>为解决定义键名的重复问题</li>
<li>为对象添加一个独一无二的属性名</li>
<li>可以作为对象的私有属性：获取这种私有属性Object.getOwnPropertySmbol()</li>
</ul>
<pre><code class="copyable">cosnt s = Symbol()
console.log(s)
cosnt obj = &#123;&#125;
obj[Symbol()] = '123'
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">for...of循环</h4>
<ul>
<li>for, for...in, forEach 有局限
<ul>
<li>for 适用于遍历普通的数组</li>
<li>for...in 适用于遍历键值对</li>
<li>forEach 对象的遍历方法，无法终止遍历</li>
</ul>
</li>
<li>for...of 作为遍历所有数据结构的统一方式
<ul>
<li>可以使用break方法，终止遍历;以前终止遍历，只能使用数组的some(),every().</li>
<li>Map结构，遍历出是数组形式，可以直接用key,value拿到元素值</li>
<li>无法遍历普通对象，只能遍历具有数组之类的接口；因为具有Iterable接口（相同规格标准）</li>
<li>实现Iterable接口就是forfor...of的前提</li>
</ul>
</li>
</ul>
<pre><code class="copyable">// 基本用法
const arr = [100, 200, 300, 400]
for(const item of arr) &#123;
// 不同于传统的方式，for...of拿到的是每个项的元素，而不是对应的下标
    console.log(item)
&#125;
// Set
const s = new Set(['foo', 'far'])
for(const item of s) &#123;
    console.log(item)
&#125;
// Map 
const m = new Map()
m.set('foo':'123')
m.set('far':'345')
for(const [key,value] of m) &#123;
    console.log(key, value)
&#125;
// 普通对象: 无法遍历普通对象
const obj = &#123;foo: 123, bar:123&#125;
for(const item of obj) &#123;
    cosole.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">可迭代接口</h4>
<ul>
<li>实现Iterable接口就是for...of的前提；</li>
<li>Map，Array，Set都有一个Symbol.iterator 接口（），然后返回一个next()方法</li>
</ul>
<pre><code class="copyable">    const set = new Set['foo', 'bar', 'faz']
    const iterator = set[Symbol.iterator]()
    cosole.log(iterator.next()); // foo
    cosole.log(iterator.next()); // bar
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">实现可迭代接口（）</h4>
<pre><code class="copyable">// 自定义 实现可迭代接口 iterabel，约定内部必须要有一个iterator方法
const obj = &#123;
    store: ['foo','bar','baz'], // 可迭代的数组
    //实现迭代接口iterator，约定内部必须要有一个用于迭代的next()方法
    [Symbol.iterator]: function() &#123;
        let index = 0
        const self = this
        return &#123;
            next: function() &#123;
                // 迭代结果接口IterationResult 
                const result = &#123;
                    value: self.store[index], // 迭代到的数据
                    done: true >= self.store.length // 迭代有没有结束
                &#125;
                index++
                return result
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">迭代器模式</h4>
<ul>
<li>场景：你我协同开发一个任务清单应用</li>
</ul>
<pre><code class="copyable">// 迭代器模式
// 场景：你我协同开发一个任务清单应用

// 我的代码======================
const todos = &#123; // 对象结构
    life: ['吃饭','睡觉','打游戏'],
    learn: ['','',''],
    work: ['喝茶'],
    // 对外提供一个统一的接口，对调用着而言，不用关心对象内部的结构，不用担心内部改变之后的影响
    each: function(callback) &#123; // 只适用于当前的应用结构
        const all = [].concat(this.life,this.learn, this.work)
        for(const item of all) &#123;
            callback(item)
        &#125;
    &#125;,
    [Symbol.iterator]: function() &#123; // 适用于任何的数据结构
        const all = [...this.life, ...this.learn, ...this.work]
        let index = 0
        const self = this
        return &#123;
            next: function() &#123;
                const result = &#123;
                    value: all[index],
                    done: index >= all.length
                &#125;
                index++;
                return result
            &#125;
        &#125;
    &#125;
&#125;


// 你的代码=====================
for(const item of todos.life) &#123;
    console.log(item)
&#125;
for(const item of todos.learn) &#123;
    console.log(item)
&#125;
for(const item of todos.work) &#123;
    console.log(item)
&#125;

//优化
todos.each(function(item) &#123;
    console.log(item)
&#125;)

for(const item of todos) &#123;
    console.log(item)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">生成器</h4>
<ul>
<li>在复杂的异步代码中减少回调函数嵌套的问题，提供更好的异步编程解决方案</li>
<li>生成器的组成：在普通函数名前添加一个 *</li>
<li>生成器对象也迭代了Iterabel接口</li>
<li>生成器配合yield关键词</li>
<li>生成器函数会自动帮我们返回一个自动生成器对象，调用对象next()方法。才会让这个函数体方法开始执行，执行过程中遇到了yield关键词，函数执行就会被暂停下来，而且yield后面的值将会作为next结果返回，如果我们继续调用这个函数，将会从yield暂停的地方开始执行，直到这个函数结束</li>
</ul>
<pre><code class="copyable">// 基本语法
function * foo() &#123;
    console.log('zec')
    return 100
&#125;
const result = foo()
console.log(result.next()) // zec &#123; value: 100, done: true &#125;
// yiled
function * foo() &#123;
    console.log('zec')
    yield 100
    console.log('2222')
    yield 200
&#125;
const generator = foo()
//- 生成器函数会自动帮我们返回一个自动生成器对象，调用对象next()方法。才会让这个函数体方法开始执行，执行过程中遇到了yield关键词，函数执行就会被暂停下来，
//而且yield后面的值将会作为next结果返回，如果我们继续调用这个函数，将会从yield暂停的地方开始执行，直到这个函数结束
console.log(generator.next())
console.log(generator.next())
//zec &#123; value: 100, done: false &#125;
//2222 &#123; value: 200, done: false &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">生成器应用</h4>
<pre><code class="copyable">// 案例： 发号器：自增ID，在原有的ID上加1

function * createIDMaker () &#123;
    let id = 1
    while (true) &#123;
        yield id++
    &#125;
&#125;

const idMaket = createIDMaker()

console.log(idMaket.next().value)
console.log(idMaket.next().value)
console.log(idMaket.next().value)
console.log(idMaket.next().value)

// 案例二:Iterator 方法

const todos = &#123; // 对象结构
    life: ['吃饭','睡觉','打游戏'],
    learn: ['java','html','javascript'],
    work: ['喝茶'],
    // 对外提供一个统一的接口，对调用着而言，不用关心对象内部的结构，不用担心内部改变之后的影响
    [Symbol.iterator]: function * () &#123;
        const all = [...this.life, ...this.learn, ...this.work]
        for(const item of all) &#123;
            yield item
        &#125; 
    &#125;
&#125;

for (const iterator of todos) &#123;
    console.log(iterator)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">ECMAScript 2016</h4>
<ul>
<li>Array.includes()</li>
<li>Math.pow()</li>
</ul>
<h4 data-id="heading-23">ECMAScript 2017</h4>
<ul>
<li>Object.values(); //对象当中所有值的数组</li>
<li>Object.entries();// 以数组的形式返回对象当中的所有键值对，然后可以for...of</li>
<li>Object.getOwnPropertySmbol(); 主要配合get,set去使用</li>
<li>String.prototype.padStart(); 另一个字符串填充当前字符串,从当前字符串的左侧开始填充。</li>
<li>String.prototype.padEnd();</li>
<li>在函数参数中添加尾逗号；</li>
</ul></div>  
</div>
            