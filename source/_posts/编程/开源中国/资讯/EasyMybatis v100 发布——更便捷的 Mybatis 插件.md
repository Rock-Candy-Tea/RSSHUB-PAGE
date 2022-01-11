
---
title: 'EasyMybatis v1.0.0 发布——更便捷的 Mybatis 插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1923'
author: 开源中国
comments: false
date: Mon, 10 Jan 2022 22:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1923'
---

<div>   
<div class="content">
                                                                                            <p><code>easy-mybatis</code>是一个对<code>Mybatis</code>的增强框架（插件）。在<code>Spring</code>集成<code>Mybatis</code>的基础上，将项目开发中对数据库的常用操作统一化。使用本框架可以很便捷的对数据库进行操作，提高开发效率，减少机械行为。</p> 
<hr> 
<h1>框架初衷</h1> 
<blockquote> 
 <p>这个框架的初衷是，减少Java程序员千篇一律的数据库操作。</p> 
</blockquote> 
<p>对于开发人员来说：</p> 
<ul> 
 <li>精力应该花费在业务逻辑上，而非机械式的“技术”上。</li> 
 <li>项目中减少无关痛痒的代码，从抽象的角度看实现。</li> 
 <li>各司其职，各劳其力，追求项目角度的服务流水线。</li> 
</ul> 
<h2>服务分离的时代</h2> 
<p>如今已很难看到单体架构的项目（感兴趣的可以查看我对架构演变的描述<a href="https://my.oschina.net/zuoyuip/blog/3190947">《浅谈微服务》</a>），目前的项目大都是通过<code>RESTful</code>、<code>MQ</code>、<code>Socket</code>的方式（协议）进行数据传输。</p> 
<p>这让我开始质疑传统<code>JavaWeb</code>项目中的数据库操作模式——即<code>Model(DTO)</code>存在的意义。理论上，数据库设计是不可能完全遵循视图模型的，这就导致“正确”的做法是在项目中引入<code>VO</code>，由多个<code>DTO</code>来组装。</p> 
<p><strong>那么，为什么不能用灵活的Map来替代呢？</strong></p> 
<p>对一个<code>Map</code>的方法进行拓展，增加其对<code>Json</code>的解析能力，那么是不是就可以摆脱<code>POJO</code>的各种麻烦组装。</p> 
<h2>思考框架设计</h2> 
<p>我在思考如何设计这个框架的时候，被需要考虑的方方面面给阻挡住了。</p> 
<p>因为一个数据库框架需要考虑的东西实在太多了，比如：</p> 
<ol> 
 <li>事务机制</li> 
 <li>类型转换</li> 
 <li>会话管理</li> 
</ol> 
<p>···</p> 
<p>思来想去，发现自己方向跑偏了，我只是希望<strong>统一数据库操作的接口</strong> + <strong>摆脱Model</strong>，没必要重新平地起墙，完全可以在一个现有的框架基础上进行封装。</p> 
<p>那么，对这个现有框架的选择就尤为重要了。</p> 
<h2>现有框架的选择</h2> 
<p>目前Java中主流的数据库操作框架：</p> 
<ul> 
 <li>Spring JDBC</li> 
 <li>Spring Data JPA</li> 
 <li>Mybatis</li> 
 <li>Hibernate</li> 
</ul> 
<p>选择现有框架有一个原则——“<strong>统一数据库操作的接口</strong> + <strong>摆脱Model</strong>”是对该框架的加强，而非变异；不能因为“<strong>统一数据库操作的接口</strong> + <strong>摆脱Model</strong>”而无法使用原框架的部分功能。</p> 
<p>“<strong>摆脱Model</strong>”这个特点，首先就要排除重度<code>ORM</code>框架，也就是支持<code>JPA</code>操作的数据库——<code>Spring Data JPA</code>、<code>Hibernate</code>；原因很简单，这两个框架的强大之处恰恰就在它完全面向<code>Model</code>操作。</p> 
<p>剩下的就只有两个框架了，<code>Spring JDBC</code>和<code>Mybatis</code>。其中，<code>Spring JDBC</code>留给了开发人员大量的可操作空间，更加自由，但恰恰是这种自由使得它更加繁琐。而<code>Mybatis</code>是一个轻量<code>ORM</code>框架，准确来说<code>Mybatis</code>不能称为<code>ORM</code>框架，因为它并不是面向<code>Model</code>操作数据库，仅仅是将数据库字段与<code>Model</code>字段互相赋值，并没有做到<code>ORM</code>定义的关系映射。</p> 
<h2>抉择</h2> 
<p>由以上各框架的特点，结合国内Java语言中数据库操作框架的热度，毫无疑问的选择了<code>Mybatis</code>。</p> 
<p>考虑到<code>SpringBoot</code>对<code>Mybatis</code>优秀的支持级别，我决定基于<code>mybatis-spring-boot-starter</code>开发这款框架，准备来说应该称其为“<strong>插件</strong>”。</p> 
<h1>框架特性</h1> 
<ul> 
 <li><strong>更便捷</strong></li> 
</ul> 
<p>摒弃传统<code>mybatis</code>的<code>model</code>、<code>xml</code>、<code>dao</code>数据库操作模式，避繁就简，快速开发。</p> 
<ul> 
 <li><strong>更高效</strong></li> 
</ul> 
<p>采用预编译<code>SQL</code>，拒绝运行期间反射生成<code>SQL</code>，性能更高效。</p> 
<ul> 
 <li><strong>无侵入</strong></li> 
</ul> 
<p>只是对Mybatis-Spring的增强插件，对已有工程不做任何修改，仍可使用原生框架的功能，仅仅是简化了开发阶段对数据库的操作。</p> 
<ul> 
 <li><strong>统一操作接口</strong></li> 
</ul> 
<p>对数据库的所有操作共用一个接口，降低使用门槛，轻松操作数据库。</p> 
<ul> 
 <li><strong>统一操作对象</strong></li> 
</ul> 
<p>使用<code>JsonObject</code>为数据对象，提供一系列操作方法，方便从持久化对象组装为视图对象。</p> 
<ul> 
 <li><strong>易上手</strong></li> 
</ul> 
<p>整个框架只提供了一个接口、一个注解、两个对象，仅仅一行配置便可完成对数据库进行常用操作。</p> 
<ul> 
 <li>...</li> 
</ul> 
<h2>安利</h2> 
<ul> 
 <li> <p>在<code>mybatis-spring-boot</code>环境下，使用该框架（插件），可以减少传统<code>Mybatis</code>使用中对<code>model</code>、<code>xml</code>、<code>dao</code>的机械式开发。</p> </li> 
 <li> <p>所有的数据库操作均使用<code>MapperRepository</code>接口，通过注解<code>@Magic("xxx")</code>标记接口的数据表归属，即可直接使用。</p> </li> 
 <li> <p>该框架（插件）不妨碍同时使用传统<code>Mybatis</code>中<code>model</code>、<code>xml</code>、<code>dao</code>的数据库开发方式。</p> </li> 
</ul> 
<h1>快速上手</h1> 
<h2>安装</h2> 
<ul> 
 <li><strong>安装<code>mybatis-spring-boot</code>环境</strong></li> 
</ul> 
<p>mybatis-spring-boot的Maven依赖</p> 
<pre><code class="language-xml">    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>$&#123;spring-boot.version&#125;</version>
        <relativePath/>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>$&#123;mybatis-spring-boot.version&#125;</version>
        </dependency>
    </dependencies>
</code></pre> 
<p>mybatis-spring-boot的Gradle依赖</p> 
<pre><code class="language-groovy">    plugins &#123;
    id 'org.springframework.boot' version '$&#123;springBootVersion&#125;'
    id 'io.spring.dependency-management' version '$&#123;springManagementVersion&#125;'
    id 'java'
    &#125;

    dependencies &#123;
    implementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter:$&#123;mybatisSpringVersion&#125;'
    &#125;
</code></pre> 
<ul> 
 <li><strong>安装本框架（插件）</strong></li> 
</ul> 
<p>Maven依赖引入</p> 
<pre><code class="language-xml">
<!-- https://mvnrepository.com/artifact/top.zuoyu.mybatis/easy-mybatis-spring-boot-starter -->
<dependency>
    <groupId>top.zuoyu.mybatis</groupId>
    <artifactId>easy-mybatis-spring-boot-starter</artifactId>
    <version>1.0.0</version>
</dependency>

</code></pre> 
<p>Gradle依赖引入</p> 
<pre><code class="language-groovy">
// https://mvnrepository.com/artifact/top.zuoyu.mybatis/easy-mybatis-spring-boot-starter
implementation 'top.zuoyu.mybatis:easy-mybatis-spring-boot-starter:1.0.0'

</code></pre> 
<h2>配置</h2> 
<blockquote> 
 <p>这里以<code>MySQL</code>数据库为例，<code>Oracle</code>数据库配置请参考<strong>配置说明</strong></p> 
</blockquote> 
<ol> 
 <li><strong>配置<code>spring-boot-jdbc</code>数据库</strong></li> 
</ol> 
<pre><code class="language-yaml">
spring:
  datasource:
    type: com.zaxxer.hikari.HikariDataSource
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://172.0.0.1:3306/xxxx
    username: xxxx
    password: xxxx

</code></pre> 
<p>关于<code>springBoot</code>的配置，这里不多赘述，更多移步<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot" target="_blank">springBoot官网</a>。</p> 
<ol start="2"> 
 <li><strong>配置<code>easy-mybatis</code>支持的表名（例子）</strong></li> 
</ol> 
<pre><code class="language-yaml">
easy-mybatis:
  table-names: teacher, student

</code></pre> 
<p>这里的<code>table-names</code>配置，表示需要<code>easy-mybatis</code>框架支持的数据表名，多个表名使用逗号隔开。</p> 
<p>即可使用<code>easy-mybatis</code>框架操作<code>teacher</code>和<code>student</code>两个数据表，<strong>如果需要支持其他数据表，需要在此配置</strong>。</p> 
<h2>操作数据库（例子）</h2> 
<pre><code class="language-java">
@SpringBootTest
class DemoApplicationTests &#123;

    // 表示该接口用来操作名称为'teacher'的数据表
    @Magic("teacher")
    private MapperRepository teacherRepository;

    // 表示该接口用来操作名称为'student'的数据表
    @Magic("student")
    private MapperRepository studentRepository;


    // 查询teacher表下所有数据
    @Test
    void teacherTest() &#123;
        teachertRepository.selectList().forEach(System.out::println);
    &#125;

    // 查询student表下符合特定条件的数据
    @Test
    void studentTest() &#123;
        studentRepository.selectListByExample(
          new JsonObject().put("birthday", "2009/12/12 12:12:12")
          ).forEach(System.out::println);
    &#125;

&#125;

</code></pre> 
<p>使用<code>MapperRepository</code>接口对数据库进行操作，需要使用<code>@Magic("表名称")</code>标记该接口的数据表归属。</p> 
<p>在本例中，<code>@Magic("teacher")</code>表示该<code>MapperRepository</code>为<code>"teacher"</code>数据表的操作接口，可以通过<code>teacherRepository</code>调用一系列方法完成对<code>"teacher"</code>数据表的操作。</p> 
<hr> 
<h1>相关链接</h1> 
<p>easy-mybatis的详细介绍：<a href="https://www.oschina.net/p/easy-mybatis">点击查看</a></p> 
<p>easy-mybatis的下载地址：<a href="https://gitee.com/zuoyuip/easy-mybatis">点击下载</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmybatis.zuoyu.top" target="_blank">项目主页</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmybatis.zuoyu.top" target="_blank">https://mybatis.zuoyu.top</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmybatis.zuoyu.top%2Fdoc%2Findex.html" target="_blank">API文档地址</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmybatis.zuoyu.top%2Fdoc%2Findex.html" target="_blank">https://mybatis.zuoyu.top/doc/index.html</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuoyuip%2Feasy-mybatis" target="_blank">GitHub地址</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzuoyuip%2Feasy-mybatis" target="_blank">https://github.com/zuoyuip/easy-mybatis</a></p> 
<p><a href="https://gitee.com/zuoyuip/easy-mybatis">Gitee地址</a>：<a href="https://gitee.com/zuoyuip/easy-mybatis">https://gitee.com/zuoyuip/easy-mybatis</a></p>
                                        </div>
                                      
</div>
            