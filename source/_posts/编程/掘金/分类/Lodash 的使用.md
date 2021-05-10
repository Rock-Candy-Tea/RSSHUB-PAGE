
---
title: 'Lodash 的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=357'
author: 掘金
comments: false
date: Sun, 09 May 2021 04:37:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=357'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Lodash 的使用</h1>
<h5 data-id="heading-1">安装</h5>
<ul>
<li>浏览器环境：</li>
</ul>
<pre><code class="copyable"><script src="lodash.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>or</p>
<pre><code class="copyable">npm i --save lodash
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">数组</h2>
<h5 data-id="heading-3">chunk</h5>
<ul>
<li>将数组（array）拆分成多个 size 长度的区块，并将这些区块组成一个新数组。 如果 array 无法被分割成全部等长的区块，那么最后剩余的元素将组成一个区块。</li>
</ul>
<h5 data-id="heading-4">参数</h5>
<ul>
<li>array (Array): 需要处理的数组</li>
<li>[size=1] (number): 每个数组区块的长度</li>
</ul>
<h3 data-id="heading-5">返回一个包含拆分区块的新数组（注：相当于一个二维数组）。</h3>
<pre><code class="copyable">import lodash from 'lodash';

const array = ['a', 'b', 'c', 'd'];
const result = lodash.chunk(array,2);
const res = lodash(array,3);
console.log(result);

 // result=> [['a','b'],['c','d']]
 //res => [['a', 'b', 'c'], ['d']]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">compact</h3>
<ul>
<li>创建一个新数组，包含原数组中所有的非假值元素。例如 false, null,0, "", undefined, 和 NaN 都是被认为是“假值”。</li>
</ul>
<h3 data-id="heading-7">参数</h3>
<ul>
<li>array (Array): 待处理的数组</li>
</ul>
<h3 data-id="heading-8">返回值</h3>
<p>Array): 返回过滤掉假值的新数组。</p>
<pre><code class="copyable">import lodash from 'lodash';

const array = [0, 1, false, 2, '', 3]
const result = lodash.compact(array);
console.log(result);
// => [1, 2, 3]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">concat</h3>
<ul>
<li>创建一个新数组，将array与任何数组 或 值连接在一起。</li>
</ul>
<h3 data-id="heading-10">参数</h3>
<ul>
<li>array (Array): 被连接的数组。</li>
<li>[values] (...*): 连接的值。</li>
</ul>
<h3 data-id="heading-11">返回值</h3>
<ul>
<li>返回连接后的新数组。</li>
</ul>
<pre><code class="copyable">import lodash from 'lodash';
const array = [1,2];
const array1 = [3,4];
const result = lodash.concat(array,array1);
console.log('result',result);
// => [1, 2, 3, 4]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">difference</h3>
<ul>
<li>创建一个具有唯一array值的数组，每个值不包含在其他给定的数组中。（注：即创建一个新数组，这个数组中的值，为第一个数字（array 参数）排除了给定数组中的值。） 该方法使用SameValueZero做相等比较。结果值的顺序是由第一个数组中的顺序确定。</li>
</ul>
<h3 data-id="heading-13">参数</h3>
<ul>
<li>array (Array): 要检查的数组。</li>
<li>[values] (...Array): 排除的值。</li>
</ul>
<h3 data-id="heading-14">返回值</h3>
<p>(Array): 返回一个过滤值后的新数组。</p>
<pre><code class="copyable">import lodash from 'lodash';
const array = [3,2,1];
const values = [4,2];
const result = lodash.difference(array,values);
console.log(result);
// => [3, 1]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">differenceBy</h3>
<ul>
<li>这个方法类似_.difference ，除了它接受一个 iteratee （注：迭代器）， 调用array 和 values 中的每个元素以产生比较的标准。 结果值是从第一数组中选择。iteratee 会调用一个参数：(value)。（注：首先使用迭代器分别迭代array 和 values中的每个元素，返回的值作为比较值）。</li>
</ul>
<h3 data-id="heading-16">参数</h3>
<ul>
<li>array (Array): 要检查的数组。</li>
<li>[values] (...Array): 排除的值。</li>
<li>[iteratee=_.identity] (Array|Function|Object|string): iteratee 调用每个元素。</li>
</ul>
<h3 data-id="heading-17">返回值</h3>
<ul>
<li>(Array): 返回一个过滤值后的新数组。</li>
</ul>
<pre><code class="copyable">const array = [3.1, 2.2, 1.3];
const values = [4.4, 2.5];
const result = lodash.differenceBy(array,values,(value) =>&#123;
    return value > 2;
&#125; );
console.log('result',result);
// => [1.3]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">differenceWith</h3>
<ul>
<li>这个方法类似_.difference ，除了它接受一个 comparator （注：比较器），它调用比较array，values中的元素。 结果值是从第一数组中选择。comparator 调用参数有两个：(arrVal, othVal)。</li>
</ul>
<h3 data-id="heading-19">参数</h3>
<ul>
<li>array (Array): 要检查的数组。</li>
<li>[values] (...Array): 排除的值。</li>
<li>[comparator] (Function): comparator 调用每个元素。</li>
</ul>
<h3 data-id="heading-20">返回值</h3>
<ul>
<li>(Array): 返回一个过滤值后的新数组。</li>
</ul>
<pre><code class="copyable">import lodash from 'lodash';
const objects = [&#123; 'x': 1, 'y': 2 &#125;, &#123; 'x': 2, 'y': 1 &#125;];
const values = [&#123;'x':1,'y':2&#125;]
const result = lodash.differenceWith(objects,values,lodash.isEqual);
// =>  => [&#123; 'x': 2, 'y': 1 &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">drop</h3>
<ul>
<li>创建一个切片数组，去除array前面的n个元素。（n默认值为1。）</li>
</ul>
<h3 data-id="heading-22">参数</h3>
<ul>
<li>array (Array): 要查询的数组。</li>
<li>[n=1] (number): 要去除的元素个数。</li>
</ul>
<h3 data-id="heading-23">返回值</h3>
<ul>
<li>(Array): 返回array剩余切片。</li>
</ul>
<pre><code class="copyable">import lodash from 'lodash';
const array = [1, 2, 3];
const result = lodash.drop(array,2);
// => [3]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">dropRight</h3>
<ul>
<li>创建一个切片数组，去除array尾部的n个元素。（n默认值为1。）</li>
</ul>
<h3 data-id="heading-25">参数</h3>
<ul>
<li>array (Array): 要查询的数组。</li>
<li>[n=1] (number): 要去除的元素个数。</li>
</ul>
<h3 data-id="heading-26">返回值</h3>
<ul>
<li>(Array): 返回array剩余切片。</li>
</ul>
<pre><code class="copyable">import lodash  from 'lodash';
const array = [1,2,3];
const result = lodash.dropRight(array,2);
// => [1]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">dropRightWhile</h3>
<ul>
<li>创建一个切片数组，去除array中从 predicate 返回假值开始到尾部的部分。predicate 会传入3个参数： (value, index, array)。</li>
</ul></div>  
</div>
            