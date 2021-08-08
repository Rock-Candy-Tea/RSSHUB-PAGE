
---
title: 'ES6+新增常用内容总结（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3163'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 02:10:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=3163'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">ES6+ 新增数组方法</h2>
<h3 data-id="heading-1">Array.from</h3>
<pre><code class="copyable">Array Array.from(arrayLike[, mapFn[, thisArg]]) 将类数组转换成数组
    参数：
      arrayLike 类数组
    可选参数:    
      mapFn 类似 map 方法，循环类数组时的回函函数，返回值组成新数组
      thisArg mapFn 函数执行时的 this 指向
    返回值
      根据 arrayLike 生成的新数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Array.isArray</h3>
<pre><code class="copyable"> Boolean Array.isArray(data) 检测数据是否是个数组
    参数：
        data 要检测的数据
    返回值:
        true 数组，false 非数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Array.of</h3>
<pre><code class="copyable"> Array Array.of(element0[, element1[, ...[, elementN]]]) 将参数转成一个数组

    参数：
        elementN 要放入数组中的数据

    返回值：   
        新数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">arr.find</h3>
<pre><code class="copyable"> Value arr.find(callback[, thisArg]) 查找数组中满足要求的第一个元素的值
    参数：
        callback
            在数组每一项上执行的函数，接收 3 个参数：
                element
                    当前遍历到的元素。
                index[可选]
                    当前遍历到的索引。
                array[可选]
                    数组本身
    可选参数               
        thisArg
            执行回调时用作this 的对象
    返回值
        数组中第一个满足所提供测试函数的元素的值，否则返回 undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">arr.findIndex</h3>
<pre><code class="copyable">Index arr.findIndex(callback[, thisArg]) 查找数组中满足要求的第一个元素的值的索引
    参数:
        callback
            针对数组中的每个元素, 都会执行该回调函数, 执行时会自动传入下面三个参数:
            element
                当前元素。
            index
                当前元素的索引。
            array
                调用findIndex的数组。
    可选参数：            
        thisArg
            执行callback时作为this对象的值

    返回值：
        满足要求的值的索引
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">arr.flat</h3>
<pre><code class="copyable">Array arr.flat([depth]) 扁平化多维数组
    可选参数：
        depth
            指定要提取嵌套数组的结构深度，默认值为 1。

    返回值：
        一个包含将数组与子数组中所有元素的新数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">arr.flatMap</h3>
<pre><code class="copyable">Array arr.flatMap(function callback(currentValue[, index[, array]]) &#123;
    // 返回新数组的元素
&#125;[, thisArg])  
方法首先使用映射函数映射每个元素，然后将结果压缩成一个新数组。
它与 map 和 深度值1的 flat 几乎相同，但 flatMap 通常在合并成一种方法的效率稍微高一些

    参数：
        callback
            可以生成一个新数组中的元素的函数，可以传入三个参数：
            currentValue
                当前正在数组中处理的元素
            index可选
                可选的。数组中正在处理的当前元素的索引。
            array可选
                可选的。被调用的 map 数组
    可选参数：
        thisArg
            执行 callback 函数时 使用的this 值
    返回值：
        一个包含将数组与子数组中所有元素的新数组
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">arr.fill</h3>
<pre><code class="copyable">Array arr.fill(value[, start[, end]]); 
    用一个固定值填充一个数组中从起始索引到终止索引内的全部元素。不包括终止索引

    参数：
        用来填充数组元素的值。
    可选参数：
        start 
            起始索引，默认值为0。
        end 
            终止索引，默认值为 arr.length    
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">arr.includes</h3>
<pre><code class="copyable">Boolean arr.includes(valueToFind[, fromIndex]) 判断数组中是否包含一个指定的值
    参数：
        valueToFind 需要查找的值

    可选参数：
        从 fromIndex 处开始向后查找  

    返回值：
        true 代表数组中包含 valueToFind， false 代表数组中不包含 fromIndex
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">ES6+ 新增字符串方法</h2>
<h3 data-id="heading-11">str.includes</h3>
<pre><code class="copyable">Boolean str.includes(valueToFind[, fromIndex]) 
    判断字符串是否包含一个指定的值
详细： 参考数组的 includes
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">str.endsWith</h3>
<pre><code class="copyable">Boolean str.endsWith(searchString[, length]) 
判断当前字符串是否是以另外一个给定的子字符串“结尾”

参数
    searchString
        要搜索的子字符串。
可选参数
    length
        作为 str 的长度。默认值为 str.length
返回值
    如果传入的子字符串在搜索字符串的末尾则返回true；否则将返回 false。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">str.startsWith</h3>
<pre><code class="copyable">Boolean str.startsWith(searchString[, position]) 
判断当前字符串是否以另外一个给定的子字符串开头

参数
    searchString
        要搜索的子字符串。
可选参数
    position
        在 str 中搜索 searchString 的开始位置，默认值为 0，也就是真正的字符串开头处。
返回值
    如果传入的子字符串在搜索字符串的开始则返回true；否则将返回 false。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">str.repeat</h3>
<pre><code class="copyable">String str.repeat(count) 
构造并返回一个新字符串，该字符串包含被连接在一起的指定数量的字符串的副本
    参数
        count
            介于0和正无穷大之间的整数。表示在新构造的字符串中重复了多少遍原字符串

    返回值
        生成的新字符串
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            