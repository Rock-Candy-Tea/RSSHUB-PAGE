
---
title: '京东猎户座发布开源，配置化一键生成 cms 系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img-blog.csdnimg.cn/20210416113710550.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3RpYW55YWxlaXhpYW93dQ==,size_16,color_FFFFFF,t_70'
author: 开源中国
comments: false
date: Fri, 16 Apr 2021 11:48:00 GMT
thumbnail: 'https://img-blog.csdnimg.cn/20210416113710550.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3RpYW55YWxlaXhpYW93dQ==,size_16,color_FFFFFF,t_70'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">猎户座核心配置化功能开源啦！<br> <br> 在降本提效的大环境下，猎户座系统为了扩展更多应用场景，近期完成了第一阶段的开源工作。此次开源的代码内容涉及两个代码库，内容为CCMS管理系统核心配置化功能以及包含表格列与表单项在内的常用组件。   </p> 
<ul> 
 <li style="text-align:start">配置化核心业务逻辑（<a href="https://gitee.com/jd-platform-opensource/ccms">开源地址</a>）</li> 
 <li style="text-align:start">UI实现代码库（<a href="https://gitee.com/jd-platform-opensource/ccms-antd">开源地址</a>） </li> 
</ul> 
<p style="text-align:start">希望通过开源吸引更多贡献者参与共建，完善对各类表单项、列表项的展示、校验需求的覆盖，促进产品的长期发展。收集Issue以及社区的反馈，不断优化功能的同时全面掌握用户诉求。<br> <br> <strong>开源介绍</strong></p> 
<p style="text-align:start"><strong>1、简介</strong></p> 
<p style="text-align:start">猎户座是一套完善、通用的可配置化中后台一站式解决平台,包含快速创建系统、可视化搭建、配置界面、权限控制等能力。本次开源内容为核心配置化功能（CCMS）,通过配置化自动生成中后台（CMS）界面，可将内容管理系统页面抽象为若干API进行流转,并对后台API的请求按照逻辑类型划分为表单提交、列表展示、查询数据等,通过JSON描述各API请求的接口信息以及常见校验和简单逻辑，动态渲染前端页面,最终实现零开发搭建内容管理系统。<br>  <br> <strong>2、特点</strong></p> 
<p style="text-align:start">通过配置文件自动生成CMS后台管理界面。  </p> 
<p style="text-align:start">1.核心配置化功能包含5种步骤，超过15种包含表格列与表单项在内的各种组件等内容。   <br> 2.通过组合式配置步骤。可覆盖16种以上不同中后台系统功能与页面交互形式。   <br> 3.规范：面向对象的方式对基类统一管理；项目目录与代码统一标准化、规范化。   <br> 4.文档：提供了完善的使用文档（https://oriondoc.jd.com/)，便于开发者参与贡献与快速使用。   <br> 5.质量：核心组件的单元测试覆盖率达到100%，确保核心组件的开发质量。<br> <br> <strong>3、架构</strong></p> 
<p style="text-align:start">1）整体架构</p> 
<p style="text-align:start">基于猎户座接入的业务应用场景，以用户为中心，进行调研，收集实际的业务需求，扩展项目的功能。主要目的是让产品配置更灵活、更便捷、易上手、功能覆盖更全面。我们首先对整体架构进行分层。下图是开源代码的整体架构思路</p> 
<p style="text-align:start"><img src="https://img-blog.csdnimg.cn/20210416113710550.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3RpYW55YWxlaXhpYW93dQ==,size_16,color_FFFFFF,t_70" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">2）组件设计</p> 
<p style="text-align:start">以面向对象的方式在基类实现业务逻辑，通过继承基类实现UI的快速切换和接入。</p> 
<p style="text-align:start"><img src="https://img-blog.csdnimg.cn/img_convert/591493e3c037baf8fc8d816ce94f8f2c.png" referrerpolicy="no-referrer"><br>  <br> 3）数据流转</p> 
<p style="text-align:start">每个页面步骤提供对输入、输出数据的传输与存储，在不同页面步骤中实现各自的业务逻辑。最终在页面中通过对步骤排列组合实现完整的业务功能。</p> 
<p style="text-align:start"><img src="https://img-blog.csdnimg.cn/img_convert/3b449a690d1a75fde77284b371a34ea4.png" referrerpolicy="no-referrer"><br>  <br> 4)无缝对接外部系统</p> 
<p style="text-align:start">以中间件的形式抽离权限配置，配置文件存储，UI框架等模块实现在不同系统间的快速切换。</p> 
<p style="text-align:start"><img src="https://img-blog.csdnimg.cn/img_convert/7d8543cd95efb7bb81503342cf8deaf1.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>4、接入与使用</strong></p> 
<p style="text-align:start">完整demo可参照（http://coding.jd.com/publicdemo/ccms-demo/）   </p> 
<p style="text-align:start">快速使用：安装<code>ccms</code> 和<code>ccms-antd</code>   npm install ccms-antd ccms   在项目中引入和及配置</p> 
<pre><code>import &#123; CCMS &#125; from 'ccms-antd';
 
const App = () => (
<>
  <CCMS
   checkPageAuth=&#123;async () => true&#125;
   loadPageURL=&#123;async (id) => `/url?id=$&#123;id&#125;&type=page`&#125;
   loadPageFrameURL=&#123;async (id) => `/url?id=$&#123;id&#125;&type=open`&#125;
   // 界面操作更新CCMS config
   loadPageConfig=&#123;async (page) => newConfig &#125;
   sourceData=&#123;&#123;&#125;&#125;
   callback=&#123;() => &#123;
    if (window.history.length > 1) &#123;
     window.history.back()
    &#125; else &#123;
     window.close()
    &#125;
   &#125;&#125;
   //config的demo 详见api文档
   config=&#123;config&#125;
  />
</>
);
</code></pre> 
<p><span style="background-color:#ffffff; color:#555555">——  京东零售-平台业务中心-平台业务研发部-基础业务研发部  ——</span></p>
                                        </div>
                                      
</div>
            