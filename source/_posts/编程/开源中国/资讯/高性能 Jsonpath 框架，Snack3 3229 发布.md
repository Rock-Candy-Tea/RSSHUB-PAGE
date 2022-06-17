
---
title: '高性能 Jsonpath 框架，Snack3 3.2.29 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9679'
author: 开源中国
comments: false
date: Thu, 16 Jun 2022 22:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9679'
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
  <span><<span style="color:#e45649">version</span>></span>3.2.29<span></<span style="color:#e45649">version</span>></span>
<span></<span style="color:#e45649">dependency</span>></span>
</code></pre> 
<h3 style="text-align:start">本次累计更新：</h3> 
<ul> 
 <li>增加对 Properties 数组的转换支持</li> 
 <li>增加 @ONodeAttr(ignore,incNull)</li> 
 <li>增加特性：Feature.TransferCompatible （传输兼容处理）</li> 
 <li>增加对 isFinal 字段的注入支持</li> 
 <li>当类型为 interface 时，支持将 string 自动转换为 object</li> 
 <li>优化异常处理</li> 
 <li>增加 新特性 UseSetter（即允许使用 setXxx）</li> 
 <li>枚举支持字符大小写</li> 
 <li>增加字符串 "true" 转为 Boolean</li> 
 <li>增新加特性 Feature.DisThreadLocal</li> 
 <li>增加嵌套泛型反序列化支持</li> 
 <li>增加对 kotlin data class 和 jdk14+ record 的序列化与反序列化支持</li> 
</ul>
                                        </div>
                                      
</div>
            