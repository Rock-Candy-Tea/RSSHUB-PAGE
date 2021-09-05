
---
title: 'wind-core 4.0.5 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1058'
author: 开源中国
comments: false
date: Sun, 05 Sep 2021 13:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1058'
---

<div>   
<div class="content">
                                                                                            <ul> 
 <li> <p>新增：支持查询关联对象</p> 
  <div> 
   <div> 
    <pre>service.<span style="color:#008080">populateMapping</span>(foo, Foo::setBar);</pre> 
   </div> 
  </div> </li> 
 <li> <p>新增：Cnds，StringCnds条件构造类，任意选择，简化service调用方式</p> 
  <div> 
   <div> 
    <pre><strong>final</strong> <strong>Cnds</strong><<strong>Foo</strong>> cnds = <strong>Cnds</strong>.<span style="color:#008080">of</span>(<strong>Foo</strong>.<span style="color:#008080">class</span>).<span style="color:#008080">gt</span>(Foo::setId, <span style="color:#009999">0L</span>).<span style="color:#008080">limit</span>(<span style="color:#009999">1</span>, <span style="color:#009999">10</span>).<span style="color:#008080">orderBy</span>(Foo::getId);
<span style="color:#888888">// final StringCnds<Foo> cnds = StringCnds.of(Foo.class).gt("id", 0L).limit(1, 10).orderBy("id");</span>
service.<span style="color:#008080">list</span>(cnds);
<span style="color:#888888">// 查询指定字段</span>
<strong>final</strong> <strong>QueryColumn</strong> queryColumn = <strong>QueryColumn</strong>.<span style="color:#008080">of</span>(<strong>Foo</strong>.<span style="color:#008080">class</span>).<span style="color:#008080">col</span>(Foo::getId).<span style="color:#008080">col</span>(Foo::getName);
service.<span style="color:#008080">list</span>(cnds, queryColumn);</pre> 
   </div> 
  </div> </li> 
 <li> <p>新增：service支持表互操作</p> 
  <div> 
   <div> 
    <pre>fooService.<span style="color:#008080">create</span>(foo);
<span style="color:#888888">// 可操作bar表</span>
fooService.<span style="color:#008080">create</span>(bar);</pre> 
   </div> 
  </div> </li> 
 <li> <p>新增：打印sql和参数信息</p> 
  <div> 
   <div> 
    <pre><strong>logging.level.io.github.ramerf.wind.core</strong>=<span style="color:#dd2200">debug</span></pre> 
   </div> 
  </div> </li> 
 <li> <p>新增：Domain 域对象。继承于Domain的对象自带写入方法（create，update，delete）</p> </li> 
 <li> <p>更新：去掉实体注解<code>TableInfo</code>依赖，没有<code>TableInfo</code>注解的实体唯一的区别仅仅是不支持自动建表</p> </li> 
 <li> <p>修复：支持LocalDateTime，LocalDate，LocalTime</p> </li> 
 <li> <p>修复：当列指定备注时自动建表失败</p> </li> 
</ul>
                                        </div>
                                      
</div>
            