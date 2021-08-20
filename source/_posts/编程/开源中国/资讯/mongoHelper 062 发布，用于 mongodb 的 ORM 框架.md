
---
title: 'mongoHelper 0.6.2 发布，用于 mongodb 的 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=715'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 15:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=715'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#40485b">mongoHelper 是基于 spring-data-mongodb 的增强ORM工具包，简化 CRUD 操作，提供类似于mybatis plus的mongodb数据库操作。</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">虽然spring-data-mongodb已经对mongodb的操作做了一部分封装，但易用性依然不够，Query Criteria Sort的操作依然有比较大的局限性，而且对于习惯sql操作的人来说，理解其使用法则依然稍显别扭。mongoHelper对spring-data-mongodb又进行了进一步封装，使其更易于使用。对使用过mybatis plus的</span>开发者来说，其用法应该不会陌生。使用java对象构建查询条件，不再写sql的敏捷开发体验，mongoHelper正是基于这个理念开发的。</p> 
<p><span style="background-color:#ffffff; color:#40485b">演示应用项目：</span><a href="https://gitee.com/cym1102/mongoStudy">https://gitee.com/cym1102/mongoStudy</a></p> 
<p style="text-align:left"><strong>基本用法：</strong></p> 
<p style="text-align:left">本orm会在容器中注入一个对象MongoHelper，这个对象拥有诸多单表查询功能，摘要如下</p> 
<ul> 
 <li>按id删除：deleteById(String, Class<?>)</li> 
 <li>按条件删除：deleteByQuery(Criteria, Class<?>)</li> 
 <li>查询所有：findAll(Class)</li> 
 <li>查询数量：findCount(Class<?>)</li> 
 <li>根据id查询：findById(String, Class)</li> 
 <li>根据条件查询：findListByQuery(Criteria, Class<?>)</li> 
 <li>根据条件查询并分页：findPage(Criteria, Page, Class<?>)</li> 
 <li>插入：insert(Object)</li> 
 <li>插入或更新：insertOrUpdate(Object)</li> 
 <li>根据id更新：updateById(Object)</li> 
 <li>根据id更新全部字段：updateAllColumnById(Object)</li> 
 <li>根据条件更新第一项：updateFirst(Criteria, Update, Class<?>)</li> 
 <li>根据条件更新所有项：updateMulti(Criteria, Update, Class<?>)</li> 
 <li>累加某一个字段的数量, 原子操作：addCountById(String id, String property, Long count, Class<?> clazz)</li> 
</ul> 
<p style="text-align:left">这个mongoHelper能够完成所有查询任务，插入和更新操作能够自动判断pojo的类型操作对应表，查询操作根据传入的Class进行对应表操作，本orm所有数据库操作都基于mongoHelper的功能，不用像mybatis一样，每个表都要建立一套Mapper，xml，Service，model，大大减少数据层的代码量。可以将mongoHelper直接注入到controller层，简单的操作直接调用mongoHelper进行操作，不需要调用service层。</p> 
<p style="text-align:left">而复杂的操作及事务处理需要service层，将mongoHelper注入service，并使用service层的@Transactional注解就能使用springBoot管理的事务功能。</p> 
<p><strong>打印查询语句：</strong></p> 
<p style="text-align:left">spring-data-mongodb默认的打印语句方式为修改配置文件logging.level.root: debug。但这里打印出来的语句基本不可读，也不能像sql一样直接复制出来到数据库中进行执行，处于集群模式下还每隔数秒发送一次检测当前数据库isMaster的命令，很干扰debug。本orm重写了查询语句的打印功能，只要配置spring.data.mongodb.print：true就能打印出如下的语句：</p> 
<div style="text-align:left"> 
 <div> 
  <pre>db.admin.find(&#123;
    "$and": [
        &#123;
            "name": &#123;
                "$regex": "^.*ad.*$",
                "$options": "i"
            &#125;
        &#125;
    ]
&#125;).projection(&#123;
    "name": 1
&#125;).sort(&#123;
    "id": -1
&#125;);</pre> 
 </div> 
</div> 
<p style="text-align:left">可直接复制到mongodb客户端中进行执行，非常方便调试。</p> 
<p><strong>多数据源：</strong></p> 
<p style="text-align:left">如果需要连接两个以上的mongodb数据库，可先在yml文件中配一个uri2:</p> 
<div style="text-align:left"> 
 <div> 
  <pre>spring:
  data:
    mongodb:
      uri2:     mongodb://user:pass@host:27017/study?replicaSet=rs0&authSource=admin&w=majority&j=true&wtimeout=5000&readPreference=primary</pre> 
 </div> 
</div> 
<p style="text-align:left">再配置一个MongoHelper2类继承MongoHelper:</p> 
<div style="text-align:left"> 
 <div> 
  <pre>@Service("mongoHelper2")
public class MongoHelper2 extends MongoHelper &#123;

@Value("$&#123;spring.data.mongodb.uri2&#125;")
String uri2;

@PostConstruct
public void init() &#123;
// 使用uri2初始化mongoTemplate,不支持事务
this.mongoTemplate = new MongoTemplate(new SimpleMongoClientDatabaseFactory(uri2));

super.init();
&#125;
&#125;
</pre> 
 </div> 
</div> 
<p style="text-align:left">这样，注入MongoHelper2进行增删改查的操作就会被执行到uri2的数据库上</p> 
<p><strong>获取原生mongoTemplate：</strong></p> 
<p style="text-align:left">如果觉得MongoHelper的方法无法满足项目需求, 可以用mongoHelper.getMongotemplate()的方式获取springboot原生的mongotemplate对象进行操作。</p> 
<p style="text-align:left"> </p> 
<p style="text-align:left"><strong><span style="background-color:#ffffff; color:#333333">本次更新内容：</span></strong></p> 
<ol> 
 <li><span style="background-color:#ffffff; color:#40485b">修正一些编码规范，减少代码警告数量</span></li> 
 <li><span style="background-color:#ffffff; color:#40485b">添加多数据源功能</span></li> 
 <li><span style="background-color:#ffffff; color:#40485b">添加@createTime和@updateTime注解功能</span> ，可自动插入更新时间和修改时间</li> 
 <li>更新<span style="background-color:#ffffff; color:#40485b">springBoot版本, 增加支持mongodb 5.0</span></li> 
 <li><span style="background-color:#ffffff; color:#40485b">修复大量bug</span></li> 
</ol>
                                        </div>
                                      
</div>
            