
---
title: 'Magician 2.0 发布，彻底抛弃底层，全面迎接 Netty'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1580'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 22:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1580'
---

<div>   
<div class="content">
                                                                    
                                                        <p>经过了将近 4 个月，我终于又有了一点点闲置的时间，刚好趁这波机会 将项目进行了一次大升级，所以版本号也是飞跃式的上升，从1.1.17 直接升级到2.0。</p> 
<h2>本次升级主要是以下三个方面</h2> 
<ol> 
 <li>Magician 的定位发生了改变，以前是一个网络编程包，现在改成了小型http服务，因为底层被彻底抛弃了，全部换成了Netty，现在只是基于Netty开发的http服务，不在具备自定义协议的能力了。</li> 
 <li>Magician-Web 为了配合Magician的升级，也进行了一次升级</li> 
 <li>Magician-JDBC彻底进行了重构，抛弃了SQL构建器，改成了更为简单的方式，单表操作不需要写SQL，有条件构造器可以使用，复杂操作可以自己写sql，同时提供了事务管理器</li> 
</ol> 
<h2>具体的变化</h2> 
<p>Magician 除了底层大换血，全部改成了Netty，其他基本没变，只是少了一个UDP的支持，从使用者的角度来看 基本没啥变化</p> 
<p>Magician-Web只是配合Magician进行的一次小小的调整，所以几乎没变化。</p> 
<p>重点在Magician-JDBC</p> 
<h2>Magician-JDBC的变化</h2> 
<p>依然保留了多数据源的支持，其他变化如下</p> 
<h2 style="text-align:start">单表无SQL操作</h2> 
<h3 style="text-align:start">插入数据</h3> 
<div style="text-align:start"> 
 <pre><code class="language-java">ParamPO paramPO = new ParamPO();
paramPO.setUserName("a");
paramPO.setUserEmail("test@qq.com");

int result = JDBCTemplate.get().insert("表名", paramPO);</code></pre> 
</div> 
<h3 style="text-align:start">修改数据</h3> 
<div style="text-align:start"> 
 <pre><code class="language-java">// 构建修改条件
List<Condition> conditionList = new ArrayList<>();
conditionList.add(Condition.get("id = ?", 4));

// 构建修改数据
ParamPO paramPO = new ParamPO();
paramPO.setUserName("a");
paramPO.setUserEmail("test@qq.com");

// 执行修改
int result = JDBCTemplate.get().update("表名", paramPO, conditionList);</code></pre> 
</div> 
<h3 style="text-align:start">删除数据</h3> 
<div style="text-align:start"> 
 <pre><code class="language-java">// 构建删除条件
List<Condition> conditionList = new ArrayList<>();
conditionList.add(Condition.get("id = ?", 42));

// 执行删除
int result = JDBCTemplate.get().delete("表名", conditionList);</code></pre> 
</div> 
<h3 style="text-align:start">查询数据</h3> 
<div style="text-align:start"> 
 <pre><code class="language-java">// 构建查询条件
List<Condition> conditionList = new ArrayList<>();
conditionList.add(Condition.get("id > ?", 10));
conditionList.add(Condition.get("and user_name != ?", "a"));
conditionList.add(Condition.get("order by create_time desc", Condition.NOT_WHERE));

// 执行查询
List<ParamPO> result = JDBCTemplate.get().select("xt_message_board", conditionList, ParamPO.class);</code></pre> 
 <h2 style="text-align:start">自定义sql</h2> 
 <h3 style="text-align:start">增删改</h3> 
 <div style="text-align:start"> 
  <pre><code class="language-java">ParamPO paramPO = new ParamPO();
paramPO.setUserName("testTx222");
paramPO.setUserEmail("testTx222@qq.com");
paramPO.setId(4);

// 采用&#123;&#125;占位符的写法
int result = JDBCTemplate.get().exec("update xt_message_board set user_name = &#123;user_name&#125; , user_email = &#123;user_email&#125; where id = &#123;id&#125;", paramPO);

// 采用 ? 占位符的写法
int result = JDBCTemplate.get().exec("update xt_message_board set user_name = ? , user_email = ? where id = ?", new Object[]&#123;"testTx222","testTx222@qq.com", 4&#125;);</code></pre> 
 </div> 
 <h3 style="text-align:start">查询数据</h3> 
 <div style="text-align:start"> 
  <pre><code class="language-java">ParamPO paramPO = new ParamPO();
paramPO.setId(5);
paramPO.setUserName("a");

// 采用&#123;&#125;占位符的写法
List<ParamPO> result = JDBCTemplate.get("dataSource").selectList("select * from xt_message_board where id > &#123;id&#125; and user_name != &#123;user_name&#125;", paramPO, ParamPO.class);

// 采用 ? 占位符的写法
List<ParamPO> result = JDBCTemplate.get("dataSource").selectList("select * from xt_message_board where id > ? and user_name != ?", new Object[]&#123;5, "a"&#125;, ParamPO.class);</code></pre> 
 </div> 
 <h3 style="text-align:start">分页查询</h3> 
 <div style="text-align:start"> 
  <pre><code class="language-java">// 查询条件
ParamPO paramPO = new ParamPO();
paramPO.setId(5);
paramPO.setUserName("a");

// 查询参数
PageParamModel pageParamModel = new PageParamModel();
pageParamModel.setCurrentPage(1);
pageParamModel.setPageSize(10);
pageParamModel.setParam(paramPO);

// 使用默认countSql查询
PageModel<ParamPO> pageModel =  JDBCTemplate.get().selectPage("select * from xt_message_board where id > &#123;id&#125; and user_name != &#123;user_name&#125;", pageParamModel, ParamPO.class);

// 使用自定义countSql查询
String countSql = "自己定义countSql";

PageModel<ParamPO> pageModel =  JDBCTemplate.get().selectPageCustomCountSql("select * from xt_message_board where id > &#123;id&#125; and user_name != &#123;user_name&#125;", countSql, pageParamModel, ParamPO.class);
</code></pre> 
 </div> 
 <h2 style="text-align:start">事务管理</h2> 
 <div style="text-align:start"> 
  <pre><code class="language-java">// 开启事务
TransactionManager.beginTraction();

try &#123;
    ParamPO paramPO = new ParamPO();
    paramPO.setUserName("testTx222");
    paramPO.setUserEmail("testTx222@qq.com");
    paramPO.setId(4);
    int result = JDBCTemplate.get().exec("update xt_message_board set user_name = &#123;user_name&#125; , user_email = &#123;user_email&#125; where id = &#123;id&#125;", paramPO);

    // 提交
    TransactionManager.commit();
&#125; catch(Execption e)&#123;
    // 回滚
    TransactionManager.rollback();
&#125;</code></pre> 
  <h2>详情可以访问官方查看文档哦</h2> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmagician-io.com" target="_blank">https://magician-io.com</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            