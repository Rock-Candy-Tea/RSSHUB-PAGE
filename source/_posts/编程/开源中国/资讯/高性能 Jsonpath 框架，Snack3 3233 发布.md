
---
title: '高性能 Jsonpath 框架，Snack3 3.2.33 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3823'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 03:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3823'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292e; text-align:start">Snack3，一个高性能的 JsonPath 框架</p> 
<p style="color:#24292e; text-align:start">借鉴了 Javascript 所有变量由 var 申明，及 Xml dom 一切都是 Node 的设计。其下一切数据都以ONode表示，ONode也即 One node 之意，代表任何类型，也可以转换为任何类型。</p> 
<ul> 
 <li>强调文档树的操控和构建能力</li> 
 <li>高性能Json path查询（顶级的兼容性和性能）</li> 
 <li>顺带支持序列化、反序列化</li> 
 <li>基于 无参构造函数 + 字段 操作实现（反序列化时不会有触发危险动作的风险）</li> 
</ul> 
<pre style="text-align:start"><code class="language-xml"><span><<span style="color:#e45649">dependency</span>></span>
  <span><<span style="color:#e45649">groupId</span>></span>org.noear<span></<span style="color:#e45649">groupId</span>></span>
  <span><<span style="color:#e45649">artifactId</span>></span>snack3<span></<span style="color:#e45649">artifactId</span>></span>
  <span><<span style="color:#e45649">version</span>></span>3.2.33<span></<span style="color:#e45649">version</span>></span>
<span></<span style="color:#e45649">dependency</span>></span>
</code></pre> 
<h3 style="text-align:start">本次累计更新：</h3> 
<ul> 
 <li>增加 jsonpath 内的选项传导</li> 
 <li>增加 LongAdder，DoubleAdder 反序列化支持</li> 
 <li>增加 name 值的格式控制</li> 
 <li>调整 \ 的解析方式</li> 
 <li>修复 name 特定情况下会出现空隔的问题</li> 
</ul> 
<h3 style="text-align:start">简单演示：</h3> 
<pre style="text-align:start"><code class="language-java"><span style="color:#986801">ONode</span> <span style="color:#986801">o</span> <span>=</span> ONode.loadStr(json); <em>//将json String 转为 ONode</em>
<span style="color:#986801">ONode</span> <span style="color:#986801">o</span> <span>=</span> ONode.loadObj(user); <em>//将java Object 转为 ONode</em>

<em>//不确定返回数量的，者会返回array类型</em>
<em>//找到所有的187开头的手机号，改为186，最后输出修改后的json</em>
o.select(<span style="color:#50a14f">"$..mobile[?(@ =~ /^187/)]"</span>).forEach(n->n.val(<span style="color:#50a14f">"186"</span>)).toJson();
<em>//找到data.list[1]下的的mobile字段，并转为long</em>
o.select(<span style="color:#50a14f">"$.data.list[1].mobile"</span>).getLong();

<em>//查找所有手机号，并转为List<String> </em>
List<String> list = o.select(<span style="color:#50a14f">"$..mobile"</span>).toObject(List.class);
<em>//查询data.list下的所有mobile，并转为List<String></em>
List<String> list = o.select(<span style="color:#50a14f">"$.data.list[*].mobile"</span>).toObject(List.class);
<em>//找到187手机号的用户，并输出List<UserModel></em>
List<UserModel> list = o.select(<span style="color:#50a14f">"$.data.list[?(@.mobile =~ /^187/)]"</span>)
                        .toObjectList(UserModel.class);
<em>//或</em>
List<UserModel> list = o.select(<span style="color:#50a14f">"$.data.list[?(@.mobile =~ /^187/)]"</span>)
                        .toObjectList(UserModel.class);</code></pre>
                                        </div>
                                      
</div>
            