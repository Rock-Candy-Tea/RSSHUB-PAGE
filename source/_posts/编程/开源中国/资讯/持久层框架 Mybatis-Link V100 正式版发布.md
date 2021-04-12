
---
title: '持久层框架 Mybatis-Link V1.0.0 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8422'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 11:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8422'
---

<div>   
<div class="content">
                                                                                            <h2>欢迎使用 Mybatis-Link V1.0.0 持久层框架</h2> 
<p>Mybatis Link是一个Mybatis Plus的增强工具，在Mybatis Plus的基础上进行了增强，主要解决一对一、一对多等多表联查，以及允许分布式应用远程调用和优化问题，从而达到敏捷开发的目的，实现零SQL编写。</p> 
<h3>关于1.0.0 版本更新内容</h3> 
<ul> 
 <li><strong>【</strong>新增<strong>】: </strong>源码官网发布<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feasy4use.cn%2F" target="_blank">Mybatis-Link</a></li> 
 <li><strong>【</strong>新增<strong>】: </strong>全新的Mgr业务层和Dao支持层抽象类。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>注解@Link类，作用在 Dao 方法上，可以实现一对一连表查询（包括左连接、右连接、内连接），一对多连表查询。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>新增支持Wrapper在RPC中的调用，新建了FindWrapper查询类。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>新增支持枚举类，以及枚举类翻译输出。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>新增分页查询二级缓存返回列表和条数。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>增加注解@VoDef类，对查询结果，可以直接返回实体类（Vo）。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>增加动态表名，查询可以通过表名过滤。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>增加数据库层面的批量新增。</li> 
</ul> 
<h3>零SQL：</h3> 
<p>采用注解的方式支持连表查询，满足大多数项目连表要求，可以实现零SQL编写。</p> 
<h3>连表查询示例：</h3> 
<p>更多连表示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feasy4use.cn%2Fguide%2Flink-search.html" target="_blank">https://easy4use.cn/guide/link-search.html</a></p> 
<pre><code class="language-java">/**
 * a 内连 c
 * a表的c_id字段，与c表中的id主键字段，进行连表查询。
 */
@Link(ones = &#123; @OneToOne(leftColumn = "c_id", rightClass = TestCVo.class) &#125;)
List<TestADto> listTestAATestC(@Param(Constants.WRAPPER) Wrapper<TestAVo> wrapper);

/**
 * a 左连 b
 */
@Link( ones = &#123; 
    @OneToOne(leftColumn = "b_id", rightClass = TestBVo.class, 
        joinType = JoinType.LEFT, onArgName = "abOn") &#125;)
List<TestADto> listTestALtTestB(@Param(Constants.WRAPPER) Wrapper<TestAVo> wrapper);

/**
 * a 一对多 b
 */
@Link( manys = &#123; 
    @OneToMany(leftColumn = "b_id", rightClass = TestBVo.class, 
        ofTypeClass = TestBDto.class, property = "testBList") &#125;)
List<TestADto> listTestAWTestB(@Param(Constants.WRAPPER) Wrapper<TestAVo> wrapper);</code></pre> 
<h3>配置：</h3> 
<pre><code class="language-json">mybatis-plus:
  typeAliasesPackage: yui.bss.*.vo
  mapperLocations: classpath:/mapper/**/*.xml
  global-config:
    db-config:
      id-type: ASSIGN_ID
      field-strategy: NOT_NULL
      column-underline: true
      logic-delete-value: 1 # 逻辑已删除值(默认为 1)
      logic-not-delete-value: 0 # 逻辑未删除值(默认为 0)
    banner: false
    sql-parser-cache: true
    super-mapper-class: yui.comn.mybatisx.core.mapper.BaseDao</code></pre> 
<h3>最新Maven版本：</h3> 
<pre><code class="language-xml"><dependency>
    <groupId>com.gitee.easy4use</groupId>
    <artifactId>mybatis-link-boot-starter</artifactId>
    <version>1.0.0</version>
</dependency></code></pre> 
<h2 style="text-align:start"> </h2> 
<h2 style="text-align:start">欢迎使用 Mybatis-Link 插件 Hub-Link V1.0.0 数据处理</h2> 
<p>Hub Link是数据加工中心，作为Mybatis Link的增强工具，可以就像咖啡伴侣一样，在使用Mybatis-Link的时候更加丝滑。作为数据加工中心，会对进出数据进行加工处理。</p> 
<h3>关于1.0.0 版本更新内容</h3> 
<ul> 
 <li><strong>【</strong>新增<strong>】: </strong>支持阿里JSON序列化。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>支持枚举类过滤输出</li> 
 <li><strong>【</strong>新增<strong>】: </strong>支持连表查询，数据输出。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>增加处理机质，可以在数据输出前，对数据进行处理。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>支持查询条件配置。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>支持数据输出同时，增加字段翻译。</li> 
 <li><strong>【</strong>新增<strong>】: </strong>增加query.js前端查询封装。</li> 
</ul> 
<h3><strong>特性</strong></h3> 
<ul> 
 <li><strong>无侵入: </strong>采用插件的形式，对进出数据进行加功处理。</li> 
 <li><strong>插件: </strong>可以作为Mybatis-Link的增强工具，两者可以一起使用。</li> 
 <li><strong>请求数据: </strong>每个controller都会对应一个xml，通过xml配置对请求数据进行加功处理。</li> 
 <li><strong>返回数据:</strong> 每个controller都会对应一个xml，通过xml配置对返回数据进行加功处理。</li> 
</ul> 
<h3 style="text-align:start">查询示例：</h3> 
<p>更多查询示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feasy4use.cn%2Fguide%2Fquery-start.html" target="_blank">https://easy4use.cn/guide/query-start.html</a></p> 
<p><span style="background-color:#ffffff; color:#2c3e50">查询接口</span></p> 
<pre><code>sys/user/list?this.$query.toQ(qry)</code></pre> 
<p style="text-align:start"><span style="background-color:#ffffff; color:#2c3e50">过滤条件</span></p> 
<pre><code class="language-javascript">let qry = this.$query.new()
this.$query.toR(qry, 'username', 'test')</code></pre> 
<p style="text-align:start">查询参数</p> 
<pre><code class="language-json">&#123;"w":[],"r":[&#123;"n":"a1","t":"and","w":[&#123;"k":"username","v":"test","m":"",
    "t":"and","s":0&#125;]&#125;],"o":[],"j":[],"p":&#123;&#125;,"s":&#123;&#125;&#125;</code></pre> 
<p style="text-align:start"><span style="color:#2c3e50">sql输出</span></p> 
<pre><code class="language-sql">SELECT t_sys_user.`id` t_sys_user__id, t_sys_user.`role_id` t_sys_user__role_id, t_sys_user.`username` t_sys_user__username, t_sys_user.`email` t_sys_user__email, t_sys_user.`rmks` t_sys_user__rmks, t_sys_user.`type` t_sys_user__type 
FROM t_sys_user 
WHERE ((t_sys_user.USERNAME LIKE ?))</code></pre> 
<p>返回结果</p> 
<pre><code class="language-json">&#123;
    "code": 0,
    "header": &#123;
        "typeDsr": "类型（0：管理员，1：非管理员）描述",
        "id": "ID",
        "roleId": "角色ID",
        "username": "登录名",
        "email": "邮件",
        "rmks": "备注",
        "type": "类型（0：管理员，1：非管理员）"
    &#125;,
    "data": &#123;
        "list": [
            &#123;
                "id": 3,
                "roleId": 3,
                "username": "test",
                "email": "test@163.com",
                "rmks": "test",
                "type": 1,
                "typeDsr": "普通用户"
            &#125;
        ]
    &#125;
&#125;</code></pre> 
<h3>出参示例：</h3> 
<p>更多查询示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feasy4use.cn%2Fguide%2Fdata-out.html" target="_blank">https://easy4use.cn/guide/data-out.html</a></p> 
<p><span style="background-color:#ffffff; color:#2c3e50">XML配置</span></p> 
<pre><code class="language-xml"><grid name="USER_ROLE">
    <col type="yui.bss.demo.vo.SysUserVo" />
    <col prefix="role" type="yui.bss.demo.vo.SysRoleVo" />
</grid></code></pre> 
<p>返回结果</p> 
<pre><code class="language-json">&#123;
    "code": 0,
    "header": &#123;
        "typeDsr": "类型（0：管理员，1：非管理员）描述",
        "id": "ID",
        "roleId": "ID",
        "username": "登录名",
        "email": "邮件",
        "rmks": "备注",
        "type": "类型（0：管理员，1：非管理员）",
        "roleCd": "编码",
        "roleNm": "名称",
        "roleRmks": "备注"
    &#125;,
    "data": &#123;
        "list": [
            &#123;
                "id": 1,
                "roleId": 1,
                "username": "admin",
                "email": "demo@163.com",
                "rmks": "admin",
                "type": 0,
                "roleCd": "ROLE_ADMIN",
                "roleNm": "管理员",
                "roleRmks": "管理员",
                "typeDsr": "管理员"
            &#125;
        ]
    &#125;
&#125;</code></pre> 
<h3>最新Maven版本：</h3> 
<pre><code class="language-xml"><dependency>
    <groupId>com.gitee.easy4use</groupId>
    <artifactId>hub-link-annotation</artifactId>
    <version>1.0.0</version>
</dependency>

<dependency>
    <groupId>com.gitee.easy4use</groupId>
    <artifactId>hub-link-core</artifactId>
    <version>1.0.0</version>
</dependency></code></pre> 
<h2>附：项目信息</h2> 
<p>项目官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Feasy4use.cn%2F" target="_blank">https://easy4use.cn/</a></p> 
<p>Mybaits-Link项目源码：<a href="https://gitee.com/easy4use/mybatis-link">https://gitee.com/easy4use/mybatis-link</a></p> 
<p>Hub-Link源码：<a href="https://gitee.com/easy4use/hub-link">https://gitee.com/easy4use/hub-link</a></p> 
<p>项目示例：<a href="https://gitee.com/easy4use/mybatis-link-samples">https://gitee.com/easy4use/mybatis-link-samples</a></p>
                                        </div>
                                      
</div>
            