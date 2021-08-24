
---
title: '《JavaScript 高级程序设计》 阅读笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81cc3028085a40fbb82b8f0467fd62d4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 02:59:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81cc3028085a40fbb82b8f0467fd62d4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h3 data-id="heading-0">第1章 什么是JavaScript</h3>
<p>背景介绍</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81cc3028085a40fbb82b8f0467fd62d4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210809164107369.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>ECMAScript: <code>JavaScript</code>实现了<code>ECMAScript</code>,<code>ECMAScript</code>描述语言的语法、类型等</li>
<li>DOM(文本对象模型)：DOM将整个页面抽象为一组分层节点，通过创建表示文档的树，控制网页的内容和结构</li>
<li>BOM(浏览器对象模型)：用于支持访问和操作浏览器的窗口</li>
</ul>
<h3 data-id="heading-1">第2章 HTML中的JavaScript</h3>
<p>介绍<code>script</code> 标签</p>
<ul>
<li><code>script</code> 可以加载行内代码和外部文件，外部问价更有利于维护</li>
<li><code>defer</code> 和 <code>async</code> 都可以更改加载顺序，区别是前者<code>script</code> 标签之间加载顺序固定都在<code>DOMContentLoaded</code> 之前加载，后者加载顺序不确定在页面load事件前执行</li>
<li><code>type</code> 属性为<code>module</code> 可以实现ES6当中的模块化</li>
</ul>
<h3 data-id="heading-2">第3章 语言基础</h3>
<p>基础语法</p>
<ul>
<li>
<p>变量声明</p>





























<table><thead><tr><th></th><th>作用域</th><th>可变性</th><th>备注</th></tr></thead><tbody><tr><td>var</td><td>函数; 作用域提升;</td><td>可变</td><td>可重复声明</td></tr><tr><td>let</td><td>块级; 作用域不能提升；</td><td>可变</td><td>不可重复声明</td></tr><tr><td>const</td><td>块级</td><td>不可变</td><td></td></tr></tbody></table>
</li>
<li>
<p>数据类型</p>















<table><thead><tr><th>基本数据类型</th><th>Undefined、Null、Boolean、Nunber、String、Symbol</th><th></th></tr></thead><tbody><tr><td>复杂数据类型</td><td>Object</td><td></td></tr></tbody></table>
<blockquote>
<p>Undefined 声明未赋值，Null 未声明</p>
</blockquote>
</li>
<li>
<p>整型转换</p>

























<table><thead><tr><th>函数</th><th>字符串</th><th>备注</th></tr></thead><tbody><tr><td>Number()</td><td>非空 =>NaN "" => 0</td><td></td></tr><tr><td>parseInt()</td><td>非空 => 数字前几位 "" => NaN</td><td>含有第二个参数指定进制数</td></tr><tr><td>parseFloat()</td><td>同上，转浮点</td><td>忽略进制</td></tr></tbody></table>
</li>
<li>
<p>模板字面量标签函数</p>
<pre><code class="copyable">const a = 3
const b = 4
// strings `` 字符串分割
// expressions 参数
function simpleTag(strings, ...expressions) &#123;
    ...
&#125;
const result simpleTag `$&#123;a&#125; + $&#123;b&#125; = $&#123;a+b&#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>String.raw 原始字符串</p>
</blockquote>
</li>
<li>
<p>内置Symbol符号</p>

























































<table><thead><tr><th>Symbol熟悉</th><th>描述</th></tr></thead><tbody><tr><td>Symbol.asyncIterator</td><td>该方法返回对象默认的AsyncIterator，由for-await-of语句使用</td></tr><tr><td>Symbol.hasInstance</td><td>该方法决定一个构造器对象是否认可一个对象是它的实例</td></tr><tr><td>Symbol.isConcatSpreadable</td><td>返回值决定用Array.prototype.concat()打平其数组元素方式</td></tr><tr><td>Symbol.iterator</td><td>该方法返回对象默认的迭代器。由for-of语句使用</td></tr><tr><td>Symbol.match</td><td>该方法用正则表达式匹配字符串，由String.prototype.match()方法使用</td></tr><tr><td>Symbol.replace</td><td>该方法替换一个字符串中匹配的子串。由String.prototype.replace()方法使用</td></tr><tr><td>Symbol.search</td><td>该方法返回字符串中匹配正则表达式的索引。由String.prototype.search()方法使用</td></tr><tr><td>Symbol.split</td><td>该方法在匹配正则表达式的索引位置拆分字符串。由String.prototype.split()方法使用</td></tr><tr><td>Symbol.species</td><td>该函数作为创建派生对象的构造函数</td></tr><tr><td>Symbol.toPrimitive</td><td>该方法将对象转换为相应的原始值。由ToPrimitive抽象操作使用</td></tr><tr><td>Symbol.toStringTag</td><td>该字符串用于创建对象的默认字符串描述。由内置方法Object.prototype.toString()使用</td></tr><tr><td>Symbol.unscopables</td><td>对象所有的以及继承的属性，都会从关联对象的with环境绑定中排除</td></tr></tbody></table>
</li>
<li>
<p>操作符</p>





















































<table><thead><tr><th>操作符</th><th>描述</th></tr></thead><tbody><tr><td>一元操作符</td><td>前置++、--；后置++，--；一元+、-</td></tr><tr><td>位操作符</td><td>~ 、& 、</td></tr><tr><td>布尔操作符</td><td>!、&&、</td></tr><tr><td>乘性操作符</td><td>*、/、%</td></tr><tr><td>指数操作符</td><td>**</td></tr><tr><td>加性操作符</td><td>+、-</td></tr><tr><td>关系操作符</td><td>>、<、>=、<=</td></tr><tr><td>相等操作符</td><td>==、!=、===、!===</td></tr><tr><td>条件操作符</td><td>?:</td></tr><tr><td>赋值操作符</td><td>=（复合赋值）</td></tr><tr><td>逗号操作符</td><td>, (多变量初始化)</td></tr></tbody></table>
</li>
<li>
<p>语句</p>













































<table><thead><tr><th>语句</th><th>描述</th></tr></thead><tbody><tr><td>if语句</td><td>逻辑判断语句</td></tr><tr><td>do-while</td><td>只到性循环</td></tr><tr><td>while</td><td>当型循环</td></tr><tr><td>for...i</td><td>确定循环</td></tr><tr><td>for...in</td><td>枚举对象中的非符号键属性</td></tr><tr><td>for...of</td><td>遍历可迭代对象的元</td></tr><tr><td>break、continue</td><td>break跳出循环、continue跳出本次循环</td></tr><tr><td>swich</td><td>分支语句，确实break具有穿透性</td></tr><tr><td>标签语句、with</td><td>不常用</td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-3">第4章 变量、作用域与内存</h3>
<ul>
<li>
<p>原始值和引用值</p>
<ul>
<li>原始值（primitive value）就是最简单的数据，不能添加动态属性</li>
<li>引用值（reference value）则是由多个值构成的对象，能添加动态属性</li>
</ul>
</li>
<li>
<p>复制值</p>
<ul>
<li>原始值本身会被复制到新变量的位置</li>
<li>引用值复制实际上是一个引用（实质是指针），一个对象上面的变化会在另一个对象上反映出来</li>
</ul>
</li>
<li>
<p>传递参数</p>
<ul>
<li>ECMAScript中所有函数的参数都是按值传递的</li>
</ul>
</li>
<li>
<p>确定类型</p>
<ul>
<li><code>typeof</code> 判断一个变量是否为原始类型</li>
<li><code>instanceof</code> 判断原型关系</li>
</ul>
</li>
<li>
<p>执行上下文和作用域</p>
<ul>
<li>变量查询由内而外</li>
</ul>
</li>
<li>
<p>垃圾回收</p>

















<table><thead><tr><th>方式</th><th>描述</th></tr></thead><tbody><tr><td>标记清理</td><td>垃圾回收程序运行的时候，会标记内存中存储的所有变量，然后将所有在上下文中的变量，以及被在上下文中的变量引用的变量的标记去掉，随后垃圾回收程序做一次内存清理</td></tr><tr><td>引用计数</td><td>对每个值都记录它被引用的次数。声明变量并给它赋一个引用值时，这个值的引用数为1。如果同一个值又被赋给另一个变量，那么引用数加1，如果保存对该值引用的变量被其他值给覆盖了，那么引用数减1，当一个值的引用数为0时，就说明没办法再访问到这个值了，因此可以安全地收回其内存了。</td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-4">第5章 基本引用类型</h3>
<ul>
<li>
<p>Date</p>
<ul>
<li>Date.parse()</li>
<li>Date.UTC()</li>
<li>原生Date 显示因浏览器而已，项目中可使用dayjs</li>
</ul>
</li>
<li>
<p>RegExp</p>
<ul>
<li>字符串创建 <code>let expression = /pattern/flags</code></li>
<li>对象创建 <code>let expression = new RegExp()</code></li>
</ul>

















<table><thead><tr><th>实例方法</th><th>描述</th></tr></thead><tbody><tr><td>exec()</td><td>用于配合捕获组使用</td></tr><tr><td>test()</td><td>测试模式是否匹配</td></tr></tbody></table>
</li>
<li>
<p>原始数据包装类型</p>





















<table><thead><tr><th></th><th>方法</th></tr></thead><tbody><tr><td>new Boolean()</td><td></td></tr><tr><td>new Number()</td><td>toFixed()、isInteger()</td></tr><tr><td>new String()</td><td></td></tr></tbody></table>
</li>
<li>
<p>字符串操作方法</p>

























































<table><thead><tr><th>字符串操作方法</th><th>描述</th></tr></thead><tbody><tr><td>concat()</td><td>拼接字符串</td></tr><tr><td>str.slice(beginIndex[, endIndex])</td><td>负参数字符串长度加上负参数值</td></tr><tr><td>str.substr(start[, length])</td><td>第一个负参数值当成字符串长度加上该值，将第二个负参数值转换为0</td></tr><tr><td>str.substring(indexStart[, indexEnd])</td><td>将所有负参数值都转换为0</td></tr><tr><td>indexOf()、lastIndexOf()</td><td></td></tr><tr><td>startsWith()、endsWith()和includes()</td><td></td></tr><tr><td>trim()</td><td></td></tr><tr><td>repeat()</td><td></td></tr><tr><td>padStart()和padEnd()</td><td></td></tr><tr><td>toLowerCase()、toLocaleLowerCase()、toUpperCase()和toLocaleUpperCase()</td><td></td></tr><tr><td>match()、search()、replace()</td><td>传入正则</td></tr><tr><td>localeCompare()</td><td></td></tr></tbody></table>
</li>
<li>
<p>单例内置对象</p>




















<table><thead><tr><th></th><th></th><th>备注</th></tr></thead><tbody><tr><td>Global</td><td>URL编码方法、eval()</td><td>浏览器将window对象实现为Global对象的代理</td></tr><tr><td>Math</td><td>min()、max()、ceil()、floor()、round()random()</td><td></td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-5">第6章 集合引用类型</h3>
<ul>
<li>
<p>Object</p>
<ul>
<li>创建： new Object() 和 字面量</li>
<li>属性取值：<code>.</code> 和<code>[]</code></li>
</ul>
</li>
<li>
<p>可迭代对象</p>













































<table><thead><tr><th></th><th>创建</th><th>方法</th></tr></thead><tbody><tr><td>共同</td><td></td><td>迭代方法：keys()、values()、entries() 迭代：every()、filter()、forEach()、map()、some()</td></tr><tr><td>Array</td><td>new Array() 、字面量、Array.form、Array.of</td><td>检测数组：Array.isArray() 填充：fill()、copyWithin() 转换: toLocaleString()、toString()和valueOf() 尾部方法：push()、pop() 头部方法：unshift()、shift() 排序：reverse()和sort() 搜索：indexOf()、lastIndexOf()和includes() 操作：concat()、slice()、splice() 归并：reduce()、reduceRight()</td></tr><tr><td>定型数组</td><td>在ArrayBuffer上创建视图DataView或者定型数组(XxxyyArray)</td><td></td></tr><tr><td>Map</td><td>new Map()</td><td>基本：set()、get()、has()、delete()、clear()和属性size 迭代方法：keys()、values()、entries()</td></tr><tr><td>WeakMap</td><td>new WeakMap()、key为对象</td><td>不可迭代</td></tr><tr><td>Set</td><td>new Set()</td><td>基本：add()、has()、delete()</td></tr><tr><td>WeakSet</td><td>new WeakSet()</td><td>不可迭代</td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-6">第7章 迭代器和生成器</h3>
<ul>
<li>
<p>迭代可以没有终止条件，循环不行</p>
</li>
<li>
<p>迭代器模式：实现了正式的Iterable接口，而且可以通过迭代器Iterator消费</p>
</li>
<li>
<p>自定义迭代器</p>
<pre><code class="copyable">class Count &#123;
    constructor(limit) &#123;
        this.limit = limit;
    &#125;
    [Symbol.iterator]() &#123;
        let limit = this.limit, count  = 1;
        return &#123;
            next() &#123;
                if(count <= limit) &#123;
                    return &#123; done: false, value: count++&#125;;
                &#125;else &#123;
                    return &#123; done: true, value: undefined &#125;;
                &#125;
            &#125;,
            return() &#123; // throw break 时调用
                console.log("breal/throw");
                return &#123; done: true &#125;;
            &#125;
        &#125;
    &#125;
&#125;
​
let count = new Count(10);
for(let i of count) &#123;
    if(i > 5) &#123;
        break
    &#125;
    console.log(i);
&#125;
​
for(let i of count) &#123;
    console.log(i);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>生成器： 生成器的形式是一个函数，函数名称前面加一个星号（＊）表示它是一个生成器，yield关键字可以让生成器停止和开始执行，yield＊实际上只是将一个可迭代对象序列化为一连串可以单独产出的值</p>
</li>
<li>
<p>与迭代器不同，所有生成器对象都有return()方法，return()方法会强制生成器进入关闭状态</p>
</li>
</ul>
<h3 data-id="heading-7">第8章 对象、类和面向对象编程</h3>
<ul>
<li>
<p>创建对象： <code>new Object()</code> 和字面量</p>
</li>
<li>
<p>对于数据属性包含configurable、enumerable、writable和value属性，对于访问器属性包含configurable、enumerable、get和set属性。</p>
</li>
<li>
<p>Object.assign() 合并对象</p>
</li>
<li>
<p>原型模式</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56c38d95b52f440f80a7fe829b5d9d37~tplv-k3u1fbpfcp-watermark.image" alt="image-20210816145905079.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>原型链 （针对构造方法）</p>
<ul>
<li>
<p>实现</p>
<pre><code class="copyable">function Parent1() &#123;
    this.name = 'parent1';
    this.play = [1, 2, 3]
&#125;
function Child1() &#123;
    this.type = 'child2';
&#125;
Child1.prototype = new Parent1();
console.log(new Child1());
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>优点： 实现继承</p>
</li>
<li>
<p>缺点：引用值共享、父类传参</p>
</li>
</ul>
</li>
<li>
<p>盗用构造函数</p>
<ul>
<li>
<p>实现</p>
<pre><code class="copyable">function Parent1()&#123;
    this.name = 'parent1';
&#125;
​
Parent1.prototype.getName = function () &#123;
    return this.name;
&#125;
​
function Child1()&#123;
    Parent1.call(this);
    this.type = 'child1'
&#125;
​
let child = new Child1();
console.log(child);  // 没问题
console.log(child.getName());  // 会报错
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>优点： 可以传参</p>
</li>
<li>
<p>缺点：子类无法继承父类之前自己定义的方法</p>
</li>
</ul>
</li>
<li>
<p>组合继承</p>
<ul>
<li>
<p>实现</p>
<pre><code class="copyable">function Parent3 () &#123;
    this.name = 'parent3';
    this.play = [1, 2, 3];
&#125;
​
Parent3.prototype.getName = function () &#123;
    return this.name;
&#125;
function Child3() &#123;
    // 第二次调用 Parent3()
    Parent3.call(this);
    this.type = 'child3';
&#125;
​
// 第一次调用 Parent3()
Child3.prototype = new Parent3();
// 手动挂上构造器，指向自己的构造函数
Child3.prototype.constructor = Child3;
var s3 = new Child3();
var s4 = new Child3();
s3.play.push(4);
console.log(s3.play, s4.play);  // 不互相影响
console.log(s3.getName()); // 正常输出'parent3'
console.log(s4.getName()); // 正常输出'parent3'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>优点： 弥补了原型链和盗用构造函数的不足，保留了instanceof操作符和isPrototypeOf()方法识别合成对象的能力</p>
</li>
</ul>
</li>
<li>
<p>原型式继承 （针对普通对象）</p>
<ul>
<li>
<p>实现</p>
<pre><code class="copyable">let parent4 = &#123;
    name: "parent4",
    friends: ["p1", "p2", "p3"],
    getName: function() &#123;
      return this.name;
    &#125;
&#125;;
​
let person4 = Object.create(parent4);
person4.name = "tom";
person4.friends.push("jerry");
​
let person5 = Object.create(parent4);
person5.friends.push("lucy");
​
console.log(person4.name);
console.log(person4.name === person4.getName());
console.log(person5.name);
console.log(person4.friends);
console.log(person5.friends);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>缺点： 遮蔽原型对象上的同名属性，多个实例的引用类型属性指向相同的内存</p>
</li>
</ul>
</li>
<li>
<p>寄生式继承</p>
<ul>
<li>
<p>实现：</p>
<pre><code class="copyable">let parent5 = &#123;
    name: "parent5",
    friends: ["p1", "p2", "p3"],
    getName: function() &#123;
      return this.name;
    &#125;
  &#125;;
​
function clone(original) &#123;
    let clone = Object.create(original);
    clone.getFriends = function() &#123;
        return this.friends;
    &#125;;
    return clone;
&#125;
​
let person5 = clone(parent5);
​
console.log(person5.getName());
console.log(person5.getFriends());
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>缺点：两次调用父类的构造函数造成浪</p>
</li>
</ul>
</li>
<li>
<p>寄生组合式继承</p>
<ul>
<li>
<p>实现：</p>
<pre><code class="copyable">function clone (parent, child) &#123;
    // 这里改用 Object.create 就可以减少组合继承中多进行一次构造的过程
    child.prototype = Object.create(parent.prototype);
    child.prototype.constructor = child;
&#125;
​
function Parent6() &#123;
    this.name = 'parent6';
    this.play = [1, 2, 3];
&#125;
Parent6.prototype.getName = function () &#123;
    return this.name;
&#125;
function Child6() &#123;
    Parent6.call(this);
    this.friends = 'child5';
&#125;
​
clone(Parent6, Child6);
​
Child6.prototype.getFriends = function () &#123;
return this.friends;
&#125;
​
let person6 = new Child6();
console.log(person6);
console.log(person6.getName());
console.log(person6.getFriends());
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>类</p>
<ul>
<li>背后使用的仍然是原型和构造函数的概念</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">第9章 代理和反射</h3>
<ul>
<li>
<p>创建代理</p>
<pre><code class="copyable">// 普通代理
const proxy = new Proxy(target, handle);
​
// 可撤销代理
const &#123; proxy, revoke &#125;  = Proxy.revocable(target, handle);
...
revoke()
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>捕获器</p>





























































<table><thead><tr><th>捕获器</th><th>触发时机</th></tr></thead><tbody><tr><td>get()</td><td>获取属性值的操作中被调用</td></tr><tr><td>set()</td><td>设置属性值的操作中被调用</td></tr><tr><td>has()</td><td>在in操作符中被调用</td></tr><tr><td>defineProperty()</td><td>在Object.defineProperty()中被调用</td></tr><tr><td>getOwnPropertyDescriptor()</td><td>在Object.getOwnPropertyDescriptor()中被调用</td></tr><tr><td>deleteProperty()</td><td>在delete操作符中被调用</td></tr><tr><td>ownKeys()</td><td>在Object.keys()及类似方法中被调用</td></tr><tr><td>getPrototypeOf()</td><td>在Object.getPrototypeOf()</td></tr><tr><td>setPrototypeOf()</td><td>在Object.setPrototypeOf()中被调用</td></tr><tr><td>isExtensible()</td><td>在Object.isExtensible()中被调用</td></tr><tr><td>preventExtensions()</td><td>在Object.preventExtensions()中被调用</td></tr><tr><td>apply()</td><td>在调用函数时中被调用</td></tr><tr><td>construct()</td><td>在new操作符中被调用</td></tr></tbody></table>
</li>
<li>
<p>代理不足</p>
<ul>
<li>代理对象的this指向自身</li>
<li>有些ECMAScript内置类型代理对象上不存在某些内部槽位</li>
</ul>
</li>
<li>
<p>代理模式</p>
<ul>
<li>通过捕获get、set和has等操作，监控对象</li>
<li>代理内部实现对外部代码是不可见的</li>
<li>在set()中根据所赋的值决定允许还是拒绝赋值（返回布尔值）</li>
<li>利用apply()、construct()对函数和构造函数参数进行审查</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">第10章 函数</h3>
<ul>
<li>
<p>函数形式</p>
<ul>
<li>
<p>函数声明</p>
</li>
<li>
<p>函数表达式</p>
<ul>
<li>作用域不提升</li>
</ul>
</li>
<li>
<p>箭头函数</p>
<ul>
<li>简写<code>()</code> 、返回值</li>
<li>无<code>arguments</code></li>
<li>外部<code>this</code></li>
</ul>
</li>
<li>
<p>Function构造函数</p>
</li>
</ul>
</li>
<li>
<p>参数</p>
<ul>
<li>严格模式arguments不可修改</li>
<li>默认参数</li>
<li><code>...</code> 形参是归并参数，实参是解构参数</li>
<li><code>new.target</code>可用于函数实例化</li>
</ul>
</li>
<li>
<p>函数方法</p>
<ul>
<li>
<p>apply 第二个参数数组</p>
</li>
<li>
<p>call 第二个分别传入</p>
<ul>
<li>bind 创建新的函数实例， 第二个参数数组</li>
</ul>
</li>
</ul>
</li>
<li>
<p>闭包</p>
<ul>
<li>引用了另一个函数作用域中变量的函数，通常是在嵌套函数中实现的</li>
</ul>
</li>
</ul>
<h3 data-id="heading-10">第11 章 期约和异步函数</h3>
<ul>
<li>
<p>异步编程： 回调函数 => <code>Promise</code> => <code>await/async</code></p>
</li>
<li>
<p>Promise</p>
<ul>
<li>创建： <code>new Promise()</code>、<code>Promise.resolve</code>、<code>Promiste.reject</code></li>
<li><code>Promise</code>状态： pending、fulfilled、rejected</li>
<li>实例方法： then()、catch()、finally()</li>
<li>Promise.all()和Promise.race()</li>
</ul>
</li>
<li>
<p>async/await</p>
</li>
</ul>
<h3 data-id="heading-11">第12章 BOM</h3>
<ul>
<li>
<p>浏览器对象模型(BOM)</p>



































<table><thead><tr><th>对象</th><th>详情</th><th>属性、方法</th></tr></thead><tbody><tr><td>window</td><td>ECMAScript的Global对象、浏览器窗口的JavaScript接口</td><td>窗口大小相关、视口滚动、open()、定时器、系统对话框</td></tr><tr><td>location</td><td>当前窗口中加载文档的信息，以及通常的导航功能</td><td>search、assign()、reload()</td></tr><tr><td>navigator</td><td>navigator对象的属性通常用于确定浏览器的类型</td><td>plugins、registerProtocolHandler()</td></tr><tr><td>screen</td><td>浏览器窗口外面的客户端显示器的信息</td><td></td></tr><tr><td>history</td><td>当前窗口首次使用以来用户的导航历史记录</td><td>go()、back()、forward()</td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-12">第13 章 客户端检测</h3>
<ul>
<li>能力检测：先普遍，后特例</li>
<li>用户代理：navigator.userAgent 不准确可篡改</li>
<li>软件硬件检测：navigator、screen</li>
</ul>
<h3 data-id="heading-13">第14章 DOM</h3>
<ul>
<li>
<p>DOM中总共有12种节点类型，这些类型都继承一种Node类型</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a74d605a1d7745a2bc0338cc305af0ff~tplv-k3u1fbpfcp-watermark.image" alt="image-20210818110157966.png" loading="lazy" referrerpolicy="no-referrer"></p>























































<table><thead><tr><th>DOM节点</th><th>描述</th><th>属性和方法</th></tr></thead><tbody><tr><td>Node类型</td><td>所有节点类型都继承Node类型</td><td>nodeType、nodeName、nodeValue、childNodes<br>appendChild()、insertBefore()、replaceChild()、cloneNode()、normalize()</td></tr><tr><td>Document类型</td><td>HTMLDocument继承Document</td><td>documentElement、body、doctype、title、implementation<br>getElementById()、getElementsByTagName()、write()、writeln()、open()、close()</td></tr><tr><td>Element类型</td><td>对外暴露出访问元素标签名、子节点和属性的能力</td><td>nodeName或tagName属性来获取元素的标签名（无自定义属性）、attributes、childNodes<br>getAttribute()、setAttribute()、removeAttribute()、document.createElement()</td></tr><tr><td>Text类型</td><td>纯文本，不含HTML代码</td><td>nodeValue<br>document.createTextNode()、normalize()、splitText()</td></tr><tr><td>Comment类型</td><td>注释</td><td>除splitText()之外Text节点所有的字符串操作方法<br>document.createComment()</td></tr><tr><td>CDATASection类型</td><td>XML中特有的CDATA区块</td><td>document.createCDataSection()</td></tr><tr><td>DocumentType类型</td><td>含文档的文档类型信息</td><td>name、entities和notations</td></tr><tr><td>DocumentFragment类型</td><td>标记中没有对应表示的类型，临时容器</td><td>document.createDocumentFragment()</td></tr><tr><td>Attr类型</td><td>元素数据在DOM中通过Attr类型表示</td><td>name、value和specified<br>document.createAttribute()</td></tr></tbody></table>
<ul>
<li>
<p>DOM编程</p>
<ul>
<li>动态脚本</li>
<li>动态样式</li>
<li>操作表格</li>
<li>使用NodeList (动态变化，记录初值)</li>
</ul>
</li>
<li>
<p>MutationObserver</p>
<pre><code class="copyable">let observe = new MutationObserver((mutationRecords) => console.log('DOM was mutated', mutationRecords));
observe.observe(document.body, &#123; attributes: true &#125;)
document.body.className = "foo";
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-14">第15章 DOM扩展</h3>
<ul>
<li>
<p>Selectors API</p>





















<table><thead><tr><th>方法</th><th>描述</th></tr></thead><tbody><tr><td>querySelector()</td><td>接收CSS选择符参数</td></tr><tr><td>querySelectorAll()</td><td>也接收一个用于查询的参数，返回所有匹配的节点</td></tr><tr><td>matches()</td><td>接收一个CSS选择符参数，检测某个元素是否匹配规则</td></tr></tbody></table>
</li>
<li>
<p>Element Traversal API</p>

































<table><thead><tr><th>属性</th><th>描述</th></tr></thead><tbody><tr><td>childElementCount</td><td>不会把元素间的空格当成空白节点</td></tr><tr><td>firstElementChild</td><td></td></tr><tr><td>lastElementChild</td><td></td></tr><tr><td>lastElementChild</td><td></td></tr><tr><td>previousElementSibling</td><td></td></tr><tr><td>nextElementSibling</td><td></td></tr></tbody></table>
</li>
<li>
<p>HTML5</p>
</li>
</ul>





















































<table><thead><tr><th>方法、属性</th><th>描述</th></tr></thead><tbody><tr><td>getElementsByClassName()</td><td>接受一个或多个类名，返回类名中包含相应类的元素的NodeList</td></tr><tr><td>classList属性</td><td>add()、contains()、 remove()、toggle()</td></tr><tr><td>focus()</td><td></td></tr><tr><td>readyState属性</td><td>文档是否加载完毕：loading、complete</td></tr><tr><td>compatMode属性</td><td>指示浏览器当前处于什么渲染模式</td></tr><tr><td>head属性</td><td>指向文档的元素</td></tr><tr><td>characterSet属性</td><td></td></tr><tr><td>data-</td><td>自定义属性，dataset获取</td></tr><tr><td>innerHTML属性、outerHTML属性</td><td></td></tr><tr><td>insertAdjacentHTML()与insertAdjacentText()</td><td></td></tr><tr><td>scrollIntoView()</td><td>滚动浏览器窗口或容器元素以便包含元素进入视口</td></tr></tbody></table>
<ul>
<li>
<p>专用扩展</p>

























<table><thead><tr><th>属性、方法</th><th>描述</th></tr></thead><tbody><tr><td>children属性</td><td>只包含元素的Element类型的子节点</td></tr><tr><td>contains()、compareDocumentPosition()</td><td></td></tr><tr><td>innerText、outerText</td><td></td></tr><tr><td>scrollIntoViewIfNeeded()</td><td></td></tr></tbody></table>
</li>
</ul>
<h3 data-id="heading-15">第16章 DOM2和DOM3</h3>
<ul>
<li>
<p>DOM2给大部分DOM1方法提供了特定于命名空间的版本</p>
<ul>
<li>Node的变化：isSameNode()和isEqualNode()</li>
<li>Document的变化:  XxxNs、importNode()、defaultView、document.implementation</li>
<li>Element的变化：XxxNs</li>
<li>NamedNodeMap的变化: XxxNs</li>
<li>DocumentType的变化</li>
<li>内嵌窗格的变化： contentDocument、contentWindow</li>
</ul>
</li>
<li>
<p>样式</p>
<ul>
<li>任何支持style属性的HTML元素在JavaScript中都会有一个对应的style属性，style属性是CSSStyleDeclaration类型的实例</li>
<li>DOM2 Style在document.defaultView上增加了getComputedStyle()方法</li>
<li>CSSStyleSheet类型继承StyleSheet，包括使用元素和通过元素定义的样式表，CSSRule类型表示样式表中的一条规则
</li></ul>
</li>
<li>
<p>遍历</p>
<ul>
<li>
<p>NodeIterator</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> div1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"div1"</span>)
<span class="hljs-keyword">const</span> iterator = <span class="hljs-built_in">document</span>.createNodeIterator(div1, NodeFilter.SHOW_ELEMENT, <span class="hljs-literal">null</span>, <span class="hljs-literal">false</span>)
<span class="hljs-keyword">let</span> node = iterator.nextNode()
<span class="hljs-keyword">while</span>(node !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-built_in">console</span>.log(node.tagName);
    node = iterator.nextNode()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>TreeWalker 同NodeIterator 更灵活，previousSibling()、nextSibling()、firstChild()、lastChild()、parentNode()、currentNode</p>
</li>
</ul>
</li>
<li>
<p>范围</p>
<ul>
<li>创建createRange()，简单选择设置范围selectNode()或selectNodeContents()</li>
<li>setStart()和setEnd()</li>
<li>操作： deleteContents()、extractContents()、cloneContents()、insertNode()、surroundContents()、collapse()、compareBoundaryPoints()、cloneRange()、detach()</li>
</ul>
</li>
</ul>
<h3 data-id="heading-16">第17章 事件</h3>
<ul>
<li>
<p>事件流</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/560ea9dcfb7945e8ac81db611b7ac4f4~tplv-k3u1fbpfcp-watermark.image" alt="image-20210819103451472.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>事件处理程序</p>
<ul>
<li>
<p>HTML事件处理程序</p>
<pre><code class="hljs language-html copyable" lang="html">// 方式一
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mybtn"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Click me"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"console.log('bbb')"</span>></span>

// 方式二
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"mybtn"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Click me"</span> <span class="hljs-attr">onclick</span>=<span class="hljs-string">"showMessage()"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showMessage</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'bbb'</span>)
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>    
    
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>DOM0事件处理程序</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加事件</span>
<span class="hljs-keyword">const</span> mybtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"mybtn"</span>);
mybtn.onclick = <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aaa"</span>); &#125;

<span class="hljs-comment">// 移除事件</span>
mybtn.onclick = <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>DOM2事件处理程序</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 添加事件</span>
<span class="hljs-keyword">const</span> mybtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"mybtn"</span>);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">showMessage</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aaa"</span>); 
&#125;
mybtn.addEventListener(<span class="hljs-string">"click"</span>, showMessage, <span class="hljs-literal">false</span>) 

<span class="hljs-comment">// 移除事件</span>
mybtn.removeEventListener(<span class="hljs-string">"click"</span>, showMessage, <span class="hljs-literal">false</span>) 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>IE事件处理程序: attachEvent()和detachEvent()</li>
</ul>
</li>
<li>
<p>事件对象</p>
</li>
<li>
<p>DOM事件对象，回调函数参数event：type、eventPhase、preventDefault()、stopPropagation()</p>
</li>
<li>
<p>IE事件对象，event对象只是window对象的一个属性</p>
</li>
<li>
<p>事件类型</p>
<ul>
<li>用户界面事件: load、unload、abort、error、select、resize、scroll</li>
<li>焦点事件：  blur、DOMFocusIn、DOMFocusOut、focus、focusin</li>
<li>鼠标和滚轮事件: click、dblclick、mousedown、mouseenter、mouseleave、mousemove、mouseover、mouseup、mousewheel</li>
<li>键盘与输入事件：keydown、textInput(keypress)、keyup</li>
<li>合成事件：compositionstart、compositionupdate、 compositionend</li>
<li>HTML5事件： contextmenu、beforeunload、DOMContentLoaded、eadystatechange、pageshow与pagehide、hashchange</li>
<li>设备事件：orientationchange、deviceorientation、devicemotion</li>
<li>触摸及手势事件：touchstart、touchmove、touchend、touchcancel、gesturestart、 gesturechange、gestureend</li>
</ul>
</li>
<li>
<p>内存与性能</p>
</li>
<li>
<p>事件委托：事件委托利用事件冒泡，可以只使用一个事件处理程序来管理一种类型的事件</p>
</li>
<li>
<p>模拟事件</p>
<ul>
<li>
<p>document.createEvent()方法创建一个event对象，UIEvents、MouseEvents、HTMLEvents、HTMLEvents、CustomEvent</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mybtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"mybtn"</span>);
mybtn.onclick = <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"aaa"</span>); &#125;
<span class="hljs-keyword">const</span> event = <span class="hljs-built_in">document</span>.createEvent(<span class="hljs-string">"MouseEvents"</span>);
event.initEvent(<span class="hljs-string">"click"</span>);
mybtn.dispatchEvent(event);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-17">第18章 动画与Canvas图形</h3>
<ul>
<li>JavaScript动画：requestAnimationFrame</li>
<li>canvas：getContext('2d')、fillRect()、strokeRect()、clearRect()、fillText()、strokeText()</li>
<li>WebGL内容太多，得找教程重新学习</li>
</ul>
<h3 data-id="heading-18">第19章 表单脚本</h3>
<ul>
<li>获取表单、提交表单、重置表单</li>
<li>表单事件： 选择文本、输入过滤</li>
<li>表单序列化：字符串拼接</li>
</ul>
<h3 data-id="heading-19">第20章 JavaScriptAPI</h3>
<ul>
<li>Atomics API可以保证SharedArrayBuffer上的JavaScript操作是线程安全的</li>
<li>Encoding API主要用于实现字符串与定型数组之间的转换</li>
<li>File API与Blob API是为了让Web开发者能以安全的方式访问客户端机器上的文件</li>
<li>Notifications API用于向用户显示通知</li>
<li>Page Visibility API旨在为开发者提供页面对用户是否可见的信息</li>
<li>Streams API解决Web应用如何消费有序的小信息块</li>
<li>计时API，所有与页面相关的指标，包括已经定义和将来会定义的，都会存在于window.performance对象上</li>
<li>Web Cryptography API描述了一套密码学工具</li>
</ul>
<h3 data-id="heading-20">第21章 错误处理与调试</h3>
<ul>
<li>try/catch语句</li>
<li>throw</li>
</ul>
<h3 data-id="heading-21">第22章 处理XML</h3>
<ul>
<li>DOMParser/ XMLSerializer</li>
</ul>
<h3 data-id="heading-22">第23章 JSON</h3>
<ul>
<li>语法：简单值、对象、数组</li>
<li>JSON.stringify()，可用oJSON()更改值</li>
<li>JSON.parse()</li>
</ul>
<h3 data-id="heading-23">第24章 网络请求与远程资源</h3>
<ul>
<li>XMLHttpRequest</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> xhr = <span class="hljs-keyword">new</span> XMLHttpRequest();
xhr.open(<span class="hljs-string">"get"</span>, <span class="hljs-string">"xxx"</span>, <span class="hljs-literal">false</span>);
xhr.send(<span class="hljs-literal">null</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>Fetch API</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> jsonHeader = <span class="hljs-keyword">new</span> Headers(&#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"cors"</span>,
&#125;)

fetch(<span class="hljs-string">"xxx"</span>, &#123;
    <span class="hljs-attr">headers</span>: jsonHeader,
&#125;).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(res);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>unload 发送请求：  Beacon API</p>
</li>
</ul>
<h3 data-id="heading-24">第25章 客户端存储</h3>
<ul>
<li>
<p>cookie: 服务端设置，特定域有效，document.cookie</p>
</li>
<li>
<p>Web Storage</p>
<ul>
<li>sessionStorage</li>
<li>localStorage</li>
</ul>
</li>
<li>
<p>IndexedDB 很多限制实际上与Web Storage一样</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> db,
    request,
    version = <span class="hljs-number">1</span>;
request = indexedDB.open(<span class="hljs-string">"admin"</span>, version);
request.onerror = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    alert(<span class="hljs-string">`Failed to open <span class="hljs-subst">$&#123;e.targer.errorCode&#125;</span>`</span>);
&#125;    
request.onsuccess = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    db = e.target.result;
    <span class="hljs-built_in">console</span>.log(db);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">第26章 模块</h3>
<ul>
<li>
<p>CommonJS(Node.js使用了轻微修改版本的CommonJS)</p>
<ul>
<li>module.exports/exports</li>
<li>require</li>
</ul>
</li>
<li>
<p>AMD浏览器为目标执行环境</p>
</li>
<li>
<p>ES Module</p>
<ul>
<li>export</li>
<li>import</li>
</ul>
</li>
</ul>
<h3 data-id="heading-26">第27章 工作者线程</h3>
<ul>
<li>专用工作者线程：创建专用工作者线程来执行在页面线程之外的其他任务</li>
<li>共享工作者线程：可以被多个可信任的执行上下文访问</li>
<li>服务工作者线程：可以拦截外出请求和缓存响应</li>
</ul>
<h3 data-id="heading-27">第28章 最佳实践</h3>
<ul>
<li>以具体项目为主</li>
</ul></div>  
</div>
            