
---
title: 'Rust 开发的应用软件管理后台 chimes-rust v0.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4011'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 10:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4011'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"> chimes-rust 这是一款使用rust进行开发实现的应用后端管理系统，类似目前大多数的基于Java的管理后端。它旨在帮助大家能够快速的使用rust来进行后台应用的开发。Rust还是比较合适业务应用的开发的，特别是对突发性用户增长的情况。相比Java来说，Rust有近3倍的语言级的性能提升，开发过程也比C/C++简单。</p> 
<p style="margin-left:0px; margin-right:0px; text-align:left"><strong>软件仓库：</strong> <a href="https://gitee.com/poethxp/chimes-rust.git">https://gitee.com/poethxp/chimes-rust.git</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Chimes-Rust是使用Rust实现的应用后台管理程序，项目中提供了一个基于eladmin最新版前端的修改版，但经过少量修改实现，主要修改是api路径的，以及表格或表单的字段绑定（因为rust的命名规范的要求进行了一些字段的修改）。 Chimes-rust，主要是实现了eladmin中的系统管理功能，以及登录和用户中心。对于其它部分的功能，可能会在后续的版本中进行实现。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">软件架构</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Chimes-rust采用actix-web作为基础的WEB框架进行开发，而在ORM方面采用了Rbatis，目前暂时没有使用Redis来缓存相应的数据。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">重点组件</h4> 
<ol> 
 <li>actix-web</li> 
 <li>rbatis</li> 
 <li>chimes-auth，基于actix-web的MiddleWare提供的权限管控的功能。</li> 
 <li>jsonwebtoken</li> 
 <li>rbatis-generator，这是另一个开源的用于生成rbatis为基础的rust源码</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">特别说明</h4> 
<ol> 
 <li>关于el-admin前端，本应用不是为了提供更好的el-admin的前端，所做的修改都是为了与后台进行对接，所以是尽可能少的修改它。同时，在此特别感谢eladmin的作者，他为应用提供了一个功能丰富的管理前端。</li> 
 <li>chimes-rust的大部分后端代码是采用rbatis-generator进行生成的，基本上达到85%。如对该项目感兴趣的，可以进仓库：<a href="https://gitee.com/poethxp/rbatis-generator">https://gitee.com/poethxp/rbatis-generator</a><span> </span>看看。</li> 
</ol> 
<h4 style="margin-left:0; margin-right:0; text-align:left">安装教程</h4> 
<ol> 
 <li>创建数据chimesrust，并导入数据 sql/chimesrust.sql；</li> 
 <li>编译 backend/chimes-rust，可以进入该目录后，直接执行cargo r</li> 
 <li>打包前端 frontend/eladmin-web</li> 
 <li>后端的一些配置可以修秘诀backend/chimes-rust/conf/app.yml</li> 
</ol>
                                        </div>
                                      
</div>
            