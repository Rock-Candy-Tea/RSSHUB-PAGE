
---
title: 'SpringBoot 使用JestClient操作Elasticsearch'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<h2>1.Jest介绍</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1848" data-height="756"><img data-original-src="//upload-images.jianshu.io/upload_images/9953332-a562ee94db6419a5" data-original-width="1848" data-original-height="756" data-original-format="image/png" data-original-filesize="290039" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>操作Elasticsearch的客户端有很多，SpringBoot也提供了方式去操作，这里介绍另外一种方式去使用Elasticsearch --- <strong>JestClient</strong></p>
<p>JestClient是一款基于HTTP方式操作的Elasticsearch的客户端，支持同步和异步操作，同时也可以结合ElasticSearch的依赖进行操作Elasticsearch。</p>
<p>支持多个版本的Elasticsearch，如下：</p>
<table>
<thead>
<tr>
<th>Jest Version</th>
<th>Elasticsearch Version</th>
</tr>
</thead>
<tbody>
<tr>
<td>>= 6.0.0</td>
<td>6</td>
</tr>
<tr>
<td>>= 5.0.0</td>
<td>5</td>
</tr>
<tr>
<td>>= 2.0.0</td>
<td>2</td>
</tr>
<tr>
<td>0.1.0 - 1.0.0</td>
<td>1</td>
</tr>
<tr>
<td><= 0.0.6</td>
<td>< 1</td>
</tr>
</tbody>
</table>
<p>更多信息可以查看github，地址是：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fsearchbox-io%2FJest" target="_blank">https://github.com/searchbox-io/Jest</a></p>
<h2>2.SpringBoot整合JestClient</h2>
<p>接下来介绍如何在SpringBoot中使用JestClient操作Elasticsearch。</p>
<h3>2.1 前置工作</h3>
<p>首先启动Elasticsearch，我这里是在本地启动的Elasticsearch，版本是6.8.2，为了方便查看数据，这里使用Elasticsearch-Head插件，如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2860" data-height="654"><img data-original-src="//upload-images.jianshu.io/upload_images/9953332-2786a24b93cab0db" data-original-width="2860" data-original-height="654" data-original-format="image/png" data-original-filesize="165267" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<h3>2.2 添加Jest依赖</h3>
<p>创建项目，在pom文件中加入Jest依赖（这里根据上面版本对应添加依赖），这里额外添加量了elasticsearch和lombok为了方便操作，如下：</p>
<pre><code><?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.dalaoyang</groupId>
    <artifactId>springboot_jestclient</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot_jestclient</name>
    <description>springboot_jestclient</description>

    <properties>
        <java.version>1.8</java.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <spring-boot.version>2.2.6.RELEASE</spring-boot.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>io.searchbox</groupId>
            <artifactId>jest</artifactId>
            <version>6.3.1</version>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.16.10</version>
        </dependency>

        <dependency>
            <groupId>org.elasticsearch</groupId>
            <artifactId>elasticsearch</artifactId>
            <version>6.8.2</version>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>$&#123;spring-boot.version&#125;</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.2.6.RELEASE</version>
            </plugin>
        </plugins>
    </build>

</project>
</code></pre>
<h3>2.3 配置文件</h3>
<p>在配置文件中添加elasticsearch相关配置，其中uris配置Elasticsearch的HTTP端口，如本文添加的配置：</p>
<pre><code>spring.application.name=springboot_jestclient
# 应用服务web访问端口
server.port=8888

spring.elasticsearch.rest.uris=http://localhost:9200
spring.elasticsearch.jest.username=elastic
spring.elasticsearch.jest.password=elastic
</code></pre>
<p>到这里其实已经整合完成了，是不是非常简单？</p>
<h2>3.Elasticsearch基本操作</h2>
<p>接下介绍如何操作Elasticsearch，这里分别介绍如下几部分内容：</p>
<ul>
<li>索引文档</li>
<li>索引类操作</li>
<li>文档类操作</li>
<li>查询操作</li>
</ul>
<h3>3.1 文档实体</h3>
<p>这里创建一个Book文档做为示例，其中@JestId为文档id，即Elasticsearch中的_id字段，本文BookDocument内容如下：</p>
<pre><code>package com.dalaoyang.document;

import io.searchbox.annotations.JestId;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class BookDocument &#123;

    @JestId
    private String id;
    private String bookName;
    private String bookAuthor;
    private Integer pages;
    private String desc;
&#125;
</code></pre>
<p>为了方便操作，这里创建了一个request对象进行操作，如下：</p>
<pre><code>package com.dalaoyang.model;

import com.dalaoyang.document.BookDocument;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class BookRequest &#123;

    //删除文档用
    private String id;
    //查询用
    private String keyword;
    private String indexName;
    private String typeName;
    //新增文档用
    private BookDocument body;
&#125;

</code></pre>
<p>在使用相关操作时，其实都是通过io.searchbox.client.JestClient#execute来进行操作（需要注意，这里没有对JestClient进行配置，只是使用的默认的配置），将对应动作当做参数传入，接下来介绍几个常用的动作。</p>
<h3>3.2 索引类操作</h3>
<p>结合MySQL来看的话，索引可以理解为一个数据库，索引相关的操作可能不是很多，这里介绍相对比较常用的是创建索引和删除索引，如下：</p>
<h4>3.2.1 创建索引</h4>
<pre><code>CreateIndex createIndex = new CreateIndex.Builder(indexName).build();
</code></pre>
<h4>3.2.2 删除索引</h4>
<pre><code>DeleteIndex deleteIndex = new DeleteIndex.Builder(indexName).build();
</code></pre>
<p>通过上面两个操作可以看到，都是通过使用对应的Index实体来操作对应实体，当然还有一些不是很常用的，如果有需要可以查看相关文档进行使用，这里不一一介绍了，完整s示例内容如下：</p>
<pre><code>package com.dalaoyang.web;

import io.searchbox.client.JestClient;
import io.searchbox.client.JestResult;
import io.searchbox.indices.CreateIndex;
import io.searchbox.indices.DeleteIndex;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class IndexController &#123;

    @Autowired
    private JestClient jestClient;

    @GetMapping("createIndex")
    public String createIndex(String indexName) throws Exception&#123;
        CreateIndex createIndex = new CreateIndex.Builder(indexName).build();
        JestResult result = jestClient.execute(createIndex);
        return result.getJsonString();
    &#125;

    @GetMapping("deleteIndex")
    public String deleteIndex(String indexName) throws Exception&#123;
        DeleteIndex deleteIndex = new DeleteIndex.Builder(indexName).build();
        JestResult result = jestClient.execute(deleteIndex);
        return result.getJsonString();
    &#125;
&#125;

</code></pre>
<h3>3.3 文档类操作</h3>
<p>文档相当于MySQL中的行记录，也就是说一条数据，由于新增和修改在同一个方法内，所以这里也是对新增（和修改）和删除方法进行介绍，如下：</p>
<h4>3.3.1 新增或修改文档</h4>
<p>首先会判断索引是否存在，不存在的话会根据索引文档进行创建索引，然后进行新增或修改操作，如果没有指定id的话（上文说的注解@JestId字段），会自动生成一个id。</p>
<pre><code>Index.Builder builder = new Index.Builder(bookRequest.getBody());
Index index = builder.index(bookRequest.getIndexName()).type(bookRequest.getTypeName()).build();
</code></pre>
<p>这里使用新增文档创建三条数据方便后面查询，如下:</p>
<pre><code>&#123;
    "indexName": "book",
    "typeName": "book",
    "body": &#123;"id":"test0001","bookName":"数学书","bookAuthor":"复旦大学","pages":100,"desc":"复旦大学的数学书"&#125;
&#125;
</code></pre>
<pre><code>&#123;
    "indexName": "book",
    "typeName": "book",
    "body": &#123;"id":"test0003","bookName":"语文书","bookAuthor":"北京大学","pages":100,"desc":"北京大学的语文书"&#125;
&#125;
</code></pre>
<pre><code>&#123;
    "indexName": "book",
    "typeName": "book",
    "body": &#123;"id":"test0003","bookName":"英文书","bookAuthor":"清华大学","pages":200,"desc":"清华大学的英文书"&#125;
&#125;
</code></pre>
<h4>3.3.2 删除文档(根据id)</h4>
<pre><code>Delete index = new Delete.Builder(bookRequest.getId()).index(bookRequest.getIndexName()).type(bookRequest.getTypeName()).build();
</code></pre>
<p>完整示例内容如下：</p>
<pre><code>package com.dalaoyang.web;

import com.dalaoyang.model.BookRequest;
import io.searchbox.client.JestClient;
import io.searchbox.client.JestResult;
import io.searchbox.core.Delete;
import io.searchbox.core.Index;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class DocumentController &#123;

    @Autowired
    private JestClient jestClient;

    @PostMapping("saveOrUpdateDocument")
    public String saveOrUpdateDocument(@RequestBody BookRequest bookRequest) throws Exception&#123;
        Index.Builder builder = new Index.Builder(bookRequest.getBody());
        Index index = builder.index(bookRequest.getIndexName()).type(bookRequest.getTypeName()).build();
        JestResult result = jestClient.execute(index);
        return result.getJsonString();
    &#125;

    @PostMapping("deleteDocumentById")
    public String deleteDocumentById(@RequestBody BookRequest bookRequest) throws Exception&#123;
        Delete index = new Delete.Builder(bookRequest.getId()).index(bookRequest.getIndexName()).type(bookRequest.getTypeName()).build();
        JestResult result = jestClient.execute(index);
        return result.getJsonString();
    &#125;
&#125;

</code></pre>
<h3>3.4 查询操作</h3>
<p>查询操作可能是对Elasticsearch最需要使用的场景，这里举一个简单的场景，输入关键字，查询对应book文档，关键字匹配（bookName，bookAuthor，desc）三个字段，这里结合Elasticsearch官方依赖进行操作，完整示例如下：</p>
<pre><code>
package com.dalaoyang.web;

import com.dalaoyang.model.BookRequest;
import io.searchbox.client.JestClient;
import io.searchbox.core.Search;
import io.searchbox.core.SearchResult;
import lombok.extern.slf4j.Slf4j;
import org.elasticsearch.index.query.MultiMatchQueryBuilder;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Slf4j
public class QueryController &#123;

    @Autowired
    private JestClient jestClient;

    @PostMapping("search")
    public String search(@RequestBody BookRequest bookRequest) throws Exception&#123;
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        searchSourceBuilder.query(new MultiMatchQueryBuilder(bookRequest.getKeyword(), "bookName","bookAuthor","desc"));
        log.info(searchSourceBuilder.toString());
        SearchResult result = jestClient.execute(new Search.Builder(searchSourceBuilder.toString())
                .addIndex(bookRequest.getIndexName())
                .addType(bookRequest.getTypeName())
                .build());
        return result.getJsonString();
    &#125;
&#125;

</code></pre>
<p>比如这里搜索清华，这里我打印了一下查询语句，如下：</p>
<pre><code>&#123;
    "query":&#123;
        "multi_match":&#123;
            "query":"清华",
            "fields":[
                "bookAuthor^1.0",
                "bookName^1.0",
                "desc^1.0"
            ],
            "type":"best_fields",
            "operator":"OR",
            "slop":0,
            "prefix_length":0,
            "max_expansions":50,
            "zero_terms_query":"NONE",
            "auto_generate_synonyms_phrase_query":true,
            "fuzzy_transpositions":true,
            "boost":1
        &#125;
    &#125;
&#125;
</code></pre>
<p>查询的结构只有一条，与在Elasticsearch-Head中查询一致，如图</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2868" data-height="1250"><img data-original-src="//upload-images.jianshu.io/upload_images/9953332-1f90f70ea0ebbe2f" data-original-width="2868" data-original-height="1250" data-original-format="image/png" data-original-filesize="377953" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<h2>4.一些建议</h2>
<p>相关操作Elasticsearch的客户端有很多，这里就不做相关对比了，JestClient本人也在真实上线项目中使用过，这里只是在使用过几种的前提下做出几点建议：</p>
<ul>
<li>Elastic官方已经开始建议使用HTTP方式去操作Elasticsearch了</li>
<li>当初选择这种的原因是考虑到更好的去扩展版本，封装响应的操作类可以兼容更多的版本。</li>
<li>在高版本的Elasticsearch中，有一些文档类型的内容被单独抽离出来了，比如父子文档。</li>
</ul>
<h2>5.源码</h2>
<p>源码地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgitee.com%2Fdalaoyang%2Fspringboot_learn%2Ftree%2Fmaster%2Fspringboot_jestclient" target="_blank">https://gitee.com/dalaoyang/springboot_learn/tree/master/springboot_jestclient</a></p>
  
</div>
            