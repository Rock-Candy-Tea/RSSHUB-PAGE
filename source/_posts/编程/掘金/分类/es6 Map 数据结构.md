
---
title: 'es6 Map 数据结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3115'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 00:19:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=3115'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">Map 介绍</h1>
<h2 data-id="heading-1">Map 基本概念</h2>
<p>ES6 提供了 Map 数据结构。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应，是一种更完善的 Hash 结构实现。如果你需要“键值对”的数据结构，Map 比 Object 更合适。</p>
<h2 data-id="heading-2">Map 特征</h2>
<ul>
<li>
<p>Map 对象保存键值对，并且能够记住键的原始插入顺序。</p>
</li>
<li>
<p>任何值(对象或者原始值) 都可以作为一个键或一个值。</p>
</li>
<li>
<p>Map 是 ES6 中引入的一种新的数据结构，可以参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fw3cnote%2Fes6-map-set.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/w3cnote/es6-map-set.html" ref="nofollow noopener noreferrer">ES6 Map 与 Set</a>。</p>
</li>
</ul>
<h2 data-id="heading-3">Maps 和 Objects 的区别</h2>
<ul>
<li>
<p>一个 Object 的键只能是字符串或者 Symbols，但一个 Map 的键可以是任意值。</p>
</li>
<li>
<p>Map 中的键值是有序的（FIFO 原则），而添加到对象中的键则不是。</p>
<p>关于对象是无序的官方解释：
1.An object is a member of the type Object. It is an unordered collection of properties each of which contains a primitive value,
object, or function. A function stored in a property of an object is
called a method.
2.Chrome Opera 的 JavaScript 解析引擎遵循的是新版 ECMA-262 第五版规范。因此，使用 for-in 语句遍历对象属性时遍历书序并非属性构建顺序。而 IE6 IE7 IE8 Firefox Safari 的 JavaScript
解析引擎遵循的是较老的 ECMA-262 第三版规范，属性遍历顺序由属性构建的顺序决定。</p>
</li>
<li>
<p>Map 的键值对个数可以从 size 属性获取，而 Object 的键值对个数只能手动计算。</p>
</li>
<li>
<p>Object 都有自己的原型，原型链上的键名有可能和你自己在对象上的设置的键名产生冲突。</p>
</li>
</ul>
<h2 data-id="heading-4">Map 属性</h2>
<ul>
<li><code>Map.prototype.size</code> – 返回 Map 对象键/值对的数量。</li>
</ul>
<h2 data-id="heading-5">Map 操作方法</h2>
<ul>
<li><code>Map.prototype.clear()</code> – 移除 Map 对象的所有键/值对 。</li>
<li><code>Map.prototype.set()</code> – 设置键值对，返回该 Map 对象。</li>
<li><code>Map.prototype.get()</code> – 返回键对应的值，如果不存在，则返回 undefined。</li>
<li><code>Map.prototype.has()</code> – 返回一个布尔值，用于判断 Map 中是否包含键对应的值。</li>
<li><code>Map.prototype.delete()</code> – 删除 Map 中的元素，删除成功返回 true，失败返回 false。</li>
</ul>
<h2 data-id="heading-6">Map 循环方法</h2>
<p>Map 的遍历顺序就是插入顺序。</p>
<ul>
<li><code>Map.prototype.keys()</code>：返回键名的遍历器。</li>
<li><code>Map.prototype.values()</code>：返回键值的遍历器。</li>
<li><code>Map.prototype.entries()</code>：返回所有成员的遍历器。</li>
<li><code>Map.prototype.forEach()</code>：遍历 Map 的所有成员。</li>
</ul>
<h2 data-id="heading-7">其他方法</h2>
<ul>
<li><code>for of</code> 由于有iterable 所以也可以使用此方法</li>
</ul>
<h2 data-id="heading-8">开始创建</h2>
<p>使用 Map 类型和 new 关键字来创建 Map：</p>
<p>不仅仅是数组，任何具有 Iterator 接口、且每个成员都是一个双元素的数组的数据结构
所以 Set Map 数组 都可以创建 Map</p>
<h3 data-id="heading-9">创建空map 再添加</h3>
<pre><code class="copyable">let map1 = new Map();
map1.set('123',123)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">数组创建Map</h3>
<pre><code class="copyable">const m2 = new Map([['baz', 3]]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">set 创建Map</h3>
<pre><code class="copyable">const set = new Set([
  ['foo', 1],
  ['bar', 2]
]);

const m3 = new Map(set);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">map 创建新的map</h3>
<p>注意 m3 === m2 //false</p>
<pre><code class="copyable">const m3 = new Map(m2);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">例子：可以做什么</h1>
<h2 data-id="heading-14">和对象最大的区别： 多类型的key</h2>
<h3 data-id="heading-15">字符串</h3>
<pre><code class="copyable">var myMap = new Map(); 
var keyString = "a string"; 
myMap.set(keyString, "和键'a string'关联的值");
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">对象</h3>
<pre><code class="copyable">var myMap = new Map(); 
var keyObj = &#123;&#125;
myMap.set(keyObj, "和键 keyObj 关联的值");
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">函数</h3>
<pre><code class="copyable">var myMap = new Map(); 
var keyFunc = function () &#123;&#125; // 函数 
myMap.set(keyFunc, "和键 keyFunc 关联的值");
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">NaN</h3>
<pre><code class="copyable">var myMap = new Map(); 
myMap.set(NaN, "not a number");
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">Map 遍历成员方法</h2>
<p><strong>keys() ， values() ， entries()</strong>
Map 的遍历顺序就是插入顺序</p>
<pre><code class="copyable">const map = new Map([
  ['F', 'no'],
  ['T',  'yes'],
]);

for (let key of map.keys()) &#123;
  console.log(key);
&#125;
// "F"
// "T"

for (let value of map.values()) &#123;
  console.log(value);
&#125;
// "no"
// "yes"

for (let item of map.entries()) &#123;
  console.log(item[0], item[1]);
&#125;
// "F" "no"
// "T" "yes"

// 或者
for (let [key, value] of map.entries()) &#123;
  console.log(key, value);
&#125;
// "F" "no"
// "T" "yes"

// 等同于使用map.entries()
for (let [key, value] of map) &#123;
  console.log(key, value);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用扩展运算符可以快速转数组</p>
<pre><code class="copyable">const map = new Map([
  [1, 'one'],
  [2, 'two'],
  [3, 'three'],
]);

[...map.keys()]
// [1, 2, 3]

[...map.values()]
// ['one', 'two', 'three']

[...map.entries()]
// [[1,'one'], [2, 'two'], [3, 'three']]

[...map]
// [[1,'one'], [2, 'two'], [3, 'three']]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转为数组后，可以使用数组的map，filter方法</p>
<pre><code class="copyable">const map0 = new Map()
  .set(1, 'a')
  .set(2, 'b')
  .set(3, 'c');

const map1 = new Map(
  [...map0].filter(([k, v]) => k < 3)
);
// 产生 Map 结构 &#123;1 => 'a', 2 => 'b'&#125;

const map2 = new Map(
  [...map0].map(([k, v]) => [k * 2, '_' + v])
    );
// 产生 Map 结构 &#123;2 => '_a', 4 => '_b', 6 => '_c'&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">Map 增 删 查 清空</h2>
<pre><code class="copyable">const m = new Map();
const o = &#123;p: 'Hello World'&#125;;

m.set(o, 'content')
m.get(o) // "content"

m.has(o) // true
m.delete(o) // true
m.has(o) // false
m.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">与其他数据结构的互相转换</h2>
<p><strong>（1）Map 转为数组</strong></p>
<p>前面已经提过，Map 转为数组最方便的方法，就是使用扩展运算符（<code>...</code>）。</p>
<pre><code class="copyable">const myMap = new Map()
  .set(true, 7)
  .set(&#123;foo: 3&#125;, ['abc']);
[...myMap]
// [ [ true, 7 ], [ &#123; foo: 3 &#125;, [ 'abc' ] ] ]

var outArray = Array.from(myMap);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（2）数组 转为 Map</strong></p>
<p>将数组传入 Map 构造函数，就可以转为 Map。</p>
<pre><code class="copyable">new Map([
  [true, 7],
  [&#123;foo: 3&#125;, ['abc']]
])
// Map &#123;
//   true => 7,
//   Object &#123;foo: 3&#125; => ['abc']
// &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（3）Map 转为对象</strong></p>
<p>如果所有 Map 的键都是字符串，它可以无损地转为对象。</p>
<pre><code class="copyable">function strMapToObj(strMap) &#123;
  let obj = Object.create(null);
  for (let [k,v] of strMap) &#123;
    obj[k] = v;
  &#125;
  return obj;
&#125;

const myMap = new Map()
  .set('yes', true)
  .set('no', false);
strMapToObj(myMap)
// &#123; yes: true, no: false &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有非字符串的键名，那么这个键名会被转成字符串，再作为对象的键名。</p>
<p><strong>（4）对象转为 Map</strong></p>
<p>对象转为 Map 可以通过<code>Object.entries()</code>。</p>
<pre><code class="copyable">let obj = &#123;"a":1, "b":2&#125;;
let map = new Map(Object.entries(obj));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外，也可以自己实现一个转换函数。</p>
<pre><code class="copyable">function objToStrMap(obj) &#123;
  let strMap = new Map();
  for (let k of Object.keys(obj)) &#123;
    strMap.set(k, obj[k]);
  &#125;
  return strMap;
&#125;

objToStrMap(&#123;yes: true, no: false&#125;)
// Map &#123;"yes" => true, "no" => false&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（5）Map 转为 JSON</strong></p>
<p>Map 转为 JSON 要区分两种情况。一种情况是，Map 的键名都是字符串，这时可以选择转为对象 JSON。</p>
<pre><code class="copyable">function strMapToJson(strMap) &#123;
  return JSON.stringify(strMapToObj(strMap));
&#125;

let myMap = new Map().set('yes', true).set('no', false);
strMapToJson(myMap)
// '&#123;"yes":true,"no":false&#125;'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种情况是，Map 的键名有非字符串，这时可以选择转为数组 JSON。</p>
<pre><code class="copyable">function mapToArrayJson(map) &#123;
  return JSON.stringify([...map]);
&#125;

let myMap = new Map().set(true, 7).set(&#123;foo: 3&#125;, ['abc']);
mapToArrayJson(myMap)
// '[[true,7],[&#123;"foo":3&#125;,["abc"]]]'
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（6）JSON 转为 Map</strong></p>
<p>JSON 转为 Map，正常情况下，所有键名都是字符串。</p>
<pre><code class="copyable">function jsonToStrMap(jsonStr) &#123;
  return objToStrMap(JSON.parse(jsonStr));
&#125;

jsonToStrMap('&#123;"yes": true, "no": false&#125;')
// Map &#123;'yes' => true, 'no' => false&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，有一种特殊情况，整个 JSON 就是一个数组，且每个数组成员本身，又是一个有两个成员的数组。这时，它可以一一对应地转为 Map。这往往是 Map 转为数组 JSON 的逆操作。</p>
<pre><code class="copyable">function jsonToMap(jsonStr) &#123;
  return new Map(JSON.parse(jsonStr));
&#125;

jsonToMap('[[true,7],[&#123;"foo":3&#125;,["abc"]]]')
// Map &#123;true => 7, Object &#123;foo: 3&#125; => ['abc']&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">其他</h2>
<h3 data-id="heading-23">Map 的合并</h3>
<pre><code class="copyable">var first = new Map([[1, 'one'], [2, 'two'], [3, 'three'],]); 
var second = new Map([[1, 'uno'], [2, 'dos']]); // 合并两个 Map 对象时，如果有重复的键值，则后面的会覆盖前面的，对应值即 uno，dos， three 
var merged = new Map([...first, ...second]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">Map 的克隆</h3>
<pre><code class="copyable">var myMap1 = new Map([["key1", "value1"], ["key2", "value2"]]); 
var myMap2 = new Map(myMap1); 
console.log(original === clone); // 打印 false。 Map 对象构造函数生成实例，迭代出新的对象。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">注意事项</h2>
<p>注意，只有对同一个对象的引用，Map 结构才将其视为同一个键。这一点要非常小心。</p>
<pre><code class="copyable">const map = new Map();

map.set(['a'], 555);
map.get(['a']) // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然<code>NaN</code>不严格相等于自身，但 Map 将其视为同一个键。</p>
<pre><code class="copyable">let map = new Map();
map.set(NaN, 123);
map.get(NaN) // 123
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：参考 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/" ref="nofollow noopener noreferrer">阮一峰</a>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fset-map%23Map" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/set-map#Map" ref="nofollow noopener noreferrer">es6.ruanyifeng.com/#docs/set-m…</a></p></div>  
</div>
            