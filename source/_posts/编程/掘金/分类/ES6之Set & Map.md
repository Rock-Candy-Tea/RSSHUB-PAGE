
---
title: 'ES6之Set & Map'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8291'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 21:57:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=8291'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h4 data-id="heading-0">1.Set是什么</h4>
<p>Set是ES6的一种数据结构，类似于数组，但是成员的值是唯一的，没有重复的（当向Set中添加成员时，相同的值不会被添加进去）。</p>
<p>Set本身是一个构造函数，用来生成Set数据结构。</p>
<pre><code class="copyable">let set = new Set()
set.add(1) //向set中增加元素
set.add('1')
set.size // 2

let set1 = new Set([NaN,NaN])
set1.size  //1
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">let set = new Set();
set.add(&#123;&#125;);
set.size // 1
set.add(&#123;&#125;);
set.size // 2    由于两个空对象不相等，所以它们被视为两个值。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>向 Set 加入值的时候，不会发生类型转换，所以1和"1"是两个不同的值。Set 内部判断两个值是否不同，使用的算法叫做“Same-value-zero equality”，它类似于精确相等运算符（===），主要的区别是向 Set 加入值时认为NaN等于自身，而精确相等运算符认为NaN不等于自身。</p>
<pre><code class="copyable">let set = new Set([1, 2, 3, 4, 4]); //接收一个数组作为参数用来初始化
set.size // 4
[...set] // [1, 2, 3, 4]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Set可以用于去除重复的成员，用法如下：</p>
<pre><code class="copyable">//去除数组重复成员
let array = [1,3,4,4,5,2,2]
[...new Set(array)] // [1,3,4,5,2]

Array.from(new Set(array))

//去除字符串重复成员
[...new Set('ababbc')].join('') //abc
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2. Set的属性和方法</h4>
<p>Set.prototype.constructor : 构造函数，默认就是Set函数</p>
<p>Set.prototype.size: 返回Set实例的成员总数</p>
<p>Set的操作方法：</p>
<p>add(value) : 添加某个值，返回Set结构本身</p>
<p>delete(value) ：删除某个值，返回一个布尔值，表示是否删除成功</p>
<p>has(vaule) : 返回一个布尔值，表示参数知否为Set的成员</p>
<p>clear() : 清除所有成员，没有返回值</p>
<pre><code class="copyable">let set = new Set()
set.add(1).add(2).add(2)
set.size // 2
set.delete(1) // true
set.has(1) //false
set.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Set的遍历方法：</p>
<p>keys() : 返回键命的遍历器</p>
<p>values() : 返回键值的遍历器</p>
<p>entries() : 返回键值对的遍历器</p>
<p>forEach ： 使用回调函数遍历每个成员</p>
<p>注意：Set的遍历顺序就是插入顺序</p>
<pre><code class="copyable">let set = new Set(['red', 'green', 'blue']);
for (let item of set.keys()) &#123;
  console.log(item);
&#125;
// red
// green
// blue

for (let item of set.values()) &#123;
  console.log(item);
&#125;
// red
// green
// blue

for (let item of set.entries()) &#123;
  console.log(item);
&#125;
// ["red", "red"]
// ["green", "green"]
// ["blue", "blue"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Set 结构的实例与数组一样，也拥有forEach方法，用于对每个成员执行某种操作，没有返回值。</p>
<pre><code class="copyable">let set = new Set([1, 4, 9]);
set.forEach((value, key) => console.log(key + ' : ' + value))
// 1 : 1
// 4 : 4
// 9 : 9
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3.WeakSet是什么</h4>
<p>WeakSet 结构与 Set 类似，也是不重复的值的集合。但是，它与 Set 有两个区别。</p>
<ul>
<li>WeakSet 的成员只能是对象，而不能是其他类型的值。</li>
<li>WeakSet 中的对象都是弱引用。</li>
</ul>
<p>弱引用</p>
<p>即垃圾回收机制不考虑 WeakSet 对该对象的引用，也就是说，如果其他对象都不再引用该对象，那么垃圾回收机制会自动回收该对象所占用的内存，不考虑该对象还存在于 WeakSet 之中。</p>
<p>这是因为垃圾回收机制根据对象的可达性（reachability）来判断回收，如果对象还能被访问到，垃圾回收机制就不会释放这块内存。结束使用该值之后，有时会忘记取消引用，导致内存无法释放，进而可能会引发内存泄漏。WeakSet 里面的引用，都不计入垃圾回收机制，所以就不存在这个问题。因此，WeakSet 适合临时存放一组对象，以及存放跟对象绑定的信息。只要这些对象在外部消失，它在 WeakSet 里面的引用就会自动消失。</p>
<p>由于上面这个特点，WeakSet 的成员是不适合引用的，因为它会随时消失。另外，由于 WeakSet 内部有多少个成员，取决于垃圾回收机制有没有运行，运行前后很可能成员个数是不一样的，而垃圾回收机制何时运行是不可预测的，因此 ES6 规定 WeakSet 不可遍历。</p>
<pre><code class="copyable">let ws = new WeakSet();

let a = [[1, 2], [3, 4]];
let ws = new WeakSet(a); //是a数组的成员成为 WeakSet 的成员，而不是a数组本身。这意味着，数组的成员只能是对象。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>WeakSet的操作方法：</p>
<p>add()：向 WeakSet 实例添加一个新成员。</p>
<p>delete()：清除 WeakSet 实例的指定成员。</p>
<p>has()：返回一个布尔值，表示某个值是否在。</p>
<p>注意：WeakSet没有size属性，不能用forEach遍历它的成员，是因为成员都是弱引用，随时可能消失，遍历机制无法保证成员的存在，很可能刚刚遍历结束，成员就取不到了。</p>
<h4 data-id="heading-3">4.Map是什么</h4>
<p>JavaScript 的对象(Object)只能用字符串当作键。Map 它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。也就是说，Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应，是一种更完善的 Hash 结构实现。</p>
<pre><code class="copyable">let m = new Map();
let o = &#123;p: 'Hello World'&#125;;

m.set(o, 'content')
m.get(o) // "content"

const map = new Map([  // Map可以接受一个数组作为参数,该数组的成员是一个个表示键值对的数组。 
  ['name', '张三'], //不仅仅是数组，任何具有Iterator 接口、且每个成员都是一个双元素的数组的数据结构都可以当作Map构造函数的参数。
  ['title', 'Author']
]);
map.size // 2
map.get('name') // "张三"
map.get('title') // "Author"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5.Map的属性和方法</h4>
<p>size：属性, 返回 Map 结构的成员总数。</p>
<p>set(key, value)：方法，设置键名key对应的键值为value，然后返回整个 Map 结构。如果key已经有值，则键值会被更新，否则就新生成该键。</p>
<p>get(key)：方法，读取key对应的键值，如果找不到key，返回undefined。</p>
<p>has(key)：方法，返回一个布尔值，表示某个键是否在当前 Map 对象之中。</p>
<p>delete(key)：方法，删除某个键，返回true。如果删除失败，返回false。</p>
<p>clear()：方法，清除所有成员，没有返回值。</p>
<pre><code class="copyable">let map = new Map()
map.set('a',23).set('b',44)
map.size // 2
map.get('a') //23
map.has('a') //true
map.delete('a') //true
map.delete('a') // false
map.clear()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>遍历方法（Map 的遍历顺序就是插入顺序）</strong></p>
<p>keys()：返回键名的遍历器。</p>
<p>values()：返回键值的遍历器。</p>
<p>entries()：返回所有成员的遍历器。</p>
<p>forEach()：遍历 Map 的所有成员。</p>
<pre><code class="copyable">let map = new Map([
  [1, 'one'],
  [2, 'two'],
  [3, 'three'],
]);
[...map.keys()] // [1, 2, 3]
[...map.values()] // ['one', 'two', 'three']
[...map.entries()] // [[1,'one'], [2, 'two'], [3, 'three']]
[...map] // [[1,'one'], [2, 'two'], [3, 'three']]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">6.Map与其他类型相互转换</h4>
<pre><code class="copyable">let map = new Map([
  [1, 'one'],
  [2, 'two'],
  [3, 'three'],
]);
[...map] //Map转数组

new Map([ //数组转Map，把数组传入Map构造函数
  [true, 7],
  [&#123;foo: 3&#125;, ['abc']]
])

function strMapToObj(map) &#123; //map转对象
  for (let [k,v] of map) &#123;
    obj[k] = v;
  &#125;
  return obj;
&#125;
strMapToObj(map) // &#123;1: "one", 2: "two", 3: "three"&#125; 如果所有 Map 的键都是字符串，它可以无损地转为对象。如果有非字符串的键名，那么这个键名会被转成字符串，再作为对象的键名。
  let obj = &#123;&#125;;

let obj = &#123;"a":1, "b":2&#125;;
let map = new Map(Object.entries(obj)); //对象转map
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">7.Map的应用</h4>
<p>Map 的应用最直接的就是策略模式。举个例子抽奖：一等奖是手机，二等奖是耳机，三等奖是数据线，四等奖是徽章。那一般会这么写：</p>
<pre><code class="copyable">function getPrizes(level) &#123;
  if (level === "一等奖") &#123;
    return "手机"
  &#125; else if (level === "二等奖") &#123;
    return "耳机"
  &#125; else if (level === "三等奖") &#123;
    return "数据线"
  &#125; else if (level === "四等奖") &#123;
    return "徽章"
  &#125;
&#125;
getPrizes("一等奖");
// 或者
function getPrizes(level) &#123;
  switch (level) &#123;
    case "一等奖":
      return "手机"
    case "二等奖":
      return "耳机"
    case "三等奖":
      return "数据线"
    case "四等奖":
      return "徽章"
    default:
      break;
  &#125;
&#125;
getPrizes("一等奖");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述两种写法，如果条件越来越多的话，那写的 if...else...和 case 越来越长，代码相当的臃肿。 运用 Map 来写策略模式，简洁明了：</p>
<pre><code class="copyable">let prizes = new Map([
  ['一等奖', '手机'],
  ['二等奖', '耳机'],
  ['三等奖', '数据线'],
  ['四等奖', '徽章']
]);
function getPrizes(level) &#123;
  return prizes.get(level);
&#125;
getPrizes("一等奖");
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">8.WeakMap是什么</h4>
<p>WeakMap结构与Map结构类似，也是用于生成键值对的集合。</p>
<p>与Map也有区别：</p>
<ul>
<li>WeakMap只接受对象作为键名（null除外），不接受其他类型的值作为键名。</li>
<li>WeakMap的键名所指向的对象，不计入垃圾回收机制。</li>
</ul>

<ul>
<li>WeakMap没有遍历操作（即没有keys()、values()和entries()方法），也没有size属性。</li>
</ul>
<p>why</p>
<p>因为没有办法列出所有键名，某个键名是否存在完全不可预测，跟垃圾回收机制是否运行相关。这一刻可以取到键名，下一刻垃圾回收机制突然运行了，这个键名就没了，为了防止出现不确定性，就统一规定不能取到键名。</p>
<ul>
<li>WeakMap无法清空，即不支持clear方法。</li>
<li>WeakMap只有四个方法可用：get()、set()、has()、delete()。</li>
</ul></div>  
</div>
            