
---
title: 'JeeSite 快速开发平台  Vue3 前端版本公测发布开源了'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-db83c334daab05d89a0930d8497816da6a4.png'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 02:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-db83c334daab05d89a0930d8497816da6a4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">介绍</h2> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">基于 Vue3、Vite、Ant-Design-Vue、TypeScript、Vue Vben Admin，最先进的技术栈，让初学者能够更快的入门并投入到团队开发中去。包括模块如：组织机构、角色用户、菜单授权、数据权限、系统参数等。强大的组件封装，数据驱动视图。为微小中大型项目的开发，提供现成的开箱解决方案及丰富的示例。</p> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">在 Vben Admin 基础上做的改进：</p> 
<ul> 
 <li>更精致的界面细节优化改进，非常适合信息化管理后台</li> 
 <li>主题风格改进，不同的布局风格，菜单及权限体验优化</li> 
 <li>顶部菜单、分隔菜单、混合菜单的活动状态激活和加载优化改进</li> 
 <li>树表支持异步的封装，提升展开折叠性能，支持按层次展开折叠树表</li> 
 <li>树结构新增快捷刷新、动态生成树、层次独立和不独立的数据返回兼容</li> 
 <li>增加左树右表功能展示，可折叠左树，树组件增加默认图标</li> 
 <li>表单组件适应各种数据格式来源，特别是多选字符串到数组的互转兼容</li> 
 <li>表单新增各种便捷属性和表单组件，下拉框和树选择支持标签名回显</li> 
 <li>表单组件，改进折叠表单 Action 的算法，智能化布局</li> 
 <li>表格组件，Action 更多，支持横向显示操作，更方便</li> 
 <li>表格组件，子表编辑改进，表格列排序和重置改进优化</li> 
 <li>新增字典组件，支持展示到表格列、表单组件下拉框单选框等</li> 
 <li>字典标签支持 Tag、Badge、自定义 class、style 等，显示风格</li> 
 <li>更方便的支持 Tab 页面的缓存，切换页签的时候不重载页面内容</li> 
 <li>Tab 页签界面美化、图标显示、任何标签上右键，可快速刷新等等</li> 
 <li>全局 Axios 改进，兼容各种数据格式，超时消息提醒改进</li> 
 <li>功能权限鉴权改进，并兼容本地路由和后台路由同时使用</li> 
 <li>等等各种细节改进，体验优化，黑暗布局细节优化</li> 
 <li>Vue端完全开源，用上你就会爱上，实在太方便了</li> 
</ul> 
<h2 style="text-align:start">设计特点</h2> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">定义众多组件，非常贴心的组件属性及小功能，符合 JeeSite 以往的设计思想，列表和表单以数据驱动视图，极大简化了业务功能开发，注释分解详见本页最下【源码解析】</p> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">为什么做数据驱动视图？前端向下兼容一直是最大的问题，有了一套相应的标准，会对框架升级帮助很大。比如你可以非常小的成本，业务代码改动非常小的情况下，去升级前端；数据驱动视图可以为未来自定义拖拽表单做更好的铺垫，数据存储结构更清晰化，更利于维护。</p> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">提示：请仔细阅读源码解析，表单视图和列表视图上的注释哦，复杂表单可以多表单联合使用。</p> 
<h2 style="margin-left:0px; margin-right:0px; text-align:start">截图鉴赏</h2> 
<p><img height="630" src="https://oscimg.oschina.net/oscnet/up-db83c334daab05d89a0930d8497816da6a4.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img height="531" src="https://oscimg.oschina.net/oscnet/up-5c77650a51b32799a0252b12bb454ec5e92.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img height="531" src="https://oscimg.oschina.net/oscnet/up-8152e009e410925f9b88c5129e90ed3b28c.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img height="487" src="https://oscimg.oschina.net/oscnet/up-6a4c84696b589ba2a3bd034c2b9026b40e1.png" width="935" referrerpolicy="no-referrer"></p> 
<p><img height="567" src="https://oscimg.oschina.net/oscnet/up-f03d07d58b351e1f2fc9931ea2dba550429.png" width="1080" referrerpolicy="no-referrer"></p> 
<p><img height="634" src="https://oscimg.oschina.net/oscnet/up-a36a005290cb95bc625e0933c867edc7e6f.png" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">演示地址</h2> 
<ol> 
 <li>地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvue.jeesite.com%2F" target="_blank">http://vue.jeesite.com/</a></li> 
 <li>账号：system</li> 
 <li>密码：admin</li> 
</ol> 
<h2 style="text-align:start">学习准备</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fnodejs.org%2F" target="_blank">Node.js 16</a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgit-scm.com%2F" target="_blank">git</a><span> </span>- 开发环境</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvitejs.dev%2F" target="_blank">Vite</a><span> </span>- 熟悉 Vite 特性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2F" target="_blank">Vue-v3</a><span> </span>- 熟悉 Vue 基础语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.typescriptlang.org%2F" target="_blank">TypeScript</a><span> </span>- 熟悉<span> </span><code>TypeScript</code><span> </span>基本语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fes6.ruanyifeng.com%2F" target="_blank">ES6+</a><span> </span>- 熟悉 ES6 基本语法</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnext.router.vuejs.org%2F" target="_blank">Vue-Router-v4</a><span> </span>- 熟悉 vue-router 基本使用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvvbin.cn%2Fdoc-next%2F" target="_blank">Vue-Vben-Admin</a><span> </span>- 熟悉 UI 及表单列表及常用组件使用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2F2x.antdv.com%2Fdocs%2Fvue%2Fintroduce-cn%2F" target="_blank">Ant-Design-Vue</a><span> </span>- 熟悉 UI 基本使用</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnuysoft%2FMock" target="_blank">Mock.js</a><span> </span>- mockjs 基本语法</li> 
 <li><a href="https://gitee.com/thinkgem/jeesite4/tree/v5.0-beta/">JeeSite-v5</a><span> </span>- 后台服务</li> 
</ul> 
<h2 style="text-align:start">安装使用</h2> 
<ul> 
 <li>如果没有安装 Node.js（不低于 14，建议 16）</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code>下载安装 Node.js 16：https://nodejs.org
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>如果没有安装 Yarn 执行安装（要求 Yarn v1.x）</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code>npm i <span style="color:#000080">-g</span> yarn
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>获取代码</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code>git clone https://gitee.com/thinkgem/jeesite-vue.git
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>安装依赖</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code><span style="color:#0086b3">cd </span>jeesite-vue

yarn config <span style="color:#0086b3">set </span>registry https://registry.npm.taobao.org
yarn <span style="color:#0086b3">install</span>
</code></pre> 
 </div> 
</div> 
<ul> 
 <li>运行</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code>yarn serve
</code></pre> 
 </div> 
</div> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">开发环境会加载文件较多，便于调试，请耐心等待。</p> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">编译打包后，会合并这些文件，所以访问性能会大大提高。</p> 
<ul> 
 <li>打包</li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code>yarn build
</code></pre> 
 </div> 
</div> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">打包完成后，会在根目录生成 dist 文件夹，发布 nginx。</p> 
<p style="color:#444444; margin-left:0; margin-right:0; text-align:start">有一些打包参数，详见 .env.production 里面有注释。</p> 
<h3 style="text-align:start">如果您使用的 VSCode 的话，推荐安装以下插件：</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dantfu.iconify" target="_blank">Iconify IntelliSense</a><span> </span>- Iconify 图标插件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dvoorjaar.windicss-intellisense" target="_blank">windicss IntelliSense</a><span> </span>- windicss 提示插件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3DLokalise.i18n-ally" target="_blank">I18n-ally</a><span> </span>- i18n 插件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Djohnsoncodehk.volar" target="_blank">Volar</a><span> </span>- Vue3 开发必备（Vetur禁用）</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Ddbaeumer.vscode-eslint" target="_blank">ESLint</a><span> </span>- 脚本代码检查</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Desbenp.prettier-vscode" target="_blank">Prettier</a><span> </span>- 代码格式化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dstylelint.vscode-stylelint" target="_blank">Stylelint</a><span> </span>- CSS 格式化</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Dmikestead.dotenv" target="_blank">DotENV</a><span> </span>- .env 文件高亮</li> 
</ul> 
<h2 style="text-align:start">常见问题</h2> 
<ul> 
 <li>如何将表单抽屉改为弹窗，替换 list 和 form 页面的 Drawer 为 Modal 即可。</li> 
 <li>浏览器支持情况：支持所有现代浏览器，Vue3 已不再支持 IE 浏览器。</li> 
</ul> 
<h2 style="text-align:start">源码解析</h2> 
<h3 style="text-align:start">表单视图</h3> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code><span style="color:#000080"><template></span>
  <span style="color:#1d7e21"><!-- 弹出抽屉组件，如果想改为弹窗，Drawer 换为 Modal 即可快速替换 --></span>
  <span style="color:#000080"><BasicDrawer</span>
    <span style="color:#008080">v-bind=</span><span style="color:#dd1144">"$attrs"</span>    <span style="color:#008080">--</span> <span>传递来自父组件的属性</span>
    <span style="color:#008080">:showFooter=</span><span style="color:#dd1144">"true"</span> <span style="color:#008080">--</span> <span>显示弹窗底部按钮组</span>
    <span style="color:#008080">:okAuth=</span><span style="color:#dd1144">"'test:testData:edit'"</span> <span style="color:#008080">--</span> <span>提交按钮权限，控制按钮是否显示</span>
    <span>@</span><span style="color:#008080">register=</span><span style="color:#dd1144">"registerDrawer"</span>     <span style="color:#008080">--</span> <span>弹窗后的回调方法</span>
    <span>@</span><span style="color:#008080">ok=</span><span style="color:#dd1144">"handleSubmit"</span> <span style="color:#008080">--</span> <span>提交按钮调用方法</span>
    <span style="color:#008080">width=</span><span style="color:#dd1144">"60%"</span>        <span style="color:#008080">--</span> <span>弹窗宽度，支持按比例</span>
  <span style="color:#000080">></span>
    <span style="color:#1d7e21"><!-- 弹窗标题 --></span>
    <span style="color:#000080"><template</span> <span style="color:#008080">#title</span><span style="color:#000080">></span>
      <span style="color:#000080"><Icon</span> <span style="color:#008080">:icon=</span><span style="color:#dd1144">"getTitle.icon"</span> <span style="color:#008080">class=</span><span style="color:#dd1144">"pr-1 m-1"</span> <span style="color:#000080">/></span> -- 图标
      <span style="color:#000080"><span></span> &#123;&#123; getTitle.value &#125;&#125; <span style="color:#000080"></span></span>  -- 标题名称
    <span style="color:#000080"></template></span>
    <span style="color:#1d7e21"><!-- 表单组件 --></span>
    <span style="color:#000080"><BasicForm</span> <span>@</span><span style="color:#008080">register=</span><span style="color:#dd1144">"registerForm"</span><span style="color:#000080">></span>
      <span style="color:#1d7e21"><!-- 定义表单控件插槽、个性化表单控件，如：这是一个表单子表插槽 --></span>
      <span style="color:#000080"><template</span> <span style="color:#008080">#testDataChildList</span><span style="color:#000080">></span>
        <span style="color:#000080"><BasicTable</span>
          <span>@</span><span style="color:#008080">register=</span><span style="color:#dd1144">"registerTestDataChildTable"</span>
          <span>@</span><span style="color:#008080">row-click=</span><span style="color:#dd1144">"handleTestDataChildRowClick"</span>
        <span style="color:#000080">/></span>
        <span style="color:#1d7e21"><!-- 子表新增按钮 --></span>
        <span style="color:#000080"><a-button</span> <span style="color:#008080">class=</span><span style="color:#dd1144">"mt-2"</span> <span>@</span><span style="color:#008080">click=</span><span style="color:#dd1144">"handleTestDataChildAdd"</span><span style="color:#000080">></span>
          <span style="color:#000080"><Icon</span> <span style="color:#008080">icon=</span><span style="color:#dd1144">"ant-design:plus-circle-outlined"</span> <span style="color:#000080">/></span> &#123;&#123; t('新增') &#125;&#125;
        <span style="color:#000080"></a-button></span>
      <span style="color:#000080"></template></span>
    <span style="color:#000080"></BasicForm></span>
  <span style="color:#000080"></BasicDrawer></span>
<span style="color:#000080"></template></span>
<span style="color:#000080"><script </span><span style="color:#008080">lang=</span><span style="color:#dd1144">"ts"</span><span style="color:#000080">></span>
  <strong>export</strong> <strong>default</strong> <span>defineComponent</span><span>(&#123;</span>
    <span style="color:#1d7e21">// 当前组件名称（与路由名一致，如果不一致会页面缓存失效）</span>
    <span style="color:#008080">name</span><span>:</span> <span>'</span><span style="color:#dd1144">ViewsTestTestDataForm</span><span>'</span><span>,</span>
  <span>&#125;);</span>
<span style="color:#000080"></script></span>
<span style="color:#000080"><script </span><span style="color:#008080">lang=</span><span style="color:#dd1144">"ts"</span> <span style="color:#008080">setup</span><span style="color:#000080">></span>

  <span style="color:#1d7e21">// 导入当前用到的对象，部分省略</span>
  <strong>import</strong> <span>&#123;</span> <span>defineComponent</span><span>,</span> <span>ref</span> <span>&#125;</span> <strong>from</strong> <span>'</span><span style="color:#dd1144">vue</span><span>'</span><span>;</span>
  <strong>import</strong> <span>&#123;</span> <span>officeTreeData</span> <span>&#125;</span> <strong>from</strong> <span>'</span><span style="color:#dd1144">/@/api/sys/office</span><span>'</span><span>;</span>
  <strong>import</strong> <span>&#123;</span> <span>areaTreeData</span> <span>&#125;</span> <strong>from</strong> <span>'</span><span style="color:#dd1144">/@/api/sys/area</span><span>'</span><span>;</span>

  <span style="color:#1d7e21">// 页面事件定义</span>
  <strong>const</strong> <span>emit</span> <strong>=</strong> <span>defineEmits</span><span>([</span><span>'</span><span style="color:#dd1144">success</span><span>'</span><span>,</span> <span>'</span><span style="color:#dd1144">register</span><span>'</span><span>]);</span>

  <span style="color:#1d7e21">// 国际化方法调用，参数是国际化编码的跟路径</span>
  <strong>const</strong> <span>&#123;</span> <span>t</span> <span>&#125;</span> <strong>=</strong> <span>useI18n</span><span>(</span><span>'</span><span style="color:#dd1144">test.testData</span><span>'</span><span>);</span>

  <span style="color:#1d7e21">// 消息弹窗方法</span>
  <strong>const</strong> <span>&#123;</span> <span>showMessage</span> <span>&#125;</span> <strong>=</strong> <span>useMessage</span><span>();</span>

  <span style="color:#1d7e21">// 当前页面数据记录</span>
  <strong>const</strong> <span>record</span> <strong>=</strong> <span>ref</span><strong><</strong><span>Recordable</span><strong>></strong><span>(&#123;&#125;);</span>

  <span style="color:#1d7e21">// 当前页面标题定义，来自菜单管理定义</span>
  <strong>const</strong> <span>getTitle</span> <strong>=</strong> <span>&#123;</span>
    <span style="color:#008080">icon</span><span>:</span> <span>router</span><span>.</span><span>currentRoute</span><span>.</span><span>value</span><span>.</span><span>meta</span><span>.</span><span>icon</span> <strong>||</strong> <span>'</span><span style="color:#dd1144">ant-design:book-outlined</span><span>'</span><span>,</span>
    <span style="color:#008080">value</span><span>:</span> <span>record</span><span>.</span><span>value</span><span>.</span><span>isNewRecord</span> <span>?</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">新增数据</span><span>'</span><span>)</span> <span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">编辑数据</span><span>'</span><span>),</span>
  <span>&#125;;</span>

  <span style="color:#1d7e21">// 输入表单控件定义</span>
  <strong>const</strong> <span>inputFormSchemas</span><span>:</span> <span>FormSchema</span><span>[]</span> <strong>=</strong> <span>[</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">单行文本</span><span>'</span><span>),</span> <span style="color:#1d7e21">// 控件前面的页签</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testInput</span><span>'</span><span>,</span>  <span style="color:#1d7e21">// 字段提交参数名</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">Input</span><span>'</span><span>,</span>  <span style="color:#1d7e21">// 控件类型（可自定义，更多查看 componentMap.ts ）</span>
      <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>    <span style="color:#1d7e21">// 组件属性定义</span>
        <span style="color:#008080">maxlength</span><span>:</span> <span style="color:#009999">200</span><span>,</span>
      <span>&#125;,</span>
      <span style="color:#008080">required</span><span>:</span> <strong>true</strong><span>,</span>      <span style="color:#1d7e21">// 表单验证，是否必填（快速定义）</span>
      <span style="color:#008080">rules</span><span>:</span> <span>[</span>             <span style="color:#1d7e21">// 如果不只是必填，需要通过 rules 定义，举例：</span>
        <span>&#123;</span> <span style="color:#008080">required</span><span>:</span> <strong>true</strong> <span>&#125;,</span>
        <span>&#123;</span> <span style="color:#008080">min</span><span>:</span> <span style="color:#009999">4</span><span>,</span> <span style="color:#008080">max</span><span>:</span> <span style="color:#009999">20</span><span>,</span> <span style="color:#008080">message</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">请输入长度在 4 到 20 个字符之间</span><span>'</span><span>)</span> <span>&#125;,</span>
        <span>&#123;</span> <span style="color:#008080">pattern</span><span>:</span> <span style="color:#009926">/^</span><span style="color:#dd1144">[\u</span><span style="color:#009926">0391-</span><span style="color:#dd1144">\u</span><span style="color:#009926">FFE5</span><span style="color:#dd1144">\w]</span><span style="color:#009926">+$/</span><span>,</span> <span style="color:#008080">message</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">不能输入特殊字符</span><span>'</span><span>)</span> <span>&#125;,</span>
        <span>&#123;</span>
          <span>validator</span><span>(</span><span>_rule</span><span>,</span> <span>value</span><span>)</span> <span>&#123;</span>
             <strong>return</strong> <strong>new</strong> <span style="color:#0086b3">Promise</span><span>((</span><span>resolve</span><span>,</span> <span>reject</span><span>)</span> <strong>=></strong> <span>&#123;</span>
              <strong>if</strong> <span>(</span><strong>!</strong><span>value</span> <strong>||</strong> <span>value</span> <strong>===</strong> <span>''</span><span>)</span> <strong>return</strong> <span>resolve</span><span>();</span>
              <span style="color:#1d7e21">// 远程验证，访问后台校验数据是否重复</span>
              <span>checkTestInput</span><span>(</span><span>record</span><span>.</span><span>value</span><span>.</span><span>testInput</span> <strong>||</strong> <span>''</span><span>,</span> <span>value</span><span>)</span>
                <span>.</span><span>then</span><span>((</span><span>res</span><span>)</span> <strong>=></strong> <span>(</span><span>res</span> <span>?</span> <span>resolve</span><span>()</span> <span>:</span> <span>reject</span><span>(</span><span>t</span><span>(</span><span>'</span><span style="color:#dd1144">数据已存在</span><span>'</span><span>))))</span>
                <span>.</span><strong>catch</strong><span>((</span><span>err</span><span>)</span> <strong>=></strong> <span>reject</span><span>(</span><span>err</span><span>.</span><span>message</span> <strong>||</strong> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">验证失败</span><span>'</span><span>)));</span>
            <span>&#125;);</span>
          <span>&#125;,</span>
        <span>&#125;,</span>
      <span>],</span>
      <span style="color:#008080">colProps</span><span>:</span> <span>&#123;</span> <span style="color:#008080">lg</span><span>:</span> <span style="color:#009999">24</span><span>,</span> <span style="color:#008080">md</span><span>:</span> <span style="color:#009999">24</span> <span>&#125;,</span> <span style="color:#1d7e21">// 栅格布局（遵循 Ant Design 风格）</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">下拉框</span><span>'</span><span>),</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testSelect</span><span>'</span><span>,</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">Select</span><span>'</span><span>,</span>    <span style="color:#1d7e21">// 选择框还有 RadioGroup、CheckboxGroup</span>
      <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>
        <span style="color:#008080">dictType</span><span>:</span> <span>'</span><span style="color:#dd1144">sys_menu_type</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 下拉框选项数据（支持直接指定字典类型）</span>
        <span style="color:#008080">allowClear</span><span>:</span> <strong>true</strong><span>,</span>          <span style="color:#1d7e21">// 启用空选项，可清空选择</span>
        <span style="color:#008080">mode</span><span>:</span> <span>'</span><span style="color:#dd1144">multiple</span><span>'</span><span>,</span>          <span style="color:#1d7e21">// 下拉框模块，启用多选</span>
      <span>&#125;,</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">日期选择</span><span>'</span><span>),</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testDate</span><span>'</span><span>,</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">DatePicker</span><span>'</span><span>,</span>
      <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>
        <span style="color:#008080">format</span><span>:</span> <span>'</span><span style="color:#dd1144">YYYY-MM-DD</span><span>'</span><span>,</span>      <span style="color:#1d7e21">// 日期选择</span>
        <span style="color:#008080">showTime</span><span>:</span> <strong>false</strong><span>,</span>           <span style="color:#1d7e21">// 关闭时间选择</span>
      <span>&#125;,</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">日期时间</span><span>'</span><span>),</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testDatetime</span><span>'</span><span>,</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">DatePicker</span><span>'</span><span>,</span>
      <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>
        <span style="color:#008080">format</span><span>:</span> <span>'</span><span style="color:#dd1144">YYYY-MM-DD HH:mm</span><span>'</span><span>,</span>    <span style="color:#1d7e21">// 日期时间选择</span>
        <span style="color:#008080">showTime</span><span>:</span> <span>&#123;</span> <span style="color:#008080">format</span><span>:</span> <span>'</span><span style="color:#dd1144">HH:mm</span><span>'</span> <span>&#125;,</span> <span style="color:#1d7e21">// 设置时间的格式</span>
      <span>&#125;,</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">用户选择</span><span>'</span><span>),</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testUser.userCode</span><span>'</span><span>,</span>
      <span style="color:#008080">fieldLabel</span><span>:</span> <span>'</span><span style="color:#dd1144">testUser.userName</span><span>'</span><span>,</span> <span style="color:#1d7e21">//【支持返回，如下拉框或树选择的节点名】</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">TreeSelect</span><span>'</span><span>,</span>         <span style="color:#1d7e21">// 树选择控件</span>
      <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>
        <span style="color:#008080">api</span><span>:</span> <span>officeTreeData</span><span>,</span>           <span style="color:#1d7e21">// 数据源 API 定义，支持 ztree 格式</span>
        <span style="color:#008080">params</span><span>:</span> <span>&#123;</span> <span style="color:#008080">isLoadUser</span><span>:</span> <strong>true</strong><span>,</span> <span style="color:#008080">userIdPrefix</span><span>:</span> <span>''</span> <span>&#125;,</span> <span style="color:#1d7e21">// API 参数</span>
        <span style="color:#008080">canSelectParent</span><span>:</span> <strong>false</strong><span>,</span>        <span style="color:#1d7e21">// 是否允许选择父级</span>
        <span style="color:#008080">allowClear</span><span>:</span> <strong>true</strong><span>,</span>
      <span>&#125;,</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">子表数据</span><span>'</span><span>),</span>
      <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testDataChildList</span><span>'</span><span>,</span>
      <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">Input</span><span>'</span><span>,</span>
      <span style="color:#008080">colProps</span><span>:</span> <span>&#123;</span> <span style="color:#008080">lg</span><span>:</span> <span style="color:#009999">24</span><span>,</span> <span style="color:#008080">md</span><span>:</span> <span style="color:#009999">24</span> <span>&#125;,</span>
      <span style="color:#008080">slot</span><span>:</span> <span>'</span><span style="color:#dd1144">testDataChildList</span><span>'</span><span>,</span>      <span style="color:#1d7e21">// 指定插槽、个性化控件内容</span>
    <span>&#125;,</span>
  <span>];</span>

  <span style="color:#1d7e21">// 当前表单的参数定义</span>
  <strong>const</strong> <span>[</span><span>registerForm</span><span>,</span> <span>&#123;</span> <span>resetFields</span><span>,</span> <span>setFieldsValue</span><span>,</span> <span>validate</span> <span>&#125;]</span> <strong>=</strong> <span>useForm</span><span>(&#123;</span>
    <span style="color:#008080">labelWidth</span><span>:</span> <span style="color:#009999">120</span><span>,</span>                  <span style="color:#1d7e21">// 控件前面的标签宽度</span>
    <span style="color:#008080">schemas</span><span>:</span> <span>inputFormSchemas</span><span>,</span>        <span style="color:#1d7e21">// 控件定义列表</span>
    <span style="color:#008080">baseColProps</span><span>:</span> <span>&#123;</span> <span style="color:#008080">lg</span><span>:</span> <span style="color:#009999">12</span><span>,</span> <span style="color:#008080">md</span><span>:</span> <span style="color:#009999">24</span> <span>&#125;,</span> <span style="color:#1d7e21">// 控件默认栅格布局方式（响应式）</span>
  <span>&#125;);</span>

  <span style="color:#1d7e21">// 当前表单子表格定义</span>
  <strong>const</strong> <span>[</span><span>registerTestDataChildTable</span><span>,</span> <span>testDataChildTable</span><span>]</span> <strong>=</strong> <span>useTable</span><span>(&#123;</span>
    <span style="color:#008080">actionColumn</span><span>:</span> <span>&#123;</span>  <span style="color:#1d7e21">// 子表的操作列定义</span>
      <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">60</span><span>,</span>     <span style="color:#1d7e21">// 操作列宽度</span>
      <span style="color:#008080">actions</span><span>:</span> <span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <strong>=></strong> <span>[</span>
        <span>&#123;</span>
          <span style="color:#008080">icon</span><span>:</span> <span>'</span><span style="color:#dd1144">ant-design:delete-outlined</span><span>'</span><span>,</span>
          <span style="color:#008080">color</span><span>:</span> <span>'</span><span style="color:#dd1144">error</span><span>'</span><span>,</span>
          <span style="color:#008080">popConfirm</span><span>:</span> <span>&#123;</span> <span style="color:#1d7e21">// 是否需要启用确认框</span>
            <span style="color:#008080">title</span><span>:</span> <span>'</span><span style="color:#dd1144">是否确认删除</span><span>'</span><span>,</span>
            <span style="color:#008080">confirm</span><span>:</span> <span>handleTestDataChildDelete</span><span>.</span><span>bind</span><span>(</span><strong>this</strong><span>,</span> <span>record</span><span>),</span>
          <span>&#125;,</span>
          <span style="color:#008080">auth</span><span>:</span> <span>'</span><span style="color:#dd1144">sys:empUser:edit</span><span>'</span><span>,</span>  <span style="color:#1d7e21">// 按钮权限（可控制按钮是否显示）</span>
        <span>&#125;,</span>
      <span>],</span>
    <span>&#125;,</span>
    <span style="color:#008080">rowKey</span><span>:</span> <span>'</span><span style="color:#dd1144">id</span><span>'</span><span>,</span>     <span style="color:#1d7e21">// 子表主键名</span>
    <span style="color:#008080">pagination</span><span>:</span> <strong>false</strong><span>,</span><span style="color:#1d7e21">// 关闭分页</span>
    <span style="color:#008080">bordered</span><span>:</span> <strong>true</strong><span>,</span>   <span style="color:#1d7e21">// 开启表格边框</span>
    <span style="color:#008080">size</span><span>:</span> <span>'</span><span style="color:#dd1144">small</span><span>'</span><span>,</span>    <span style="color:#1d7e21">// 单元格间距</span>
    <span style="color:#008080">inset</span><span>:</span> <strong>true</strong><span>,</span>      <span style="color:#1d7e21">// 是否内嵌（去除一些边距）</span>
  <span>&#125;);</span>

  <span style="color:#1d7e21">// 当前表单子表自动定义</span>
  <strong>async</strong> <strong>function</strong> <span>setTestDataChildTableData</span><span>(</span><span style="color:#008080">_res</span><span>:</span> <span>Recordable</span><span>)</span> <span>&#123;</span>
    <span>testDataChildTable</span><span>.</span><span>setColumns</span><span>([</span>
      <span>&#123;</span>
        <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">单行文本</span><span>'</span><span>),</span>
        <span style="color:#008080">dataIndex</span><span>:</span> <span>'</span><span style="color:#dd1144">testInput</span><span>'</span><span>,</span>
        <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">230</span><span>,</span>
        <span style="color:#008080">align</span><span>:</span> <span>'</span><span style="color:#dd1144">left</span><span>'</span><span>,</span>
        <span style="color:#008080">editRow</span><span>:</span> <strong>true</strong><span>,</span>          <span style="color:#1d7e21">// 是否启用编辑</span>
        <span style="color:#008080">editComponent</span><span>:</span> <span>'</span><span style="color:#dd1144">Input</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 编辑控件（可自定义，更多查看 componentMap.ts ）</span>
        <span style="color:#008080">editRule</span><span>:</span> <strong>true</strong><span>,</span>         <span style="color:#1d7e21">// 控件验证（是否必填）</span>
      <span>&#125;,</span>
      <span>&#123;</span>
        <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">下拉框</span><span>'</span><span>),</span>
        <span style="color:#008080">dataIndex</span><span>:</span> <span>'</span><span style="color:#dd1144">testSelect</span><span>'</span><span>,</span>
        <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">130</span><span>,</span>
        <span style="color:#008080">align</span><span>:</span> <span>'</span><span style="color:#dd1144">left</span><span>'</span><span>,</span>
        <span style="color:#008080">dictType</span><span>:</span> <span>'</span><span style="color:#dd1144">sys_menu_type</span><span>'</span><span>,</span>   <span style="color:#1d7e21">// 指定字典类型，自动显示字典标签</span>
        <span style="color:#008080">editRow</span><span>:</span> <strong>true</strong><span>,</span>
        <span style="color:#008080">editComponent</span><span>:</span> <span>'</span><span style="color:#dd1144">Select</span><span>'</span><span>,</span>
        <span style="color:#008080">editComponentProps</span><span>:</span> <span>&#123;</span>        <span style="color:#1d7e21">// 控件属性</span>
          <span style="color:#008080">dictType</span><span>:</span> <span>'</span><span style="color:#dd1144">sys_menu_type</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 下拉框的字段类型</span>
          <span style="color:#008080">allowClear</span><span>:</span> <strong>true</strong><span>,</span>
        <span>&#125;,</span>
        <span style="color:#008080">editRule</span><span>:</span> <strong>false</strong><span>,</span>
      <span>&#125;,</span>
      <span style="color:#1d7e21">// 更多组件控件不举例了，同表单控件 ...</span>
    <span>]);</span>
    <span style="color:#1d7e21">// 设定子表数据</span>
    <span>testDataChildTable</span><span>.</span><span>setTableData</span><span>(</span><span>record</span><span>.</span><span>value</span><span>.</span><span>testDataChildList</span> <strong>||</strong> <span>[]);</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 点击行，启用编辑</span>
  <strong>function</strong> <span>handleTestDataChildRowClick</span><span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <span>&#123;</span>
    <span>record</span><span>.</span><span>onEdit</span><span>?.(</span><strong>true</strong><span>,</span> <strong>false</strong><span>);</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 添加编辑行，可指定初始数据</span>
  <strong>function</strong> <span>handleTestDataChildAdd</span><span>()</span> <span>&#123;</span>
    <span>testDataChildTable</span><span>.</span><span>insertTableDataRecord</span><span>(&#123;</span>
      <span style="color:#008080">id</span><span>:</span> <strong>new</strong> <span style="color:#0086b3">Date</span><span>().</span><span>getTime</span><span>(),</span>
      <span style="color:#008080">isNewRecord</span><span>:</span> <strong>true</strong><span>,</span>
      <span style="color:#008080">editable</span><span>:</span> <strong>true</strong><span>,</span>
    <span>&#125;);</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 删除编辑行方法</span>
  <strong>function</strong> <span>handleTestDataChildDelete</span><span>(</span><span>record</span><span>:</span> <span>Recordable</span><span>)</span> <span>&#123;</span>
    <span>testDataChildTable</span><span>.</span><span>deleteTableDataRecord</span><span>(</span><span>record</span><span>);</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 获取子表数据（支持返回删除未提交的数据）</span>
  <strong>async</strong> <strong>function</strong> <span>getTestDataChildList</span><span>()</span> <span>&#123;</span>
    <strong>let</strong> <span>testDataChildListValid</span> <strong>=</strong> <strong>true</strong><span>;</span>
    <strong>let</strong> <span style="color:#008080">testDataChildList</span><span>:</span> <span>Recordable</span><span>[]</span> <strong>=</strong> <span>[];</span>
    <strong>for</strong> <span>(</span><strong>const</strong> <span>record</span> <strong>of</strong> <span>testDataChildTable</span><span>.</span><span>getDataSource</span><span>())</span> <span>&#123;</span>
      <span style="color:#1d7e21">// 验证控件内容，并取消行的编辑状态（如果验证失败返回false）</span>
      <strong>if</strong> <span>(</span><strong>!</strong><span>(</span><strong>await</strong> <span>record</span><span>.</span><span>onEdit</span><span>?.(</span><strong>false</strong><span>,</span> <strong>true</strong><span>)))</span> <span>&#123;</span>
        <span>testDataChildListValid</span> <strong>=</strong> <strong>false</strong><span>;</span>
      <span>&#125;</span>
      <span>testDataChildList</span><span>.</span><span>push</span><span>(&#123;</span>
        <span>...</span><span>record</span><span>,</span>
        <span style="color:#008080">id</span><span>:</span> <strong>!!</strong><span>record</span><span>.</span><span>isNewRecord</span> <span>?</span> <span>''</span> <span>:</span> <span>record</span><span>.</span><span>id</span><span>,</span>
      <span>&#125;);</span>
    <span>&#125;</span>
    <strong>for</strong> <span>(</span><strong>const</strong> <span>record</span> <strong>of</strong> <span>testDataChildTable</span><span>.</span><span>getDelDataSource</span><span>())</span> <span>&#123;</span>
      <strong>if</strong> <span>(</span><strong>!!</strong><span>record</span><span>.</span><span>isNewRecord</span><span>)</span> <strong>continue</strong><span>;</span>
      <span>testDataChildList</span><span>.</span><span>push</span><span>(&#123;</span>
        <span>...</span><span>record</span><span>,</span>
        <span style="color:#008080">status</span><span>:</span> <span>'</span><span style="color:#dd1144">1</span><span>'</span><span>,</span>
      <span>&#125;);</span>
    <span>&#125;</span>
    <span style="color:#1d7e21">// 子表验证事件，抛出异常消息</span>
    <strong>if</strong> <span>(</span><strong>!</strong><span>testDataChildListValid</span><span>)</span> <span>&#123;</span>
      <strong>throw</strong> <strong>new</strong> <span style="color:#0086b3">Error</span><span>(</span><span>'</span><span style="color:#dd1144">testDataChildList valid.</span><span>'</span><span>);</span>
    <span>&#125;</span>
    <strong>return</strong> <span>testDataChildList</span><span>;</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 弹窗后的回调事件，进行一些表单数据初始化等操作</span>
  <strong>const</strong> <span>[</span><span>registerDrawer</span><span>,</span> <span>&#123;</span> <span>setDrawerProps</span><span>,</span> <span>closeDrawer</span> <span>&#125;]</span> <strong>=</strong> <span>useDrawerInner</span><span>(</span><strong>async</strong> <span>(</span><span>data</span><span>)</span> <strong>=></strong> <span>&#123;</span>
    <span>resetFields</span><span>();</span> <span style="color:#1d7e21">// 重置表单数据</span>
    <span>setDrawerProps</span><span>(&#123;</span> <span style="color:#008080">loading</span><span>:</span> <strong>true</strong> <span>&#125;);</span> <span style="color:#1d7e21">// 显示加载框</span>
    <strong>const</strong> <span>res</span> <strong>=</strong> <strong>await</strong> <span>testDataForm</span><span>(</span><span>data</span><span>);</span> <span style="color:#1d7e21">// 查询表单数据</span>
    <span>record</span><span>.</span><span>value</span> <strong>=</strong> <span>(</span><span>res</span><span>.</span><span>testData</span> <strong>||</strong> <span>&#123;&#125;)</span> <strong>as</strong> <span>Recordable</span><span>;</span>
    <span>setFieldsValue</span><span>(</span><span>record</span><span>.</span><span>value</span><span>);</span>  <span style="color:#1d7e21">// 设置字段值</span>
    <span>setTestDataChildTableData</span><span>(</span><span>res</span><span>);</span>  <span style="color:#1d7e21">// 设置子表数据（没有子表可不写）</span>
    <span>setDrawerProps</span><span>(&#123;</span> <span style="color:#008080">loading</span><span>:</span> <strong>false</strong> <span>&#125;);</span> <span style="color:#1d7e21">// 隐藏加载框</span>
  <span>&#125;);</span>

  <span style="color:#1d7e21">// 表单提交按钮方法</span>
  <strong>async</strong> <strong>function</strong> <span>handleSubmit</span><span>()</span> <span>&#123;</span>
    <strong>try</strong> <span>&#123;</span>
      <strong>const</strong> <span>data</span> <strong>=</strong> <strong>await</strong> <span>validate</span><span>();</span> <span style="color:#1d7e21">// 验证表单，并返回数据</span>
      <span>setDrawerProps</span><span>(&#123;</span> <span style="color:#008080">confirmLoading</span><span>:</span> <strong>true</strong> <span>&#125;);</span> <span style="color:#1d7e21">// 显示提交加载中</span>
      <span style="color:#1d7e21">// 设置提交的参数（QueryString，后台 Controller 的 get 接受）</span>
      <strong>const</strong> <span style="color:#008080">params</span><span>:</span> <span>any</span> <strong>=</strong> <span>&#123;</span>
        <span style="color:#008080">isNewRecord</span><span>:</span> <span>record</span><span>.</span><span>value</span><span>.</span><span>isNewRecord</span><span>,</span>
        <span style="color:#008080">id</span><span>:</span> <span>record</span><span>.</span><span>value</span><span>.</span><span>id</span><span>,</span>
      <span>&#125;;</span>
      <span style="color:#1d7e21">// 获取并设置子表数据</span>
      <span>data</span><span>.</span><span>testDataChildList</span> <strong>=</strong> <strong>await</strong> <span>getTestDataChildList</span><span>();</span>
      <span style="color:#1d7e21">// console.log('submit', params, data, record);</span>
      <span style="color:#1d7e21">// 将数据提交给后台（如果失败跳转到 catch）</span>
      <strong>const</strong> <span>res</span> <strong>=</strong> <strong>await</strong> <span>testDataSave</span><span>(</span><span>params</span><span>,</span> <span>data</span><span>);</span>
      <span>showMessage</span><span>(</span><span>res</span><span>.</span><span>message</span><span>);</span> <span style="color:#1d7e21">// 显示提交结果</span>
      <span>setTimeout</span><span>(</span><span>closeDrawer</span><span>);</span>  <span style="color:#1d7e21">// 隐藏抽屉弹窗</span>
      <span>emit</span><span>(</span><span>'</span><span style="color:#dd1144">success</span><span>'</span><span>,</span> <span>data</span><span>);</span>    <span style="color:#1d7e21">// 触发事件，列表数据刷新</span>
    <span>&#125;</span> <strong>catch</strong> <span>(</span><span style="color:#008080">error</span><span>:</span> <span>any</span><span>)</span> <span>&#123;</span>
      <strong>if</strong> <span>(</span><span>error</span> <strong>&&</strong> <span>error</span><span>.</span><span>errorFields</span><span>)</span> <span>&#123;</span>
        <span>showMessage</span><span>(</span><span>t</span><span>(</span><span>'</span><span style="color:#dd1144">您填写的信息有误，请根据提示修正。</span><span>'</span><span>));</span>
      <span>&#125;</span>
      <span>console</span><span>.</span><span>log</span><span>(</span><span>'</span><span style="color:#dd1144">error</span><span>'</span><span>,</span> <span>error</span><span>);</span>
    <span>&#125;</span> <strong>finally</strong> <span>&#123;</span>
      <span>setDrawerProps</span><span>(&#123;</span> <span style="color:#008080">confirmLoading</span><span>:</span> <strong>false</strong> <span>&#125;);</span> <span style="color:#1d7e21">// 隐藏提交加载中</span>
    <span>&#125;</span>
  <span>&#125;</span>
<span style="color:#000080"></script></span>
</code></pre> 
 </div> 
</div> 
<h3 style="text-align:start">列表视图</h3> 
<div style="text-align:start"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><code><span style="color:#000080"><template></span>
  <span style="color:#000080"><div></span>
    <span style="color:#1d7e21"><!-- 表格组件 --></span>
    <span style="color:#000080"><BasicTable</span> <span>@</span><span style="color:#008080">register=</span><span style="color:#dd1144">"registerTable"</span><span style="color:#000080">></span>
      <span style="color:#1d7e21"><!-- 表格标题插槽 --></span>
      <span style="color:#000080"><template</span> <span style="color:#008080">#tableTitle</span><span style="color:#000080">></span>
        <span style="color:#000080"><Icon</span> <span style="color:#008080">:icon=</span><span style="color:#dd1144">"getTitle.icon"</span> <span style="color:#008080">class=</span><span style="color:#dd1144">"m-1 pr-1"</span> <span style="color:#000080">/></span>
        <span style="color:#000080"><span></span> &#123;&#123; getTitle.value &#125;&#125; <span style="color:#000080"></span></span>
      <span style="color:#000080"></template></span>
      <span style="color:#1d7e21"><!-- 表格右侧按钮插槽，其中 v-auth 是按钮权限控制 --></span>
      <span style="color:#000080"><template</span> <span style="color:#008080">#toolbar</span><span style="color:#000080">></span>
        <span style="color:#000080"><a-button</span> <span style="color:#008080">type=</span><span style="color:#dd1144">"primary"</span> <span>@</span><span style="color:#008080">click=</span><span style="color:#dd1144">"handleForm(&#123;&#125;)"</span> <span style="color:#008080">v-auth=</span><span style="color:#dd1144">"'test:testData:edit'"</span><span style="color:#000080">></span>
          <span style="color:#000080"><Icon</span> <span style="color:#008080">icon=</span><span style="color:#dd1144">"fluent:add-12-filled"</span> <span style="color:#000080">/></span> &#123;&#123; t('新增') &#125;&#125;
        <span style="color:#000080"></a-button></span>
      <span style="color:#000080"></template></span>
      <span style="color:#1d7e21"><!-- 首列插槽 --></span>
      <span style="color:#000080"><template</span> <span style="color:#008080">#firstColumn</span><span>="&#123;</span> <span style="color:#008080">record</span> <span>&#125;"</span><span style="color:#000080">></span>
        <span style="color:#000080"><a</span> <span>@</span><span style="color:#008080">click=</span><span style="color:#dd1144">"handleForm(&#123; id: record.id &#125;)"</span><span style="color:#000080">></span>
          &#123;&#123; record.testInput &#125;&#125;
        <span style="color:#000080"></a></span>
      <span style="color:#000080"></template></span>
    <span style="color:#000080"></BasicTable></span>
    <span style="color:#1d7e21"><!-- 点击表格行进入的输入表单弹窗 --></span>
    <span style="color:#000080"><InputForm</span> <span>@</span><span style="color:#008080">register=</span><span style="color:#dd1144">"registerDrawer"</span> <span>@</span><span style="color:#008080">success=</span><span style="color:#dd1144">"handleSuccess"</span> <span style="color:#000080">/></span>
  <span style="color:#000080"></div></span>
<span style="color:#000080"></template></span>
<span style="color:#000080"><script </span><span style="color:#008080">lang=</span><span style="color:#dd1144">"ts"</span><span style="color:#000080">></span>
  <strong>export</strong> <strong>default</strong> <span>defineComponent</span><span>(&#123;</span>
    <span style="color:#1d7e21">// 当前组件名称（与路由名一致，如果不一致会页面缓存失效）</span>
    <span style="color:#008080">name</span><span>:</span> <span>'</span><span style="color:#dd1144">ViewsTestTestDataList</span><span>'</span><span>,</span>
  <span>&#125;);</span>
<span style="color:#000080"></script></span>
<span style="color:#000080"><script </span><span style="color:#008080">lang=</span><span style="color:#dd1144">"ts"</span> <span style="color:#008080">setup</span><span style="color:#000080">></span>

  <span style="color:#1d7e21">// 导入当前用到的对象，部分省略</span>
  <strong>import</strong> <span>&#123;</span> <span>defineComponent</span> <span>&#125;</span> <strong>from</strong> <span>'</span><span style="color:#dd1144">vue</span><span>'</span><span>;</span>
  <strong>import</strong> <span>InputForm</span> <strong>from</strong> <span>'</span><span style="color:#dd1144">./form.vue</span><span>'</span><span>;</span>

  <span style="color:#1d7e21">// 国际化方法调用，参数是国际化编码的跟路径</span>
  <strong>const</strong> <span>&#123;</span> <span>t</span> <span>&#125;</span> <strong>=</strong> <span>useI18n</span><span>(</span><span>'</span><span style="color:#dd1144">test.testData</span><span>'</span><span>);</span>

  <span style="color:#1d7e21">// 消息弹窗方法</span>
  <strong>const</strong> <span>&#123;</span> <span>showMessage</span> <span>&#125;</span> <strong>=</strong> <span>useMessage</span><span>();</span>

  <span style="color:#1d7e21">// 当前页面标题定义，来自菜单管理定义</span>
  <strong>const</strong> <span>getTitle</span> <strong>=</strong> <span>&#123;</span>
    <span style="color:#008080">icon</span><span>:</span> <span>router</span><span>.</span><span>currentRoute</span><span>.</span><span>value</span><span>.</span><span>meta</span><span>.</span><span>icon</span> <strong>||</strong> <span>'</span><span style="color:#dd1144">ant-design:book-outlined</span><span>'</span><span>,</span>
    <span style="color:#008080">value</span><span>:</span> <span>router</span><span>.</span><span>currentRoute</span><span>.</span><span>value</span><span>.</span><span>meta</span><span>.</span><span>title</span> <strong>||</strong> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">数据管理</span><span>'</span><span>),</span>
  <span>&#125;;</span>

  <span style="color:#1d7e21">// 表格搜索表单控件定义</span>
  <strong>const</strong> <span>searchForm</span><span>:</span> <span>FormProps</span> <strong>=</strong> <span>&#123;</span>
    <span style="color:#008080">baseColProps</span><span>:</span> <span>&#123;</span> <span style="color:#008080">lg</span><span>:</span> <span style="color:#009999">6</span><span>,</span> <span style="color:#008080">md</span><span>:</span> <span style="color:#009999">8</span> <span>&#125;,</span> <span style="color:#1d7e21">// 表单栅格布局</span>
    <span style="color:#008080">labelWidth</span><span>:</span> <span style="color:#009999">90</span><span>,</span>                 <span style="color:#1d7e21">// 表单标签宽度</span>
    <span style="color:#008080">schemas</span><span>:</span> <span>[</span>
      <span>&#123;</span>
        <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">单行文本</span><span>'</span><span>),</span>        <span style="color:#1d7e21">// 表单标签</span>
        <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testInput</span><span>'</span><span>,</span>         <span style="color:#1d7e21">// 字段提交参数名</span>
        <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">Input</span><span>'</span><span>,</span>         <span style="color:#1d7e21">// 表单控件</span>
      <span>&#125;,</span>
      <span>&#123;</span>
        <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">下拉框</span><span>'</span><span>),</span>
        <span style="color:#008080">field</span><span>:</span> <span>'</span><span style="color:#dd1144">testSelect</span><span>'</span><span>,</span>
        <span style="color:#008080">component</span><span>:</span> <span>'</span><span style="color:#dd1144">Select</span><span>'</span><span>,</span>    <span style="color:#1d7e21">// 选择框还有 RadioGroup、CheckboxGroup</span>
        <span style="color:#008080">componentProps</span><span>:</span> <span>&#123;</span>
          <span style="color:#008080">dictType</span><span>:</span> <span>'</span><span style="color:#dd1144">sys_menu_type</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 下拉框选项数据（支持直接指定字典类型）</span>
          <span style="color:#008080">allowClear</span><span>:</span> <strong>true</strong><span>,</span>          <span style="color:#1d7e21">// 启用空选项，可清空选择</span>
          <span style="color:#008080">mode</span><span>:</span> <span>'</span><span style="color:#dd1144">multiple</span><span>'</span><span>,</span>          <span style="color:#1d7e21">// 下拉框模块，启用多选</span>
        <span>&#125;,</span>
      <span>&#125;,</span>
      <span style="color:#1d7e21">// 更多控件，再次不展示了，和上一节表单视图一致</span>
    <span>],</span>
  <span>&#125;;</span>

  <span style="color:#1d7e21">// 表格列定义</span>
  <strong>const</strong> <span>tableColumns</span><span>:</span> <span>BasicColumn</span><span>[]</span> <strong>=</strong> <span>[</span>
    <span>&#123;</span>
      <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">单行文本</span><span>'</span><span>),</span>    <span style="color:#1d7e21">// 表头标题</span>
      <span style="color:#008080">dataIndex</span><span>:</span> <span>'</span><span style="color:#dd1144">testInput</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 表列实体属性名</span>
      <span style="color:#008080">key</span><span>:</span> <span>'</span><span style="color:#dd1144">a.test_input</span><span>'</span><span>,</span>    <span style="color:#1d7e21">// 排序数据库字段名</span>
      <span style="color:#008080">sorter</span><span>:</span> <strong>true</strong><span>,</span>           <span style="color:#1d7e21">// 点击表头是否可排序</span>
      <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">230</span><span>,</span>             <span style="color:#1d7e21">// 列宽</span>
      <span style="color:#008080">align</span><span>:</span> <span>'</span><span style="color:#dd1144">left</span><span>'</span><span>,</span>          <span style="color:#1d7e21">// 列的对齐方式</span>
      <span style="color:#1d7e21">// 个性化列，可定义插槽（如样式，增加控件等）</span>
      <span style="color:#008080">slots</span><span>:</span> <span>&#123;</span> <span style="color:#008080">customRender</span><span>:</span> <span>'</span><span style="color:#dd1144">firstColumn</span><span>'</span> <span>&#125;,</span>
    <span>&#125;,</span>
    <span>&#123;</span>
      <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">下拉框</span><span>'</span><span>),</span>
      <span style="color:#008080">dataIndex</span><span>:</span> <span>'</span><span style="color:#dd1144">testSelect</span><span>'</span><span>,</span>
      <span style="color:#008080">key</span><span>:</span> <span>'</span><span style="color:#dd1144">a.test_select</span><span>'</span><span>,</span>
      <span style="color:#008080">sorter</span><span>:</span> <strong>true</strong><span>,</span>
      <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">130</span><span>,</span>
      <span style="color:#008080">align</span><span>:</span> <span>'</span><span style="color:#dd1144">center</span><span>'</span><span>,</span>
      <span style="color:#008080">dictType</span><span>:</span> <span>'</span><span style="color:#dd1144">sys_menu_type</span><span>'</span><span>,</span> <span style="color:#1d7e21">// 字典列，快速显示字典标签</span>
    <span>&#125;,</span>
  <span>];</span>

  <span style="color:#1d7e21">// 表格操作列定义</span>
  <strong>const</strong> <span>actionColumn</span><span>:</span> <span>BasicColumn</span> <strong>=</strong> <span>&#123;</span>
    <span style="color:#008080">width</span><span>:</span> <span style="color:#009999">160</span><span>,</span> <span style="color:#1d7e21">// 操作列宽</span>
    <span style="color:#008080">actions</span><span>:</span> <span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <strong>=></strong> <span>[</span>
      <span>&#123;</span>
        <span style="color:#008080">icon</span><span>:</span> <span>'</span><span style="color:#dd1144">clarity:note-edit-line</span><span>'</span><span>,</span>
        <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">编辑数据</span><span>'</span><span>),</span>
        <span style="color:#008080">onClick</span><span>:</span> <span>handleForm</span><span>.</span><span>bind</span><span>(</span><strong>this</strong><span>,</span> <span>&#123;</span> <span style="color:#008080">id</span><span>:</span> <span>record</span><span>.</span><span>id</span> <span>&#125;),</span>
        <span style="color:#1d7e21">// 按钮权限控制，指定权限字符串</span>
        <span style="color:#008080">auth</span><span>:</span> <span>'</span><span style="color:#dd1144">test:testData:edit</span><span>'</span><span>,</span>
      <span>&#125;,</span>
      <span>&#123;</span>
        <span style="color:#008080">icon</span><span>:</span> <span>'</span><span style="color:#dd1144">ant-design:stop-outlined</span><span>'</span><span>,</span>
        <span style="color:#008080">color</span><span>:</span> <span>'</span><span style="color:#dd1144">error</span><span>'</span><span>,</span>
        <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">停用数据</span><span>'</span><span>),</span>
        <span style="color:#1d7e21">// 是否需要启用确认框</span>
        <span style="color:#008080">popConfirm</span><span>:</span> <span>&#123;</span>
          <span style="color:#008080">title</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">是否确认停用数据</span><span>'</span><span>),</span>
          <span style="color:#008080">confirm</span><span>:</span> <span>handleDisable</span><span>.</span><span>bind</span><span>(</span><strong>this</strong><span>,</span> <span>&#123;</span> <span style="color:#008080">id</span><span>:</span> <span>record</span><span>.</span><span>id</span> <span>&#125;),</span>
        <span>&#125;,</span>
        <span style="color:#1d7e21">// 按钮权限控制，指定权限字符串</span>
        <span style="color:#008080">auth</span><span>:</span> <span>'</span><span style="color:#dd1144">test:testData:edit</span><span>'</span><span>,</span>
        <span style="color:#1d7e21">// 控制按钮是否显示（区别：show 是显示或隐藏；ifShow 是显示或移除）</span>
        <span style="color:#008080">show</span><span>:</span> <span>()</span> <strong>=></strong> <span>record</span><span>.</span><span>status</span> <strong>===</strong> <span>'</span><span style="color:#dd1144">0</span><span>'</span><span>,</span>
        <span style="color:#008080">ifShow</span><span>:</span> <span>()</span> <strong>=></strong> <span>record</span><span>.</span><span>status</span> <strong>===</strong> <span>'</span><span style="color:#dd1144">0</span><span>'</span><span>,</span>
      <span>&#125;,</span>
    <span>],</span>
    <span style="color:#1d7e21">// 操作列更多按钮定义</span>
    <span style="color:#008080">dropDownActions</span><span>:</span> <span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <strong>=></strong> <span>[</span>
      <span>&#123;</span>
        <span style="color:#008080">icon</span><span>:</span> <span>'</span><span style="color:#dd1144">ant-design:reload-outlined</span><span>'</span><span>,</span>
        <span style="color:#008080">label</span><span>:</span> <span>t</span><span>(</span><span>'</span><span style="color:#dd1144">重置密码</span><span>'</span><span>),</span>
        <span style="color:#008080">onClick</span><span>:</span> <span>handleResetpwd</span><span>.</span><span>bind</span><span>(</span><strong>this</strong><span>,</span> <span>&#123;</span> <span style="color:#008080">userCode</span><span>:</span> <span>record</span><span>.</span><span>userCode</span> <span>&#125;),</span>
        <span style="color:#008080">auth</span><span>:</span> <span>'</span><span style="color:#dd1144">sys:empUser:resetpwd</span><span>'</span><span>,</span>
      <span>&#125;,</span>
    <span>],</span>
  <span>&#125;;</span>

  <span style="color:#1d7e21">// 点击首列或编辑按钮是的抽屉弹窗定义</span>
  <strong>const</strong> <span>[</span><span>registerDrawer</span><span>,</span> <span>&#123;</span> <span>openDrawer</span> <span>&#125;]</span> <strong>=</strong> <span>useDrawer</span><span>();</span>

  <span style="color:#1d7e21">// 表格定义</span>
  <strong>const</strong> <span>[</span><span>registerTable</span><span>,</span> <span>&#123;</span> <span>reload</span> <span>&#125;]</span> <strong>=</strong> <span>useTable</span><span>(&#123;</span>
    <span style="color:#008080">api</span><span>:</span> <span>testDataListData</span><span>,</span>     <span style="color:#1d7e21">// 表格数据源 API</span>
    <span style="color:#008080">beforeFetch</span><span>:</span> <span>(</span><span>params</span><span>)</span> <strong>=></strong> <span>&#123;</span>
      <strong>return</strong> <span>params</span><span>;</span>           <span style="color:#1d7e21">// API 提交之前的参数修改</span>
    <span>&#125;,</span>
    <span style="color:#008080">columns</span><span>:</span> <span>tableColumns</span><span>,</span>     <span style="color:#1d7e21">// 表格列</span>
    <span style="color:#008080">actionColumn</span><span>:</span> <span>actionColumn</span><span>,</span><span style="color:#1d7e21">// 操作列</span>
    <span style="color:#008080">formConfig</span><span>:</span> <span>searchForm</span><span>,</span>    <span style="color:#1d7e21">// 搜索表单</span>
    <span style="color:#008080">showTableSetting</span><span>:</span> <strong>true</strong><span>,</span>    <span style="color:#1d7e21">// 是否显示右上角的设置按钮</span>
    <span style="color:#008080">useSearchForm</span><span>:</span> <strong>true</strong><span>,</span>       <span style="color:#1d7e21">// 是否显示搜索表单</span>
    <span style="color:#008080">canResize</span><span>:</span> <strong>true</strong><span>,</span>           <span style="color:#1d7e21">// 是否自适应表单高度</span>
  <span>&#125;);</span>

  <span style="color:#1d7e21">// 弹窗操作方法</span>
  <strong>function</strong> <span>handleForm</span><span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <span>&#123;</span>
    <span>openDrawer</span><span>(</span><strong>true</strong><span>,</span> <span>record</span><span>);</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 操作列停用按钮方法</span>
  <strong>async</strong> <strong>function</strong> <span>handleDisable</span><span>(</span><span style="color:#008080">record</span><span>:</span> <span>Recordable</span><span>)</span> <span>&#123;</span>
    <strong>const</strong> <span>res</span> <strong>=</strong> <strong>await</strong> <span>testDataDisable</span><span>(</span><span>record</span><span>);</span>
    <span>showMessage</span><span>(</span><span>res</span><span>.</span><span>message</span><span>);</span>
    <span>handleSuccess</span><span>();</span>
  <span>&#125;</span>

  <span style="color:#1d7e21">// 刷新表格数据（含表单回调）</span>
  <strong>function</strong> <span>handleSuccess</span><span>()</span> <span>&#123;</span>
    <span>reload</span><span>();</span>
  <span>&#125;</span>
<span style="color:#000080"></script></span></code></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            