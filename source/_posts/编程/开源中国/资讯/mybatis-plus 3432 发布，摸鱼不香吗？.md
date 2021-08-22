
---
title: 'mybatis-plus 3.4.3.2 发布，摸鱼不香吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6889'
author: 开源中国
comments: false
date: Sat, 21 Aug 2021 10:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6889'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:justify"><span style="background-color:#ffffff">Mybatis-Plus 是一款 MyBatis 的增强工具包，简化 CRUD 操作。启动加载 XML 配置时注入单表 SQL 操作 ，为简化开发工作、提高生产率而生。Mybatis-Plus 启动注入非拦截实现、性能更优，让你专注业务快速敏捷开发。  </span></p> 
<p style="text-align:justify"><span style="background-color:#ffffff; color:#ff4c00">MP 的小目标让您拥有更多的时间、去养生、去摸鱼 ！！！</span></p> 
<h4 style="text-align:left">演示例子 <a href="https://gitee.com/baomidou/mybatis-plus-samples">mybatis-plus-samples</a>   <a href="https://gitee.com/baomidou/mybatis-plus-samples"> </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2Fguide%2Fmybatis-mate.html" target="_blank">高级特性</a>     <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2F" target="_blank">帮助文档 </a> </h4> 
<ul> 
 <li>增加 goldilocks 数据库 csiidb 数据库 的支持</li> 
 <li>新增对CUBRID数据库的支持</li> 
 <li>增加对南大通用GBase 8s数据库的支持（GBASEDBT)，区别于原有定义（GBASE)</li> 
 <li>优化 selectOne 查询方式，精简 SQL 注入</li> 
 <li>PropertyMapper.whenNotBlack to whenNotBlank</li> 
 <li>BaseMapper新增deleteById(T entity)方法</li> 
 <li>jsqlparser 版本 4.0 升级 4.1</li> 
 <li>TableInfo新增原生Reflector反射操作.</li> 
 <li>解决 lambda 构造器在 JDK16 中无法运行的问题</li> 
 <li>wrapper clear 将sqlSegment重置为空串 缓存标志重置为true</li> 
 <li>注入器调整无主键不注入ById方法</li> 
 <li>自动构建 resultMap 处理主键获取真正的字段名</li> 
 <li>Wrapper optimized: 优化警告</li> 
 <li>Wrapper 新增 gtSql geSql ltSql leSql 方法</li> 
 <li>fix github pull/3557 乐观锁新增版本号 null 自定义异常，租户插入忽略逻辑允许自定义</li> 
 <li>fix github issues/2931 解决结果集大于 Integer 异常问题</li> 
 <li>fix github issues/3652 k8s 网络获取失败问题</li> 
 <li>fix gitee issues/I3Z2RG 优化 Order By SQL 注入识别率</li> 
 <li>fix gitee issues/3826 优化动态表名处理器</li> 
 <li>fix gitee issues/I3UQH5 修复注解@OrderBy，使用limit 异常</li> 
 <li>fix github issues/3768 mysql 批量自增 bug</li> 
 <li>修复自动构建resultMap时主键字段映射错误&OrderBySegmentList懒加载执行</li> 
 <li>源代码升级相关测试依赖，构建环境 gradle 升级为 7.1 新增更多测试用例</li> 
</ul> 
<p style="text-align:justify"><strong>往下看，这个姿势你会吗？</strong></p> 
<pre><code>// 实体注解 @OrderBy 默认 MP 内置f方法自动排序</code><code>@OrderBy</code><code>private Date createTime;</code>
<code>// 注解类如下</code><code>public @interface OrderBy &#123;</code>
<code>    /**</code><code>     * 是否倒序查询，默认是</code><code>     */</code><code>    boolean isDesc() default true;</code>
<code>    /**</code><code>     * 数字越小越靠前</code><code>     */</code><code>    short sort() default Short.MAX_VALUE;</code>
<code>&#125;</code>
</pre> 
<p style="text-align:justify"><strong><strong>Wrapper 指定映射，这个姿势用过吗？</strong></strong></p> 
<pre><code> Wrappers.<User>lambdaUpdate().set(User::getWallets, ..</code><code> ,"typeHandler=com.baomidou.mybatisplus.samples.typehandler.WalletListTypeHandler");</code></pre> 
<p style="text-align:justify"><strong>升级日志</strong></p> 
<ul> 
 <li> <p>增加 goldilocks 数据库 csiidb 数据库 的支持</p> </li> 
 <li> <p>增加对南大通用GBase 8s数据库的支持（GBASEDBT)，区别于原有定义（GBASE)</p> </li> 
 <li> <p>优化 selectOne 查询方式，精简 SQL 注入</p> </li> 
 <li> <p>PropertyMapper.whenNotBlack to whenNotBlank</p> </li> 
 <li> <p>BaseMapper新增deleteById(T entity)方法</p> </li> 
 <li> <p>jsqlparser 版本 4.0 升级 4.1</p> </li> 
 <li> <p>TableInfo新增原生Reflector反射操作.</p> </li> 
 <li> <p>解决 lambda 构造器在 JDK16 中无法运行的问题</p> </li> 
 <li> <p>wrapper clear 将sqlSegment重置为空串 缓存标志重置为true</p> </li> 
 <li> <p>注入器调整无主键不注入ById方法</p> </li> 
 <li> <p>自动构建 resultMap 处理主键获取真正的字段名</p> </li> 
 <li> <p>Wrapper optimized: 优化警告</p> </li> 
 <li> <p>Wrapper 新增 gtSql geSql ltSql leSql 方法</p> </li> 
 <li> <p>新增对CUBRID数据库的支持</p> </li> 
 <li> <p>fix github pull/3557 乐观锁新增版本号 null 自定义异常，租户插入忽略逻辑允许自定义</p> </li> 
 <li> <p>fix github issues/2931 解决结果集大于 Integer 异常问题</p> </li> 
 <li> <p>fix github issues/3652 k8s 网络获取失败问题</p> </li> 
 <li> <p>fix gitee issues/I3Z2RG 优化 Order By SQL 注入识别率</p> </li> 
 <li> <p>fix gitee issues/3826 优化动态表名处理器</p> </li> 
 <li> <p>fix gitee issues/I3UQH5 修复注解@OrderBy，使用limit 异常</p> </li> 
 <li> <p>fix github issues/3768 mysql 批量自增 bug</p> </li> 
 <li> <p>修复自动构建resultMap时主键字段映射错误&OrderBySegmentList懒加载执行</p> </li> 
 <li> <p>源代码升级相关测试依赖，构建环境 gradle 升级为 7.1 新增更多测试用例</p> </li> 
</ul>
                                        </div>
                                      
</div>
            