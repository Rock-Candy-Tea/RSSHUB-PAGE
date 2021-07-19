
---
title: 'javascript精进之路手写系列第二弹实际应用篇（18个）（附详解）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5740'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:31:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=5740'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. 实现日期格式化函数</h3>
<p>输入：</p>
<pre><code class="copyable">dateFormat(new Date('2020-12-01'), 'yyyy/MM/dd') // 2020/12/01
dateFormat(new Date('2020-04-01'), 'yyyy/MM/dd') // 2020/04/01
dateFormat(new Date('2020-04-01'), 'yyyy年MM月dd日') // 2020年04月01日
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">const dateFormat = (dateInput, format)=>&#123;
    var day = dateInput.getDate() 
    var month = dateInput.getMonth() + 1  
    var year = dateInput.getFullYear()   
    format = format.replace(/yyyy/, year)
    format = format.replace(/MM/,month)
    format = format.replace(/dd/,day)
    return format
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 交换a,b的值，不能用临时变量</h3>
<p>巧妙的利用两个数的和、差：</p>
<pre><code class="copyable">a = a + b
b = a - b
a = a - b
//[a,b]=[b,a];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 实现数组的乱序输出</h3>
<p>主要的实现思路就是：</p>
<ul>
<li>取出数组的第一个元素，随机产生一个索引值，将该第一个元素和这个索引对应的元素进行交换。</li>
<li>第二次取出数据数组第二个元素，随机产生一个除了索引为1的之外的索引值，并将第二个元素与该索引值对应的元素进行交换</li>
<li>按照上面的规律执行，直到遍历完成</li>
</ul>
<pre><code class="copyable">var arr = [1,2,3,4,5,6,7,8,9,10];
for (var i = 0; i < arr.length; i++) &#123;
  const randomIndex = Math.round(Math.random() * (arr.length - 1 - i)) + i;
  [arr[i], arr[randomIndex]] = [arr[randomIndex], arr[i]];
&#125;
console.log(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一方法就是倒序遍历：</p>
<pre><code class="copyable">var arr = [1,2,3,4,5,6,7,8,9,10];
let length = arr.length,
    randomIndex,
    temp;
  while (length) &#123;
    randomIndex = Math.floor(Math.random() * length--);
    temp = arr[length];
    arr[length] = arr[randomIndex];
    arr[randomIndex] = temp;
  &#125;
console.log(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 实现数组元素求和</h3>
<ul>
<li>arr=[1,2,3,4,5,6,7,8,9,10]，求和</li>
</ul>
<pre><code class="copyable">let arr=[1,2,3,4,5,6,7,8,9,10]
let sum = arr.reduce( (total,i) => total += i,0);
console.log(sum);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>arr=[1,2,3,[[4,5],6],7,8,9]，求和</li>
</ul>
<pre><code class="copyable">var = arr=[1,2,3,[[4,5],6],7,8,9]
let arr= arr.toString().split(',').reduce( (total,i) => total += Number(i),0);
console.log(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>递归实现：</p>
<pre><code class="copyable">let arr = [1, 2, 3, 4, 5, 6] 

function add(arr) &#123;
    if (arr.length == 1) return arr[0] 
    return arr[0] + add(arr.slice(1)) 
&#125;
console.log(add(arr)) // 21
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. 实现数组的扁平化</h3>
<p><strong>（1）递归实现</strong></p>
<p>普通的递归思路很容易理解，就是通过循环递归的方式，一项一项地去遍历，如果每一项还是一个数组，那么就继续往下遍历，利用递归程序的方法，来实现数组的每一项的连接：</p>
<pre><code class="copyable">let arr = [1, [2, [3, 4, 5]]];
function flatten(arr) &#123;
  let result = [];

  for(let i = 0; i < arr.length; i++) &#123;
    if(Array.isArray(arr[i])) &#123;
      result = result.concat(flatten(arr[i]));
    &#125; else &#123;
      result.push(arr[i]);
    &#125;
  &#125;
  return result;
&#125;
flatten(arr);  //  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（2）reduce 函数迭代</strong></p>
<p>从上面普通的递归函数中可以看出，其实就是对数组的每一项进行处理，那么其实也可以用reduce 来实现数组的拼接，从而简化第一种方法的代码，改造后的代码如下所示：</p>
<pre><code class="copyable">let arr = [1, [2, [3, 4]]];
function flatten(arr) &#123;
    return arr.reduce(function(prev, next)&#123;
        return prev.concat(Array.isArray(next) ? flatten(next) : next)
    &#125;, [])
&#125;
console.log(flatten(arr));//  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（3）扩展运算符实现</strong></p>
<p>这个方法的实现，采用了扩展运算符和 some 的方法，两者共同使用，达到数组扁平化的目的：</p>
<pre><code class="copyable">let arr = [1, [2, [3, 4]]];
function flatten(arr) &#123;
    while (arr.some(item => Array.isArray(item))) &#123;
        arr = [].concat(...arr);
    &#125;
    return arr;
&#125;
console.log(flatten(arr)); //  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（4）split 和 toString</strong></p>
<p>可以通过 split 和 toString 两个方法来共同实现数组扁平化，由于数组会默认带一个 toString 的方法，所以可以把数组直接转换成逗号分隔的字符串，然后再用 split 方法把字符串重新转换为数组，如下面的代码所示：</p>
<pre><code class="copyable">let arr = [1, [2, [3, 4]]];
function flatten(arr) &#123;
    return arr.toString().split(',');
&#125;
console.log(flatten(arr)); //  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这两个方法可以将多维数组直接转换成逗号连接的字符串，然后再重新分隔成数组。</p>
<p>**（5）**<strong>ES6 中的 flat</strong></p>
<p>我们还可以直接调用 ES6 中的 flat 方法来实现数组扁平化。flat 方法的语法：<code>arr.flat([depth])</code></p>
<p>其中 depth 是 flat 的参数，depth 是可以传递数组的展开深度（默认不填、数值是 1），即展开一层数组。如果层数不确定，参数可以传进 Infinity，代表不论多少层都要展开：</p>
<pre><code class="copyable">let arr = [1, [2, [3, 4]]];
function flatten(arr) &#123;
  return arr.flat(Infinity);
&#125;
console.log(flatten(arr)); //  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出，一个嵌套了两层的数组，通过将 flat 方法的参数设置为 Infinity，达到了我们预期的效果。其实同样也可以设置成 2，也能实现这样的效果。在编程过程中，如果数组的嵌套层数不确定，最好直接使用 Infinity，可以达到扁平化。</p>
<p><strong>（6）正则和 JSON 方法</strong></p>
<p>在第4种方法中已经使用 toString 方法，其中仍然采用了将 JSON.stringify 的方法先转换为字符串，然后通过正则表达式过滤掉字符串中的数组的方括号，最后再利用 JSON.parse 把它转换成数组：</p>
<pre><code class="copyable">let arr = [1, [2, [3, [4, 5]]], 6];
function flatten(arr) &#123;
  let str = JSON.stringify(arr);
  str = str.replace(/([|])/g, '');
  str = '[' + str + ']';
  return JSON.parse(str); 
&#125;
console.log(flatten(arr)); //  [1, 2, 3, 4，5]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 实现数组去重</h3>
<p>给定某无序数组，要求去除数组中的重复数字并且返回新的无重复数组。</p>
<p>ES6方法（使用数据结构集合）：</p>
<pre><code class="copyable">const array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];

Array.from(new Set(array)); // [1, 2, 3, 5, 9, 8]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES5方法：使用map存储不重复的数字</p>
<pre><code class="copyable">const array = [1, 2, 3, 5, 1, 5, 9, 1, 2, 8];

uniqueArray(array); // [1, 2, 3, 5, 9, 8]

function uniqueArray(array) &#123;
  let map = &#123;&#125;;
  let res = [];
  for(var i = 0; i < array.length; i++) &#123;
    if(!map.hasOwnProperty([array[i]])) &#123;
      map[array[i]] = 1;
      res.push(array[i]);
    &#125;
  &#125;
  return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7. 实现数组的flat方法</h3>
<pre><code class="copyable">function _flat(arr, depth) &#123;
  if(!Array.isArray(arr) || depth <= 0) &#123;
    return arr;
  &#125;
  return arr.reduce((prev, cur) => &#123;
    if (Array.isArray(cur)) &#123;
      return prev.concat(_flat(cur, depth - 1))
    &#125; else &#123;
      return prev.concat(cur);
    &#125;
  &#125;, []);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8. 实现数组的push方法</h3>
<pre><code class="copyable">let arr = [];
Array.prototype.push = function() &#123;
    for( let i = 0 ; i < arguments.length ; i++)&#123;
        this[this.length] = arguments[i] ;
    &#125;
    return this.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9. 实现数组的filter方法</h3>
<pre><code class="copyable">Array.prototype._filter = function(fn) &#123;
    if (typeof fn !== "function") &#123;
        throw Error('参数必须是一个函数');
    &#125;
    const res = [];
    for (let i = 0, len = this.length; i < len; i++) &#123;
        fn(this[i]) && res.push(this[i]);
    &#125;
    return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10. 实现数组的map方法</h3>
<pre><code class="copyable">Array.prototype._map = function(fn) &#123;
   if (typeof fn !== "function") &#123;
        throw Error('参数必须是一个函数');
    &#125;
    const res = [];
    for (let i = 0, len = this.length; i < len; i++) &#123;
        res.push(fn(this[i]));
    &#125;
    return res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">11. 实现字符串的repeat方法</h3>
<p>输入字符串s，以及其重复的次数，输出重复的结果，例如输入abc，2，输出abcabc。</p>
<pre><code class="copyable">function repeat(s, n) &#123;
    return (new Array(n + 1)).join(s);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>递归：</p>
<pre><code class="copyable">function repeat(s, n) &#123;
    return (n > 0) ? s.concat(repeat(s, --n)) : "";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">12. 实现字符串翻转</h3>
<p>在字符串的原型链上添加一个方法，实现字符串翻转：</p>
<pre><code class="copyable">String.prototype._reverse = function(a)&#123;
    return a.split("").reverse().join("");
&#125;
var obj = new String();
var res = obj._reverse ('hello');
console.log(res);    // olleh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，必须通过实例化对象之后再去调用定义的方法，不然找不到该方法。</p>
<h3 data-id="heading-12">13. 将数字每千分位用逗号隔开</h3>
<p><strong>数字有小数版本：</strong></p>
<pre><code class="copyable">let format = n => &#123;
    let num = n.toString() // 转成字符串
    let decimals = ''
        // 判断是否有小数
    num.indexOf('.') > -1 ? decimals = num.split('.')[1] : decimals
    let len = num.length
    if (len <= 3) &#123;
        return num
    &#125; else &#123;
        let temp = ''
        let remainder = len % 3
        decimals ? temp = '.' + decimals : temp
        if (remainder > 0) &#123; // 不是3的整数倍
            return num.slice(0, remainder) + ',' + num.slice(remainder, len).match(/\d&#123;3&#125;/g).join(',') + temp
        &#125; else &#123; // 是3的整数倍
            return num.slice(0, len).match(/\d&#123;3&#125;/g).join(',') + temp 
        &#125;
    &#125;
&#125;
format(12323.33)  // '12,323.33'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>数字无小数版本：</strong></p>
<pre><code class="copyable">let format = n => &#123;
    let num = n.toString() 
    let len = num.length
    if (len <= 3) &#123;
        return num
    &#125; else &#123;
        let remainder = len % 3
        if (remainder > 0) &#123; // 不是3的整数倍
            return num.slice(0, remainder) + ',' + num.slice(remainder, len).match(/\d&#123;3&#125;/g).join(',') 
        &#125; else &#123; // 是3的整数倍
            return num.slice(0, len).match(/\d&#123;3&#125;/g).join(',') 
        &#125;
    &#125;
&#125;
format(1232323)  // '1,232,323'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">14. 实现非负大整数相加</h3>
<p>JavaScript对数值有范围的限制，限制如下：</p>
<pre><code class="copyable">Number.MAX_VALUE // 1.7976931348623157e+308
Number.MAX_SAFE_INTEGER // 9007199254740991
Number.MIN_VALUE // 5e-324
Number.MIN_SAFE_INTEGER // -9007199254740991
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想要对一个超大的整数(<code>> Number.MAX_SAFE_INTEGER</code>)进行加法运算，但是又想输出一般形式，那么使用 + 是无法达到的，一旦数字超过 <code>Number.MAX_SAFE_INTEGER</code> 数字会被立即转换为科学计数法，并且数字精度相比以前将会有误差。</p>
<p>实现一个算法进行大数的相加：</p>
<pre><code class="copyable">function sumBigNumber(a, b) &#123;
  let res = '';
  let temp = 0;
  
  a = a.split('');
  b = b.split('');
  
  while (a.length || b.length || temp) &#123;
    temp += ~~a.pop() + ~~b.pop();
    res = (temp % 10) + res;
    temp  = temp > 9
  &#125;
  return res.replace(/^0+/, '');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其主要的思路如下：</p>
<ul>
<li>首先用字符串的方式来保存大数，这样数字在数学表示上就不会发生变化</li>
<li>初始化res，temp来保存中间的计算结果，并将两个字符串转化为数组，以便进行每一位的加法运算</li>
<li>将两个数组的对应的位进行相加，两个数相加的结果可能大于10，所以可能要仅为，对10进行取余操作，将结果保存在当前位</li>
<li>判断当前位是否大于9，也就是是否会进位，若是则将temp赋值为true，因为在加法运算中，true会自动隐式转化为1，以便于下一次相加</li>
<li>重复上述操作，直至计算结束</li>
</ul>
<h3 data-id="heading-14">13. 实现 add(1)(2)(3)</h3>
<p>函数柯里化概念： 柯里化（Currying）是把接受多个参数的函数转变为接受一个单一参数的函数，并且返回接受余下的参数且返回结果的新函数的技术。</p>
<p>1）粗暴版</p>
<pre><code class="copyable">function add (a) &#123;
return function (b) &#123;
    return function (c) &#123;
      return a + b + c;
    &#125;
&#125;
&#125;
console.log(add(1)(2)(3)); // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2）柯里化解决方案</p>
<ul>
<li>参数长度固定</li>
</ul>
<pre><code class="copyable">var add = function (m) &#123;
  var temp = function (n) &#123;
    return add(m + n);
  &#125;
  temp.toString = function () &#123;
    return m;
  &#125;
  return temp;
&#125;;
console.log(add(3)(4)(5)); // 12
console.log(add(3)(6)(9)(25)); // 43
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于add(3)(4)(5)，其执行过程如下：</p>
<ol>
<li>先执行add(3)，此时m=3，并且返回temp函数；</li>
<li>执行temp(4)，这个函数内执行add(m+n)，n是此次传进来的数值4，m值还是上一步中的3，所以add(m+n)=add(3+4)=add(7)，此时m=7，并且返回temp函数</li>
<li>执行temp(5)，这个函数内执行add(m+n)，n是此次传进来的数值5，m值还是上一步中的7，所以add(m+n)=add(7+5)=add(12)，此时m=12，并且返回temp函数</li>
<li>由于后面没有传入参数，等于返回的temp函数不被执行而是打印，了解JS的朋友都知道对象的toString是修改对象转换字符串的方法，因此代码中temp函数的toString函数return m值，而m值是最后一步执行函数时的值m=12，所以返回值是12。</li>
</ol>
<ul>
<li>参数长度不固定</li>
</ul>
<pre><code class="copyable">function add (...args) &#123;
    //求和
    return args.reduce((a, b) => a + b)
&#125;
function currying (fn) &#123;
    let args = []
    return function temp (...newArgs) &#123;
        if (newArgs.length) &#123;
            args = [
                ...args,
                ...newArgs
            ]
            return temp
        &#125; else &#123;
            let val = fn.apply(this, args)
            args = [] //保证再次调用时清空
            return val
        &#125;
    &#125;
&#125;
let addCurry = currying(add)
console.log(addCurry(1)(2)(3)(4, 5)())  //15
console.log(addCurry(1)(2)(3, 4, 5)())  //15
console.log(addCurry(1)(2, 3, 4, 5)())  //15
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">14. 实现类数组转化为数组</h3>
<p>类数组转换为数组的方法有这样几种：</p>
<ul>
<li>通过 call 调用数组的 slice 方法来实现转换</li>
</ul>
<pre><code class="copyable">Array.prototype.slice.call(arrayLike);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过 call 调用数组的 splice 方法来实现转换</li>
</ul>
<pre><code class="copyable">Array.prototype.splice.call(arrayLike, 0);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过 apply 调用数组的 concat 方法来实现转换</li>
</ul>
<pre><code class="copyable">Array.prototype.concat.apply([], arrayLike);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过 Array.from 方法来实现转换</li>
</ul>
<pre><code class="copyable">Array.from(arrayLike);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">15. 使用 reduce 求和</h3>
<p>arr = [1,2,3,4,5,6,7,8,9,10]，求和</p>
<pre><code class="copyable">let arr = [1,2,3,4,5,6,7,8,9,10]
arr.reduce((prev, cur) => &#123; return prev + cur &#125;, 0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>arr = [1,2,3,[[4,5],6],7,8,9]，求和</p>
<pre><code class="copyable">let arr = [1,2,3,4,5,6,7,8,9,10]
arr.flat(Infinity).reduce((prev, cur) => &#123; return prev + cur &#125;, 0)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>arr = [&#123;a:1, b:3&#125;, &#123;a:2, b:3, c:4&#125;, &#123;a:3&#125;]，求和</p>
<pre><code class="copyable">let arr = [&#123;a:9, b:3, c:4&#125;, &#123;a:1, b:3&#125;, &#123;a:3&#125;] 

arr.reduce((prev, cur) => &#123;
    return prev + cur["a"];
&#125;, 0)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">16. 将js对象转化为树形结构</h3>
<pre><code class="copyable">// 转换前：
source = [&#123;
            id: 1,
            pid: 0,
            name: 'body'
          &#125;, &#123;
            id: 2,
            pid: 1,
            name: 'title'
          &#125;, &#123;
            id: 3,
            pid: 2,
            name: 'div'
          &#125;]
// 转换为: 
tree = [&#123;
          id: 1,
          pid: 0,
          name: 'body',
          children: [&#123;
            id: 2,
            pid: 1,
            name: 'title',
            children: [&#123;
              id: 3,
              pid: 1,
              name: 'div'
            &#125;]
          &#125;
        &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码实现：</p>
<pre><code class="copyable">function jsonToTree(data) &#123;
  // 初始化结果数组，并判断输入数据的格式
  let result = []
  if(!Array.isArray(data)) &#123;
    return result
  &#125;
  // 使用map，将当前对象的id与当前对象对应存储起来
  let map = &#123;&#125;;
  data.forEach(item => &#123;
    map[item.id] = item;
  &#125;);
  // 
  data.forEach(item => &#123;
    let parent = map[item.pid];
    if(parent) &#123;
      (parent.children || (parent.children = [])).push(item);
    &#125; else &#123;
      result.push(item);
    &#125;
  &#125;);
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">17. 使用ES5和ES6求函数参数的和</h3>
<p>ES5：</p>
<pre><code class="copyable">function sum() &#123;
    let sum = 0
    Array.prototype.forEach.call(arguments, function(item) &#123;
        sum += item * 1
    &#125;)
    return sum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6：</p>
<pre><code class="copyable">function sum(...nums) &#123;
    let sum = 0
    nums.forEach(function(item) &#123;
        sum += item * 1
    &#125;)
    return sum
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">18. 解析 URL Params 为对象</h3>
<pre><code class="copyable">let url = 'http://www.domain.com/?user=anonymous&id=123&id=456&city=%E5%8C%97%E4%BA%AC&enabled';
parseParam(url)
/* 结果
&#123; user: 'anonymous',
  id: [ 123, 456 ], // 重复出现的 key 要组装成数组，能被转成数字的就转成数字类型
  city: '北京', // 中文需解码
  enabled: true, // 未指定值得 key 约定为 true
&#125;
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function parseParam(url) &#123;
  const paramsStr = /.+?(.+)$/.exec(url)[1]; // 将 ? 后面的字符串取出来
  const paramsArr = paramsStr.split('&'); // 将字符串以 & 分割后存到数组中
  let paramsObj = &#123;&#125;;
  // 将 params 存到对象中
  paramsArr.forEach(param => &#123;
    if (/=/.test(param)) &#123; // 处理有 value 的参数
      let [key, val] = param.split('='); // 分割 key 和 value
      val = decodeURIComponent(val); // 解码
      val = /^\d+$/.test(val) ? parseFloat(val) : val; // 判断是否转为数字
      if (paramsObj.hasOwnProperty(key)) &#123; // 如果对象有 key，则添加一个值
        paramsObj[key] = [].concat(paramsObj[key], val);
      &#125; else &#123; // 如果对象没有这个 key，创建 key 并设置值
        paramsObj[key] = val;
      &#125;
    &#125; else &#123; // 处理没有 value 的参数
      paramsObj[param] = true;
    &#125;
  &#125;)
  return paramsObj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">结语</h2>
<ul>
<li>点赞关注不迷路</li>
<li>干完这些题；欢迎关注公众号<a href="https://juejin.cn/user/1943592288395479/pins" target="_blank" title="https://juejin.cn/user/1943592288395479/pins">前端要努力</a>,一起努力学习！</li>
</ul></div>  
</div>
            