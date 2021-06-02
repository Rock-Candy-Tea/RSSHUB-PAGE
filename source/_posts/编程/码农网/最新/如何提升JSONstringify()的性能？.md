
---
title: '如何提升JSON.stringify()的性能？'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/11.png'
author: 码农网
comments: false
date: Wed, 12 Jun 2019 13:46:11 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/11.png'
---

<div>   
<h2 id="articleHeader0">1.熟悉的<code>JSON.stringify()</code></h2>
<p>在浏览器端或服务端，<code>JSON.stringify()</code>都是我们很常用的方法：</p>
<ul>
<li>将 JSON object 存储到 localStorage 中；</li>
<li>POST 请求中的 JSON body；</li>
<li>处理响应体中的 JSON 形式的数据；</li>
<li>甚至某些条件下，我们还会用它来实现一个简单的深拷贝；</li>
<li>……</li>
</ul>
<p>在一些性能敏感的场合下（例如服务端处理大量并发），或面对大量 stringify 的操作时，我们会希望它的性能更好，速度更快。这也催生了一些优化的 stringify 方案/库，下图是它们与原生方法的性能对比：</p>
<p><img class="aligncenter size-full wp-image-57059" title="11" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/11.png" alt width="1200" height="488" referrerpolicy="no-referrer"></p>
<p>绿色部分时原生<code>JSON.stringify()</code>，可见性能相较这些库都要低很多。那么，在大幅的性能提升背后的技术原理是什么呢？</p>
<h2 id="articleHeader1">2. 比 <code>stringify</code> 更快的 <code>stringify</code></h2>
<p>由于 JavaScript 是动态性很强的语言，所以对于一个 Object 类型的变量，其包含的键名、键值、键值类型最终只能在运行时确定。因此，执行<code>JSON.stringify()</code>时会有很多工作要做。在一无所知的情况下，我们想要大幅优化显然无能为力。</p>
<p>那么如果我们知道这个 Object 中的键名、键值信息呢 —— 也就是知道它的结构信息，这会有帮助么？</p>
<p>看个例子：</p>
<p>下面这个 Object，</p>
<pre class="brush: javascript; gutter: true; first-line: 1">const obj = &#123;
    name: 'alienzhou',
    status: 6,
    working: true
&#125;;</pre>
<p>我们对它应用<code>JSON.stringify()</code>，得到结果为</p>
<pre class="brush: javascript; gutter: true; first-line: 1">JSON.stringify(obj);
// &#123;"name":"alienzhou","status":6,"working":true&#125;</pre>
<p>现在如果我们知道这个<code>obj</code>的结构是固定的：</p>
<ul>
<li>键名不变</li>
<li>键值的类型一定</li>
</ul>
<p>那么其实，我可以创建一个“定制化”的 stringify 方法</p>
<pre class="brush: javascript; gutter: true; first-line: 1">function myStringify(o) &#123;
    return (
        '&#123;"name":"'
        + o.name
        + '","status":'
        + o.status
        + ',"isWorking":'
        + o.working
        + '&#125;'
    );
&#125;</pre>
<p>看看我们的<code>myStringify</code>方法的输出：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">myStringify(&#123;
    name: 'alienzhou',
    status: 6,
    working: true
&#125;);
// &#123;"name":"alienzhou","status":6,"isWorking":true&#125;

myStringify(&#123;
    name: 'mengshou',
    status: 3,
    working: false
&#125;);
// &#123;"name":"mengshou","status":3,"isWorking":false&#125;</pre>
<p>可以得到正确的结果，但只用到了类型转换和字符串拼接，所以“定制化”方法可以让“stringify”更快。</p>
<p>总结来看，如何得到比 <code>stringify</code> 更快的 <code>stringify</code> 方法呢？</p>
<ol>
<li>需要先确定对象的结构信息；</li>
<li>根据其结构信息，为该种结构的对象创建“定制化”的<code>stringify</code>方法，其内部实际是通过字符串拼接生成结果的；</li>
<li>最后，使用该“定制化”的方法来 stringify 对象即可。</li>
</ol>
<p>这也是大多数 stringify 加速库的套路，转化为代码就是类似：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">import faster from 'some_library_faster_stringify';

// 1. 通过相应规则，定义你的对象结构
const theObjectScheme = &#123;
    // ……
&#125;;

// 2. 根据结构，得到一个定制化的方法
const stringify = faster(theObjectScheme);

// 3. 调用方法，快速 stringify
const target = &#123;
    // ……
&#125;;
stringify(target);</pre>
<h2 id="articleHeader2">3. 如何生成“定制化”的方法</h2>
<p>根据上面的分析，核心功能在于，<strong>根据其结构信息，为该类对象创建“定制化”的stringify方法，其内部实际是简单的属性访问与字符串拼接。</strong></p>
<p>为了了解具体的实现方式，下面我以两个实现上略有差异的开源库为例来简单介绍一下。</p>
<h3 id="articleHeader3">3.1. fast-json-stringify</h3>
<p><img class="aligncenter size-full wp-image-57063" title="22" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/22.png" alt width="800" height="45" referrerpolicy="no-referrer"></p>
<p>下图是根据 <a href="https://github.com/fastify/fast-json-stringify#benchmarks" rel="nofollow noreferrer" target="_blank">fast-json-stringify</a> 提供的 benchmark 结果，整理出来的性能对比。</p>
<p><img class="aligncenter size-full wp-image-57064" title="33" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/33.png" alt width="800" height="398" referrerpolicy="no-referrer"></p>
<p>可以看到，在大多数场景下具备2-5倍的性能提升。</p>
<h4>3.1.1. scheme 的定义方式</h4>
<p>fast-json-stringify 使用了 <a href="http://json-schema.org/latest/json-schema-validation.html" rel="nofollow noreferrer" target="_blank">JSON Schema Validation </a>来定义（JSON）对象的数据格式。其 scheme 定义的结构本身也是 JSON 格式的，例如对象</p>
<pre class="brush: javascript; gutter: true; first-line: 1">&#123;
    name: 'alienzhou',
    status: 6,
    working: true
&#125;</pre>
<p>对应的 scheme 就是：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">&#123;
    title: 'Example Schema',
    type: 'object',
    properties: &#123;
        name: &#123;
            type: 'string'
        &#125;,
        status: &#123;
            type: 'integer'
        &#125;,
        working: &#123;
            type: 'boolean'
        &#125;
    &#125;
&#125;</pre>
<p>其 scheme 定义规则丰富，具体使用可以参考 <a href="https://ajv.js.org/" rel="nofollow noreferrer" target="_blank">Ajv</a> 这个 JSON 校验库。</p>
<h4>3.1.2. stringify 方法的生成</h4>
<p>fast-json-stringify 会根据刚才定义的 scheme，拼接生成出实际的函数代码字符串，然后使用 <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function" rel="nofollow noreferrer" target="_blank">Function 构造函数</a>在运行时动态生成对应的 stringify 函数。</p>
<p>在代码生成上，首先它会注入预先定义好的各类工具方法，这一部分不同的 scheme 都是一样的：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">var code = `
    'use strict'
  `

  code += `
    $&#123;$asString.toString()&#125;
    $&#123;$asStringNullable.toString()&#125;
    $&#123;$asStringSmall.toString()&#125;
    $&#123;$asNumber.toString()&#125;
    $&#123;$asNumberNullable.toString()&#125;
    $&#123;$asIntegerNullable.toString()&#125;
    $&#123;$asNull.toString()&#125;
    $&#123;$asBoolean.toString()&#125;
    $&#123;$asBooleanNullable.toString()&#125;
  `</pre>
<p>其次，就会根据 scheme 定义的具体内容生成 stringify 函数的具体代码。而生成的方式也比较简单：通过遍历 scheme。</p>
<p>遍历 scheme 时，根据定义的类型，在对应代码处插入相应的工具函数用于键值转换。例如上面例子中<code>name</code>这个属性：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">var accessor = key.indexOf('[') === 0 ? sanitizeKey(key) : `['$&#123;sanitizeKey(key)&#125;']`
switch (type) &#123;
    case 'null':
        code += `
            json += $asNull()
        `
        break
    case 'string':
        code += nullable ? `json += obj$&#123;accessor&#125; === null ? null : $asString(obj$&#123;accessor&#125;)` : `json += $asString(obj$&#123;accessor&#125;)`
        break
    case 'integer':
        code += nullable ? `json += obj$&#123;accessor&#125; === null ? null : $asInteger(obj$&#123;accessor&#125;)` : `json += $asInteger(obj$&#123;accessor&#125;)`
        break
    ……</pre>
<p>上面代码中的<code>code</code>变量保存的就是最后生成的函数体的代码串。由于在 scheme 定义中，<code>name</code>为<code>string</code>类型，且不为空，所以会在<code>code</code>中添加如下一段代码字符串：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">"json += $asString(obj['name'])"</pre>
<blockquote><p>由于还需要处理数组、及联对象等复杂情况，实际的代码省略了很多。</p></blockquote>
<p>然后，生成的完整的<code>code</code>字符串大致如下：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">function $asString(str) &#123;
    // ……
&#125;
function $asStringNullable(str) &#123;
    // ……
&#125;
function $asStringSmall(str) &#123;
    // ……
&#125;
function $asNumber(i) &#123;
    // ……
&#125;
function $asNumberNullable(i) &#123;
    // ……
&#125;
/* 以上是一系列通用的键值转换方法 */

/* $main 就是 stringify 的主体函数 */
function $main(input) &#123;
    var obj = typeof input.toJSON === 'function'
        ? input.toJSON()
        : input

    var json = '&#123;'
    var addComma = false
    if (obj['name'] !== undefined) &#123;
        if (addComma) &#123;
            json += ','
        &#125;
        addComma = true
        json += '"name":'
        json += $asString(obj['name'])
    &#125;

    // …… 其他属性(status、working)的拼接

    json += '&#125;'
    return json
&#125;

return $main</pre>
<p>最后，将<code>code</code>字符串传入 Function 构造函数来创建相应的 stringify 函数。</p>
<pre class="brush: javascript; gutter: true; first-line: 1">// dependencies 主要用于处理包含 anyOf 与 if 语法的情况
dependenciesName.push(code)
return (Function.apply(null, dependenciesName).apply(null, dependencies))</pre>
<h3 id="articleHeader4">3.2. slow-json-stringify</h3>
<p><a href="http://static.codeceo.com/images/2019/06/44.png"><img class="aligncenter size-full wp-image-57065" title="44" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/44.png" alt width="800" height="45" referrerpolicy="no-referrer"></a></p>
<p><a href="https://github.com/lucagez/slow-json-stringify" rel="nofollow noreferrer" target="_blank">slow-json-stringify</a> 虽然名字叫 “slow”，但其实是一个 “fast” 的 stringify 库（命名很调皮）。</p>
<blockquote><p>The slowest stringifier in the known universe. Just kidding, it’s the fastest (:</p></blockquote>
<p>它的实现比前面提到的 fast-json-stringify 更轻量级，思路也很巧妙。同时它<a href="https://github.com/lucagez/slow-json-stringify/blob/master/benchmark.md" rel="nofollow noreferrer" target="_blank">在很多场景下效率会比 fast-json-stringify 更快</a>。</p>
<p><img class="aligncenter size-full wp-image-57066" title="55" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/55.png" alt width="800" height="325" referrerpolicy="no-referrer"></p>
<p><img class="aligncenter size-full wp-image-57067" title="66" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2019/06/66.png" alt width="800" height="290" referrerpolicy="no-referrer"></p>
<h4>3.2.1. scheme 的定义方式</h4>
<p>slow-json-stringify 的 scheme 定义更自然与简单，主要就是将键值替换为类型描述。还是上面这个对象的例子，scheme 会变为</p>
<pre class="brush: javascript; gutter: true; first-line: 1">&#123;
    name: 'string',
    status: 'number',
    working: 'boolean'
&#125;</pre>
<p>确实非常直观。</p>
<h4>3.2.2. stringify 方法的生成</h4>
<p>不知道你注意到没有</p>
<pre class="brush: javascript; gutter: true; first-line: 1">// scheme
&#123;
    name: 'string',
    status: 'number',
    working: 'boolean'
&#125;

// 目标对象
&#123;
    name: 'alienzhou',
    status: 6,
    working: true
&#125;</pre>
<p>scheme 和原对象的结构是不是很像？</p>
<p>这种 scheme 的巧妙之处在于，这样定义之后，我们可以先把 scheme <code>JSON.stringify</code>一下，然后“扣去”所有类型值，最后等着我们的就是把实际的值直接填充到 scheme 对应的类型声明处。</p>
<p>具体如何操作呢？</p>
<p>首先，可以直接对 scheme 调用<code>JSON.stringify()</code>来生成基础模版，同时借用<code>JSON.stringify()</code>的第二个参数来作为遍历方法收集属性的访问路径：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">let map = &#123;&#125;;
const str = JSON.stringify(schema, (prop, value) => &#123;
    const isArray = Array.isArray(value);
    if (typeof value !== 'object' || isArray) &#123;
        if (isArray) &#123;
            const current = value[0];
            arrais.set(prop, current);
        &#125;

        _validator(value);

        map[prop] = _deepPath(schema, prop);
        props += `"$&#123;prop&#125;"|`;
    &#125;
    return value;
&#125;);</pre>
<p>此时，<code>map</code> 里收集所有属性的访问路径。同时生成的<code>props</code>可以拼接为匹配相应类型字符还的正则表达式，例如我们这个例子里的正则表达式为<code>/name|status|working"(string|number|boolean|undef)"|\\[(.*?)\\]/</code>。</p>
<p>然后，根据正则表达式来顺序匹配这些属性，替换掉属性类型的字符串，换成统一的占位字符串<code>"__par__"</code>，并基于<code>"__par__"</code>拆分字符串：</p>
<pre class="brush: javascript; gutter: true; first-line: 1">const queue = [];
const chunks = str
    .replace(regex, (type) => &#123;
      switch (type) &#123;
        case '"string"':
        case '"undefined"':
          return '"__par__"';
        case '"number"':
        case '"boolean"':
        case '["array-simple"]':
        case '[null]':
          return '__par__';
        default:
          const prop = type.match(/(?<=\").+?(?=\")/)[0];
          queue.push(prop);
          return type;
      &#125;
    &#125;)
    .split('__par__');</pre>
<p>这样你就会得到<code>chunks</code>和<code>props</code>两个数组。<code>chunks</code>里包含了被分割的 JSON 字符串。以例子来说，两个数组分别如下</p>
<pre class="brush: javascript; gutter: true; first-line: 1">// chunks
[
    '&#123;"name":"',
    '","status":"',
    '","working":"',
    '"&#125;'
]

// props
[
    'name',
    'status',
    'working'
]</pre>
<p>最后，由于 map 中保存了属性名与访问路径的映射，因此可以根据 prop 访问到对象中某个属性的值，循环遍历数组，将其与对应的 chunks 拼接即可。</p>
<p>从代码量和实现方式来看，这个方案会更轻便与巧妙，同时也不需要通过 Function、eval 等方式动态生成或执行函数。</p>
<h2 id="articleHeader5">4. 总结</h2>
<p>虽然不同库的实现有差异，但从整体思路上来说，实现高性能 stringify 的方式都是一样的：</p>
<ol>
<li>开发者定义 Object 的 JSON scheme；</li>
<li>stringify 库根据 scheme 生成对应的模版方法，模版方法里会对属性与值进行字符串拼接（显然，属性访问与字符串拼接的效率要高多了）；</li>
<li>最后开发者调用返回的方法来 stringify Object 即可。</li>
</ol>
<p>归根到底，它本质上是通过静态的结构信息将优化与分析前置了。</p>
<h2 id="articleHeader6">Tips</h2>
<p>最后，还是想提一下</p>
<ul>
<li>所有的 benchmark 只能作为一个参考，具体是否有性能提升、提升多少还是建议你在实际的业务中测试；</li>
<li>fast-json-stringify 中使用到了 Function 构造函数，因此建议不要将用户输入直接用作 scheme，以防一些安全问题。</li>
</ul>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            