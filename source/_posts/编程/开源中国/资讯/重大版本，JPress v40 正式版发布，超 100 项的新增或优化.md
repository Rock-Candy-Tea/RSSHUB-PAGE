
---
title: '重大版本，JPress v4.0 正式版发布，超 100 项的新增或优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-db94afbeb9078ac1af7bba07540f6e02011.png'
author: 开源中国
comments: false
date: Fri, 04 Jun 2021 11:22:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-db94afbeb9078ac1af7bba07540f6e02011.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">JPress v4.0 正式版终于来了，相对 JPress v3.x 来说，超过 100 项的新增或者细节优化，模板制作对于模板作者来说也更加简单了。</p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">JPress 是一个使用 Java 开发的类似 WordPress 的产品，具有完善的模板和插件功能，并在此基础上新增了在线商城、会员中心以及和微信深度整合的功能。到目前为止， 已经有 10w+ 网站使用 JPress 进行驱动，其中包括多个政府机构，200+上市公司，中科院、红+字会等。</span></p> 
<p style="text-align:left">其中一些 UI 细节大家可以对比一下：</p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-db94afbeb9078ac1af7bba07540f6e02011.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">（v3老版本的收款设置）</span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-97933bf9a98074b21955944caf0bd520b99.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(v4新版本的收款设置）</span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-2bfe3f23d621062c3828e8113a235ec331a.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">（v3老版本的文章编写）</span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-cd044fddaafebe82a542201ba0e6861050c.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(v4新版本的文章编写）</span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-792765a31bcb50a042b309d1835d3a5cd26.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">（v3老版本的用户中心）</span></p> 
<p style="text-align:center"> </p> 
<p style="text-align:center"><img src="https://oscimg.oschina.net/oscnet/up-8bcb1b5017ab9963b73c8ace5eb0ee93fa9.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#bdc3c7">(v4新版本的用户中心）</span></p> 
<p style="text-align:left"><strong>V4.0.0 正式版更新内容如下：</strong></p> 
<ul> 
 <li style="text-align:left">新增：模板预览功能，自由在后台开启或关闭</li> 
 <li style="text-align:left">新增：#@defaultMenu() 指令，更加方便用于渲染前台菜单</li> 
 <li style="text-align:left">新增：登录开启验证码功能，默认为开启</li> 
 <li style="text-align:left">新增：扁平化 URL 功能开关的功能，更加有利于 SEO，例如 /article/category/1.html 为 /article-category-1.html</li> 
 <li style="text-align:left">新增：全新的图片选择组件，日期组件的前端 UI 组件</li> 
 <li style="text-align:left">新增：全新的选择用户的 input 组件</li> 
 <li style="text-align:left">新增：AddonBase 类，方便用户编写 插件 入口类</li> 
 <li style="text-align:left">新增：模板的后台设置新增 setting_v4.html 的支持</li> 
 <li style="text-align:left">优化：升级 AdminLte 和 Bootstrap 到最新版本</li> 
 <li style="text-align:left">优化：升级 fontawesome 到最新版本</li> 
 <li style="text-align:left">优化：删除 ckeditor4 和 simplemde，使用 ckeditor5 和 vditor 代替</li> 
 <li style="text-align:left">优化：DatetimeRender 组件，时间相关的弹出UI更加简洁</li> 
 <li style="text-align:left">优化：合并 article.js、product.js、page.js 到 jpressfront.js</li> 
 <li style="text-align:left">优化：合并 article.css、product.css、page.css 到 jpressfront.css</li> 
 <li style="text-align:left">优化：管理员重置用户密码不再需要原密码</li> 
 <li style="text-align:left">优化：全面优化 layer 弹出的相关 UI</li> 
 <li style="text-align:left">优化：优化 JPress 内置的 4 套模板 UI 细节</li> 
 <li style="text-align:left">优化：后台相关必填输入框添加相关前端验证</li> 
 <li style="text-align:left">优化：微信相关功能的 url 目录结构</li> 
 <li style="text-align:left">优化：优化 logback 的日志输出目录结构</li> 
 <li style="text-align:left">优化：重构 jpress maven 目录，修改 service-api 为 service</li> 
 <li style="text-align:left">优化：后台评论列表页面，新增根据用户搜索的功能</li> 
 <li style="text-align:left">优化：附件选择功能，增加可以选择每页数量的选择</li> 
 <li style="text-align:left">修复：v3.x 发布评论的头像显示不正确的问题</li> 
 <li style="text-align:left">修复：v3.x page 评论分页 404 的问题</li> 
 <li style="text-align:left">修复：v3.x 后台的评论列表新增 待审核 的 tab 标签不显示的问题</li> 
 <li style="text-align:left">修复：v3.x 页面修改后，SEO Ping 出错的问题</li> 
 <li style="text-align:left">修复：v3.x 企业版在某些配置不能同步到其他分布式节点的问题<br>  </li> 
</ul> 
<p style="text-align:left"><strong>通过 Eclipse 或者 Idea 等开发工具运行</strong></p> 
<ul> 
 <li>1、在本地安装好 Java、Maven 等开发环境</li> 
 <li>2、将源码下载、并导入 eclipse 或者 idea</li> 
 <li>3、在项目的<strong>根目录</strong>，执行 <code>mvn clean install</code> 命令进行编译</li> 
 <li>4、在开发工具，右键运行 <code>starter/src/main/java/io.jpress.Starter</code> 下的 <code>main()</code> 方法</li> 
 <li>5、通过浏览器访问 <code>http://127.0.0.1:8080</code>，进行自动安装</li> 
</ul> 
<p style="text-align:left">使用过程中有任何问题，直接到 <a href="https://gitee.com/JPressProjects/jpress/issues">https://gitee.com/JPressProjects/jpress/issues</a> 反馈即可。</p>
                                        </div>
                                      
</div>
            