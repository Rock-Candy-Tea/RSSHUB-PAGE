
---
title: 'mybatis-mapper 1.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5ff10ba71ab6b0e39ff33929e1e12d5ee71.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 07:40:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5ff10ba71ab6b0e39ff33929e1e12d5ee71.png'
---

<div>   
<div class="content">
                                                                                            <h3 style="text-align:start"><img alt height="246" src="https://oscimg.oschina.net/oscnet/up-5ff10ba71ab6b0e39ff33929e1e12d5ee71.png" width="561" referrerpolicy="no-referrer"></h3> 
<h3 style="text-align:start">2021年8月12日 - 1.0.0 发布了🎉🎉🎉</h3> 
<p style="text-align:left">项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmapper.mybatis.io%2F" target="_blank">https://mapper.mybatis.io</a></p> 
<h2 style="text-align:left">介绍</h2> 
<p style="text-align:left">这是一个不需要任何配置就可以直接使用的通用 Mapper，通过简单的学习就可以直接在项目中使用。</p> 
<h2 style="text-align:left">1.1 主要目标</h2> 
<p style="text-align:left">1. 开箱即用，无需任何配置，继承基类 Mapper 即可获得大量通用方法；<br> 2. 随心所欲，通过复制粘贴的方式可以组建自己的基类 Mapper；<br> 3. 全面贴心，提供 Service 层的封装方便业务使用和理解 Mapper；<br> 4. 简单直观，提供 ActiveRecord 模式，结合 Spring Boot 自动配置直接上手用；<br> 5. 自定义方法，简单几行代码即可实现自定义通用方法；<br> 6. 轻松扩展，通过 Java SPI 轻松扩展。</p> 
<h2 style="text-align:left">1.2 系统要求</h2> 
<p style="text-align:left">MyBatis Mapper 要求 MyBatis 最低版本为3.5.1，推荐使用最新版本。</p> 
<p style="text-align:left">和 MyBatis 框架一样，最低需要 Java 8。</p> 
<h2 style="text-align:left">1.3 安装</h2> 
<p style="text-align:left">如果你使用 Maven，在你的 pom.xml 添加下面的依赖：</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependencies</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>io.mybatis<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>mybatis-mapper<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.0.1<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
  <span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
  <span style="color:#6a737d"><!-- TODO 按需选择依赖 --></span>
  <span style="color:#6a737d"><!-- 使用 Service 层封装时 --></span>
  <span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>io.mybatis<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>mybatis-service<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.0.1<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
  <span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
  <span style="color:#6a737d"><!-- TODO 按需选择依赖 --></span>
  <span style="color:#6a737d"><!-- 使用 ActiveRecord 模式时 --></span>
  <span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>io.mybatis<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>mybatis-activerecord<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.0.1<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
  <span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependencies</span>></span></code></pre> 
<p style="text-align:left">如果使用 Gradle，在 `build.gradle` 中添加：</p> 
<pre style="text-align:left"><code class="language-groovy"><span style="color:#d73a49">dependencies</span> &#123;
    <span style="color:#d73a49">compile</span>(<span style="color:#032f62">"io.mybatis:mybatis-mapper:1.0.1"</span>)
    <span style="color:#6a737d">// 使用 Service 层封装时</span>
    <span style="color:#d73a49">compile</span>(<span style="color:#032f62">"io.mybatis:mybatis-service:1.0.1"</span>)
    <span style="color:#6a737d">// 使用 ActiveRecord 模式时</span>
    <span style="color:#d73a49">compile</span>(<span style="color:#032f62">"io.mybatis:mybatis-activerecord:1.0.1"</span>)
&#125;</code></pre> 
<h2 style="text-align:left">1.4 快速设置</h2> 
<p style="text-align:left">MyBatis Mapper 的基本原理是将实体类映射为数据库中的表和字段信息，因此实体类需要通过注解配置基本的元数据，配置好实体后，只需要创建一个继承基础接口的 Mapper 接口就可以开始使用了。</p> 
<h3 style="text-align:left">1.4.1 实体类配置</h3> 
<p style="text-align:left">假设有一个表：</p> 
<pre style="text-align:left"><code class="language-sql"><span style="color:#d73a49">create</span> <span style="color:#d73a49">table</span> <span style="color:#d73a49">user</span>
(
    <span style="color:#d73a49">id</span>   INTEGER <span style="color:#d73a49">GENERATED</span> <span style="color:#d73a49">BY</span> <span style="color:#d73a49">DEFAULT</span> <span style="color:#d73a49">AS</span> <span style="color:#d73a49">IDENTITY</span> (<span style="color:#d73a49">START</span> <span style="color:#d73a49">WITH</span> 1) PRIMARY <span style="color:#d73a49">KEY</span>,
    <span style="color:#d73a49">name</span> VARCHAR(32) <span style="color:#d73a49">DEFAULT</span> <span style="color:#032f62">'DEFAULT'</span>,
    sex  VARCHAR(2)
);</code></pre> 
<p style="text-align:left">对应的实体类：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#d73a49">import</span> io.mybatis.provider.Entity;

<span style="color:#6a737d">@Entity</span>.Table(<span style="color:#032f62">"user"</span>)
<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">User</span> &#123;
  <span style="color:#6a737d">@Entity</span>.Column(id = <span style="color:#005cc5">true</span>)
  <span style="color:#d73a49">private</span> Long   id;
  <span style="color:#6a737d">@Entity</span>.Column(<span style="color:#032f62">"name"</span>)
  <span style="color:#d73a49">private</span> String username;
  <span style="color:#6a737d">@Entity</span>.Column
  <span style="color:#d73a49">private</span> String sex;

  <span style="color:#6a737d">//省略set和get方法</span>
&#125;</code></pre> 
<p style="text-align:left">实体类上<strong>必须添加</strong>@Entity.Table注解指定实体类对应的表名，建议明确指定表名，不提供表名的时候，使用类名作为表名。所有属于表中列的字段，<strong>必须添加</strong>@Entity.Column注解，不指定列名时，使用字段名（不做任何转换），通过 id=true可以标记字段为主键。</p> 
<p style="text-align:left">@Entity中包含的这两个注解提供了大量的配置属性，想要使用更多的配置，参考 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmapper.mybatis.io%2Fdocs%2F3.entity.html" target="_blank">实体类注解</a> 中的内容，下面是一个简单示例：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d">@Entity</span>.Table(value = <span style="color:#032f62">"sys_user"</span>, remark = <span style="color:#032f62">"系统用户"</span>, autoResultMap = <span style="color:#005cc5">true</span>)
<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">User</span> &#123;
  <span style="color:#6a737d">@Entity</span>.Column(id = <span style="color:#005cc5">true</span>, remark = <span style="color:#032f62">"主键"</span>, updatable = <span style="color:#005cc5">false</span>, insertable = <span style="color:#005cc5">false</span>)
  <span style="color:#d73a49">private</span> Long   id;
  <span style="color:#6a737d">@Entity</span>.Column(value = <span style="color:#032f62">"name"</span>, remark = <span style="color:#032f62">"帐号"</span>)
  <span style="color:#d73a49">private</span> String userName;
  <span style="color:#6a737d">//省略其他</span>
&#125;</code></pre> 
<h3 style="text-align:left">1.4.2 Mapper接口定义</h3> 
<p style="text-align:left">有了 User实体后，直接创建一个继承了 Mapper 的接口即可：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#6a737d">//io.mybatis.mapper.Mapper</span>
<span style="color:#d73a49">public</span> <span style="color:#d73a49">interface</span> <span style="color:#6f42c1">UserMapper</span> <span style="color:#d73a49">extends</span> <span style="color:#6f42c1">Mapper</span><<span style="color:#6f42c1">User</span>, <span style="color:#6f42c1">Long</span>> &#123;
  
&#125;</code></pre> 
<p style="text-align:left">这个接口只要被 MyBatis 扫描到即可直接使用。</p> 
<p style="text-align:left">下面是几种常见的扫描配置：<br> <br> 1. MyBatis 自带的配置文件方式 mybatis-config.xml：</p> 
<pre style="text-align:left"><code class="language-xml"> <span style="color:#333333"><<span style="color:#22863a">mappers</span>></span>
   <span style="color:#6a737d"><!-- 扫描指定的包 --></span>
   <span style="color:#333333"><<span style="color:#22863a">package</span> <span style="color:#6f42c1">name</span>=<span style="color:#032f62">"com.example.mapper"</span>/></span>
 <span style="color:#333333"></<span style="color:#22863a">mappers</span>></span></code></pre> 
<p style="text-align:left">2. Spring 中的 spring.xml 配置：</p> 
<pre style="text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">bean</span> <span style="color:#6f42c1">class</span>=<span style="color:#032f62">"org.mybatis.spring.mapper.MapperScannerConfigurer"</span>></span>
  <span style="color:#333333"><<span style="color:#22863a">property</span> <span style="color:#6f42c1">name</span>=<span style="color:#032f62">"basePackage"</span> <span style="color:#6f42c1">value</span>=<span style="color:#032f62">"com.example.mapper"</span>/></span>
  <span style="color:#333333"><<span style="color:#22863a">property</span> <span style="color:#6f42c1">name</span>=<span style="color:#032f62">"markerInterface"</span> <span style="color:#6f42c1">value</span>=<span style="color:#032f62">"io.mybatis.service.mapper.RoleMarker"</span>/></span>
  <span style="color:#333333"><<span style="color:#22863a">property</span> <span style="color:#6f42c1">name</span>=<span style="color:#032f62">"sqlSessionFactoryBeanName"</span> <span style="color:#6f42c1">value</span>=<span style="color:#032f62">"sqlSessionFactoryRole"</span>/></span>
<span style="color:#333333"></<span style="color:#22863a">bean</span>></span></code></pre> 
<p style="text-align:left">3. Spring Boot 配置，启动类注解方式：</p> 
<pre style="text-align:left"><code class="language-java"><span style="color:#032f62">@MapperScan</span>(basePackages = <span style="color:#032f62">"com.example.mapper"</span>)
<span style="color:#032f62">@SpringBootApplication</span>
public class SpringBootDemoApplication &#123;

  <span style="color:#d73a49">public</span> <span style="color:#d73a49">static</span> <span style="color:#d73a49">void</span> <span style="color:#d73a49">main</span>(String[] args) &#123;
    <span style="color:#d73a49">SpringApplication</span><span style="color:#6f42c1">.run</span>(SpringBootDemoApplication.class, args);
  &#125;

&#125;</code></pre> 
<p style="text-align:left">Spring Boot 中，还可以直接给接口添加 @org.apache.ibatis.annotations.Mapper 注解，增加注解后可以省略 @MapperScan 配置。</p> 
<blockquote> 
 <p>可以注意到上面都是 MyBatis 自己的配置方式，新版 mybatis-mapper 本身不需要任何配置即可使用。</p> 
</blockquote> 
<h3 style="text-align:left">1.4.3 使用</h3> 
<p style="text-align:left">定义好接口后，就可以获取 UserMapper 使用，下面是简单示例：</p> 
<pre style="text-align:left"><code class="language-java">User user = <span style="color:#d73a49">new</span> User();
user.setUserName(<span style="color:#032f62">"测试"</span>);
userMapper.insert(user);
<span style="color:#6a737d">//保存后自增id回写，不为空</span>
Assert.assertNotNull(user.getId());
<span style="color:#6a737d">//根据id查询</span>
user = userMapper.selectByPrimaryKey(user.getId());
<span style="color:#6a737d">//删除</span>
Assert.assertEquals(1, userMapper.deleteByPrimaryKey(user.getId()));</code></pre> 
<p style="text-align:left">看到这里，可以发现除了 MyBatis 自身的配置外，MyBatis Mapper 只需要配置实体类注解，<br> 创建对应的 Mapper 接口就可以直接使用，没有任何繁琐的配置。</p> 
<p style="text-align:left">上面的示例只是简单的使用了 MyBatis Mapper，还有很多开箱即用的功能没有涉及，<br> 建议在上述示例运行成功后，继续查看本项目其他模块的详细文档，熟悉各部分文档后，<br> 在使用 MyBatis Mapper 时会更得心应手，随心所欲。</p> 
<p style="text-align:left">更多用法可以通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmapper.mybatis.io%2F" target="_blank">https://mapper.mybatis.io</a> 进行了解。</p> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Freleases%2F1.0.0.html%23%25E5%25BC%2580%25E5%258F%2591%25E8%25BF%2587%25E7%25A8%258B" target="_blank">#</a>开发过程</h3> 
<p style="text-align:start">2014年11月开源的 tk.mybatis.mapper 算得上是 MyBatis 的一个重要里程碑，从 <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fabel533%2FMapper" target="_blank">通用Mapper </a></strong>开始， MyBatis 有了真正意义上的通用 DAO 层，增删改查真的不用在手写或者自动生成，极大的方便了开发人员。</p> 
<p style="text-align:start">通用Mapper 经历过几次大的重构，每次都从底层使用新的思路重新实现，从第一个版本发布到2020年发布的 4.1.5 版本， 一直是兼容性升级，虽然底层变化了很多，集成方式有了变化，但是业务上集成的接口一直兼容。</p> 
<p style="text-align:start">虽然经历了几次大的重构，但是由于MyBatis内部的机制，导致无法以更方便更简洁的形式来实现通用Mapper， 从2018年就一直想要从根去解决这个问题，在 2019年3月份给 MyBatis 提交的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis%2Fmybatis-3%2Fpull%2F1391" target="_blank">pr#1391</a>合并后（对应 3.5.1 版本，最低要求版本）， 终于能以更简单的方式来实现通用 Mapper 了。</p> 
<p style="text-align:start">2019年实现过一版新的通用Mapper，但是感觉不够好。2020年本来是要写新一版的《MyBatis 从入门到精通》的， 写的过程中也在想着如何把通用Mapper结合到书中，在写书的过程中，逐渐形成了一个新的思路， 结果把目标从写书转移到了开源项目（不务正业），由于工作经常 996， 直到2020年底才基本完成新的实现。本来计划在2021年1月份发布正式版， 为了提供一个更灵活的代码生成器（Mybatis 的 MBG太死板，扩展麻烦）， 工作重心又转移到了代码生成器，最终实现了一个代码简单， 功能却异常强大的代码生成器 <code>睿Rui</code>（没开源，作为工具包含在当前项目中直接使用）， 此时又过去了好几个月，想着在2021年中发布正式版， 为了尝试在新版本中尽可能通过扩展 100% 兼容 tk-mapper，又增加了一些 SPI 扩展接口。 结果一直拖到了8月份。直到这个月才把 1.0.0 发布了。</p> 
<p style="text-align:start">整个项目从构思到最终发布经历了近3年的时间，虽然已经花了无数的时间， 但是仍然不能保证有不完美的地方，项目初期，大家发现BUG或者有任何想法都可以提 issues。</p> 
<h3 style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Freleases%2F1.0.0.html%23%25E4%25B8%25BA%25E4%25BB%2580%25E4%25B9%2588%25E6%2596%25B0%25E7%2589%2588%25E6%259C%25AC%25E6%2598%25AF-1-0-0" target="_blank">#</a>为什么新版本是 1.0.0？</h3> 
<p style="text-align:start">这是一个全新的版本的，采用了新的包名 <code>io.mybatis</code>，采用了全新的实现，核心代码是独立的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis-mapper%2Fprovider" target="_blank">mybatis-provider </a>项目，在此项目之上形成了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmybatis-mapper%2Fmapper" target="_blank">mybaits-mapper </a>，这个版本不需要任何配置（不会再因为配置出错），可以简单快速的集成并使用。</p> 
<p style="text-align:start">关于新版本的特点，建议通过 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flocalhost%3A8080%2Fdocs%2F1.getting-started.html" target="_blank">快速上手</a> 进行了解。</p> 
<p style="text-align:start"> </p> 
<h3 style="text-align:start">2021年8月16日 - 1.0.1 发布了🎉🎉🎉</h3> 
<ol> 
 <li> <p>核心项目 mybatis-provider 项目升级到 1.0.1，主要解决一个bug：</p> <p>当在注解 <code>@Entity.Table(value = "user_auto", autoResultMap = true)</code> 中使用 <code>autoResultMap = true</code>，默认把所有 <code>@SelectProvider</code> 方法的返回值设置为了自动生成的 <code><resultMap></code>，这会导致 <code>selectCount</code> 这种返回值不是实体类类型的查询出错，本次更新解决了这个问题。 同时直接使用 mybatis 的方式获取返回值类型，因此支持 mybatis 本身的注解设置返回值类型，例如 <code>@ResultType</code> 注解。</p> </li> 
 <li> <p>mybatis-mapper 项目升级为 1.0.1，主要解决了一个 <code>autoResultMap = true</code> 时相关的问题，当使用 <code><resultMap></code> 时， 其中的配置包含了数据库列 <code>column</code> 和 Java 对象属性名 <code>property</code> 的映射关系，因此在 select 查询时， 不需要通过 <code>column As property</code> 方式设置别名，在 <code>Example</code> 和 <code>Fn</code> 的实现中缺少对这种情况的处理， 本次更新已解决该问题。</p> </li> 
</ol>
                                        </div>
                                      
</div>
            