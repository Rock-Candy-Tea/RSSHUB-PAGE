
---
title: '每天学习 10 个实用Javascript代码片段（六）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4823'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 01:51:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=4823'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>【这是我参与8月更文挑战的第 <strong>25</strong> 天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a>】</p>
<p>每天学习10个实用JavaScript代码片段，加深对 Javascript 语法的理解，积累代码优化经验，第<strong>六</strong>天来了，本文代码片段包括生成随机数、数字加密、四舍五入、文件扩展名、变量数字转换。如果觉得内容能够带来点帮助，可以查看专栏《<a href="https://juejin.cn/column/6981851417929580557" target="_blank" title="https://juejin.cn/column/6981851417929580557">碎片时间学习Javascript代码</a>》其他内容，又或者有用到的需求片段，不妨在留言区留言。</p>
<h3 data-id="heading-0">1. Randoms</h3>
<p>在下面的代码片段，将展示了两种生成随机数或从数组中获取随机元素的方法。</p>
<p>生成指定范围的随机数：</p>
<pre><code class="copyable">const getRandoms = (min, max) => &#123;
    return Math.round(Math.random() * (max - min) + min);
&#125;;
console.log(getRandoms(10, 100));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随机获取数组中的一项元素：</p>
<pre><code class="copyable">const arrayCities = ["北京", "上海", "广州", "深圳", "天津", "重庆"];
const getRadmonItem = (array) =>
    array[Math.floor(Math.random() * array.length)];
console.log("随机城市：", getRadmonItem(arrayCities));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 数字加密</h3>
<p>下面代码片段展示了使用<strong>数字</strong>作为密钥对<strong>数字</strong>进行加密解密操作，使用异或运算 <code>XOR(^)</code> 来实现，展示一个简单的加密解密过程。</p>
<pre><code class="copyable">function Encrypt(secretNumber) &#123;
    const _secretNumber = secretNumber;
    const encrypted = (encryptNumber) => encryptNumber ^ _secretNumber;
    const decrypted = (encryptedContent) => encryptedContent ^ _secretNumber;
    return &#123;
        encrypted,
        decrypted,
    &#125;;
&#125;

const encryptHelper = new Encrypt(202108);
const encryptNumber = 20210901;

// 加密
const encrypted = encryptHelper.encrypted(encryptNumber);
console.log(encrypted); // 20410793
// 解密
const decrypted = encryptHelper.decrypted(encrypted);
console.log(decrypted); // 20210901
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 设置必选参数</h3>
<p>通常定义的一个函数的时候，对于可预期的参数可以使用默认值，而对于必要参数希望给出友好的提示，下面代码片段展示一个必填参数的定义：</p>
<pre><code class="copyable">const mandatory = (name) => &#123;
    throw new Error(`调用错误，必须传递参数：$&#123;name&#125;`);
&#125;;

const printTitle = (title = mandatory("标题")) => &#123;
    console.log(`打印文章标题：$&#123;title&#125;`);
&#125;;

printTitle("JavaScript"); // 打印文章标题：JavaScript
printTitle(); // Error: 调用错误，必须传递参数：标题
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 动态创建函数</h3>
<p>动态创建函数是一种基于字符串动态生成函数的动态机制，通常用于动态表单的规则验证中，第一个形参是用逗号分隔的实参列表，最后一个形参是函数体的逻辑代码：</p>
<pre><code class="copyable">const multiplyFn = new Function(
    "num1",
    "num2",
    "num3",
    "return num1*num2*num3"
);
console.log(multiplyFn(1, 2, 3)); // 6
// ES6
const multiply = new Function(
    "...numbers",
    "return numbers.reduce((acc,current) => acc * current, 1)"
);
console.log(multiply(1, 2, 3)); // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. 清空数组</h3>
<p>简单的数组清空方式是改变其 <code>length</code>  ，如下代码片段：</p>
<pre><code class="copyable">const arrayCities = ["北京", "上海", "广州", "深圳", "天津", "重庆"];
console.log(arrayCities); // [ '北京', '上海', '广州', '深圳', '天津', '重庆' ]
// 清空
arrayCities.length = 0;
console.log(arrayCities); // []
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 四舍五入</h3>
<p>小数点的处理，是数字常见的操作，主要涉及的方法是 <code>toFixed</code> 和 <code>Math</code> ，下面代码片段展示常用的方法。</p>
<p>由于 JavaScript 精度原因导致小数点相加的时候与预期有偏差，下面代码片段展示了四舍五入常见的方法和小数相加的处理：</p>
<pre><code class="copyable">const pi = 3.14159265359;
console.log(pi.toFixed(3)); // 3.142

const sumFloat = 0.1 + 0.2;
console.log(sumFloat); // 0.30000000000000004
console.log(sumFloat.toFixed(1)); // 0.3
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Math</code> 方法中常见用于取整的包括：<code>Math.round()</code> 舍入到最接近的整数， <code>Math.floor()</code> 向下舍入， <code>Math.ceil()</code> 向上舍入。最接近数学意义上四舍五入的方法就只有 <code>toFixed</code> ，如下代码片段所示：</p>
<pre><code class="copyable">const pi = 3.14159265359;
console.log(pi.toFixed(0)); // 3
console.log(Math.floor(pi)); // 3
console.log(Math.ceil(pi)); // 4
console.log(Math.round(pi)); // 3

const num2 = 3.5;
console.log(num2.toFixed(0)); // 4
console.log(Math.floor(num2)); // 3
console.log(Math.ceil(num2)); // 4
console.log(Math.round(num2)); // 4
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7. 数组项的对象解构</h3>
<p>数组项的对象解构在解析 CSV 格式的数据非常实用，请看下面的代码片段：</p>
<pre><code class="copyable">const csvAddressDetail = "广东省,深圳市,南山区,科技园北区科技园大厦";

const arrayAddress = csvAddressDetail.split(",");
const &#123; 0: province, 1: city, 2: district, 3: address &#125; = arrayAddress;

console.log(province, city, district, address);  // 广东省 深圳市 南山区 科技园北区科技园大厦
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然还可以跳过一些索引，如下：</p>
<pre><code class="copyable">const arrayAddress = csvAddressDetail.split(",");
const &#123; 1: city, 3: address &#125; = arrayAddress;

console.log(city, address); // 深圳市 科技园北区科技园大厦
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8. 变量数字转换</h3>
<p>将值转换为数字，特别是将字符串转换为数字，是经常会用到的，有许多方法可以进行转换，这里展示一些常见的方式：</p>
<pre><code class="copyable">console.log(+"15"); // 15
console.log(+true); // 1
console.log(+false); // 0
console.log(+null); // 0
console.log(Number("15")); // 15
console.log(parseInt("15", 10)); // 15
console.log(parseFloat("15.42")); // 15.42
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9. 获取文件扩展名</h3>
<p>下面的代码片段展示了通过一个完整路径或者文件名称获取文件相应的扩展名称方法：</p>
<pre><code class="copyable">const arrayFiles = [
    "/attach/pics/logo.png",
    "logo.svg",
    "template.xlsx",
    "template.doc",
];
const getExtName = (fullpath) => &#123;
    const root = fullpath.split(/[\\/]/).pop();
    const pos = root.lastIndexOf(".");
    return root === "" || pos < 1 ? "" : root.slice(pos + 1);
&#125;;

const arrayExtNames = arrayFiles.map((item) => getExtName(item));
console.log(arrayExtNames); // [ 'png', 'svg', 'xlsx', 'doc' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10. 普通函数定义</h3>
<p>假设需要定义一个函数，给定一些参数和函数，然后使用这些参数执行这个函数，代码片段展示一个计算器的功能及扩展运算符的使用，如下代码：</p>
<pre><code class="copyable">const calculator = (operation, ...numbers) => &#123;
    return operation(...numbers);
&#125;;
function add(...numbers) &#123;
    return numbers.reduce((acc, num) => acc + num, 0);
&#125;
function subtract(...numbers) &#123;
    return numbers.reduce((acc, num) => acc - num, 0);
&#125;
function multiply(...numbers) &#123;
    return numbers.reduce((acc, num) => acc * num, 1);
&#125;
console.log(calculator(add, 1, 2, 3, 4, 5)); // 15
console.log(calculator(subtract, 20, 12, 1)); // -33
console.log(calculator(multiply, 1, 2, 3, 4)); // 24

// 打印JSON数据的 title 属性
function printTitle(&#123; title &#125;) &#123;
    console.log(title);
&#125;
const article = &#123;
    title: "JavaScript 函数定义",
    description: "函数定义方式",
&#125;;
printTitle(article); // JavaScript 函数定义
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            