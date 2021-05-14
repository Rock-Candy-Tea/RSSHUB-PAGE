
---
title: '【得物技术】json-schema入门教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946c16a872744f2e9be6a647497c0845~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 02:13:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946c16a872744f2e9be6a647497c0845~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>文章简介：
大白话介绍json-schema，基本概念到高阶用法，由浅入深，结合实际应用分析json-schema的实际作用。</p>
</blockquote>
<h1 data-id="heading-0">一、缘起</h1>
<h2 data-id="heading-1">什么是json-schema？</h2>
<p>在回答这个问题之前，我们先了解一下它产生的背景。</p>
<p>随着互联网的发展，前后端交互，由最初的text/html，image/*图片等文件流，到目前的application/x-www-form-urlencoded，multipart/form-data，application/json流，以及未来的application/octet-stream二进制。但毫无疑问，目前最流行的前后端交互的格式是application/json，也是我们开发者开发过程中应用最多的格式。</p>
<p>除此之外，json在前端的应用也越来越重要，无论未来如何发展，它始终有着不可或缺的重要地位，为什么呢？笔者认为最根本的原因是它本质上是一个对象，面向对象编程横行霸道的今天，自然而然，它的霸主地位便无法被撼动，同时它的轻量化，高可读，强扩展，高传输效率，也是一种重要原因，它正在为人与机器之间的交互扮演着一个重要的媒介角色。</p>
<p>正是由于json应用越来越广泛，与它相关的工具因此应用而生，json-schema就是其中之一。</p>
<p>假设我们有这样一种JSON数据格式：</p>
<pre><code class="copyable">&#123;
    "id": "1432423230",
    "name": "Jeck",
    "sex": "male"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>尽管这段json对开发的人来说简单明了，我们很容易就知道它是表示一个Person的字符串，但仍然存在一些问题，例如：</p>
<ol>
<li>id可以是数字吗？</li>
<li>name有多少字符限制吗？</li>
<li>sex是必须的吗？可以是man和woman吗？</li>
</ol>
<p>也许作为项目的创始人会十分清楚这些字段代表的含义，然而随着项目的增大，过了一年以后，他未必能想起来这些字段的含义，作为代码的初始开发者尚且如此，那接管项目的其他维护人更不必说了。</p>
<p>尽管上述json代码我们都知道什么含义（Person），里面的字段每个人的理解可能就会不一样，我们只能简单地根据属性英文的意思理解它的含义，但我们不能假定每个人的英语水平都很高，制定的属性值都能让其他人能一眼就看出什么含义。</p>
<p>所以，在团队日益凸显重要的今天，为团队共同指定一套json的规范就十分必要，让团队对它的理解是一致的，以此达到这样的目的：</p>
<ol>
<li>减少理解成本；</li>
<li>提高开发效率；</li>
<li>降低维护成本。</li>
</ol>
<p>那么回过头来，再回答一下什么是json-schema呢？相信聪明的你已经猜到了。</p>
<p>对，没错，就是json的一套规范，也有人说它是校验json的一套利器，是一个提议的IETF标准……其实都是一个含义。</p>
<p>如果你熟悉<a href="https://www.typescriptlang.org/" target="_blank" rel="nofollow noopener noreferrer">typescript</a>或者<a href="https://flow.org/en/docs/getting-started/" target="_blank" rel="nofollow noopener noreferrer">flow</a>，那么很快就能帮你理出这样的一套关系：</p>
<blockquote>
<p>json-schema之于json，就如同typescript(或flow)之于javascript</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946c16a872744f2e9be6a647497c0845~tplv-k3u1fbpfcp-watermark.image" alt="5d141762af58c89d05cf5ebda72ed5ee.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">二、介绍</h1>
<h2 data-id="heading-3">1）基本类型</h2>
<p>构成JSON的两种基本类型：Object和Array
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d7e19aba2594e65ab0d6503e4d3cbb3~tplv-k3u1fbpfcp-watermark.image" alt="b23acbb16ed954dc0726c2cc2bcd7a3b.png" loading="lazy" referrerpolicy="no-referrer">
其中value的值为：string,number,object,array,boolean, null
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ec95f9c7b04a50af9d409a0de48463~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-14 下午5.22.52.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>tips：没有undefined类型</p>
</blockquote>
<h2 data-id="heading-4">2）基本概念</h2>
<p>既然是一套规范，那么就会有很多的语义，那么我们从最简单的例子开始介绍，如下：</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;
  &#125;,
  "required": [ "id" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae78b5ff4dcc42e9963d3e25714d338d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-05-14 下午5.23.46.png" loading="lazy" referrerpolicy="no-referrer">
<em><strong>通常情况下，我们见得最多的格式和属性是type和properties，用于描述一个对象，用于描述一个数组的是items。</strong></em></p>
<h2 data-id="heading-5">3）定义属性值</h2>
<p>id时描述人的唯一标志，类似我们的身份证号码，这是对这条数据的唯一标识符，对数据库而言，它是必须的，同时我们限定了它的类型为string。</p>
<p>name是描述人的符号，这更接近人类的使用习惯，计算机通常注重标识符ID，而人类通常更注重姓名，因此它通常也是必须的，且限定它的最大长度为50。</p>
<p>description表示该字段的描述，使人更明白这个属性值想要表达的意思。</p>
<p>type限制该字段的类型。</p>
<p>required是验证必填的属性列表，不填表示不验证，属性突然的增加和减少都不会验证。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4）深入了解属性</h2>
<p>同时我们需要对性别进行规范，不然对同一含义的男性，一个人的理解为male，另一个理解为man。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;,
    "sex": &#123;
      "description": "The gender of the person",
      "type": "string",
      "enum": ["male", "female"]
    &#125;,
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>突然有一天，需求变了，产品经理说需要加入另外一个属性age年龄，年龄不能低于0吧，更不能大于1000～</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;,
    "sex": &#123;
      "description": "The gender of the person",
      "type": "string",
      "enum": ["male", "female"]
    &#125;,
    "age": &#123;
        "description": "The age for a person",
        "type": "number",
        "exclusiveMinimum": 0,
        "maximum": 1000
    &#125;
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中exclusiveMinimum是大于的意思，如果想包含0作为有效年龄，我们将指定minimum作为关键字，表示大于等于的意思，对应地，maximum和exclusiveMaximum则分别取值为小于等于和小于。</p>
<p>知道了一个人的姓名和年龄，似乎还缺少了什么，试想一下，你见到帅哥或美女后，很幸运的是你们成功搭讪上了，而且还聊得挺开心的，那么将要离别的最后一件很重要事是啥？</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;,
    "sex": &#123;
      "description": "The gender of the person",
      "type": "string",
      "enum": ["male", "female"]
    &#125;,
    "age": &#123;
        "description": "The age for a person",
        "type": "number",
        "exclusiveMinimum": 0,
        "maximum": 1000
    &#125;,
    "phone": &#123;
        "description": "The contact for a person",
        "type": "string",
        "pattern": "^[13|14|15|16|17|18|19][0-9]&#123;9&#125;$"
    &#125;
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串约束支持正则表达式的描述，使用pattern关键字。</p>
<p>随着90及00后的崛起，他们是一群有着梦想和追求自我的人，因此他们会越来越注重自己的个性和标签，而我们的起初项目居然没有这一内容字段。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;,
    "sex": &#123;
      "description": "The gender of the person",
      "type": "string",
      "enum": ["male", "female"]
    &#125;,
    "age": &#123;
        "description": "The age for a person",
        "type": "number",
        "exclusiveMinimum": 0,
        "maximum": 1000
    &#125;,
    "phone": &#123;
        "description": "The contact for a person",
        "type": "string",
        "pattern": "^[13|14|15|16|17|18|19][0-9]&#123;9&#125;$"
    &#125;,
    "tags": &#123;
        "description": "The labels to describe a person",
        "type": "array",
        "items": [
            &#123; "type": "string" &#125;
        ],
        "minItems": 1,
        "uniqueItems": true
    &#125;,
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入items规定数组的每一项，要求数组中的内容为string类型，同时如果声明了这个字段tags，那么minItems规定它的标签至少有一个以上，且uniqueItems规定每个标签都是唯一的。</p>
<h2 data-id="heading-7">5）嵌套结构</h2>
<p>我们通常遇到的数据都不是扁平的，层级一般都会比较深，这里引入给它添加上一个地址字段。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/person.schema.json",
  "title": "Person",
  "description": "it is a person object",
  "type": "object",
  "properties": &#123;
    "id": &#123;
      "description": "The unique identifier for a person",
      "type": "string"
    &#125;,
    "name": &#123;
      "description": "The identifier for a person",
      "type": "string",
      "maxLength": 50
    &#125;,
    "sex": &#123;
      "description": "The gender of the person",
      "type": "string",
      "enum": ["male", "female"]
    &#125;,
    "age": &#123;
        "description": "The age for a person",
        "type": "number",
        "exclusiveMinimum": 0,
        "maximum": 1000
    &#125;,
    "phone": &#123;
        "description": "The contact for a person",
        "type": "string",
        "pattern": "^[13|14|15|16|17|18|19][0-9]&#123;9&#125;$"
    &#125;,
    "tags": &#123;
        "description": "The labels to describe a person",
        "type": "array",
        "items": [
            &#123; "type": "string" &#125;
        ],
        "minItems": 1,
        "uniqueItems": true
    &#125;,
    "address": &#123;
        "description": "The address for a person",
        "type": "object",
        "properties": &#123;
            "country": &#123;
                "type": "string"
            &#125;,
            "province": &#123;
                "type": "string"
            &#125;,
            "city": &#123;
                "type": "string"
            &#125;,
            "region": &#123;
                "type": "string"
            &#125;,
            "detail": &#123;
                "type": "string"
            &#125;
        &#125;,
        "required": ["country", province", "city", "region"]
    &#125;,
  &#125;,
  "required": [ "id", "name" ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，让我们来看一下我们定义的json应该是怎样的。</p>
<pre><code class="copyable">&#123;
    "id": "A000000000",
    "name": "溥仪",
    "sex": "male",
    "age": 112,
    "phone": "1300000000",
    "tags": ["吃饭","睡觉","发呆","末代皇帝"],
    "address": &#123;
        "country": "天朝",
        "province": "帝都",
        "city": "帝都",
        "region": "东城区",
        "detail": "景山前街4号故宫博物馆",
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多的属性规范请移步官网：<a href="https://json-schema.org/draft/2019-09/json-schema-validation.html" target="_blank" rel="nofollow noopener noreferrer">json-schema.org/draft/2019-…</a></p>
<h1 data-id="heading-8">三、高阶用法</h1>
<h2 data-id="heading-9">1）重用</h2>
<p>大到宇宙飞船，小到家常日用手机，这个世界上很多省事的东西正因为懒才创造出来的，可爱的攻城狮们也是这样一群有智慧的动物。很多程序我们只想写一遍，比如上述的地址定义，有这样一种场景，一个人的地址可以有很多种，比如收件地址和发送地址，它们可能包括学校地址，公司地址，家庭地址，租房地址等等。而它们的结构都是相同的，那么我们就不可能重复定义那么多地址信息了，而json-schema也是支持这一操作的。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": &#123;
      "address": &#123;
        "type": "object",
        "properties": &#123;
            "country": &#123;
                "type": "string"
            &#125;,
            "province": &#123;
                "type": "string"
            &#125;,
            "city": &#123;
                "type": "string"
            &#125;,
            "region": &#123;
                "type": "string"
            &#125;,
            "detail": &#123;
                "type": "string"
            &#125;
        &#125;,
        "required": ["country", province", "city", "region"]
    &#125;,
  &#125;,
  
  "type": "object",
  
  "properties": &#123;
        "receipt_address": &#123;
            "#ref": "#/definitions/address"
        &#125;,
        "send_address": &#123;
            "#ref": "#/definitions/address"
        &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>亦或者结合<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi><mi>d</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">id和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">i</span><span class="mord mathnormal">d</span><span class="mord cjk_fallback">和</span></span></span></span></span>ref进行引用处理。</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": &#123;
      "address": &#123;
        "$id": "#address",
        "type": "object",
        "properties": &#123;
            "country": &#123;
                "type": "string"
            &#125;,
            "province": &#123;
                "type": "string"
            &#125;,
            "city": &#123;
                "type": "string"
            &#125;,
            "region": &#123;
                "type": "string"
            &#125;,
            "detail": &#123;
                "type": "string"
            &#125;
        &#125;,
        "required": ["country", province", "city", "region"]
    &#125;,
  &#125;,
  
  "type": "object",
  
  "properties": &#123;
        "receipt_address": &#123;
            "#ref": "#address"
        &#125;,
        "send_address": &#123;
            "#ref": "#address"
        &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">2）递归</h2>
<p>通过上面我们知道用$ref可以处理共用的问题，那么进一步我们可以是否可以理解为自己可以调用自己，进而形成递归？yes, we can!</p>
<p>最常见的就是html的dom结构，它本身就是用递归来生成dom的，举个栗子:</p>
<pre><code class="copyable">&#123;
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": &#123;
      "element": &#123;
        "$id": "#element",
        "type": "object",
        "properties": &#123;
            "name": &#123;
                "type": "string"
            &#125;,
            "props": &#123;
                "type": "object",
                "properties": &#123;&#125;,
            &#125;,
            "children": &#123;
                "type": "array",
                "items": &#123;"$ref": "#element"&#125;,
            &#125;,
        &#125;
    &#125;,
  &#125;,
  
  "type": "object",
  
  "properties": &#123;
        "element": &#123;
            "#ref": "#element"
        &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>需要注意的是，递归调用的时候，不要出现a和b的相互引用，否则会形成死循环。</p>
</blockquote>
<h1 data-id="heading-11">四、实际应用</h1>
<p>考虑到网络带宽和开发效率，通常实际的应用中我们都会省略很多，上面的描述有些会显得冗余，让我们来看一个实际的应用。以<a href="https://formilyjs.org/#/0yTeT0/jbUzUluaIG" target="_blank" rel="nofollow noopener noreferrer">@formily/antd</a>为例。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c0f386201a04bf08b26c4181a6e1524~tplv-k3u1fbpfcp-watermark.image" alt="2cd4c30804d51eaee527a5188c1a50e2.png" loading="lazy" referrerpolicy="no-referrer">
上述内联布局对应json-schema为：</p>
<pre><code class="copyable">&#123;
  "type": "object",
  "properties": &#123;
    "aaa": &#123;
      "key": "aaa",
      "name": "aaa",
      "type": "string",
      "title": "字段1",
      "x-component": "input"
    &#125;,
    "bbb": &#123;
      "key": "bbb",
      "name": "bbb",
      "type": "number",
      "title": "字段2",
      "x-component": "numberpicker"
    &#125;,
    "ccc": &#123;
      "key": "ccc",
      "name": "ccc",
      "type": "date",
      "title": "字段3",
      "x-component": "datepicker"
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述type规定了属性值的输入值类型应该是什么，对比你会发现用于验证的json-schema数据就只有。</p>
<pre><code class="copyable">&#123;
  "type": "object",
  "properties": &#123;
    "aaa": &#123;
      "type": "string",
    &#125;,
    "bbb": &#123;
      "type": "number",
    &#125;,
    "ccc": &#123;
      "type": "date",
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>tips: 上述的"type":"date"是draft7新增的类型。</p>
</blockquote>
<p>在@formily/antd实际应用中，校验属性与业务属性是混合在一起的，严格意义上说它并不是一个标准的json-schema，它结合自己的实际业务制定了一套属于自己的json-schema，你可以理解为伪json-schema，但它值得我们借鉴和学习。</p>
<p>通常情况下，我们还可以通过使用第三方工具来主动验证我们写的json的合法性，如jsonschema，react的form表单schema校验react-jsonschema-form。</p>
<h1 data-id="heading-12">五、总结</h1>
<p>今天这里只是介绍了json-schema的一些基础用法，只是它的冰山一角，它还有很多强大的功能，如dependencies，additionalItems，consts, allOf, anyOf, oneOf, not, if……then……else等等，更多的玩法可以去<a href="https://json-schema.org/" target="_blank" rel="nofollow noopener noreferrer">json-schema官网</a>。</p>
<p>最后，让我们总结一下json-schema的基础知识，它是一套用于校验json的规范，让读写都同时遵循的一套规则。</p>
<p>由小及大，我们再将json-schema拆解一下，那么什么是schema呢？</p>
<p>维基百科给出的定义是:</p>
<blockquote>
<p>The word schema comes from the Greek word σχῆμα (skhēma), which means shape, or more generally, plan.</p>
</blockquote>
<p>严格意义上，schema是一种架构或模式，在数据库系统中是形式语言描述的一种结构，是对象的集合。</p>
<p>举一反三，就会有xml-schema，yaml-schema……它们指的都是XXX数据的一种规范和模式。</p>
<h1 data-id="heading-13">参考</h1>
<ol>
<li>json-schema官网：<a href="https://json-schema.org/" target="_blank" rel="nofollow noopener noreferrer">json-schema.org/</a></li>
<li>json-schema使用教程文档：<a href="http://xaber.co/2015/10/20/JSON-schema-%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B%E6%96%87%E6%A1%A3/" target="_blank" rel="nofollow noopener noreferrer">xaber.co/2015/10/20/…</a></li>
<li>@formily/antd的SchemaForm：<a href="https://formilyjs.org/#/0yTeT0/jbUzUluaIG" target="_blank" rel="nofollow noopener noreferrer">formilyjs.org/#/0yTeT0/jb…</a></li>
</ol>
<p>文｜Alan</p>
<p>关注得物技术，携手走向技术的云端</p></div>  
</div>
            