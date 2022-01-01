
---
title: 'mybatis-plus 3.5.0 发布，定个小目标。'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6553'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 21:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6553'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Mybatis-Plus 是一款 MyBatis 的增强工具包，简化 CRUD 操作。启动加载 XML 配置时注入单表 SQL 操作 ，为简化开发工作、提高生产率而生。Mybatis-Plus 启动注入非拦截实现、性能更优，让你专注业务快速敏捷开发。  </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#ff4c00">MP 的小目标让您拥有更多的时间、去养生、去摸鱼 ！！！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#ff4c00">2022 年定个小目标，重构 mp 4.0 </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#ff4c00"> </span><a href="https://www.oschina.net/question/2918182_2324827" target="_blank">2021 年度 OSC 中国开源项目评选结果公布</a>  很高兴 MP 连续 5 年入围 OSC 最受欢迎软件名单，感谢各位粉丝的积极踊跃投票，祝各位新春快乐 。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/baomidou/mybatis-plus-samples"><span style="background-color:#ffffff">演示</span><span style="background-color:#ffffff">例</span><span style="background-color:#ffffff">子 mybatis-plus-samples</span></a>   <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2F" target="_blank">帮助文档 </a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新日志 </h4> 
<ul> 
 <li>升级 mybatis 3.5.9</li> 
 <li>升级 jsqlparser 4.3</li> 
 <li>新增移除 Mapper 相关缓存，支持 GroovyClassLoader 动态注入 Mapper</li> 
 <li>添加动态表名的钩子函数<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fbaomidou%2Fmybatis-plus%2Fpull%2F3965">https://github.com/baomidou/mybatis-plus/pull/3965</a></li> 
 <li>注入类 DefaultSqlInjector 优化调整</li> 
 <li>反射类 ReflectionKit 优化 field -> field 改为 Function.identity()</li> 
 <li>baseMapper 新增方法 exist 方法</li> 
 <li>解决 sysbase 小写 from 导致 index 取不到正确的索引值问题</li> 
 <li>新增通过 entityClass 获取 Mapper 方法<span> </span><code>BaseMapper<Entity> mapper = SqlHelper.getMapper(Entity.class);</code></li> 
 <li>注入方法 byId 注入优化</li> 
 <li>多租户 right join bug<span> </span><a href="https://gitee.com/baomidou/mybatis-plus/issues/I4FP6E">https://gitee.com/baomidou/mybatis-plus/issues/I4FP6E</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fbaomidou%2Fmybatis-plus%2Fpull%2F4035">https://github.com/baomidou/mybatis-plus/pull/4035</a></li> 
 <li>自定义注入方法名优化<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fbaomidou%2Fmybatis-plus%2Fpull%2F4159">https://github.com/baomidou/mybatis-plus/pull/4159</a></li> 
 <li>新增 sap hana 内存数据库</li> 
 <li>新增 SimpleQuery 工具栏查询</li> 
 <li>SQL 注入验证工具类 代码修改写法</li> 
 <li>整理字符串常量的使用</li> 
 <li>upgrade license-gradle-plugin version</li> 
 <li>自定义注入方法名优化 (不兼容)</li> 
 <li>重载columnsToString方法允许子类调整</li> 
 <li>修复 et 判断逻辑 fixed gitee issues/I4L4XV</li> 
 <li>逻辑删除 byId 支持转换为实体删除填充</li> 
</ul>
                                        </div>
                                      
</div>
            