
---
title: 手写实现apply、call、bind
categories: 
    - 编程
    - segmentfault - 频道
author: segmentfault - 频道
comments: false
date: 2021-03-21 16:40:59
thumbnail: 
---

<div>   
<p><a href="https://github.com/bilibili-lab/Blog" rel="nofollow">本文github地址，欢迎star</a></p><h2>apply、call、bind区别</h2><p>这三个方法都是挂载 <code>Funtion</code> 原型上的方法，所以调用者必须是个函数。</p><ul><li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/call" rel="nofollow">Function.prototype.call()</a></li><li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" rel="nofollow">Function.prototype.apply()</a></li><li><a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" rel="nofollow">Function.prototype.bind()</a></li></ul><p>这三个函数的使用语法：</p><pre><code class="js">func.call(thisArg, param1, param2, ...)
func.apply(thisArg, [param1, param2, ...])
func.bind(thisArg, param1, param2, ...)</code></pre><p>他们共有的作用都可以改变函数运行时 <code>this</code> 的指向。</p><p><code>call</code> 和 <code>apply</code> 的区别在于传递参数的方式不同：</p><ul><li><code>apply</code> 的第 <code>2</code> 个参数为数组</li><li><code>call</code> 则是从第 <code>2</code> 个至第 <code>N</code> 个都是给 <code>func</code> 的传参</li></ul><p><code>bind</code> 和 <code>call</code> 、 <code>apply</code> 的区别在于函数是否立即执行：</p><ul><li><code>call</code>、<code>apply</code>是在改变了函数的 <code>this</code> 指向之后立马执行</li><li><code>bind</code> 会返回一个函数，虽然改变了 <code>func</code> 的 <code>this</code> 指向，但不是马上执行, 而是调用返回的函数才执行</li></ul><h2>apply、call、bind 使用场景</h2><h3>获取数组的最值</h3><p>可以通过 <code>apply</code> 来获取 <code>Math.max()</code> 最大值和 <code>Math.min()</code> 最小值。当然也可以展开来获取数组的最值。</p><pre><code class="js">let arr = [1, 2, 3];
const max = Math.max.apply(null, arr); // es6 Math.max(...arr)
const min = Math.min.apply(null, arr); // es6 Math.min(...arr)
console.log(max); // 3
console.log(min); // 1</code></pre><h3>判断数据类型</h3><p>可以通过 <code>Object.toString.call</code> 来判断所有的数据类型。</p><pre><code class="js">// 判断原生对象
const isPlainObject = val => Object.toString.call(val) === '[object Object]'
// 判断字符串
const isString = val => Object.toString.call(val) === '[object String]'</code></pre><h3>将类数组转为数组</h3><p>类数组因为不是真正的数组，所有没有数组类型上自带的种种方法，所以要转为数组，才能调用数组的方法.</p><pre><code class="js">let arrayLike = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    length: 3
};

// ES5的写法
let arr1 = [].slice.call(arrayLike); // ['a', 'b', 'c']

// ES6的写法
let arr2 = Array.from(arrayLike); // ['a', 'b', 'c']</code></pre><h3>继承</h3><p>组合继承使用<code>call</code>来实现。</p><pre><code class="js">function Parent() {
    this.name = '张三';
    this.age = 18;
}

Parent3.prototype.getName = function() {
    return this.name;
}

function Child() {
    Parent3.call(this);
    this.address = 'beijing';
}

Child.prototype = new Parent3();
Child.prototype.constructor = Child3;
var s = new Child();
console.log(s.getName()); // '张三'</code></pre><h2>手写实现</h2><h3>call的实现</h3><pre><code class="js">Function.prototype.call = function (context, ...args) {
  var context = context || window;
  context.fn = this;
  var result = eval('context.fn(...args)');
  delete context.fn
  return result;
}</code></pre><h3>apply的实现</h3><p>apply 和 call 基本原理是差不多的，只是参数存在区。</p><pre><code class="js">Function.prototype.apply = function (context, args) {
  let context = context || window;
  context.fn = this;
  let result = eval('context.fn(...args)');
  delete context.fn
  return result;
}c</code></pre><h3>bind的实现</h3><p><code>bind</code> 的实现思路基本和 <code>apply</code> 一样，但是在最后实现返回结果这里，<code>bind</code> 和 <code>apply</code> 有着比较大的差异，<code>bind</code> 不需要直接执行,需要通过返回一个函数的方式将结果返回，之后再通过执行这个结果，得到想要的执行效果。</p><pre><code class="js">Function.prototype.bind = function (context, ...args) {
    if (typeof this !== "function") {
      throw new Error("this must be a function");
    }
    var self = this;
    var fbound = function () {
        self.apply(this instanceof self ? this : context, args.concat(Array.prototype.slice.call(arguments)));
    }
    if(this.prototype) {
      fbound.prototype = Object.create(this.prototype);
    }
    return fbound;
}</code></pre><ul><li><code>bind</code>需要返回一个函数，但是不能丢失函数原型上的属性，因此<code>fbound.prototype = Object.create(this.prototype);</code></li><li><code>this instanceof self</code>当这个绑定函数被当做普通函数调用的时候，可以直接用<code>context</code>； 而返回的这个之后当做构造函数使用的时候，却是指向这个实例，所以<code>this instanceof self</code>为<code>true</code>时，要用<code>this</code>。 因此这里加了这个判断。</li></ul><h2>总结</h2><p>经过上述的分析，我们来总结下这三个函数的相同点和不同点，来帮助更好的理解。</p><table><thead><tr><th>方法</th><th>call</th><th>apply</th><th>bind</th></tr></thead><tbody><tr><td>函数参数</td><td>一个参数列表</td><td>一个包含多个参数的数组</td><td>多个参数</td></tr><tr><td>函数作用</td><td>改变函数运行时 <code>this</code> 指向</td><td>改变函数运行时 <code>this</code> 指向</td><td>改变函数运行时 <code>this</code> 指向</td></tr><tr><td>返回结果</td><td>直接执行</td><td>直接执行</td><td>等待执行函数</td></tr><tr><td>底层实现</td><td>通过<code>eval</code></td><td>通过<code>eval</code></td><td>调用<code>apply</code></td></tr></tbody></table>  
</div>
            