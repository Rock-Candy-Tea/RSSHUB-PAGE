
---
title: '高性能 Jsonpath 框架，Snack3 3.2.35 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9962'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 15:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9962'
---

<div>   
<div class="content">
                                                                                            <p>Snack3，一个高性能的 JsonPath 框架</p> 
<p>借鉴了 Javascript 所有变量由 var 申明，及 Xml dom 一切都是 Node 的设计。其下一切数据都以ONode表示，ONode也即 One node 之意，代表任何类型，也可以转换为任何类型。</p> 
<ul> 
 <li>强调文档树的操控和构建能力</li> 
 <li>高性能Json path查询（顶级的兼容性和性能）</li> 
 <li>顺带支持序列化、反序列化</li> 
 <li>基于 无参构造函数 + 字段 操作实现（反序列化时不会有触发危险动作的风险）</li> 
</ul> 
<pre><code class="language-xml"><dependency>
  <groupId>org.noear</groupId>
  <artifactId>snack3</artifactId>
  <version>3.2.35</version>
</dependency>
</code></pre> 
<h3>本次累计更新：</h3> 
<ul> 
 <li>修复 值为""时，转为 LocalDateTime 会出错的问题</li> 
 <li>增加 val 可自动转为集合的一部分（如果接收的是集合字段）</li> 
</ul> 
<h3>简单演示：</h3> 
<pre><code class="language-java">ONode o = ONode.loadStr(json); //将json String 转为 ONode
ONode o = ONode.loadObj(user); //将java Object 转为 ONode

//不确定返回数量的，者会返回array类型
//找到所有的187开头的手机号，改为186，最后输出修改后的json
o.select("$..mobile[?(@ =~ /^187/)]").forEach(n->n.val("186")).toJson();
//找到data.list[1]下的的mobile字段，并转为long
o.select("$.data.list[1].mobile").getLong();

//查找所有手机号，并转为List<String> 
List<String> list = o.select("$..mobile").toObject(List.class);
//查询data.list下的所有mobile，并转为List<String>
List<String> list = o.select("$.data.list[*].mobile").toObject(List.class);
//找到187手机号的用户，并输出List<UserModel>
List<UserModel> list = o.select("$.data.list[?(@.mobile =~ /^187/)]")
                        .toObjectList(UserModel.class);
//或
List<UserModel> list = o.select("$.data.list[?(@.mobile =~ /^187/)]")
                        .toObjectList(UserModel.class);
</code></pre> 
<h3>项目地址：</h3> 
<ul> 
 <li><a href="https://gitee.com/noear/snack3">https://gitee.com/noear/snack3</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsnack3" target="_blank">https://github.com/noear/snack3</a></li> 
</ul>
                                        </div>
                                      
</div>
            