
---
title: 'FASTJSON 2.0 和 2.0.1 发布，FASTJSON 项目的重要升级'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=317'
author: 开源中国
comments: false
date: Mon, 18 Apr 2022 15:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=317'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">FASTJSON 2.0 是 FASTJSON 项目的重要升级，目标是为下一个十年提供一个高性能的 JSON 库，同一套 API 支持 JSON/JSONB 两种协议，JSONPath 是一等公民，支持全量解析和部分解析，支持 Java 服务端、客户端 Android、大数据场景。</p> 
<h1 style="color:#24292f; text-align:start">1. 介绍</h1> 
<ul> 
</ul> 
<ul> 
 <li>FASJTONS2 代码<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.1" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.1</a></li> 
 <li>JSONB 格式文档<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fwiki%2Fjsonb_format_cn" target="_blank">https://github.com/alibaba/fastjson2/wiki/jsonb_format_cn</a></li> 
 <li>FASTJSON 2 性能有了很大提升，具体性能数据看这里<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fwiki%2Ffastjson_benchmark" target="_blank">https://github.com/alibaba/fastjson2/wiki/fastjson_benchmark</a></li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:start">2. 使用前准备</h1> 
<h2 style="text-align:start">2.1 Maven依赖</h2> 
<p style="color:#24292f; text-align:start">在fastjson 2.0中，groupId和1.x不一样，是com.alibaba.fastjson2</p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.1</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/</a></p> 
<h2 style="text-align:start">2.2</h2> 
<p style="color:#24292f; text-align:start">如果原来使用fastjson 1.2.x版本，可以使用兼容包，兼容包不能保证100%兼容，请仔细测试验证，发现问题请及时反馈。</p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.1</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<h2 style="text-align:start">2.2 常用类和方法</h2> 
<p style="color:#24292f; text-align:start">在fastjson 2.0中，package和1.x不一样，是com.alibaba.fastjson2。如果你之前用的是fastjson1，大多数情况直接更包名就即可。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> <span>com</span>.<span>alibaba</span>.<span>fastjson2</span>;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSON</span> &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 将字符串解析成JSONObject</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONObject</span> <span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将字符串解析成JSONArray</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONArray</span> <span style="color:var(--color-prettylights-syntax-entity)">parseArray</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将字符串解析成Java对象</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span> <span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>utf8Bytes</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Class</span><<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span>> <span>objectClass</span>);

    <span style="color:var(--color-prettylights-syntax-comment)">// 将Java对象输出成字符串</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span style="color:var(--color-prettylights-syntax-entity)">toJSONString</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>object</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将Java对象输出成UT8编码的byte[]</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span style="color:var(--color-prettylights-syntax-entity)">toJSONBytes</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>object</span>);
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONB</span> &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 将jsonb格式的byte[]解析成Java对象</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span> <span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Class</span><<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span>> <span>objectClass</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将Java对象输出成jsonb格式的byte[]</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span style="color:var(--color-prettylights-syntax-entity)">toBytes</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>object</span>);
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONObject</span> &#123;
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span style="color:var(--color-prettylights-syntax-entity)">get</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-entity)">getIntValue</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Integer</span> <span style="color:var(--color-prettylights-syntax-entity)">getInteger</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">long</span> <span style="color:var(--color-prettylights-syntax-entity)">getLongValue</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Long</span> <span style="color:var(--color-prettylights-syntax-entity)">getLong</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span> <span style="color:var(--color-prettylights-syntax-entity)">getObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>key</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Class</span><<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span>> <span>objectClass</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将JSONObject对象转换为Java对象</span>
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span> <span style="color:var(--color-prettylights-syntax-entity)">toJavaObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Class</span><<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span>> <span>objectClass</span>);
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONArray</span> &#123;
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span style="color:var(--color-prettylights-syntax-entity)">get</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-entity)">getIntValue</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Integer</span> <span style="color:var(--color-prettylights-syntax-entity)">getInteger</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">long</span> <span style="color:var(--color-prettylights-syntax-entity)">getLongValue</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Long</span> <span style="color:var(--color-prettylights-syntax-entity)">getLong</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>);
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span> <span style="color:var(--color-prettylights-syntax-entity)">getObject</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>index</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Class</span><<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">T</span>> <span>objectClass</span>);
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONPath</span> &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 构造JSONPath</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONPath</span> <span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>path</span>);

    <span style="color:var(--color-prettylights-syntax-comment)">// 根据path直接解析输入，会部分解析优化，不会全部解析</span>
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span style="color:var(--color-prettylights-syntax-entity)">extract</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span>jsonReader</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 根据path对对象求值</span>
    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span style="color:var(--color-prettylights-syntax-entity)">eval</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>rootObject</span>);
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> &#123;
    <span style="color:var(--color-prettylights-syntax-comment)">// 构造基于String输入的JSONReader</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 构造基于ut8编码byte数组输入的JSONReader</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>utf8Bytes</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 构造基于char[]输入的JSONReader</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">char</span>[] <span>chars</span>);
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 构造基于json格式byte数组输入的JSONReader</span>
    <span style="color:var(--color-prettylights-syntax-keyword)">static</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span style="color:var(--color-prettylights-syntax-entity)">ofJSONB</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span>)
&#125;</pre> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:start">3. 读取JSON对象</h1> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span> = <span style="color:var(--color-prettylights-syntax-string)">"&#123;\"id\":123&#125;"</span>;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONObject</span> <span>jsonObject</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span>str</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>id</span> = <span>jsonObject</span>.<span style="color:var(--color-prettylights-syntax-entity)">getIntValue</span>(<span style="color:var(--color-prettylights-syntax-string)">"id"</span>);</pre> 
</div> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span> = <span style="color:var(--color-prettylights-syntax-string)">"[\"id\", 123]"</span>;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONArray</span> <span>jsonArray</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseArray</span>(<span>str</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>name</span> = <span>jsonArray</span>.<span style="color:var(--color-prettylights-syntax-entity)">getString</span>(<span style="color:var(--color-prettylights-syntax-constant)">0</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>id</span> = <span>jsonArray</span>.<span style="color:var(--color-prettylights-syntax-entity)">getIntValue</span>(<span style="color:var(--color-prettylights-syntax-constant)">1</span>);</pre> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:start">4. 将JavaBean对象生成JSON</h1> 
<h2 style="text-align:start">4.1 将JavaBean对象生成JSON格式的字符串</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">class</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span>id</span>;
<span style="color:var(--color-prettylights-syntax-keyword)">public</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>name</span>;
&#125;

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = <span style="color:var(--color-prettylights-syntax-keyword)">new</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span>();
<span>product</span>.<span>id</span> = <span style="color:var(--color-prettylights-syntax-constant)">1001</span>;
<span>product</span>.<span>name</span> = <span style="color:var(--color-prettylights-syntax-string)">"DataWorks"</span>;

<span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">toJSONString</span>(<span>product</span>);

<span style="color:var(--color-prettylights-syntax-comment)">// 生成如下的结果</span>
&#123;
<span style="color:var(--color-prettylights-syntax-string)">"id"</span>: <span style="color:var(--color-prettylights-syntax-constant)">1001</span>,
<span style="color:var(--color-prettylights-syntax-string)">"name"</span>: <span style="color:var(--color-prettylights-syntax-string)">"DataWorks"</span>
&#125;

<span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">toJSONString</span>(<span>product</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONWriter</span>.<span>Feature</span>.<span>BeanToArray</span>);
<span style="color:var(--color-prettylights-syntax-comment)">// 生成如下的结果</span>
[<span style="color:var(--color-prettylights-syntax-constant)">123</span>, <span style="color:var(--color-prettylights-syntax-string)">"DataWorks"</span>]</pre> 
</div> 
<h2 style="text-align:start">4.2 将JavaBean对象生成UTF8编码的byte[]</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = ...;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>utf8JSONBytes</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">toJSONBytes</span>(<span>product</span>);</pre> 
</div> 
<h2 style="text-align:start">4.3 将JavaBean对象生成JSONB格式的byte[]</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = ...;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONB</span>.<span style="color:var(--color-prettylights-syntax-entity)">toBytes</span>(<span>product</span>);

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONB</span>.<span style="color:var(--color-prettylights-syntax-entity)">toBytes</span>(<span>product</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONWriter</span>.<span>Feature</span>.<span>BeanToArray</span>);</pre> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:start">5. 读取JavaBean</h1> 
<h2 style="text-align:start">5.1 将字符串读取成JavaBean</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span> = <span style="color:var(--color-prettylights-syntax-string)">"&#123;\"id\":123&#125;"</span>;
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span>str</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span>.<span>class</span>);</pre> 
</div> 
<h2 style="text-align:start">5.2 将UTF8编码的byte[]读取成JavaBean</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>utf8Bytes</span> = <span style="color:var(--color-prettylights-syntax-string)">"&#123;\"id\":123&#125;"</span>.<span style="color:var(--color-prettylights-syntax-entity)">getBytes</span>(<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">StandardCharsets</span>.<span style="color:var(--color-prettylights-syntax-constant)">UTF_8</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSON</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span>utf8Bytes</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span>.<span>class</span>);</pre> 
</div> 
<h2 style="text-align:start">5.3 将JSONB数据读取成JavaBean</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span> = ...
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONB</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span>jsonbBytes</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span>.<span>class</span>);

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span> <span>product</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONB</span>.<span style="color:var(--color-prettylights-syntax-entity)">parseObject</span>(<span>jsonbBytes</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Product</span>.<span>class</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span>.<span>Feature</span>.<span>SupportBeanArrayMapping</span>);</pre> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:start">6. 使用JSONPath</h1> 
<h2 style="text-align:start">6.1 使用JSONPath部分读取数据</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">String</span> <span>str</span> = ...;

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONPath</span> <span>path</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONPath</span>.<span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-string)">"$.id"</span>); <span style="color:var(--color-prettylights-syntax-comment)">// 缓存起来重复使用能提升性能</span>

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span>parser</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONReader</span>.<span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span>str</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>result</span> = <span>path</span>.<span style="color:var(--color-prettylights-syntax-entity)">extract</span>(<span>parser</span>);</pre> 
</div> 
<h2 style="text-align:start">6.2 使用JSONPath读取部分utf8Bytes的数据</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>utf8Bytes</span> = ...;

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONPath</span> <span>path</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONPath</span>.<span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-string)">"$.id"</span>); <span style="color:var(--color-prettylights-syntax-comment)">// 缓存起来重复使用能提升性能</span>

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span>parser</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONReader</span>.<span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span>utf8Bytes</span>);
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>result</span> = <span>path</span>.<span style="color:var(--color-prettylights-syntax-entity)">extract</span>(<span>parser</span>);</pre> 
</div> 
<h2 style="text-align:start">6.3 使用JSONPath读取部分jsonbBytes的数据</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>[] <span>jsonbBytes</span> = ...;

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONPath</span> <span>path</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONPath</span>.<span style="color:var(--color-prettylights-syntax-entity)">of</span>(<span style="color:var(--color-prettylights-syntax-string)">"$.id"</span>); <span style="color:var(--color-prettylights-syntax-comment)">// 缓存起来重复使用能提升性能</span>

<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">JSONReader</span> <span>parser</span> = <span style="color:var(--color-prettylights-syntax-constant)">JSONReader</span>.<span style="color:var(--color-prettylights-syntax-entity)">ofJSONB</span>(<span>jsonbBytes</span>); <span style="color:var(--color-prettylights-syntax-comment)">// 注意，这是利用ofJSONB方法</span>
<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Object</span> <span>result</span> = <span>path</span>.<span style="color:var(--color-prettylights-syntax-entity)">extract</span>(<span>parser</span>);</pre> 
</div> 
<p> 详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases" target="_blank">https://github.com/alibaba/fastjson2/releases</a></p>
                                        </div>
                                      
</div>
            