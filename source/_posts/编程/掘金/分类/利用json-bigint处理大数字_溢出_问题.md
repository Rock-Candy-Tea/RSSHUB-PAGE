
---
title: '利用json-bigint处理大数字_溢出_问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00129b66024d4f15aad0934a2d3c0840~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 23:17:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00129b66024d4f15aad0934a2d3c0840~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">关于后端返回数据中的大数字问题</h2>
<blockquote>
<p>假设后端需要根据传入的id来返回请求的数据，而传入的id超过了<code>-2^53</code>到<code>2^53</code>的范围，此时就无法接收准确的id，这样就会导致后端拿不到正确的id，导致出现<code>404</code>的错误</p>
</blockquote>
<p>JavaScript 能够准确表示的整数范围在<code>-2^53</code>到<code>2^53</code>之间（不含两个端点），超过这个范围，无法精确表示这个值，这使得 JavaScript 不适合进行科学和金融方面的精确计算。</p>
<pre><code class="copyable">Math.pow(2, 53) // 9007199254740992
​
9007199254740992  // 9007199254740992
9007199254740993  // 9007199254740992
​
Math.pow(2, 53) === Math.pow(2, 53) + 1
// true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，超出 2 的 53 次方之后，一个数就不精确了。 ES6 引入了<code>Number.MAX_SAFE_INTEGER</code>和<code>Number.MIN_SAFE_INTEGER</code>这两个常量，用来表示这个范围的上下限。</p>
<pre><code class="copyable">Number.MAX_SAFE_INTEGER === Math.pow(2, 53) - 1
// true
Number.MAX_SAFE_INTEGER === 9007199254740991
// true
​
Number.MIN_SAFE_INTEGER === -Number.MAX_SAFE_INTEGER
// true
Number.MIN_SAFE_INTEGER === -9007199254740991
// true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，可以看到 JavaScript 能够精确表示的极限。</p>
<p>后端返回的数据一般都是 <strong>JSON 格式的字符串</strong>。</p>
<pre><code class="copyable">'&#123; "id": 9007199254740995, "name": "Jack", "age": 18 &#125;'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果这个字符不做任何处理，你能方便的获取到字符串中的指定数据吗？非常麻烦。所以我们要把它转换为 JavaScript 对象来使用就很方便了。</p>
<p>幸运的是 axios 为了方便我们使用数据，它会在内部使用 <code>JSON.parse()</code> 把后端返回的数据转为 JavaScript 对象。</p>
<pre><code class="copyable">// &#123; id: 9007199254740996, name: 'Jack', age: 18 &#125;
JSON.parse('&#123; "id": 9007199254740995, "name": "Jack", "age": 18 &#125;')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，超出安全整数范围的 id 无法精确表示，这个问题并不是 axios 的错。</p>
<p>了解了什么是大整数的概念，接下来的问题是如何解决？</p>
<h2 data-id="heading-1">利用JSON-BIGINT处理大数字问题</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsidorares%2Fjson-bigint" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sidorares/json-bigint" ref="nofollow noopener noreferrer">json-bigint</a> 是一个第三方包，它可以帮我们很好的处理这个问题。</p>
<p>使用它的第一步就是把它安装到你的项目中。</p>
<pre><code class="copyable">npm i json-bigint
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是使用它的一个简单示例。</p>
<pre><code class="copyable">const jsonStr = '&#123; "art_id": 1245953273786007552 &#125;'
​
console.log(JSON.parse(jsonStr)) // 1245953273786007600
​
// JSONBig 可以处理数据中超出 JavaScript 安全整数范围的问题
console.log(JSONBig.parse(jsonStr)) // 把 JSON 格式的字符串转为 JavaScript 对象
​
// 使用的时候需要把 BigNumber 类型的数据转为字符串来使用
console.log(JSONBig.parse(jsonStr).art_id.toString()) // 1245953273786007552
​
console.log(JSON.stringify(JSONBig.parse(jsonStr)))
​
console.log(JSONBig.stringify(JSONBig.parse(jsonStr))) // 把 JavaScript 对象 转为 JSON 格式的字符串转
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00129b66024d4f15aad0934a2d3c0840~tplv-k3u1fbpfcp-watermark.image" alt="1582099315865-5e805425-7abf-4cf2-9df3-acc2ef8f9bb9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>json-bigint 会把超出 JS 安全整数范围的数字转为一个 BigNumber 类型的对象，对象数据是它内部的一个算法处理之后的，我们要做的就是在使用的时候转为字符串来使用。</p>
</blockquote>
<p>通过 Axios 请求得到的数据都是 Axios 处理（JSON.parse）之后的，我们应该在 Axios 执行处理之前手动使用 json-bigint 来解析处理。Axios 提供了自定义处理原始后端返回数据的 API：<code>transformResponse</code> 。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd769fcf383d4222880f9fb57722830d~tplv-k3u1fbpfcp-watermark.image" alt="5731630397570_.pic_hd.jpg" loading="lazy" referrerpolicy="no-referrer">
在<code>src/utils/request.js</code>处理axios文件中进行配置</p>
<pre><code class="copyable">import axios from 'axios'
​
import jsonBig from 'json-bigint'
​
var json = '&#123; "value" : 9223372036854775807, "v2": 123 &#125;'
​
console.log(jsonBig.parse(json))
​
const request = axios.create(&#123;
  baseURL: 'http://ttapi.research.itcast.cn/', // 接口基础路径
​
  // transformResponse 允许自定义原始的响应数据（字符串）
  transformResponse: [function (data) &#123;
    try &#123;
      // 如果转换成功则返回转换的数据结果
      return jsonBig.parse(data)
    &#125; catch (err) &#123;
      // 如果转换失败，则包装为统一数据格式并返回
      return &#123;
        data
      &#125;
    &#125;
  &#125;]
&#125;)
​
export default request
​
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改props类型</p>
<pre><code class="copyable">props: &#123;
    articleId: &#123;
      type: [Number, String, Object],
      required: true
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>扩展：ES2020 BigInt</p>
<p>ES2020 引入了一种新的数据类型 BigInt（大整数），来解决这个问题。BigInt 只用来表示整数，没有位数的限制，任何位数的整数都可以精确表示。</p>
</blockquote>
<p>参考链接：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FBigInt" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/BigInt" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fnumber%23BigInt-%25E6%2595%25B0%25E6%258D%25AE%25E7%25B1%25BB%25E5%259E%258B" target="_blank" rel="nofollow noopener noreferrer" title="http://es6.ruanyifeng.com/#docs/number#BigInt-%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B" ref="nofollow noopener noreferrer">es6.ruanyifeng.com/#docs/numbe…</a></li>
</ul></div>  
</div>
            