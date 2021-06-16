
---
title: 'Mybatis-Plus 3.4.3.1 发布，腾出手来干别的不香吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7483'
author: 开源中国
comments: false
date: Wed, 16 Jun 2021 09:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7483'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">Mybatis-Plus 是一款 MyBatis 的增强工具包，简化 CRUD 操作。启动加载 XML 配置时注入单表 SQL 操作 ，为简化开发工作、提高生产率而生。Mybatis-Plus 启动注入非拦截实现、性能更优，让你专注业务快速敏捷开发。</p> 
<p style="text-align:left"><span style="background-color:#2ecc71">还在用 Mybatis 在 xml 中吭哧坑次的 crud 吗？腾出手来干别的不香吗？</span></p> 
<h4 style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fbaomidou%2Fmybatis-plus-samples" target="_blank">演示例子 mybatis-plus-samples</a>    <br> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fbaomidou.com" target="_blank">帮助文档</a> </h4> 
<h2 style="text-align:left">更新日志：</h2> 
<ul> 
 <li>支持多重继承获取泛型</li> 
 <li>应要求 pageDto 修改为 PageDTO</li> 
 <li>分页排序优化</li> 
 <li>TableField 新增 ResultMapping#property 注解支持</li> 
 <li>fixed github pull/3550 优化排序</li> 
 <li>fix #I3T0LA</li> 
 <li>开放KtUpdateChainWrapper、KtQueryChainWrapper的继承</li> 
 <li>新增 exists 方法判断 count 存在</li> 
 <li>优化数据方言获取方式减少对象创建</li> 
 <li>feat GlobalConfig增加whereStrategy属性和适配selectStrategy的getWhereStrategy()方法</li> 
 <li>扩展 p6spy 优化</li> 
 <li>fix github#3390 SqlRunner.selectPage()方法未释放连接克隆</li> 
 <li>优化 JDK 默认不推荐泛型数组</li> 
 <li>perf: 替换为 JVM 中本身的方法</li> 
 <li>当用户指定ID时，不用自动生成，不指定时自增</li> 
 <li>Github Merge pull request #3549 #3555 #3565 #3571 #3587 #3591 #3592 #3595 #3599 #3605 #3606</li> 
 <li>提供处理Map多key取值工具方法</li> 
 <li>调整 page 注解泛型 E 为 P 方便阅读</li> 
 <li>Pattern定义为静态常量，优化正则匹配速度</li> 
 <li>Fix 主键添加@OrderBy无效</li> 
 <li>去除addMappedStatement日志打印</li> 
 <li>NoKeyGenerator Jdbc3KeyGenerator shared instance</li> 
</ul>
                                        </div>
                                      
</div>
            