
---
title: 'ORM 框架 Bee V1.11_4.22 发布，添加 SPI 预加载接口 PreLoad 提高缓存安全等'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-21b5cdfb840f2b2b58e01f55dac317dc60e.png'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 07:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-21b5cdfb840f2b2b58e01f55dac317dc60e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#3498db">Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#c0392b">Bee让程序员/软件工程师，从手工编码中解放出来，Bee更适合智能软件制造时代！</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#e74c3c">立志做最懂用户的软件!</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>V1.11.0.4.22 (世界地球日)</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>增加Registry接口</strong>；增加NameRegistry.<br> 更改Serializer接口抛出异常方式.<br> MapSuid,MapSq<strong>l支持解析字符串的Boolean</strong>类型.<br> <strong>GenBean</strong>，还不支持的jdbc类型，提醒在哪个文件设置.<br> <strong>GenBean</strong>增加获取字段支持，使用字段名可以不直接使用字符串.<br> <strong>GenBean</strong>增加支持是否覆盖原有文件设置。<br> systemLogger支持设置日志级别，方便开发调试.<br> Logger增加public static void debug(String msg,Throwable t)(方便开发调试).<br> SuidRich的selectString方法支持可变参数:<br> public List<String[]> selectString(T entity,String... selectFields);<br> nocache增加日志提示.<br> 提高缓存安全.<br> 添加<strong>SPI预加载</strong>接口PreLoad.<br> 添加用于<strong>全局的拦截器注册器</strong>InterceptorChainRegistry.<br> 添加配置项:<br> 是否是limit offset语法<strong>分页</strong> pagingWithLimitOffset<br> 是否捕获单条插入时的重复键异常 notCatchModifyDuplicateException<br> 是否显示单条插入时的重复键异常 notShowModifyDuplicateException<br> fixed bug for type converter.<br> fixed bug about @PrimaryKey in Suid update(entity).</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>部分实例:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用字段名,不再直接使用字符串,更好适应数据库表变更. <strong>实体名_F</strong>  就可以引用字段名</p> 
<pre><code class="language-java">//方式1
objSQLRichService.update(download, "genProject");
//方式2, 本次新增.
objSQLRichService.update(download, Download_F.genProject);</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>生成文件实例:</strong></p> 
<pre><code class="language-java">//config.setGenComment(true);
config.setGenFieldFile(true); //本次新增功能
config.setCommentPlace(1);

config.setOverride(true); //是否覆盖原来的文件   本次新增功能

genBean.genSomeBeanFile("download");</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>变长参数,  列出你要查询的字段</strong></p> 
<pre><code class="language-java">    //V1.11.0.4.22 变长参数,  列出你要查询的字段
    list=suidRich.selectString(new TestUser(), TestUser_F.name,TestUser_F.lastName,TestUser_F.email);
    Printer.print(list);</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下期功能预告:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>准备向复杂的分库分表进军了。。。</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>好消息:</strong><br> 2022年<strong><span style="color:#c0392b">5月1日</span>劳动节</strong>前登记的企业用户，可获得专业的生产环境使用帮助,为你的系统保驾护航、提高性能；<br> 个人用户登记后入群(扣群:<strong>992650213</strong>)，可获得个性化的使用咨询!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">登记地址：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee/issues/I3PIUJ">https://gitee.com/automvc/bee/issues/I3PIUJ</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee%2Fissues%2F43" target="_blank">https://github.com/automvc/bee/issues/43</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff; color:#333333">近期已添加功能:</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/177042/bee-1-11-0-1-1-released" target="_blank">ORM 框架 Bee V1.11.0.1.1（2022新年版）发布，更快、更简单、更自动</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/180926/bee-1-11-0-2-1-released" target="_blank">ORM 框架 Bee V1.11.0.2.1（2022 春节版）发布，拦截器、多租户(过年不打烊)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.4 (2022北京冬奥版)发布,二级缓存扩展支持(Redis)</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">ORM 框架</a> <a href="https://www.oschina.net/news/181491/bee-1-11-0-2-4-2022-released" target="_blank">Bee<span> </span></a><a href="https://www.oschina.net/news/182304/bee-2022-romantic-released" target="_blank">2022 Romantic 版发布,加 JustFetch,Datetime 等注解和 Jndi 支持</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/183310/bee-1-11-0-2-20-2022-released" target="_blank">ORM 框架 Bee V1.11.0.2.20 2022(荣耀)版发布，完善拦截器，增加多种注解简化开发</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/184359" target="_blank">ORM 框架 Bee V1.11.0.2.28 发布，查询结果拦截、ShardingStruct 为分库分表准备</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/185450/bee-1-11-3-8-released" target="_blank">ORM 框架 Bee V1.11.0.3.8(</a><span style="background-color:#ffffff; color:#333333"><span><strong><span><span style="color:#ef39a1">Lady First)</span></span></strong></span></span><a href="https://www.oschina.net/news/185450/bee-1-11-3-8-released" target="_blank">发布，设置参数转换器，Json 与 Javabean 属性自动转化</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/186854/bee-1-11-3-12-released" target="_blank">ORM 框架 Bee V1.11.0.3.12(植树节版) 发布，支持 Cassandra (还可自动生成表)，方言注册器</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/187804" target="_blank">ORM 框架 Bee V1.11.0.3.20(春分版) 发布，自定义动态 SQL 标签</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee#bee%E4%B8%BB%E8%A6%81%E5%8A%9F%E8%83%BD%E7%89%B9%E7%82%B9%E4%BB%8B%E7%BB%8D">https://gitee.com/automvc/bee#bee主要功能特点介绍</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由Bee框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与DB交互的编码工作量, 是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的Java 框架!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee简单易用：单表操作、多表关联操作，可以不用写sql,极少语句就可以完成SQL操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333">,10分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="color:#e74c3c"><span style="background-color:#ffffff">高级要求，还可以方便自定义SQL语句</span></span></strong><span style="background-color:#ffffff; color:#333333">。</span></p> 
<p> </p> 
<p><img height="817" src="https://oscimg.oschina.net/oscnet/up-21b5cdfb840f2b2b58e01f55dac317dc60e.png" width="752" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            