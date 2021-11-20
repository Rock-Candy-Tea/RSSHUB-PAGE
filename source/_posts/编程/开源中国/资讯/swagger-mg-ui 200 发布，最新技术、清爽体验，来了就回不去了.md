
---
title: 'swagger-mg-ui 2.0.0 发布，最新技术、清爽体验，来了就回不去了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-60fd1aca723538fcda57ed295f6c97a339e.png'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 18:05:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-60fd1aca723538fcda57ed295f6c97a339e.png'
---

<div>   
<div class="content">
                                                                                            <p>swagger-mg-ui是swagger的一个前端实现，使用简单、解析速度快、走心的设计，给你带来不一样的体验！</p> 
<p><strong>为何要重复造轮子呢？</strong></p> 
<p><strong>1. 现有UI还不够好，我觉得我能做个更好的</strong></p> 
<p>官方的UI：功能全面，基本上把已有的特性都支持了，但文档查看不够友好，不支持搜索，一次性全部渲染，接口太多的时候解析速度很慢，源码云里雾里，基本看不懂也改不动。</p> 
<p>其他UI：前端技术老旧，还有很多一看界面和源码就知道是后端人员写的，模块不清晰，代码冗余，代码量奇高，界面看上去有一种没规划、拉垮的感觉。</p> 
<p>本项目1.x是用jQuery开发的，学会了Vue之后就没动力维护了，于是使用 Vue3 + Ant-design-vue 重构出了2.x版本，重构后感觉神清气爽。新版本的代码每一行都是新敲出来的，解析速度更快，逻辑更清晰，代码更简洁，界面更清爽。</p> 
<p><strong>2. 有用户有这种仅需要引入一个好看UI的需求</strong></p> 
<p><strong>3. 新技术总是如此的吸引人，想去体验一番</strong></p> 
<p><strong>说明</strong></p> 
<p>2.x版本仅为一个UI前端，无任何后端代码，用以满足只想要一个好看的UI为目的单项目使用，无任何心智负担的引入和使用。</p> 
<p>本项目为zyplayer-doc项目Swagger模块前端的精简版，有任何问题都可统一提给<a href="https://gitee.com/zyplayer/zyplayer-doc">zyplayer-doc</a>项目，将同步升级至本项目，zyplayer-doc能提供更强大的统一文档管理功能，欢迎前往了解。</p> 
<p>开源地址：<a href="https://gitee.com/zyplayer/swagger-mg-ui">https://gitee.com/zyplayer/swagger-mg-ui</a></p> 
<p><strong>本次更新内容</strong></p> 
<p>使用 Vue3 + Ant-design-vue 完全重构了一个新UI</p> 
<p><strong>使用方法</strong></p> 
<p>1. pom引入maven依赖</p> 
<pre><code class="language-xml"><!-- https://mvnrepository.com/artifact/com.zyplayer/swagger-mg-ui -->
<dependency>
    <groupId>com.zyplayer</groupId>
    <artifactId>swagger-mg-ui</artifactId>
    <version>2.0.0</version>
</dependency></code></pre> 
<p>也可clone源码后自行 mvn install 到本地或 mvn deploy 到自己的maven仓库</p> 
<p>2. 启动项目后访问：http://localhost:8080/document.html，即项目地址+document.html</p> 
<p>新东西可能有一些不完善的地方，欢迎提交issues，将会很快解决所有问题。</p> 
<p><strong>界面截图</strong></p> 
<p><img height="929" src="https://oscimg.oschina.net/oscnet/up-60fd1aca723538fcda57ed295f6c97a339e.png" width="1914" referrerpolicy="no-referrer"></p> 
<p><img height="1078" src="https://oscimg.oschina.net/oscnet/up-7af58ab17ee20fa71d92d1d18088f48f2c2.png" width="1917" referrerpolicy="no-referrer"></p> 
<p><img height="1078" src="https://oscimg.oschina.net/oscnet/up-ce201eda54bbcf89458c35498f2167ea8f9.png" width="1917" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            