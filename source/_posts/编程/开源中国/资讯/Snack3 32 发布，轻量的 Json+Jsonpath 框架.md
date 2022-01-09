
---
title: 'Snack3 3.2 发布，轻量的 Json+Jsonpath 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4501'
author: 开源中国
comments: false
date: Sat, 08 Jan 2022 11:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4501'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; text-align:start">Snack3 是一个轻量的 JSON + Jsonpath 框架。</p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292e; text-align:start">借鉴了 Javascript 所有变量由 var 申明，及 Xml dom 一切都是 Node 的设计。其下一切数据都以ONode表示，ONode也即 One node 之意，代表任何类型，也可以转换为任何类型。</p> 
<ul> 
 <li>强调文档树的操控和构建能力</li> 
 <li>做为中间媒体，方便不同格式互转</li> 
 <li>高性能Json path查询（兼容性和性能很赞）</li> 
 <li>支持序列化、反序列化</li> 
 <li>基于 无参构造函数 + 字段 操作实现（反序列化时不会有触发危险动作的风险）</li> 
</ul> 
<pre style="text-align:start"><code class="language-xml"><span><<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">dependency</span>></span>
  <span><<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">groupId</span>></span>org.noear<span></<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">groupId</span>></span>
  <span><<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">artifactId</span>></span>snack3<span></<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">artifactId</span>></span>
  <span><<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">version</span>></span>3.2.7<span></<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">version</span>></span>
<span></<span data-darkreader-inline-color style="--darkreader-inline-color:#e65f53; color:#e45649">dependency</span>></span>
</code></pre> 
<h3 style="text-align:start">本次累计更新：</h3> 
<ul> 
 <li>增加自定义编码与解码支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">DemoTest</span> </span>&#123;
    <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">void</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">test</span><span>(UserDto user)</span> </span>&#123;
        Options options = Options.def();
        options.addEncoder(Date<span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span>, (<span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">data</span>, <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">node</span>)-></span>&#123;
            node.val().setNumber(data.getTimes());
        &#125;);
        
        ONode oNode = ONode.loadObj(user, options);
    &#125;
&#125;
</code></pre> 
<ul> 
 <li>增加 @ONodeAttr 注解，取代旧的 @NodeName</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">UserModel</span> </span>&#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> id;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@ONodeAttr</span>(serialize = <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">false</span>)
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> String name;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@ONodeAttr</span>(deserialize = <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">false</span>)
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> String note;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@ONodeAttr</span>(format = <span data-darkreader-inline-color style="--darkreader-inline-color:#6db76c; color:#50a14f">"yyyyMMdd"</span>)
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> Date date;
&#125;
</code></pre> 
<ul> 
 <li>增加更复杂的泛型传导</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@lombok</span>.Data
<span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">Data</span><<span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">X</span>> </span>&#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> List<X> content;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> X obj;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> pageNum;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> pageSize;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> totalElements;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> pages;
&#125;

<span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@lombok</span>.Data
<span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">House</span> </span>&#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String sn;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String dver_type;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String data_status;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String created_by;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String updated_by;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> String updated_date;
&#125;

<span data-darkreader-inline-color style="--darkreader-inline-color:#4a9bf3; color:#4078f2">@lombok</span>.Data
<span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">Result</span><<span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">T</span>> </span>&#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> code;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">private</span> Data<T> data;
&#125;


Result<House> result = ONode.deserialize(json, <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">new</span> Result<House>() &#123;&#125;.getClass());
</code></pre> 
<ul> 
 <li>增加对成员类的反序列化支持</li> 
</ul> 
<pre style="text-align:start"><code class="language-java"><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">Server</span> </span>&#123;
    <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">static</span> <span><span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#fec345; color:#c18401">One</span></span>&#123;
        <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">int</span> id;
        <span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">public</span> String name;
    &#125;
&#125;

Server.One one = ONode.deserialize(json, Server.One<span>.<span data-darkreader-inline-color style="--darkreader-inline-color:#db61d9; color:#a626a4">class</span>)</span>;
</code></pre> 
<ul> 
 <li>增加接口 ONode::getRawString()</li> 
 <li>增加接口 ONode::getRawNumber()</li> 
 <li>增加接口 ONode::getRawBoolean()</li> 
 <li>增加接口 ONode::getRawDate()</li> 
 <li>增加接口 Options::getFeatures()</li> 
 <li>增加接口 ONode::options(ops->...);</li> 
 <li>调整接口 ONode::get(key) ，不再自动为文档树添加节点；如有需要改用 ONode::getOrNew(key)</li> 
 <li>等等</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            