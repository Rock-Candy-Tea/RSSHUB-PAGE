
---
title: 'jSqlBox 5.0.15 发布，300 行代码干掉 GraphQL'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2951'
author: 开源中国
comments: false
date: Sat, 10 Sep 2022 22:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2951'
---

<div>   
<div class="content">
                                                                                            <h4>前言</h4> 
<p>看GraphQL不爽很久了，一直认为这是个<span style="background-color:#ffffff; color:#4d5156">鸡肋技术，过分复杂，功能有限，定位不清，存在安全问题。个人觉得GraphQL主要价值是两点，一是提供了一种模式，把业务逻辑前推到前端，让前端动态查询，第二个是结构化查询，输出结果和输入结构一样，所见即所得。前者个人认为只有用MyServerless的开发模式才能理想地同时解决安全和开发效率问题，后者则是本次更新内容，即在jSqlBox这个后端ORM工具添加类似GraphQL的结构化查询功能，但要做到不像GraphQL那么复杂，要让学习和使用成本最低。<br> <br> 顺便介绍一下</span>jSqlBox本身，这是一个全功能开源Java数据库持久层工具，只要是与数据库操作相关的功能，jSqlBox都已具备，如DDL操作、分页、分库分表、声明式事务、关联映射查询、ActiveRecord等，所有这些功能都包含在一个1M大小的jar包中，不依赖任何第三方库。jSqlBox主要特点是Java和SQL混写，把SQL写出花来了，包括这次的主从表结构化查询也是。<br> 使用jSqlBox只要在项目中添加以下依赖：</p> 
<pre><code class="language-xml"><dependency>
   <groupId>com.github.drinkjava2</groupId>
   <artifactId>jsqlbox</artifactId>  
   <version>5.0.15.jre8</version> <!-- 或最新版 -->
</dependency> </code></pre> 
<p><span>本次更新内容</span></p> 
<p>本次5.0.15.jre8更新增加了类似GraphQL的结构化查询功能，这个功能在编程序时发现非常简单，在原有jSqlBox基础上，只需要300行代码即可实现。<br> jSqlBox的主从表结构化查询是依然采用jSqlBox的Java/SQL混写方式，但是这次将查询写成方法嵌套的结构，即可实现类似GraphQL的结构化查询，输入和输出的树状结构一致，所见即所得。<br> jSqlBox主从表结构化查询主要优点有：<br> 1.只需要编写针对单表查询的SQL，会自动按主从关联列名生成类似“id in (?, ?...?)”的SQL片段，并将最终查询结果组装成主从表树状结构。<br> 2.采用纯Java和原生SQL混写，功能强，学习成本低，可以同时用Java执行复杂的参数、安全检查、写数据库等业务逻辑。<br> 3.没有直接输出为JSON，而是输出Map/List对象或Java实体对象，查询结果可以被继续修改后再发送JSON给前端。<br> 4.可以直接利用Java的IDE格式化和语法检查功能，不需要第三方工具。格式化功能可以直观显示出树结构的嵌套层级。  <br> 5.jSqlBox的内嵌式SQL参数、分页、分库分表、拦截器、事务等依然可以直接使用。<br> 6.不提供安全、权限功能，无学习成本。安全、权限这些功能不属于ORM工具的职能，应该由后端的SpringSecurity/Shiro工具包或独立的Serverless/JsonAPI服务器来提供。<br> 7.如果结合我的MyServerless开源项目，可以实现前端直接在html里书写Java、定制主从表多级查询并返回json, 将业务逻辑前移到前端。<br> 8.性能好，用"in"的方式进行数据库表的关联查询，不存在1+N问题。<br> 9.源码简洁(实现这个功能仅用了300行源码，见GraphQuery.java)，可扩充性好。<br> <br> 使用示例：</p> 
<pre><code>        GraphQuery q1 = <span>//</span>
                <span>$</span>(<span>"addresstb as addresses"</span>, <span>"where id>"</span>, que(<span>"a1"</span>), <span>" and id<"</span>, que(<span>"a5"</span>), pagin(<span>1</span>, <span>10</span>), <span>//</span>
                        <span>$</span><span>1</span>(<span>"usertb"</span>, key(<span>"user"</span>), ms(<span>"userId"</span>, <span>"id"</span>), <span>$</span>(<span>"userroletb as userRoleList"</span>, ms(<span>"id"</span>, <span>"userId"</span>), <span>//</span>
                                <span>$</span>(<span>"roletb as roleList"</span>, ms(<span>"rid"</span>, <span>"id"</span>), <span>// ms方法也可以写成DB.masterSlave()</span>
                                        <span>$</span>(<span>"roleprivilegetb as rolePrivilegeList"</span>, ms(<span>"id"</span>, <span>"rid"</span>), <span>//</span>
                                                <span>$</span><span>1</span>(<span>"privilegetb as privilege"</span>, ms(<span>"pid"</span>, <span>"id"</span>)) <span>//                                                 </span>
                                        )<span>//</span>
                                )<span>//</span>
                        ), <span>//</span>
                                <span>$</span><span>1</span>(<span>"select * from emailtb as email"</span>, ms(<span>"id"</span>, <span>"userId"</span>)), <span>//</span>
                                <span>$</span>(<span>"addresstb as addressList"</span>, ms(<span>"id"</span>, <span>"userId"</span>), <span>"and addressName like ?"</span>, par(<span>"addr%"</span>))<span>//</span>
                        )<span>//</span>
                );
        GraphQuery q2 = <span>//</span>
                <span>$</span>(<span>"usertb as u"</span>, <span>"where id>"</span>, que(<span>"u2"</span>), pagin(<span>1</span>, <span>10</span>), entity(User.class), <span>//映射成User实体Bean</span>
                        <span>$</span><span>1</span>(<span>"emailtb as emailMap"</span>, ms(<span>"id"</span>, <span>"userId"</span>)), <span>//$1表示是单个元素，而不是一个List</span>
                        <span>$</span>(<span>"addresstb as addressList"</span>, ms(<span>"id"</span>, <span>"userId"</span>))<span>//</span>
                );
        Object result = DB.graphQuery(q1, q2); <span>//result是查询结果</span>
        String json = JsonUtil.toJSONFormatted(result); <span>//输出为JSON文本</span>
</code></pre> 
<p>以上示例详见单元测试下的GraphQueryTest.java，输出结果如下：</p> 
<pre><code>&#123;
   <span>"addresses"</span>:[
      &#123;
         <span>"addressName"</span>:<span>"address2"</span>,
         <span>"id"</span>:<span>"a2"</span>,
         <span>"userId"</span>:<span>"u2"</span>,
         <span>"user"</span>:&#123;
            <span>"id"</span>:<span>"u2"</span>,
            <span>"userName"</span>:<span>"user2"</span>,
            <span>"userRoleList"</span>:[
               &#123;
                  <span>"id"</span>:<span>"3i6yaxy2fusjkgisyfhypkti9"</span>,
                  <span>"rid"</span>:<span>"r1"</span>,
                  <span>"userId"</span>:<span>"u2"</span>,
                  <span>"roleList"</span>:[
                     &#123;
                        <span>"id"</span>:<span>"r1"</span>,
                        <span>"roleName"</span>:<span>"role1"</span>,
                        <span>"rolePrivilegeList"</span>:[
                           &#123;
                              <span>"id"</span>:<span>"b484ze4k44xemtkstehnprhxq"</span>,
                              <span>"pid"</span>:<span>"p1"</span>,
                              <span>"rid"</span>:<span>"r1"</span>,
                              <span>"privilege"</span>:&#123;
                                 <span>"id"</span>:<span>"p1"</span>,
                                 <span>"privilegeName"</span>:<span>"privilege1"</span>
                              &#125;
                           &#125;
                        ]
                     &#125;
                  ]
               &#125;,
               &#123;
                  <span>"id"</span>:<span>"e41dln9m4jehmc7somvu5s2pf"</span>,
                  <span>"rid"</span>:<span>"r2"</span>,
                  <span>"userId"</span>:<span>"u2"</span>,
                  <span>"roleList"</span>:[
                     &#123;
                        <span>"id"</span>:<span>"r2"</span>,
                        <span>"roleName"</span>:<span>"role2"</span>,
                        <span>"rolePrivilegeList"</span>:[
                           &#123;
                              <span>"id"</span>:<span>"dhrh5kgsod6w76e6xtl36u8b9"</span>,
                              <span>"pid"</span>:<span>"p1"</span>,
                              <span>"rid"</span>:<span>"r2"</span>,
                              <span>"privilege"</span>:&#123;
                                 <span>"id"</span>:<span>"p1"</span>,
                                 <span>"privilegeName"</span>:<span>"privilege1"</span>
                              &#125;
                           &#125;,
                           &#123;
                              <span>"id"</span>:<span>"b9h2aenn6jjacns9ng5vwhaiq"</span>,
                              <span>"pid"</span>:<span>"p3"</span>,
                              <span>"rid"</span>:<span>"r2"</span>,
                              <span>"privilege"</span>:&#123;
                                 <span>"id"</span>:<span>"p3"</span>,
                                 <span>"privilegeName"</span>:<span>"privilege3"</span>
                              &#125;
                           &#125;
                        ]
                     &#125;
                  ]
               &#125;,
               &#123;
                  <span>"id"</span>:<span>"994a5o65pfa7wx8vq99gi1lkg"</span>,
                  <span>"rid"</span>:<span>"r3"</span>,
                  <span>"userId"</span>:<span>"u2"</span>,
                  <span>"roleList"</span>:[
                     &#123;
                        <span>"id"</span>:<span>"r3"</span>,
                        <span>"roleName"</span>:<span>"role3"</span>,
                        <span>"rolePrivilegeList"</span>:[
                           &#123;
                              <span>"id"</span>:<span>"7qf9us50mw95hijwkfvuzus4q"</span>,
                              <span>"pid"</span>:<span>"p3"</span>,
                              <span>"rid"</span>:<span>"r3"</span>,
                              <span>"privilege"</span>:&#123;
                                 <span>"id"</span>:<span>"p3"</span>,
                                 <span>"privilegeName"</span>:<span>"privilege3"</span>
                              &#125;
                           &#125;
                        ]
                     &#125;
                  ]
               &#125;
            ],
            <span>"email"</span>:&#123;
               <span>"emailName"</span>:<span>"email3"</span>,
               <span>"id"</span>:<span>"e3"</span>,
               <span>"userId"</span>:<span>"u2"</span>
            &#125;,
            <span>"addressList"</span>:[
               &#123;
                  <span>"addressName"</span>:<span>"address2"</span>,
                  <span>"id"</span>:<span>"a2"</span>,
                  <span>"userId"</span>:<span>"u2"</span>
               &#125;
            ]
         &#125;
      &#125;,
      &#123;
         <span>"addressName"</span>:<span>"address4"</span>,
         <span>"id"</span>:<span>"a4"</span>,
         <span>"userId"</span>:<span>"u4"</span>,
         <span>"user"</span>:&#123;
            <span>"id"</span>:<span>"u4"</span>,
            <span>"userName"</span>:<span>"user4"</span>,
            <span>"userRoleList"</span>:[
               &#123;
                  <span>"id"</span>:<span>"bb2d1kuwvii0gpa0pxgaph8zr"</span>,
                  <span>"rid"</span>:<span>"r1"</span>,
                  <span>"userId"</span>:<span>"u4"</span>,
                  <span>"roleList"</span>:[
                     &#123;
                        <span>"id"</span>:<span>"r1"</span>,
                        <span>"roleName"</span>:<span>"role1"</span>,
                        <span>"rolePrivilegeList"</span>:[
                           &#123;
                              <span>"id"</span>:<span>"b484ze4k44xemtkstehnprhxq"</span>,
                              <span>"pid"</span>:<span>"p1"</span>,
                              <span>"rid"</span>:<span>"r1"</span>,
                              <span>"privilege"</span>:&#123;
                                 <span>"id"</span>:<span>"p1"</span>,
                                 <span>"privilegeName"</span>:<span>"privilege1"</span>
                              &#125;
                           &#125;
                        ]
                     &#125;
                  ]
               &#125;
            ],
            <span>"addressList"</span>:[
               &#123;
                  <span>"addressName"</span>:<span>"address4"</span>,
                  <span>"id"</span>:<span>"a4"</span>,
                  <span>"userId"</span>:<span>"u4"</span>
               &#125;
            ]
         &#125;
      &#125;
   ],
   <span>"u"</span>:[
      &#123;
         <span>"id"</span>:<span>"u3"</span>,
         <span>"userName"</span>:<span>"user3"</span>,
         <span>"addressList"</span>:[
            &#123;
               <span>"addressName"</span>:<span>"address3"</span>,
               <span>"id"</span>:<span>"a3"</span>,
               <span>"userId"</span>:<span>"u3"</span>
            &#125;
         ],
         <span>"emailMap"</span>:&#123;
            <span>"emailName"</span>:<span>"email5"</span>,
            <span>"id"</span>:<span>"e5"</span>,
            <span>"userId"</span>:<span>"u3"</span>
         &#125;
      &#125;,
      &#123;
         <span>"id"</span>:<span>"u5"</span>,
         <span>"userName"</span>:<span>"user5"</span>,
         <span>"addressList"</span>:[
            &#123;
               <span>"addressName"</span>:<span>"address5"</span>,
               <span>"id"</span>:<span>"a5"</span>,
               <span>"userId"</span>:<span>"u5"</span>
            &#125;
         ]
      &#125;
   ]
&#125;
</code></pre> 
<h3>用法详解(下面就是全部文档了, 一共10条，看完就学会了，看看比GraphQL简单多少！)</h3> 
<ul> 
 <li><code>每个数据库表格对应一个SQL查询，写在$()或$<span>1</span>()方法中</code></li> 
 <li><code>$()方法的第一个参数如果没有空格，则系统自动转换为 select * <span>from</span> xxx</code></li> 
 <li><code>$()方法的第一个参数如果有空格，如<span>"select id, name from tb"</span>，则系统不转换</code></li> 
 <li><code>$()方法的第一个参数的最后一个单词，将作为输出结果的键名。键名也可以用key(<span>"键名"</span>)来手工指定。</code></li> 
 <li><code>ms()方法也可以写成DB.masterSlave(),它的参数是主表和从表的键名，参数个数必须是<span>2</span>的倍数， ms()支持复合主键，如ms(<span>"m1"</span>, <span>"m2"</span>, <span>"c1"</span>,<span>"c2"</span> )表示主表的(m1，m2)列关联到从行的(c1,c2)列, 主表还是从表的判定与数据库定义无关，而是:如果一个$()方法写在另一个$()方法里，则它就是从表, ms()方法会被编译成 <span>" where xxId in (?, ?,...,?) "</span> 片段。问号是根据主表的所有关联列值填充为SQL参数</code></li> 
 <li><code>$<span>1</span>()方法表示仅输出单个元素而不是一个列表，$<span>1</span>()也可以写成$(<span>"xxxxx"</span>, DB.one)</code></li> 
 <li><code>从第二个参数起，即可使用jSqlBox的内嵌sql式语法，普通文本解析为SQL片段，pagin、par、que等方法都可以使用</code></li> 
 <li><code>缺省情况下，输出结果为<span>Map</span>/List结构，但是如果出现DB.entity(XxxClass)参数后，这个SQL的输出结果被转换为一 个实体Bean对象。实体Bean也可以嵌套从表的内容，但是要注意Bean里要有相应的字段定义。</code></li> 
 <li><code>使用DB.graphQuery($(), $()...)可以对一个或多个$()方法进行查询。</code></li> 
 <li><code>输出对象需要输出为Json时，需要使用者自行在pom中添加<span>JSON</span>工具依赖，并手工进行转换，jSqlBox是个ORM工具，本身并不提供<span>JSON</span>工具</code></li> 
</ul>
                                        </div>
                                      
</div>
            