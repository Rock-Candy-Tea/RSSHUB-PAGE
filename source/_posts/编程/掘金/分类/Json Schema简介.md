
---
title: 'Json Schema简介'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1651'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 02:58:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=1651'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>[top]</p>
<h3 data-id="heading-0">介绍</h3>
<p><strong><strong>Json Schema定义了一套词汇和规则，这套词汇和规则用来定义Json元数据，且元数据也是通过Json数据形式表达的。Json元数据定义了Json数据需要满足的规范，规范包括成员、结构、类型、约束等</strong></strong></p>
<pre><code class="copyable">eg:
&#123; 
    "city":"chicago",
    "number": 20,
    "user" : &#123; 
        "name":"Alex",
        "age":20 
     &#125; 
 &#125;

在上面的例子中，web api要求提供city，number，user三个成员，其中city是字符串，number是数值，user是一个对象，又包含了name和age两个成员

对应的Json Schema如下:
&#123; 
    "type": "object",
    "properties": &#123;
        "city": &#123; "type": "string" &#125;,
        "number": &#123; "type": "number" &#125;,
        "user": &#123; 
            "type": "object",
            "properties": &#123;
                "name" : &#123;"type": "string"&#125;,
                "age" : &#123;"type": "number"&#125;
            &#125;                       
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">关键字</h3>
<h4 data-id="heading-2">1.<code>type 类型</code></h4>
<h5 data-id="heading-3">1.&#123;"type":"string"&#125;</h5>
<p>1.字符串长度 <code>**关键字： minLength, maxLength**</code> 对字符串的最小长度、最大长度做规范</p>
<pre><code class="copyable">eg:
&#123; "type" : "string", "minLength" : 2, "maxLength" : 3, &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>正则表达式<code>**关键字： pattern**</code></li>
</ol>
<pre><code class="copyable">eg:
&#123; "type" : "string", "pattern" : "^(\\([0-9]&#123;3&#125;\\))?[0-9]&#123;3&#125;-[0-9]&#123;4&#125;$", &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>字符串Format <code>**关键字： format**</code>用于电子邮件、日期、域名等</li>
</ol>
<pre><code class="copyable">&#123; "type" : "string", "format" : "date", &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">2.&#123;"type" : "object"&#125;</h5>
<ul>
<li>Json对象是最常见的Json数据类型，合法的数据可以是</li>
</ul>
<pre><code class="copyable">&#123; 
    "name": "Froid", 
    "age" : 26, 
    "address" : &#123; "city" : "New York", "country" : "USA" &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>成员的Schema<code>**关键字：properties**</code></li>
</ul>
<pre><code class="copyable">&#123; 
    "type": "object",      
    "properties": &#123;      
        "name": &#123;"type" : "string"&#125;, 
        "age" : &#123;"type" : "integer"
     &#125;, 
     "address" : &#123; 
         "type" : "object", 
         "properties" : &#123; 
             "city" : &#123;"type" : "string"&#125;, 
             "country" : &#123;"type" : "string"&#125; 
         &#125; 
       &#125; 
    &#125; 
&#125;

对于上例中的Schema，合法的data是
&#123; 
    "name": "Froid", 
    "age" : 26, 
    "address" : &#123; 
        "city" : "New York", 
        "country" : "USA" 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>批量定义成员Schema <code>**关键字：patternProperties**</code></li>
</ul>
<pre><code class="copyable">eg: &#123;"S_1" : "abc"&#125;
    &#123;"S_1" : "abc", "I_3" : 1&#125;
&#123; 
    "type": "object", 
    "patternProperties": &#123; 
        "^S_": &#123; "type": "string" &#125;, 
        "^I_": &#123; "type": "integer" &#125; 
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>必须出现的成员 <code>**关键字：required**</code></li>
</ul>
<pre><code class="copyable">&#123; 
    "type": "object",      
    "properties": &#123;      
        "name": &#123;"type" : "string"&#125;, 
        "age" : &#123;"type" : "integer"&#125;, 
    &#125;, 
    "required" : ["name"] 
&#125;

上例中"name"成员是必须的，因此合法的数据可以是
&#123;"name" : "mary", "age" : 26&#125;
&#123;"name" ： "mary"&#125;

但缺少"name"则是非法的
&#123;"age" : 26&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>成员依赖关系<code>**关键字：dependencies**</code></li>
</ul>
<pre><code class="copyable">规定某些成员的依赖成员，不能在依赖成员缺席的情况下单独出现，属于数据完整性方面的约束。
&#123; 
    "type": "object", 
    "dependencies": &#123; 
        "credit_card": ["billing_address"] 
    &#125; 
&#125;
dependencies也是一个字典结构，key是Json数据的属性名，value是一个数组，数组内也是Json数据的属性名，表示key必须依赖的其他属性

上面Json Schema合法的数据可以是
&#123;&#125;
&#123;"billing_address" : "abc"&#125;

但如果有"credit_card"属性，则"billing_address" 属性不能缺席。下面的数据是非法的
&#123;"credit_card": "7389301761239089"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>是否允许额外属性<code>**关键字：additionaProperties**</code></li>
</ul>
<pre><code class="copyable">规定object类型是否允许出现不在properties中规定的属性，只能取true/false
&#123; 
    "type": "object",      
    "properties": &#123;      
        "name": &#123;"type" : "string"&#125;, 
        "age" : &#123;"type" : "integer"&#125;, 
    &#125;, 
    "required" : ["name"], 
    "additionalProperties" : false 
&#125;

上例中规定对象不能有"name"和"age"之外的成员。
合法的数据
&#123;"name" : "mary"&#125;
&#123;"name" : "mary", "age" : 26&#125;
非法的数据
&#123;"name" : "mary", "phone" : ""84893948&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li> 属性个数的限制<code>**关键字：minProperties, maxProperties**</code>规定最少、最多有几个属性成员</li>
</ul>
<pre><code class="copyable">&#123; 
    "type": "object", 
    "minProperties": 2, 
    "maxProperties": 3 
&#125;
合法数据
&#123;"name" : "mary", "age" : 26&#125;
&#123;"name" : "mary", "age" : 26, "phone" : "37839233"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">3.&#123;"type" : "number"&#125;</h5>
<p>1.number的合法数值可以是 2或0.1 而 integer只能是整数<br>
2.<code>**关键字：multipleOf**</code></p>
<pre><code class="copyable">要求数值必须是10的整数倍
&#123; "type" : "number", "multipleOf" : 10, &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.<code>**关键字： minimum, maximum, exclusiveMinimum, exclusiveMaximum**</code>可以限制数值的方位，包括最大值、最小值、开区间最大值、开区间最小值</p>
<pre><code class="copyable">要求数值在[0, 100)范围内:
&#123; 
    "type" : "number", 
    "minimum": 0, 
    "exclusiveMaximum": 100 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">4.&#123;"type": "integer"&#125;  要求数据必须是整数</h5>
<h5 data-id="heading-7">5.&#123;"type" : "array"&#125;</h5>
<p>1.Json数组合法数据</p>
<pre><code class="copyable">[1, 2, 3]
[1, "abc", &#123;"name" : "alex"&#125;]
[]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.数组的类型特定参数，可以用来限制<strong>成员类型</strong>、<strong>是否允许额外成员</strong>、<strong>最小元素个数</strong>、<strong>最大元素个数</strong>、<strong>是否允许元素重复</strong><br></p>
<ul>
<li>数组成员类型 <code>**关键字： items**</code></li>
</ul>
<pre><code class="copyable">1.可以要求数组内每个成员都是某种类型，通过关键字items实现
&#123; 
    "type": "array", 
    "items": &#123; 
        "type": 
        "number" 
    &#125; 
&#125;
2.关键字items还可以对应一个数组，这时Json数组内的元素必须与Json Schema内items数组内的每个Schema按位置一一匹配  
    eg: [1, "abc"]
&#123; 
    "type": "array", 
    "items": [ 
        &#123;"type": "number" &#125;, 
        &#123; "type": "string" &#125;
    ] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组是否允许额外成员 <code>**关键字： additionalItems**</code></li>
</ul>
<pre><code class="copyable">当使用了items关键字，并且items关键字对应的是Schema数组，这个限制才起作用。
关键字additionalItems规定Json数组内的元素，除了一一匹配items数组内的Schema外，
是否还允许多余的元组。当additionalItems为true时，允许额外元素
eg:[1, "abc", "x"]
&#123; 
    "type": "array", 
    "items": [ 
        &#123; "type": "number" &#125;, 
        &#123; "type": "string" &#125;
    ], 
    "additionalItems" : true 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组元素个数 <code>**关键字： minItems, maxItems**</code> 可以限制数组内元素的个数</li>
</ul>
<pre><code class="copyable">eg:[1,2,3,4,5,6]
&#123; 
    "type": "array", 
    "items": &#123; "type": "number" &#125;, 
    "minItems" : 5, 
    "maxItems" : 10 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组内元素是否必须唯一 <code>**关键字： uniqueItems**</code><br></li>
</ul>
<pre><code class="copyable">eg:[1,2,3,4,5]
&#123; 
    "type": "array", 
    "items": &#123; "type": "number" &#125;, 
    "uniqueItems" : true 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">6.&#123;"type" : "boolean"&#125;</h5>
<h5 data-id="heading-9">7.&#123;"type" : "null"&#125;</h5>
<h5 data-id="heading-10">8.逻辑组合<code>**关键字：allOf, anyOf, oneOf, not**</code><br></h5>
<ol>
<li>从关键字名字可以看出其含义，满足所有、满足任意、满足一个。前三个关键字的使用形式是一致的，以allOf为例说明其形式</li>
</ol>
<pre><code class="copyable">&#123; 
    "allOf" : [ 
        Schema1, 
        Schema2, ... 
    ] 
&#125;
其中，"allOf"的内容是一个数组，数组内的成员都是内嵌的Json Schema。上例Schema1、Schema2都是内嵌的Json Schema。整个Schema表示当前Json数据，需要同时满足Schema1、Schema2。

需要注意，不论在内嵌的Schema里还是外部的Schema里，都不应该使"additionalProperties"为false。否则可能会生成任何数据都无法满足的矛盾Schema。
可以用来实现类似“继承”的关系，例如我们定义了一个Schema_base，如果想要对其进行进一步修饰，可以这样来实现。

&#123; 
    "allOf" : [ Schema_base ],
    "properties" : &#123; 
        "other_pro1" : &#123;"type" : "string"&#125;, 
        "other_pro2" : &#123;"type" : "string"&#125; 
    &#125;, 
    "required" : ["other_pro1", "other_pro2"] 
&#125;
Json数据既需要满足Schema_base，又要具备属性"other_pro1"、"other_pro2"。
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li> 关键字<code>not</code>  规定 Json不能满足not所对应的Schema</li>
</ol>
<pre><code class="copyable">只要不是string类型的都Json数据都可以
&#123; "not" : &#123;"type" : "string"&#125; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">9.复杂结构</h3>
<ul>
<li><code>**关键字：无**</code></li>
</ul>
<pre><code class="copyable">定义一个类型，并不需要特殊的关键字。通常的习惯是在root节点的definations下面，定义需要多次引用的schema。definations是一个json对象，key是想要定义的“类型”的名称，value是一个json schema
&#123;
    "definitions": &#123;
        "address": &#123;
            "type": "object",
            "properties": &#123;
                "street_address": &#123; "type": "string" &#125;,
                "city":           &#123; "type": "string" &#125;,
                "state":          &#123; "type": "string" &#125;
            &#125;,
            "required": ["street_address", "city", "state"]
        &#125;
    &#125;，
    "type": "object",
    "properties": &#123;
        "billing_address": &#123; "$ref": "#/definitions/address" &#125;,
        "shipping_address": &#123; "$ref": "#/definitions/address" &#125;
    &#125;
&#125;
上例中定义了一个address的schema，并且在两个地方引用了它，`#/definitions/address`表示从根节点开始的路径
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>**关键字：$id**</code></li>
</ul>
<pre><code class="copyable">可以在上面的定义中加入id属性，这样可以通过id属性，这样可以通过id属性的值对该schema进行引用，而不需要完整的路径。

"address": &#123;
    "type": "object",
    "$id" : "address",
    "properties": &#123;
        "street_address": &#123; "type": "string" &#125;,
        "city":           &#123; "type": "string" &#125;,
        "state":          &#123; "type": "string" &#125;
    &#125;,
    "required": ["street_address", "city", "state"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>**关键字：$ref**</code></li>
</ul>
<pre><code class="copyable">关键字`$ref`可以用在任何需要使用json schema的地方。如上例中，billing_address的value应该是一个json schema，通过一个`$ref`替代了。

`$ref`的value，是该schema的定义在json中的路径，以#开头代表根节点。
&#123;
    "properties": &#123;
        "billing_address": &#123; "$ref": "#/definitions/address" &#125;,
        "shipping_address": &#123; "$ref": "#/definitions/address" &#125;
    &#125;
&#125;
如果schema定义了$id属性，也可以通过该属性的值进行引用。

&#123;
    "properties": &#123;
        "billing_address": &#123; "$ref": "#address" &#125;,
        "shipping_address": &#123; "$ref": "#address" &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">10. 通用关键字</h3>
<ul>
<li>enum<code>**关键字：enum**</code></li>
</ul>
<pre><code class="copyable">可以在任何json schema中出现，其value是一个list，表示json数据的取值只能是list中的某个
&#123;
    "type": "string",
    "enum": ["red", "amber", "green"]
&#125;
上例的schema规定数据只能是一个string，且只能是"red"、"amber"、"green"之一。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>metadata<code>**关键字：title，description，default，example**</code></li>
</ul>
<pre><code class="copyable">&#123;
    "title" : "Match anything",
    "description" : "This is a schema that matches anything.",
    "default" : "Default value",
    "examples" : [
        "Anything",
        4035
    ]
&#125;
只作为描述作用，不影响对数据的校验
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            