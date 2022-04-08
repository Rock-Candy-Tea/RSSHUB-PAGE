
---
title: 'fastmybatis 2.2.1 发布，mybatis 开发利器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5942'
author: 开源中国
comments: false
date: Fri, 08 Apr 2022 16:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5942'
---

<div>   
<div class="content">
                                                                    
                                                        <p>fastmybatis 2.2.1 发布，本次更新内如如下：</p> 
<ul> 
 <li>去除spring依赖，项目无需依赖spring也能跑，具体查看<a href="https://gitee.com/durcframework/fastmybatis/tree/master/fastmybatis-demo/fastmybatis-demo-standard" target="_blank">fastmybatis-demo/fastmybatis-demo-standard</a></li> 
 <li>新增Vert.x示例，具体查看<a href="https://gitee.com/durcframework/fastmybatis/tree/master/fastmybatis-demo/fastmybatis-demo-vertx" target="_blank">fastmybatis-demo/fastmybatis-demo-vertx</a></li> 
</ul> 
<p>本次更新最大的改动是不需要依赖spring框架，具体用法如下：</p> 
<pre><code class="language-java">public static void main(String[] args) &#123;
    // 启动加载
    Fastmybatis.create()
        // 指定mybatis-config.xml文件classpath路径
        .configLocation("mybatis/mybatis-config.xml")
        // 指定mybatis sql文件classpath目录
        .mapperLocations("mybatis/mapper")
        // 指定Mapper接口package
        .basePackage("com.myapp.dao")
        .load();

    // 使用mapper
    TUser user = Mappers.run(TUserMapper.class, mapper -> &#123;
        return mapper.getById(6);
    &#125;);
    System.out.println(user);
&#125;</code></pre> 
<p>因为没有依赖spring框架，需要对SqlSession进行管理，比如提交，回滚，关闭。因此fastmybatis提供了一个简单的工具类，用来自动commit，close</p> 
<pre><code class="language-java">Mappers.run(TUserMapper.class, mapper -> &#123;
        return mapper.getById(6);
    &#125;);</code></pre> 
<p>如果是Spring项目可以使用依赖注入，@Autowired private TUserMapper mapper; </p> 
<p>更多用法可以前往项目首页查看。</p> 
<p><strong>关于fastmybatis</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fastmybatis是一个mybatis开发框架，其宗旨为：简单、快速、有效。</p> 
<ul> 
 <li>零配置快速上手，无需依赖Spring</li> 
 <li>无需编写xml文件即可完成增删改查操作</li> 
 <li>支持mysql、sqlserver、oracle、postgresql、sqlite</li> 
 <li>支持自定义sql，对于基本的增删改查不需要写SQL，对于其它特殊SQL（如统计SQL）可写在xml中</li> 
 <li>支持与spring-boot集成，依赖starter即可</li> 
 <li>支持插件编写</li> 
 <li>支持ActiveRecord模式</li> 
 <li>支持多租户</li> 
 <li>提供通用Service</li> 
 <li>API丰富，多达40+方法，满足日常开发需求。</li> 
 <li>轻量级，无侵入性，是官方mybatis的一种扩展</li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            