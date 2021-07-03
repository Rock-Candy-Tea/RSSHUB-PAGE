
---
title: '4个 JavaScript 字符串操作技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6068'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 04:56:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=6068'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>字符串是编程世界最基本最重要的数据类型之一，JavaScript 也不例外。JavaScript 字符串是不可变的，对于存储可以由字符、数字和 Unicode 组成的文本很便捷。JavaScript 提供了许多内置函数，允许以不同的方式创建和操作字符串。在本文将分享一些优雅的操作 JavaScript 字符串的技巧。</p>
<h3 data-id="heading-0">1. 拆分字符串</h3>
<p>JavaScript中的 <code>split()</code> 方法使用指定的分隔符字符串将一个 <code>String</code> 对象分割成子字符串数组，以一个指定的分割字串来决定每个拆分的位置。 有两个可选参数（分隔符和可选限制计数）将字符串转换为字符或子字符串数组，不设置分隔符将返回数组中的完整字符串。分隔符可以采用单个字符、字符串，甚至正则表达式。下面是使用正则表达式将使用逗号和空格拆分字符串的代码：</p>
<pre><code class="copyable">const title = "4个，JavaScript 字符串技巧";
console.log(title.split(/[\s+，/]+/)); // [ '4个', 'JavaScript', '字符串技巧' ]
console.log(title.split(/[\s+，/]+/, 2)); // [ '4个', 'JavaScript' ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过 <code>split()</code> 函数拆分的字符串可以通过简单地通过<code>join("")</code> 连接起来。</p>
<h3 data-id="heading-1">2. JSON格式化和解析</h3>
<p>JSON 不是仅限 JavaScript 的数据类型，并且广泛用于前后端数据交互。<code>JSON.stringify()</code> 函数用于将对象转换为 <code>JSON</code> 格式的字符串。通常，只需将对象作为参数即可，如下所示：</p>
<pre><code class="copyable">const article = &#123;
    title: "JavaScript 字符串技巧",
    view: 30000,
    comments: null,
    content: undefined,
&#125;;
const strArticle = JSON.stringify(article); 

console.log(strArticle); // &#123;"title":"JavaScript 字符串技巧","view":30000,"comments":null&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码可以看到，在 <code>stringify</code> 中会过滤掉 <code>undefined</code> 的值，但 <code>null</code> 值不会。</p>
<p><code>JSON.stringify()</code>  可以接受两个可选参数，第二个参数是一个替换器，可以在其中指定要打印的键的数组或清除它们的函数。如下代码：</p>
<pre><code class="copyable">console.log(JSON.stringify(article, ["title", "comments"])); // &#123;"title":"JavaScript 字符串技巧","comments":null&#125;
console.log(JSON.stringify(article, [])); // &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于一个巨大的 JSON，传递一个长数组可能影响可读性及效率。因此，可以设置替换函数并为要跳过的键返回 <code>undefined</code> ，如下代码：</p>
<pre><code class="copyable">const result = JSON.stringify(article, (key, value) =>
    key === "title" ? undefined : value
);
console.log(result); // &#123;"view":30000,"comments":null&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>JSON.stringify()</code>  的第三个参数通过指定缩进（在嵌套块中很有用）来格式化 <code>JSON</code>，可以传递一个数字来设置缩进间距，甚至可以传递一个字符串来替换空格。如下代码：</p>
<pre><code class="copyable">console.log(JSON.stringify(article, ["title"], "\t")); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出的格式如下：</p>
<pre><code class="copyable">&#123;
    "title": "JavaScript 字符串技巧"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个 <code>JSON.parse()</code> 函数，它接受一个 <code>JSON</code> 字符串并将其转换为一个 JavaScript 对象。它还接受一个 <code>reviver</code> 函数，可以在返回值之前拦截对象属性并修改属性值。</p>
<pre><code class="copyable">const reviver = (key, value) => (key === "view" ? 0 : value);

var jsonString = JSON.stringify(article);
var jsonObj = JSON.parse(jsonString, reviver);

console.log(jsonObj); // &#123; title: 'JavaScript 字符串技巧', view: 0, comments: null &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. 多行字符串和嵌入式表达式</h3>
<p>在 JavaScript 中有三种创建字符串的方式，可以使用单引号<code> ''</code> 、双引号 <code>""</code> 或反引号（键盘的左上方，<code> 1</code> 的左边按键）。</p>
<pre><code class="copyable">const countries1 = "China";
const countries2 = "China";
const countries3 = `China`;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前两种创建方式基本相同，并且可以混合和匹配以连接或添加带引号的字符串（通过使用相反的语法风格），而反引号可以对字符串进行花哨而强大的操作。</p>
<p>反引号也称为模板字面量，反引号在创建多行字符串和嵌入表达式时很方便。下面是如何在 JavaScript 中使用字符串插值创建多行字符串的代码：</p>
<pre><code class="copyable">const year = "2021";
const month = 7;
const day = 2;
const detail = `今天是$&#123;year&#125;年$&#123;month&#125;月$&#123;day&#125;日，
是个不错的日子！`;

console.log(detail);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出的结果也换行了，如下：</p>
<pre><code class="copyable">今天是2021年7月2日，
是个不错的日子！
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了字符串字面量，在 <code>$&#123;&#125;</code> 中允许任何有效的表达式，它可以是一个函数调用或表达式，甚至是一个嵌套模板。</p>
<p>标记模板是模板字面量的一种高级形式，它允许使用一个函数来解析模板字面量，其中内嵌的表达式是参数。如下代码：</p>
<pre><code class="copyable">const title = "JavaScript 字符串技巧";
const view = 30000;

const detail = (text, titleExp, viewExp) => &#123;
    const [string1, string2, string3] = [...text];
    return `$&#123;string1&#125;$&#123;titleExp&#125;$&#123;string2&#125;$&#123;viewExp&#125;$&#123;string3&#125;`;
&#125;;

const intro = detail`本文的标题是《$&#123;title&#125;》，当前阅读量是： $&#123;view&#125;`;

console.log(intro); // 文的标题是《JavaScript 字符串技巧》，当前阅读量是：30000
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 验证字符串数组中是否存在子字符串</h3>
<p>查找 JavaScript 字符串中是否存在子字符串时间容易的事情，在 ES6 中，只需要使用 <code>includes</code> 函数。</p>
<p>但需要验证字符串是否存于数据中，主要数组中其中一项包含就返回 <code>true</code> ，如果都不包含返回 <code>false</code>，因此需要使用 <code>some</code> 函数与<code>includes</code> 一起使用，如下代码：</p>
<pre><code class="copyable">const arrayTitles = ["Javascript", "EScript", "Golang"];
const hasText = (array, findText) =>
    array.some((item) => item.includes(findText));

console.log(hasText(arrayTitles, "script")); // true
console.log(hasText(arrayTitles, "php")); // false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">总结</h3>
<p>JavaScript 字符串操作是项目中常见的操作，上面4个技巧值得学习并应用到实际开发中。</p></div>  
</div>
            