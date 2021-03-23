
---
title: 'js中数组常用方法'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 19:36:17 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1. push()方法</strong></p>
<ul>
<li>作用：在数组的尾部追加数组元素</li>
<li>格式：arr.push(value1, value2, value3...)</li>
<li>注意：
<ul>
<li>返回值是修改后数组的长度</li>
<li>原数组被改变</li>
</ul>
</li>
</ul>
<p><strong>2. pop()方法</strong></p>
<ul>
<li>作用：删除数组尾部的数组元素（一次只能删除一个）</li>
<li>格式：arr.pop(value1)</li>
<li>注意：
<ul>
<li>返回值是被删除的数组元素</li>
<li>原数组被改变</li>
</ul>
</li>
</ul>
<p><strong>3. unshift()方法</strong></p>
<ul>
<li>作用：在数组的头部添加元素</li>
<li>格式：arr.unshift(value1, value2, value3...)</li>
<li>注意：
<ul>
<li>返回值是修改后数组的长度</li>
<li>原数组被改变</li>
</ul>
</li>
</ul>
<p><strong>4. shift()方法</strong></p>
<ul>
<li>作用：删除数组头部的元素（一次只能删除一个）</li>
<li>格式：arr.shift(value1)</li>
<li>注意：
<ul>
<li>返回值是被删除的数组元素</li>
<li>原数组被改变</li>
</ul>
</li>
</ul>
<p><strong>5. concat()方法</strong></p>
<ul>
<li>作用：实现两个或多个数组的拼接</li>
<li>格式：arr.concat(arr2,arr3...)</li>
<li>注意：
<ul>
<li>返回值是拼接后的新的数组</li>
<li>原数组不受影响</li>
<li>concat方法的参数可以是一个数组，也可以是数值，也可以是多个数组，中间用逗号分隔</li>
</ul>
</li>
</ul>
<p><strong>6. join()方法</strong></p>
<ul>
<li>作用：将数组的每个元素以指定的字符连接形成新字符串返回</li>
<li>格式：arr.join(分割符)</li>
<li>注意：
<ul>
<li>返回值是数组元素拼接成的字符串</li>
<li>参数可选。指定要使用的分隔符。如果省略该参数，则使用逗号作为分隔符</li>
<li>原数组不受影响</li>
</ul>
</li>
</ul>
<p><strong>7. slice()方法</strong></p>
<ul>
<li>作用：从已有的数组中返回选定的元素。</li>
<li>格式：arr.slice(begin,end); begin表示开始位置的下标，end表示结束位置的下标</li>
<li>注意：
<ul>
<li>返回值为截取出来的新的数组</li>
<li>原数组不受影响</li>
<li>在截取时包含begin，但是不包含end，即含头不含尾</li>
<li>如果省略end，那么表示从begin一直截取到最后</li>
<li>如果begin和end同时省略，那么表示复制数组（生成一个独立的新的数组）</li>
<li>参数可以是负数，如果是负数，那么-1表示数组中的最后一个元素</li>
<li>如果第二个参数，即end的值大于等于数组的长度，那么表示从begin一直截取到数组的最后</li>
</ul>
</li>
</ul>
<p><strong>8. splice()方法</strong></p>
<ul>
<li>作用：对数组进行增、删、改操作</li>
<li>格式：arr.splice(index,howmany,item1,.....,itemX);</li>
</ul>





















<table><thead><tr><th>参数</th><th>描述</th></tr></thead><tbody><tr><td>index</td><td>必需。整数，规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。</td></tr><tr><td>howmany</td><td>必需。要删除的项目数量。如果设置为 0，则不会删除项目。</td></tr><tr><td>item1, ..., itemX</td><td>可选。向数组添加的新项目。</td></tr></tbody></table>
<ul>
<li>注意：
<ul>
<li>增的格式：arr.splice(下标，0，要插入的值);返回值为一个空数组;</li>
<li>删的格式：arr.splice(下标，个数);返回值为被删除的数组元素所形成的新的数组，注意delete删除的元素的值，而splice删除的是值和空间;</li>
<li>改的格式：arr.splice(下标，个数，新的值);返回值为被修改的元素所形成的新的数组</li>
</ul>
</li>
</ul>
<p><strong>9. toString()方法</strong></p>
<ul>
<li>作用：数组转换为字符串，并返回结果</li>
<li>格式：arr.toString();</li>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>数组中的元素之间用逗号分隔。</li>
</ul>
</li>
</ul>
<p><strong>10. reverse()方法</strong></p>
<ul>
<li>作用：颠倒数组中元素的顺序</li>
<li>格式：arr.reverse();</li>
<li>注意：
<ul>
<li>原数组被改变</li>
<li>数组中的元素之间用逗号分隔。</li>
</ul>
</li>
</ul>
<p><strong>11. sort()方法</strong></p>
<ul>
<li>作用：对数组的元素进行排序</li>
<li>格式：arr.sort(sortby); 参数可选。规定排序顺序。必须是函数。</li>
<li>注意：
<ul>
<li>函数的返回值为原数组</li>
<li>如果调用该方法时没有使用参数，将按字母顺序对数组中的元素进行排序，说得更精确点，是按照字符编码的顺序进行排序。要实现这一点，首先应把数组的元素都转换成字符串（如有必要），以便进行比较。</li>
<li>升序：
arr.sort(function(a,  b) &#123;
return  a – b;
&#125;);</li>
<li>降序：
arr.sort(function(a, b) &#123;
return  b – a;
&#125;);</li>
</ul>
</li>
</ul>
<p><strong>12. includes()方法</strong></p>
<ul>
<li>作用：判断一个数组是否包含一个指定的值，如果是返回 true，否则false。</li>
<li>格式：arr.includes(value);</li>
<li>注意：
<ul>
<li>原数组不受影响</li>
</ul>
</li>
</ul>
<p><strong>13. find()方法</strong></p>
<ul>
<li>作用：返回满足提供的测试函数的数组中第一个元素的值</li>
</ul>
<pre><code class="copyable">var num = [1, 30, 39, 29, 10, 13];
var val = num.find(myFunc);

function myFunc(element) &#123;
return element >= 18;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>为数组中的每个元素都调用一次函数执行：当数组中的元素在测试条件时返回 true 时, find() 返回符合条件的元素，之后的值不会再调用执行函数。如果没有符合条件的元素返回 undefined</li>
<li>find() 对于空数组，函数是不会执行的。</li>
</ul>
</li>
</ul>
<p><strong>14. every()方法</strong></p>
<ul>
<li>作用：检测数组所有元素是否都符合指定条件（通过函数提供）。</li>
</ul>
<pre><code class="copyable">var num = [1, 30, 39, 29, 10, 13];
var val = num.every(myFunc);

function myFunc(element) &#123;
return element >= 18;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>指定函数检测数组中的所有元素：如果数组中检测到有一个元素不满足，则整个表达式返回 false ，且剩余的元素不会再进行检测。如果所有元素都满足条件，则返回 true。</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul>
<p><strong>15. some()方法</strong></p>
<ul>
<li>作用：检测数组中的元素是否满足指定条件（函数提供）。</li>
</ul>
<pre><code class="copyable">var num = [1, 30, 39, 29, 10, 13];
var val = num.every(myFunc);

function myFunc(element) &#123;
return element >= 18;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>指定函数检测数组中的所有元素：如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测。如果没有满足条件的元素，则返回false。</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul>
<p><strong>16. forEach()方法</strong></p>
<ul>
<li>作用：对数组进行遍历循环，对数组中的每一项运行给定函数</li>
<li>arr.forEach(function(item,index,items)&#123;&#125;)
<ul>
<li>参数1：遍历的数组内容item</li>
<li>参数2：对应的数组索引 index</li>
<li>参数3：数组本身items</li>
</ul>
</li>
<li>注意：
<ul>
<li>没有返回值</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul>
<p><strong>17. map()方法</strong></p>
<ul>
<li>作用：返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值</li>
<li>arr.map(function(item,index,items)&#123;&#125;)
<ul>
<li>参数1：遍历的数组内容item</li>
<li>参数2：对应的数组索引 index</li>
<li>参数3：数组本身items</li>
</ul>
</li>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul>
<p><strong>18. filter()方法</strong></p>
<ul>
<li>作用：创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。</li>
</ul>
<pre><code class="copyable">var num = [1, 30, 39, 29, 10, 13];
var val = num.filter(myFunc);

function myFunc(element) &#123;
return element >= 18;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul>
<p><strong>19. reduce()方法</strong></p>
<ul>
<li>作用：接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终计算为一个值。</li>
<li>格式: arr.reduce(callback,[initialValue])
<ul>
<li>callback （执行数组中每个值的函数，包含四个参数）
<ul>
<li>1、previousValue （上一次调用回调返回的值，或者是提供的初始值（initialValue））</li>
<li>2、currentValue （数组中当前被处理的元素）</li>
<li>3、index （当前元素在数组中的索引）</li>
<li>4、array （调用 reduce 的数组）</li>
</ul>
</li>
<li>initialValue （作为第一次调用 callback 的第一个参数。）</li>
</ul>
</li>
<li>实例</li>
</ul>
<pre><code class="copyable">var arr = [1, 2, 3, 4];
var sum = arr.reduce(function(prev, cur, index, arr) &#123;
    console.log(prev, cur, index);
    return prev + cur;
&#125;)
console.log(arr, sum);
// 1 2 1
// 3 3 2
// 6 4 3
// [1, 2, 3, 4] 10
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：
<ul>
<li>原数组不受影响</li>
<li>作为一个高阶函数，用于函数的 compose。</li>
<li>不会对空数组进行检测</li>
</ul>
</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            