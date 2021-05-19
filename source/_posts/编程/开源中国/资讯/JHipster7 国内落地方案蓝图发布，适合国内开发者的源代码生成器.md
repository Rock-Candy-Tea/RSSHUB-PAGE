
---
title: 'JHipster7 国内落地方案蓝图发布，适合国内开发者的源代码生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cors.zfour.workers.dev/?http://jhipster.huibozhixin.com/static/images/pro/screenshots/index.png'
author: 开源中国
comments: false
date: Wed, 19 May 2021 01:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://jhipster.huibozhixin.com/static/images/pro/screenshots/index.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>JHipster7已经发布，做为一款功能比较齐全的代码生成器，她在国外有很多拥趸，但其部分特性不完全适合国内，目前国内用户使用的功能应该仅集中在后端Java生成方面。</p> 
<p>为了进一步适合国内开发人员，制作了些蓝图(Blueprint）。除了JHipster支持的功能以外，主要增加功能如下：</p> 
<p>1、增强用户、角色、API权限、菜单权限。</p> 
<p>    1.1 用户增加mobile字段，可以使用手机登录。</p> 
<p>    1.2 原用角色（Authority)，仅有name一个属性，现在进行了增强，包括名称、代码、描述、是否显示等属性。</p> 
<p>    1.3权限管理由单一的权限（Authority)，扩展为Authority(角色）、API权限、菜单权限（菜单、按钮等）组成，更适合实际开发的需要。角色包含多个API权限和菜单权限。</p> 
<p>2、官方仅支持Spring-Data-Jpa，本蓝图增加了Mybatis的支持，毕竟国内Mybatis开发占用半壁江山（谦虚的比例）。</p> 
<p>    2.1 基于Mybatis-plus实现，支持全部特性。</p> 
<p>    2.2 为进一步融合Spring-Data-Jpa的思想，在Mybatis-plus的基础上增加了Diboot的支持，仅需要定义几个注解，实现与Jpa关系注解相同的效果。关联关系的处理更简单。</p> 
<p>    2.3JHipster的Filter特性非常好，能够快速实现复杂的检索条件支持，前后端统一。本蓝图的Mybatis也支持类似这样的用法。</p> 
<p>    如：<em>xyz.equals=someValue、xyz.contains=something、xyz.greaterThan=someValue，这些条件可以组合使用（and）。</em></p> 
<p><em>    在mapper.xml，test="abc !=null and abc !=''"，这样的用法再也用不到了。</em></p> 
<p>3、前台页面千变万化，确实没有银弹，但国内前端后台的方案非常集中，AntDesignPro，NG-ZORRO(Alain)，AntDesign Vue Pro，Element Admin等后台方案非常主流。此蓝图增加了这4个后台方案的支持，您可以在生成的时候自己选择。目前AntDesign Vue Pro方案的成熟度最高，其他在测试阶段，后续将会不断补充完善。无论你喜欢哪一个，这里可能都有答案，等待你挖掘。</p> 
<p>  3.1 全部都基于TypeScript。毕竟官方推荐这个。</p> 
<p>  3.2 AntDesipgn Pro基于官方实现，主题一致，代码风格一致。</p> 
<p>  3.3 NG-ZORRO基于Alain实现，目前以基本功能为主，后续不断加强。</p> 
<p>  3.4 AntDesign Vue Pro采用官方方案，目前完善度最高，采用VXE-Table实现列表功能，可动态定制显示、编辑组件的渲染。使用K-Form-Design实现表单的在线自定义功能。</p> 
<p>  3.3 Element Admin为最后增加的方案，也在不断完善中，采用VXE-Table实现列表功能，可动态定制显示、编辑组件的渲染。使用Form-Generator实现表单的在线自定义功能。</p> 
<p>4、根据JHipster官方的在线生成系统，制作了中英文双语在线生成系统，并提供本文相关的非JHipster官方功能的选项供用户选择。</p> 
<p>在线生成系统除了支持直接下载zip压缩文件外，更增加GitHub仓库的创建，最可喜的是增加了Gitee的仓库创建功能，再也不用无法连接GitHub而担心了。</p> 
<p>5、在线生成系统集成了官方的jdl-studio在线JDL文件设计功能。同时多个自定义注解，实现更多的特性。</p> 
<p>  自定义注解多达十几个，例如：</p> 
<ul> 
 <li>@skipMenu：实体注解，相应实体将不会生成菜单。</li> 
 <li>@ExtendData：实体注解，表字段可扩展。</li> 
 <li><span style="background-color:#ffffff; color:#314659">@skipComponent：实体注解，可取消指定组件的生成restController,service等，防止覆盖你修改的文件。</span></li> 
 <li>@configField(editInList-hideInList-hideInForm-sortable)：字段注解，列表编辑、列表中隐藏、表单中隐藏,可排序。editInList-hideInList-hideInForm可加入关系注解</li> 
 <li>@createdById：字段注解 创建者Id，Long类型或UUID类型，根据定义的User Entity主键确定。</li> 
</ul> 
<p>6、自动从实现和字段中提取中文注释内容，这样注释除了做为数据和实体的说明以外，还可以用在菜单、字段标题上，一次定义，多处使用。</p> 
<p>7、元模型管理功能，<span style="background-color:#ffffff; color:#314659">JHipster使用JSON格式或JDL完整的保留了实体的信息，但是他们对线上系统来说是静态内容，无法利用，也不能动态改变。</span><br> <span style="background-color:#ffffff; color:#314659">元模型保存了所有实体的信息和他们之间的关系，以及前端UI样式的部分信息。这些信息可以在线上运行阶段进行修改和定制。能够部分的实现"数据+配置=系统"这一思想。</span></p> 
<p><span style="background-color:#ffffff; color:#314659">  7.1 元模型信息中包括列表定义功能，可设置列表中某列是否显示、是否可编辑、使用什么组件显示和编辑，可编辑的列在编辑后立即保存到服务器。</span></p> 
<p><span style="background-color:#ffffff; color:#314659">  7.2 元模型中定义为列表不显示的列，在数据检索时也不会向数据库发送检索这个字段的SQL，减少对数据库性能的影响。</span></p> 
<p><span style="background-color:#ffffff; color:#314659">  7.3 单元格中的值可编辑为任何值，服务器都会保存，不会出现服务器不保存null的情况，你要保存什么值，它就保存什么值。没有xxxField != null这样的神奇判断。</span></p> 
<p>  7.4 既然元模型保存了所有的实体和关联关系的信息，那么它们能不能在线拓展呢？答案是：能！！！。可能根据需要在实体上使用注解标注该实体是否可以拓展。能够拓展的实体，会根据持久化框架的选项，采用相应的形式拓展数据库的结构，让你的实体在线上也可以增加字段或关系。</p> 
<p>  7.5 元模型中保存了所有列和关系的信息，自然就可能基于它实现表单的在线自定义，所以你可以随意在系统上线后根据需要调整表单的显示内容和格式，以及校验等功能。通过元模型可以实现多内容模型功能，如：CMS系统不同栏目，内容模型不同。</p> 
<p>8、<span style="background-color:#ffffff; color:#314659">OSS功能是国内开发比较常用的功能了，此蓝图集成了OSS功能，支持国内多家提供商以及本地服务器保存文件功能。Aliyun OSS、minio OSS、qiniu OSS、tencent OSS。</span></p> 
<p><span style="background-color:#ffffff; color:#314659">9、SMS功能也是国内开发比较常用的功能了，此蓝图集成了SMS功能，支持国内多家提供商。Aliyun SMS、yunpian SMS、qiniu SMS、tencent SMS。</span></p> 
<p><span style="background-color:#ffffff; color:#314659">10、JHipster官方的中文或英文资料如何你感觉可能不理想的话，也可以参考本次翻译的内容，也许会有不一样的收获。地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjhipster.huibozhixin.com%2F" target="_blank">http://jhipster.huibozhixin.com/</a></p> 
<p>11、近期马上推出的新特性包括：flowable工作流、大屏设计、公告通知等等。</p> 
<p>12、还有......，我也不记得了，等着你挖掘吧。如何没有挖掘到的话怎么办？给作者提意见或建议呀！！！</p> 
<p>13、对了，还没有地址呢，在线生成地址：http://jhonline.huibozhixin.com/</p> 
<p>14、简单的上几张图吧：</p> 
<p><img alt src="https://cors.zfour.workers.dev/?http://jhipster.huibozhixin.com/static/images/pro/screenshots/index.png" width="800" referrerpolicy="no-referrer"><img alt height="298" src="https://oscimg.oschina.net/oscnet/up-bd0a7d5952e11d7e6c6bc8e36d469ad35ab.png" width="600" referrerpolicy="no-referrer"></p> 
<p><img alt height="250" src="https://oscimg.oschina.net/oscnet/up-ac9279a3f809b7e2b478ba3c27eda55caba.png" width="600" referrerpolicy="no-referrer"></p> 
<p><img alt height="297" src="https://oscimg.oschina.net/oscnet/up-27c68d65fdb1ca904434f3d09ed9c5ef311.png" width="600" referrerpolicy="no-referrer"></p> 
<p><img alt height="205" src="https://oscimg.oschina.net/oscnet/up-326df2b70c8d2919a705dafa1eb65caf5c3.png" width="600" referrerpolicy="no-referrer"></p> 
<p><img alt height="281" src="https://oscimg.oschina.net/oscnet/up-2b7f0b7cf519dd9a916c22a0e550c207b80.png" width="600" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            