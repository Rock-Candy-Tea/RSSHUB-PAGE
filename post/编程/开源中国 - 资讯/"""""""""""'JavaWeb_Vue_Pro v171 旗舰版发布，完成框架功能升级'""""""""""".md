
---
title: """""""""""'JavaWeb_Vue_Pro v1.7.1 旗舰版发布，完成框架功能升级'"""""""""""
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Mon, 22 Mar 2021 08:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-16b8156d71772f3cf73f0e862a96ef96762.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <div> 
    <div> 
     <div> 
      <div> 
       <div> 
        <p>v1.7.1更新内容：<br> 1、更新优化城市管理模块；<br> 2、升级文件上传公共文件uploadFile;<br> 3、新增导出Excel功能，自定义注解实现；<br> 4、新增AOP切换日志，使用方法如：“@Log(title = "岗位管理", logType = LogType.INSERT)”<br> 5、从国家地理信息往重新采集国家城市列表最新数据，涉及数据表"sys_city";<br> 6、后端新增权限节点颗粒度控制，集成Shiro,使用方法：@RequiresPermissions("sys:city:edit")<br> 7、前端Vue端新增按钮权限节点控制，没有节点权限则按钮不显示，使用方式如：v-if="permission.includes('sys:level:delete')"<br> 8、新增配合Jenkins多环境发布的功能与POM配置；<br> 9、新增ExcelUtils导出工具类，并在职级管理模块写了导出Excel数据案例；<br> 10、职级管理、岗位管理、登录日志集成导出Excel功能；<br> 11、完善个人中心头像上传功能，完善Base64Utils转换工具类；<br> 12、重新设计登录界面背景图片；<br> 13、解决切换账号之前打开的Tab页依然存在的问题；</p> 
        <h3>项目介绍</h3> 
        <p>JavaWeb_Vue_Pro 是基于 SpringBoot2+Vue+ElementUI+Shiro+MybatisPlus 研发的权限(RBAC)及内容管理系统，致力于做更简洁的后台管理框架，包含系统管理、代码生成、权限管理、站点、广告、布局、字段、配置等一系列常用的模块，整套系统一键生成所有模块（包括前端UI），一键实现CRUD，简化了传统手动抒写重复性代码的工作。 同时，框架提供长大量常规组件，如上传单图、上传多图、上传文件、下拉选择、复选框按钮、单选按钮，城市选择、富文本编辑器、权限颗粒度控制等高频使用的组件，代码简介，使用方便，节省了大量重复性的劳动，降低了开发成本，提高了整体开发效率，整体开发效率提交80%以上，JavaWeb框架专注于为中小企业提供最佳的行业基础后台框架解决方案，执行效率、扩展性、稳定性值得信赖，操作体验流畅，使用非常优化，欢迎大家使用及进行二次开发。</p> 
        <h2>后台演示（用户名:admin 密码:123456）</h2> 
        <ul> 
         <li>演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmanage.vue.pro.javaweb.vip" target="_blank">http://manage.vue.pro.javaweb.vip</a></li> 
         <li>登录账号：admin</li> 
         <li>登录密码：123456</li> 
         <li>验证码：520</li> 
        </ul> 
        <h2>效果图展示</h2> 
        <p><img alt height="908" src="https://oscimg.oschina.net/oscnet/up-16b8156d71772f3cf73f0e862a96ef96762.png" width="1919" referrerpolicy="no-referrer"></p> 
        <p> </p> 
        <p><img alt height="911" src="https://oscimg.oschina.net/oscnet/up-f6aa40b58b806d6f24e5aad02788b48f1f3.png" width="1918" referrerpolicy="no-referrer"></p> 
        <p> </p> 
        <p><img alt height="911" src="https://oscimg.oschina.net/oscnet/up-37b1068429a0fb515226608d3fe54294c65.png" width="1918" referrerpolicy="no-referrer"></p> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            