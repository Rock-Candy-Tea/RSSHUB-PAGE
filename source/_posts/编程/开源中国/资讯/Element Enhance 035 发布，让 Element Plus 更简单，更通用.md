
---
title: 'Element Enhance 0.3.5 发布，让 Element Plus 更简单，更通用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-840683a933633546d99ba85def81eb1c3a7.png'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 01:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-840683a933633546d99ba85def81eb1c3a7.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>📖 概述</p> 
<p>Element Enhance 是基于 Element Plus 而开发的模板组件，提供了更高级别的抽象支持，开箱即用，更加专注于页面。</p> 
<p>✒️ 更新日志</p> 
<p><strong>0.3.5</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">[新增] element-enhance 案例</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] breadcrumb 面包屑组件, 用于展示当前路由信息</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] layout 组件的 show-collapse 参数, 用于控制顶部 collapse 的隐藏显示</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] layout 组件的 banner 参数, 用于控制顶部通栏布局方式</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] layout 组件的 var.css 样式, 用于自定义布局尺寸</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] exception 组件的 image 参数, 用于自定义显示异常图片</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] exception 组件的 title 参数, 用于自定义显示异常标题</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] exception 组件的 describe 参数, 用于自定义显示异常描述</span><br> <span style="background-color:#ffffff; color:#40485b">[新增] exception 组件的 refresh 事件, 用于定义刷新的业务</span><br> <span style="background-color:#ffffff; color:#40485b">[优化] layout 组件的 white 主题, 修改 menu-item 选中状态的样式</span><br> <span style="background-color:#ffffff; color:#40485b">[优化] count-to 组件的 count up 算法</span><br> <span style="background-color:#ffffff; color:#40485b">[支持] 自定义主题色</span></p> 
<p><strong>0.3.4</strong></p> 
<p>[新增] layout 组件的 banner 参数, 用于实现通栏布局<br> [新增] exception 异常组件, 用于错误页面的构建<br> [新增] avatar-list 头像列表组件, 用于头像列表的展示<br> [新增] count-to 数字滚动组件, 用于数据的 count up 效果<br> [新增] full-screen 全屏组件, 用于页面的全屏切换<br> [新增] icon-picker 图标选择器组件, 提供 element-plus 的图标选择支持</p> 
<p>⚡ 入门</p> 
<p>安装</p> 
<p>```<br> npm install element-plus --save</p> 
<p>npm install element-enhance --save<br> ```</p> 
<p>引入</p> 
<p>```js<br> import &#123; createApp &#125; from 'vue'<br> import App from './App.vue'<br> import ElementEnhance from 'element-enhance'<br> import 'element-enhance/lib/style.css'<br> import ElementPlus from 'element-plus'<br> import 'element-plus/lib/theme-chalk/index.css'</p> 
<p>const app = createApp(App)</p> 
<p>app.use(ElementEnhance)<br> app.use(ElementPlus)<br> app.mount('#app')<br> ```</p> 
<p>路由</p> 
<p><a href="https://gitee.com/Jmysy/element-enhance-admin/blob/master/src/router/module/base-routes.ts">配置</a></p> 
<p>使用</p> 
<p>```vue<br> <template><br>   <ele-layout multi-tab="true" breadcrumb="true"><br>     <template #logo></template><br>   </ele-layout><br> </template><br> ```</p> 
<p><img height="800" src="https://oscimg.oschina.net/oscnet/up-840683a933633546d99ba85def81eb1c3a7.png" width="1701" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            